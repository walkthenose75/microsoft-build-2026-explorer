# Tasks

## ✅ 1. Project Setup
- [x] 1.1 Initialize git repository in project directory
- [x] 1.2 Install and initialize OpenSpec with GitHub Copilot tooling
- [x] 1.3 Create change proposal, specs, design, and tasks documents
- [x] 1.4 Create GitHub repository `walkthenose75/microsoft-build-2026-explorer`
- [x] 1.5 Enable GitHub Pages on the repository

## ✅ 2. Data Collection & Research
- [x] 2.1 Extract Matt Hansen's 130 announcements (5 categories) as structured data
- [x] 2.2 Research Power Platform announcements (Power Apps, Power Automate, Copilot Studio, Power BI, Power Pages, Admin, Dataverse)
- [x] 2.3 Research Dynamics 365 announcements (Finance, Sales, Customer Service, Field Service, Business Central, Contact Center, Customer Insights)
- [x] 2.4 Research Microsoft 365 Copilot and Agent 365 announcements
- [x] 2.5 Research Microsoft Foundry announcements (Agent Service, ASSERT, ACS, tools, models)
- [x] 2.6 Deep dive: Copilot Studio (11 → 37 items across 7 subcategories)
- [x] 2.7 Deep dive: Microsoft Foundry (11 → 35 items across 5 subcategories)
- [x] 2.8 Audit all 303 URLs — verify Microsoft-only sources, fix 5 non-Microsoft URLs
- [x] 2.9 Record all 82+ source references in tracking database

## ✅ 3. Self-Contained HTML Application
- [x] 3.1 Convert from fetch-based (runtime GitHub API) to fully self-contained inline data
- [x] 3.2 Remove `parseMarkdown()` function and `REPO_URL`/`REPO_LINK` constants
- [x] 3.3 Embed all 303 announcements as `ALL_CATEGORIES` JavaScript constant
- [x] 3.4 Simplify `init()` to render directly from inline data
- [x] 3.5 Update loading text from "Fetching from GitHub..." to "Loading announcements..."

## ✅ 4. Visual Design & Theming
- [x] 4.1 Extract exact brand colors from build.microsoft.com via Playwright browser automation
- [x] 4.2 Apply Build 2026 theme: dark bg #0d1017, gold accent #FFB900, surface #1a1f2e
- [x] 4.3 Force dark-only mode (light toggle hidden, CSS preserved)
- [x] 4.4 Assign unique accent colors per category (22 categories × 22 colors)
- [x] 4.5 Style announcement cards with surface color, border glow, and hover effect
- [x] 4.6 Add responsive breakpoints: mobile (<768px), tablet, desktop (≥1024px)
- [x] 4.7 Style navigation for sticky sidebar (desktop) and horizontal scroll bar (mobile)

## ✅ 5. Status Badges
- [x] 5.1 Implement `detectStatus(title, description, url)` auto-detection function
- [x] 5.2 Create CSS for 7 badge types: GA, Preview, Private Preview, Coming Soon, Open Source, Experimental, Limited Access
- [x] 5.3 Add Wave 1 badge for URLs containing `release-plan/2026wave1`
- [x] 5.4 Strip status suffix from display title for cleaner cards
- [x] 5.5 Leave items without explicit status clean (no badge) per user decision

## ✅ 6. Interactive Features
- [x] 6.1 Implement live search: filter cards by title/description, update counts, debounce 150ms
- [x] 6.2 Implement category filter: click sidebar button → show only that category
- [x] 6.3 Implement "Show All" button to reset filters
- [x] 6.4 Implement smooth-scroll bookmark navigation
- [x] 6.5 Highlight active category in sidebar during scroll (IntersectionObserver)
- [x] 6.6 Add keyboard shortcuts: `/` to focus search, `Escape` to clear
- [x] 6.7 Embed Satya Nadella keynote with video, blog, transcript, and highlights links

## ✅ 7. Attribution & Credits
- [x] 7.1 Update footer: "Inspired by Matt Hansen's Build 2026 List"
- [x] 7.2 Update sidebar: credit Matt + Microsoft sources
- [x] 7.3 Remove direct fork dependency — standalone repo

## ✅ 8. Repository & Deployment
- [x] 8.1 Create `walkthenose75/microsoft-build-2026-explorer` repository
- [x] 8.2 Delete fork `walkthenose75/matts-build-2026-list`
- [x] 8.3 Clean up git remotes to single `origin`
- [x] 8.4 Commit and push `index.html` to GitHub
- [x] 8.5 Verify GitHub Pages deployment at walkthenose75.github.io/microsoft-build-2026-explorer/

## ✅ 9. OpenSpec Documentation
- [x] 9.1 Update proposal.md to reflect 303-item self-contained architecture
- [x] 9.2 Update design.md with inline data model, status badges, and Build 2026 theme
- [x] 9.3 Update tasks.md (this file) with complete task history
- [x] 9.4 Update spec.md with current requirements and scenarios
- [x] 9.5 Create comprehensive sources reference document
- [x] 9.6 Commit OpenSpec docs to repository

## ✅ 10. Tooling (Local-Only, Not Committed)
- [x] 10.1 Create `scan_announcements.py` — Python RSS scanner for daily discovery (25+ feeds)
- [x] 10.2 Test scanner — verified working, no pip dependencies required

## 📋 Future Work
- [ ] Add newly discovered announcements from deep research (Dev Tools, Teams, Windows, Entra, Graph)
- [ ] Consider new categories: Developer Tools, Microsoft Teams, Windows, Microsoft Entra, Microsoft Graph
