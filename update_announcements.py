"""
Announcement Updater
====================
Discovers new Build 2026-related posts from official Microsoft RSS feeds and
injects them into index.html as a self-contained `AUTO_ANNOUNCEMENTS` object
(between the `/* AUTO_ANNOUNCEMENTS:START/END */` markers), keyed by category id.

At render time the page merges these into each category as a clearly-labelled
"🆕 Latest Updates" subcategory, so the hand-curated ALL_CATEGORIES is never
touched. The page still does no runtime fetch — this bakes the data in.

Relevance and dedupe:
  * Only items judged Build 2026-related (reuses scan_announcements.is_build_related).
  * Microsoft-only sources (every feed below is an official Microsoft domain).
  * Deduped against every URL already present anywhere in index.html, and across
    categories within a run (a URL lands in at most one category).

Usage:
  python update_announcements.py             # Fetch feeds and update index.html
  python update_announcements.py --dry-run   # Print what would change, write nothing
"""

import json
import re
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

from scan_announcements import fetch_url, parse_rss, is_build_related

SCRIPT_DIR = Path(__file__).parent
INDEX_FILE = SCRIPT_DIR / "index.html"
MAX_PER_CATEGORY = 6
DESC_LIMIT = 150

START_MARKER = "/* AUTO_ANNOUNCEMENTS:START */"
END_MARKER = "/* AUTO_ANNOUNCEMENTS:END */"

# Map ALL_CATEGORIES ids → official Microsoft feeds that best match that category.
# Order matters: earlier categories claim a URL first (cross-category dedupe).
CATEGORY_FEEDS: dict[str, list[tuple[str, str]]] = {
    "power-apps": [
        ("Power Apps Blog", "https://powerapps.microsoft.com/en-us/blog/feed/"),
    ],
    "power-automate": [
        ("Power Automate Blog", "https://powerautomate.microsoft.com/en-us/blog/feed/"),
    ],
    "power-bi": [
        ("Power BI Blog", "https://powerbi.microsoft.com/en-us/blog/feed/"),
    ],
    "power-platform-admin": [
        ("Power Platform Blog", "https://www.microsoft.com/en-us/power-platform/blog/feed/"),
    ],
    "microsoft-foundry": [
        ("Azure AI Foundry", "https://devblogs.microsoft.com/foundry/feed/"),
    ],
    "microsoft-365-copilot": [
        ("M365 Blog", "https://www.microsoft.com/en-us/microsoft-365/blog/feed/"),
        ("M365 Dev Blog", "https://devblogs.microsoft.com/microsoft365dev/feed/"),
    ],
    "ai-agents": [
        ("Microsoft Copilot Blog", "https://www.microsoft.com/en-us/microsoft-copilot/blog/feed/"),
    ],
    "data-analytics": [
        ("Cosmos DB Blog", "https://devblogs.microsoft.com/cosmosdb/feed/"),
        ("Fabric Updates Blog", "https://blog.fabric.microsoft.com/en-us/blog/feed/"),
    ],
    "security-governance": [
        ("Microsoft Security Blog", "https://www.microsoft.com/en-us/security/blog/feed/"),
    ],
    "windows-platform": [
        ("Windows Developer Blog", "https://blogs.windows.com/windowsdeveloper/feed/"),
    ],
    "developer-tools": [
        ("Visual Studio Blog", "https://devblogs.microsoft.com/visualstudio/feed/"),
        (".NET Blog", "https://devblogs.microsoft.com/dotnet/feed/"),
        ("Command Line Blog", "https://devblogs.microsoft.com/commandline/feed/"),
    ],
    "hardware-infrastructure": [
        ("Azure Blog", "https://azure.microsoft.com/en-us/blog/feed/"),
    ],
    "apps-development": [
        ("Azure DevBlogs", "https://devblogs.microsoft.com/feed/"),
        ("GitHub Blog", "https://github.blog/feed/"),
    ],
}


def normalize_url(url: str) -> str:
    url = (url or "").strip().lower()
    url = re.sub(r"[?#].*$", "", url)
    return url.rstrip("/")


def clean_text(text: str) -> str:
    text = unescape(re.sub(r"<[^>]+>", "", text or ""))
    return re.sub(r"\s+", " ", text).strip()


def clean_desc(text: str) -> str:
    text = clean_text(text)
    if len(text) > DESC_LIMIT:
        text = text[:DESC_LIMIT].rsplit(" ", 1)[0].rstrip() + "…"
    return text


def existing_urls(html: str) -> set[str]:
    """Every URL already present anywhere in index.html (curated + auto + links)."""
    return {normalize_url(u) for u in re.findall(r"https?://[^\s'\"<>)]+", html)}


def collect(html: str) -> dict[str, list[dict]]:
    used = existing_urls(html)
    result: dict[str, list[dict]] = {}

    for cat_id, feeds in CATEGORY_FEEDS.items():
        items: list[dict] = []
        for source, url in feeds:
            print(f"  📡 [{cat_id}] {source}...", end=" ", flush=True)
            xml_text = fetch_url(url)
            if not xml_text:
                print("SKIP")
                continue
            parsed = parse_rss(xml_text)
            added = 0
            for it in parsed:
                norm = normalize_url(it.get("url", ""))
                if not norm or norm in used:
                    continue
                if not it.get("title"):
                    continue
                if not is_build_related(it):
                    continue
                used.add(norm)
                items.append({
                    "title": clean_text(it["title"]),
                    "url": it["url"].strip(),
                    "description": clean_desc(it.get("description", "")),
                    "parsed_date": it.get("parsed_date"),
                })
                added += 1
            print(f"{len(parsed)} items, {added} new")

        items.sort(
            key=lambda x: x["parsed_date"] or datetime.min.replace(tzinfo=timezone.utc),
            reverse=True,
        )
        trimmed = [
            {"title": i["title"], "url": i["url"], "description": i["description"]}
            for i in items[:MAX_PER_CATEGORY]
        ]
        if trimmed:
            result[cat_id] = trimmed

    return result


def build_block(data: dict[str, list[dict]]) -> str:
    payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    payload = "\n".join("  " + line for line in payload.splitlines())
    updated = "Updated " + datetime.now(timezone.utc).strftime("%b %d, %Y")
    return (
        f"{START_MARKER}\n"
        f"  const AUTO_ANNOUNCEMENTS =\n{payload};\n"
        f"  const AUTO_ANNOUNCEMENTS_UPDATED = {json.dumps(updated)};\n"
        f"  {END_MARKER}"
    )


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("  🗂️  Announcement Updater")
    print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if dry_run:
        print("  🧪 DRY RUN — index.html will not be written")
    print("=" * 60)

    html = INDEX_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    if not pattern.search(html):
        print(f"\n❌ Markers not found in {INDEX_FILE.name}; aborting.")
        return 2

    data = collect(html)
    total = sum(len(v) for v in data.values())
    print(f"\n🆕 {total} new announcement(s) across {len(data)} categor(ies):")
    for cat_id, items in data.items():
        print(f"   • {cat_id}: {len(items)}")
        for it in items:
            print(f"       - {it['title'][:70]}")

    if total == 0:
        print("\n✅ Nothing new — index.html already up to date.")
        return 0

    new_html = pattern.sub(lambda _m: build_block(data), html, count=1)
    if new_html == html:
        print("\n✅ No changes — index.html already up to date.")
        return 0

    if dry_run:
        print("\n🧪 DRY RUN — would update AUTO_ANNOUNCEMENTS block in index.html.")
        return 0

    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print(f"\n💾 Updated {INDEX_FILE.name} with {total} auto announcement(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
