# 🚀 Microsoft Build 2026 Explorer

An interactive, searchable index of **Microsoft Build 2026** and **2026 Release Wave 1** announcements — organized by product category, with auto-derived status badges and a self-refreshing news feed.

### 🔗 **[Open the live site →](https://walkthenose75.github.io/microsoft-build-2026-explorer/)**

> *Unofficial community resource — every announcement links to an official Microsoft source.*

---

## What it is

A single, self-contained `index.html` (no framework, no build step, no runtime fetch) that renders **396+ announcements across 27 categories** instantly from data embedded in the page. Browse by category, search across everything, and filter by release status.

- **143 GA · 139 Preview · 60 Wave 1** — status badges are auto-derived from each announcement's title, description, and URL (not hand-tagged).
- Dark theme, keyboard-friendly search, deep-linkable, mobile-responsive.
- Inspired by [Matt Hansen's Build 2026 List](https://github.com/matthansen0/matts-build-2026-list).

## Features

- **Sidebar category navigation** — jump to any of the 27 product areas (Hardware & Infrastructure, AI & Agents, Power Platform, Dynamics 365, Microsoft 365 Copilot, Foundry, Security, Windows, and more).
- **Full-text search** — instantly filter announcements by keyword.
- **Status filter bar** — show only GA, Preview, Wave 1, Coming Soon, Announced, or Open Source items.
- **Microsoft Vision view** — the opening keynote, the five-layer AI stack, and the headline narrative.
- **📰 Latest Microsoft News** — a rolling feed of the most recent posts from official Microsoft blogs.
- **🆕 Latest Updates per category** — newly discovered announcements surfaced under the relevant category.

## How the data stays current

The page is **fully self-contained and never fetches anything at runtime** — all data is baked into `index.html`. Freshness is handled by a daily **GitHub Action** that runs two Python helpers and commits the result, so GitHub Pages redeploys automatically with zero manual steps:

| Script | Updates | Marker block in `index.html` | Rendered as |
| --- | --- | --- | --- |
| `update_latest_news.py` | Most recent posts across official Microsoft feeds | `LATEST_NEWS` | "📰 Latest Microsoft News" section |
| `update_announcements.py` | New Build 2026-related items per category | `AUTO_ANNOUNCEMENTS` | "🆕 Latest Updates" subcategory |

Both scripts fetch **official Microsoft RSS feeds only**, dedupe against everything already on the page, and rewrite their marked block. The hand-curated `ALL_CATEGORIES` data is never touched.

> ⚠️ The `LATEST_NEWS` and `AUTO_ANNOUNCEMENTS` blocks are **machine-generated — do not hand-edit them**; the daily Action will overwrite changes. To curate content permanently, edit `ALL_CATEGORIES`.

`scan_announcements.py` is a separate local discovery helper that surfaces candidate announcements for manual review; its JSON outputs are not committed.

## Running locally

No dependencies to install — everything uses the Python 3 standard library, and the site has none.

**View the site:**
```bash
# Just open the file…
start index.html            # Windows
# …or serve the folder:
python -m http.server
# then visit http://localhost:8000
```

**Refresh the data manually (optional — the Action does this daily):**
```bash
python update_latest_news.py            # Bake in the latest news
python update_announcements.py          # Bake in new per-category announcements
python update_latest_news.py --dry-run  # Preview without writing
```

**Discover candidate announcements (local helper):**
```bash
python scan_announcements.py                       # Scan all feeds
python scan_announcements.py --dry-run             # Preview, no writes
python scan_announcements.py --category "Power Platform"
```

## Project structure

```
index.html                 # The entire app: inlined HTML/CSS/JS + embedded data
update_latest_news.py      # Bakes the LATEST_NEWS block from Microsoft RSS feeds
update_announcements.py    # Bakes per-category AUTO_ANNOUNCEMENTS from RSS feeds
scan_announcements.py      # Local discovery helper (outputs not committed)
build-2026-sources.md      # Source notes
openspec/                  # Spec-driven docs (proposal, design, tasks, specs)
.github/workflows/         # Daily "Update Site Data" Action
```

Inside `index.html`, the key structures are `ALL_CATEGORIES` (the curated data model — categories → subcategories → `{ title, url, description }`), `CATEGORY_META` (per-category emoji/color/label), and `detectStatus()` (derives the status badge).

## Conventions

- **Microsoft-only sources.** Every announcement URL must resolve to an official Microsoft domain (`learn.microsoft.com`, `devblogs.microsoft.com`, `techcommunity.microsoft.com`, `azure.microsoft.com`, `blogs.windows.com`, etc.). No third-party roundups.
- **Keep `index.html` self-contained.** No framework, bundler, package.json, external CSS/JS, or runtime `fetch`.
- **Don't hand-write status badges.** Let `detectStatus()` derive them from text/URL patterns.
- Changes are documented under `openspec/` (spec-driven workflow).

## Contributing

To add or correct a **curated** announcement, edit the relevant category's `announcements` array in `ALL_CATEGORIES` inside `index.html` (`{ title, url, description }`, official Microsoft URL only), then open a PR. If you add a new category, also update `CATEGORY_META` and the counts in the page `<title>`/meta tags.

For automatically surfaced items, just let the daily Action run — or run the updater scripts above.

## Credits

- Originally inspired by and based on **[Matt Hansen's //Build 2026 List](https://github.com/matthansen0/matts-build-2026-list)**.
- Additional data from [Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/), [official Microsoft blogs](https://news.microsoft.com/build-2026/), and [DevBlogs](https://devblogs.microsoft.com/).

---

*Unofficial community resource. All links point to official Microsoft sources. Not affiliated with or endorsed by Microsoft.*
