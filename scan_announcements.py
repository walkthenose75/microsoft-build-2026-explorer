"""
Build 2026 Announcement Scanner
================================
Scans Microsoft RSS feeds daily for new Build 2026-related announcements.
Compares against tracked items, outputs new findings, and appends to a JSON log.

Usage:
  python scan_announcements.py              # Scan all feeds
  python scan_announcements.py --dry-run    # Preview without saving
  python scan_announcements.py --category "Power Platform"  # Scan one category

Schedule daily with:
  Windows Task Scheduler: schtasks /create /tn "Build2026Scan" /tr "python scan_announcements.py" /sc daily /st 08:00
  Linux/Mac cron:         0 8 * * * cd /path/to/repo && python scan_announcements.py
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError
from html import unescape

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
TRACKED_FILE = SCRIPT_DIR / "tracked_announcements.json"
NEW_FINDINGS_FILE = SCRIPT_DIR / "new_findings.json"
README_URL = "https://raw.githubusercontent.com/matthansen0/matts-build-2026-list/main/readme.md"

# Build 2026 search patterns
BUILD_KEYWORDS = [
    r"build\s*2026",
    r"microsoft\s*build",
    r"//build",
    r"2026\s*release\s*wave",
    r"2026\s*wave\s*1",
]
BUILD_PATTERN = re.compile("|".join(BUILD_KEYWORDS), re.IGNORECASE)

# Date range: Build 2026 was June 2-4, but announcements span May-July 2026
BUILD_START = datetime(2026, 5, 1, tzinfo=timezone.utc)
BUILD_END = datetime(2026, 7, 31, tzinfo=timezone.utc)

# ── RSS Feed Sources by Category ───────────────────────────────────
FEEDS = {
    "Power Platform": [
        {
            "name": "Power Platform Blog",
            "url": "https://www.microsoft.com/en-us/power-platform/blog/feed/",
            "fallback_url": "https://cloudblogs.microsoft.com/powerplatform/feed/",
        },
        {
            "name": "Power Apps Blog",
            "url": "https://powerapps.microsoft.com/en-us/blog/feed/",
        },
        {
            "name": "Power Automate Blog",
            "url": "https://powerautomate.microsoft.com/en-us/blog/feed/",
        },
        {
            "name": "Power BI Blog",
            "url": "https://powerbi.microsoft.com/en-us/blog/feed/",
        },
    ],
    "AI & Agents": [
        {
            "name": "Microsoft AI Blog",
            "url": "https://blogs.microsoft.com/ai/feed/",
        },
        {
            "name": "Azure AI Foundry Blog",
            "url": "https://devblogs.microsoft.com/foundry/feed/",
        },
        {
            "name": "Microsoft Copilot Blog",
            "url": "https://www.microsoft.com/en-us/microsoft-copilot/blog/feed/",
        },
    ],
    "Apps & Development": [
        {
            "name": "Azure DevBlogs",
            "url": "https://devblogs.microsoft.com/feed/",
        },
        {
            "name": "GitHub Blog",
            "url": "https://github.blog/feed/",
        },
        {
            "name": "Visual Studio Blog",
            "url": "https://devblogs.microsoft.com/visualstudio/feed/",
        },
        {
            "name": ".NET Blog",
            "url": "https://devblogs.microsoft.com/dotnet/feed/",
        },
        {
            "name": "TypeScript Blog",
            "url": "https://devblogs.microsoft.com/typescript/feed/",
        },
        {
            "name": "Azure SDK Blog",
            "url": "https://devblogs.microsoft.com/azure-sdk/feed/",
        },
        {
            "name": "Command Line Blog",
            "url": "https://devblogs.microsoft.com/commandline/feed/",
        },
    ],
    "Hardware & Infrastructure": [
        {
            "name": "Azure Blog",
            "url": "https://azure.microsoft.com/en-us/blog/feed/",
        },
        {
            "name": "Azure Updates (RSS)",
            "url": "https://azure.microsoft.com/en-us/updates/feed/",
        },
        {
            "name": "Azure Compute Blog",
            "url": "https://techcommunity.microsoft.com/t5/azure-compute-blog/bg-p/AzureCompute/label-name/RSS",
        },
    ],
    "Data & Analytics": [
        {
            "name": "Cosmos DB Blog",
            "url": "https://devblogs.microsoft.com/cosmosdb/feed/",
        },
        {
            "name": "Azure SQL Blog",
            "url": "https://techcommunity.microsoft.com/t5/azure-sql-blog/bg-p/AzureSQLBlog/label-name/RSS",
        },
        {
            "name": "Fabric Updates Blog",
            "url": "https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/bg-p/FabricUpdatesBlog/label-name/RSS",
        },
    ],
    "Security & Governance": [
        {
            "name": "Microsoft Security Blog",
            "url": "https://www.microsoft.com/en-us/security/blog/feed/",
        },
        {
            "name": "Defender Cloud Blog",
            "url": "https://techcommunity.microsoft.com/t5/microsoft-defender-for-cloud/bg-p/MicrosoftDefenderCloudBlog/label-name/RSS",
        },
    ],
    "Microsoft 365 Copilot": [
        {
            "name": "M365 Blog",
            "url": "https://www.microsoft.com/en-us/microsoft-365/blog/feed/",
        },
        {
            "name": "M365 Dev Blog",
            "url": "https://devblogs.microsoft.com/microsoft365dev/feed/",
        },
    ],
    "Windows & Dev Tools": [
        {
            "name": "Windows Developer Blog",
            "url": "https://blogs.windows.com/windowsdeveloper/feed/",
        },
        {
            "name": "Windows Blog",
            "url": "https://blogs.windows.com/feed/",
        },
    ],
}


def fetch_url(url: str, timeout: int = 15) -> str | None:
    """Fetch a URL and return text content, or None on failure."""
    headers = {"User-Agent": "Build2026Scanner/1.0"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, TimeoutError, OSError) as e:
        print(f"  ⚠ Failed to fetch {url}: {e}")
        return None


def parse_rss(xml_text: str) -> list[dict]:
    """Parse RSS/Atom XML into a list of items with title, link, date, description."""
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items

    # RSS 2.0 format
    for item in root.iter("item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        pub_date = item.findtext("pubDate", "").strip()
        desc = item.findtext("description", "").strip()
        desc = unescape(re.sub(r"<[^>]+>", "", desc))[:300]  # strip HTML, truncate

        parsed_date = parse_date(pub_date)
        if title and link:
            items.append({
                "title": title,
                "url": link,
                "date": pub_date,
                "parsed_date": parsed_date,
                "description": desc,
            })

    # Atom format
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.iter("{http://www.w3.org/2005/Atom}entry"):
        title = entry.findtext("atom:title", "", ns).strip()
        link_el = entry.find("atom:link[@rel='alternate']", ns) or entry.find("atom:link", ns)
        link = link_el.get("href", "") if link_el is not None else ""
        pub_date = entry.findtext("atom:published", "", ns).strip() or entry.findtext("atom:updated", "", ns).strip()
        desc = entry.findtext("atom:summary", "", ns).strip()
        desc = unescape(re.sub(r"<[^>]+>", "", desc))[:300]

        parsed_date = parse_date(pub_date)
        if title and link:
            items.append({
                "title": title,
                "url": link,
                "date": pub_date,
                "parsed_date": parsed_date,
                "description": desc,
            })

    return items


def parse_date(date_str: str) -> datetime | None:
    """Try to parse various date formats from RSS feeds."""
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",      # RFC 822
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",             # ISO 8601
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


def is_build_related(item: dict) -> bool:
    """Check if an item is related to Build 2026."""
    text = f"{item['title']} {item['description']}"
    if BUILD_PATTERN.search(text):
        return True
    # Also check date range — items from May-July 2026 with Azure/Microsoft keywords
    if item["parsed_date"] and BUILD_START <= item["parsed_date"] <= BUILD_END:
        azure_pattern = re.compile(
            r"preview|generally available|announcing|new feature|public preview|now available",
            re.IGNORECASE,
        )
        if azure_pattern.search(text):
            return True
    return False


def load_tracked() -> dict:
    """Load previously tracked announcements."""
    if TRACKED_FILE.exists():
        return json.loads(TRACKED_FILE.read_text(encoding="utf-8"))
    return {"tracked_urls": [], "last_scan": None}


def save_tracked(data: dict):
    """Save tracked announcements."""
    TRACKED_FILE.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")


def load_existing_readme_urls() -> set[str]:
    """Fetch Matt's readme.md and extract all URLs already tracked."""
    print("📥 Fetching existing announcements from Matt's repo...")
    text = fetch_url(README_URL)
    if not text:
        return set()
    urls = set(re.findall(r"https?://[^\s)\]]+", text))
    print(f"   Found {len(urls)} existing URLs in readme.md")
    return urls


