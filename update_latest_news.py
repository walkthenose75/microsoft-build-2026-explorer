"""
Latest News Updater
===================
Pulls the most recent posts from official Microsoft RSS feeds and injects them
into index.html as a self-contained `LATEST_NEWS` JavaScript array (between the
`/* LATEST_NEWS:START */` and `/* LATEST_NEWS:END */` markers).

The page itself never fetches anything at runtime — this script bakes the data
in, keeping index.html fully self-contained. It is meant to run on a schedule
via GitHub Actions (see .github/workflows/update-latest-news.yml), so the site
refreshes automatically with no manual steps.

Usage:
  python update_latest_news.py            # Fetch feeds and update index.html
  python update_latest_news.py --dry-run  # Print what would change, write nothing
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reuse the RSS plumbing already proven in the scanner.
from scan_announcements import fetch_url, parse_rss

SCRIPT_DIR = Path(__file__).parent
INDEX_FILE = SCRIPT_DIR / "index.html"
MAX_ITEMS = 12
DESC_LIMIT = 180

START_MARKER = "/* LATEST_NEWS:START */"
END_MARKER = "/* LATEST_NEWS:END */"

# Curated, official Microsoft-only sources for a general "latest news" feed.
LATEST_FEEDS = [
    ("Official Microsoft Blog",  "https://blogs.microsoft.com/feed/"),
    ("Azure Blog",              "https://azure.microsoft.com/en-us/blog/feed/"),
    ("Azure AI Foundry",        "https://devblogs.microsoft.com/foundry/feed/"),
    ("Microsoft 365 Blog",      "https://www.microsoft.com/en-us/microsoft-365/blog/feed/"),
    ("Microsoft Copilot Blog",  "https://www.microsoft.com/en-us/microsoft-copilot/blog/feed/"),
    ("Power Platform Blog",     "https://www.microsoft.com/en-us/power-platform/blog/feed/"),
    ("Windows Developer Blog",  "https://blogs.windows.com/windowsdeveloper/feed/"),
    ("Azure DevBlogs",          "https://devblogs.microsoft.com/feed/"),
]


def normalize_url(url: str) -> str:
    url = url.rstrip("/").lower()
    url = re.sub(r"[?#].*$", "", url)
    return url


def clean_desc(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) > DESC_LIMIT:
        text = text[:DESC_LIMIT].rsplit(" ", 1)[0].rstrip() + "…"
    return text


def collect_items() -> list[dict]:
    seen: set[str] = set()
    items: list[dict] = []

    for source, url in LATEST_FEEDS:
        print(f"  📡 {source}...", end=" ", flush=True)
        xml_text = fetch_url(url)
        if not xml_text:
            print("SKIP")
            continue
        parsed = parse_rss(xml_text)
        added = 0
        for it in parsed:
            norm = normalize_url(it.get("url", ""))
            if not norm or norm in seen:
                continue
            if not it.get("title") or not it.get("url"):
                continue
            seen.add(norm)
            items.append({
                "title": it["title"].strip(),
                "url": it["url"].strip(),
                "source": source,
                "description": clean_desc(it.get("description", "")),
                "parsed_date": it.get("parsed_date"),
            })
            added += 1
        print(f"{len(parsed)} items, {added} added")

    # Newest first; items without a date sink to the bottom.
    items.sort(
        key=lambda x: x["parsed_date"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return items[:MAX_ITEMS]


def build_block(items: list[dict]) -> str:
    payload = [
        {
            "title": it["title"],
            "url": it["url"],
            "source": it["source"],
            "date": it["parsed_date"].strftime("%b %d, %Y") if it["parsed_date"] else "",
            "description": it["description"],
        }
        for it in items
    ]
    # JSON is valid JS; escape "</" so it can't break out of the <script> tag.
    news_json = json.dumps(payload, ensure_ascii=False, indent=2).replace("</", "<\\/")
    news_json = "\n".join("  " + line for line in news_json.splitlines())
    updated = "Updated " + datetime.now(timezone.utc).strftime("%b %d, %Y")
    return (
        f"{START_MARKER}\n"
        f"  const LATEST_NEWS =\n{news_json};\n"
        f"  const LATEST_NEWS_UPDATED = {json.dumps(updated)};\n"
        f"  {END_MARKER}"
    )


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  📰 Latest News Updater")
    print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if dry_run:
        print("  🧪 DRY RUN — index.html will not be written")
    print("=" * 60)

    items = collect_items()
    if not items:
        print("\n⚠ No items collected — leaving index.html unchanged.")
        return 1

    print(f"\n🆕 Top {len(items)} items:")
    for it in items:
        d = it["parsed_date"].strftime("%Y-%m-%d") if it["parsed_date"] else "????-??-??"
        print(f"   {d}  [{it['source']}] {it['title'][:70]}")

    html = INDEX_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(html):
        print(f"\n❌ Markers not found in {INDEX_FILE.name}; aborting.")
        return 2

    new_html = pattern.sub(lambda _m: build_block(items), html, count=1)

    if new_html == html:
        print("\n✅ No changes — index.html already up to date.")
        return 0

    if dry_run:
        print("\n🧪 DRY RUN — would update LATEST_NEWS block in index.html.")
        return 0

    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print(f"\n💾 Updated {INDEX_FILE.name} with {len(items)} latest items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