def normalize_url(url: str) -> str:
    """Normalize URL for dedup comparison."""
    url = url.rstrip("/").lower()
    url = re.sub(r"\?.*$", "", url)  # strip query params
    url = re.sub(r"#.*$", "", url)   # strip anchors
    return url


def scan_feeds(category_filter: str | None = None) -> list[dict]:
    """Scan all RSS feeds and return new Build 2026-related items."""
    tracked = load_tracked()
    tracked_urls = set(normalize_url(u) for u in tracked.get("tracked_urls", []))
    existing_urls = set(normalize_url(u) for u in load_existing_readme_urls())
    known_urls = tracked_urls | existing_urls

    all_new = []
    categories = FEEDS if not category_filter else {
        k: v for k, v in FEEDS.items() if category_filter.lower() in k.lower()
    }

    for category, feeds in categories.items():
        print(f"\n🔍 Scanning: {category}")
        for feed in feeds:
            url = feed["url"]
            print(f"   📡 {feed['name']}...", end=" ")

            xml_text = fetch_url(url)
            if not xml_text and "fallback_url" in feed:
                xml_text = fetch_url(feed["fallback_url"])

            if not xml_text:
                print("SKIP")
                continue

            items = parse_rss(xml_text)
            new_items = []
            for item in items:
                norm = normalize_url(item["url"])
                if norm not in known_urls and is_build_related(item):
                    item["category"] = category
                    item["source"] = feed["name"]
                    item["found_at"] = datetime.now(timezone.utc).isoformat()
                    new_items.append(item)
                    known_urls.add(norm)

            print(f"{len(items)} items, {len(new_items)} NEW")
            all_new.extend(new_items)

    return all_new


def print_results(new_items: list[dict]):
    """Print findings in a readable format."""
    if not new_items:
        print("\n✅ No new Build 2026 announcements found.")
        return

    print(f"\n🆕 Found {len(new_items)} new announcement(s):\n")
    by_category = {}
    for item in new_items:
        by_category.setdefault(item["category"], []).append(item)

    for category, items in sorted(by_category.items()):
        print(f"  {'─' * 60}")
        print(f"  📁 {category} ({len(items)} new)")
        print(f"  {'─' * 60}")
        for item in items:
            date_str = item["date"][:16] if item["date"] else "Unknown"
            print(f"  📢 {item['title']}")
            print(f"     🔗 {item['url']}")
            print(f"     📅 {date_str}  |  Source: {item['source']}")
            if item["description"]:
                desc = item["description"][:120]
                print(f"     📝 {desc}...")
            print()


def main():
    dry_run = "--dry-run" in sys.argv
    category_filter = None
    if "--category" in sys.argv:
        idx = sys.argv.index("--category")
        if idx + 1 < len(sys.argv):
            category_filter = sys.argv[idx + 1]

    print("=" * 64)
    print("  🚀 Build 2026 Announcement Scanner")
    print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if category_filter:
        print(f"  🔎 Category filter: {category_filter}")
    if dry_run:
        print("  🧪 DRY RUN — results will not be saved")
    print("=" * 64)

    new_items = scan_feeds(category_filter)
    print_results(new_items)

    if new_items and not dry_run:
        # Update tracked file
        tracked = load_tracked()
        tracked["tracked_urls"] = list(set(
            tracked.get("tracked_urls", []) + [item["url"] for item in new_items]
        ))
        tracked["last_scan"] = datetime.now(timezone.utc).isoformat()
        tracked["total_tracked"] = len(tracked["tracked_urls"])
        save_tracked(tracked)

        # Save new findings
        clean_items = []
        for item in new_items:
            clean_items.append({
                "title": item["title"],
                "url": item["url"],
                "date": item["date"],
                "description": item["description"],
                "category": item["category"],
                "source": item["source"],
                "found_at": item["found_at"],
            })

        existing_findings = []
        if NEW_FINDINGS_FILE.exists():
            existing_findings = json.loads(NEW_FINDINGS_FILE.read_text(encoding="utf-8"))

        existing_findings.extend(clean_items)
        NEW_FINDINGS_FILE.write_text(
            json.dumps(existing_findings, indent=2), encoding="utf-8"
        )
        print(f"💾 Saved {len(new_items)} new items to {NEW_FINDINGS_FILE.name}")
        print(f"📊 Total tracked: {tracked['total_tracked']} URLs")


if __name__ == "__main__":
    main()
