# Proposal: Interactive Build 2026 Explorer

## Intent

Build the **most comprehensive, interactive Microsoft Build 2026 announcements explorer** — a fully self-contained HTML page with **303 announcements across 22 categories**, sourced exclusively from official Microsoft channels.

Originally inspired by [Matt Hansen's Build 2026 List](https://github.com/matthansen0/matts-build-2026-list) (130 announcements, 5 categories), the explorer was expanded with 173 additional announcements covering Power Platform, Dynamics 365, Copilot Studio, Microsoft Foundry, Agent 365, and Microsoft 365 Copilot — product families entirely absent from the original list.

## Problem

- No single resource covers all Build 2026 announcements across Azure, Power Platform, D365, and M365.
- Matt's list covers Azure infrastructure, apps, data, AI, and security well — but has **zero** Power Platform, D365, M365 Copilot, or Foundry announcements.
- Long markdown lists are hard to browse — no filtering, search, or visual hierarchy.
- Community roundup blogs mix opinions with announcements and link to non-Microsoft sources.

## Scope

### In Scope

- **Single self-contained `index.html`** — no build step, no external dependencies, no runtime fetch.
- **303 announcements** organized into **22 categories** with **60+ subcategories**.
- **All 303 URLs** verified as official Microsoft sources only (learn.microsoft.com, devblogs.microsoft.com, techcommunity.microsoft.com, azure.microsoft.com, news.microsoft.com, etc.).
- **Status badges** auto-detected: GA, Preview, Private Preview, Coming Soon, Wave 1, Open Source, Experimental, Limited Access.
- Microsoft Build 2026 conference branding (dark theme, Build gold #FFB900 accent, extracted from build.microsoft.com).
- Satya Nadella keynote embed with video, blog, transcript, and highlights links.
- Category sidebar navigation with count badges and smooth-scroll bookmarks.
- Real-time text search across all announcement titles and descriptions.
- Responsive layout (desktop sticky sidebar + mobile horizontal scroll).
- Attribution: "Inspired by Matt Hansen's Build 2026 List · Additional data from Microsoft Learn, official blogs, & DevBlogs."
- Hosted via **GitHub Pages** at `walkthenose75.github.io/microsoft-build-2026-explorer/`.
- **OpenSpec documentation** of the full project, including comprehensive source index.
- **Python RSS scanner** (`scan_announcements.py`) for daily discovery of new announcements (local-only, not committed).

### Out of Scope

- Server-side backend or database.
- Build toolchain (Webpack, Vite, etc.).
- User accounts, authentication, or persistence.
- Editing or contributing announcements from the UI.
- Non-Microsoft sources (LinkedIn, community blogs, third-party roundups).

## Approach

1. Research all Build 2026 announcements from official Microsoft sources (Learn docs, DevBlogs, TechCommunity, release plans, official blogs).
2. Create `index.html` with all 303 announcements as inline JavaScript data — fully self-contained.
3. Implement interactive UI: keynote banner, filter pills, sidebar nav, card grid, real-time search.
4. Auto-detect announcement status (GA/Preview/etc.) from title, description, and URL patterns.
5. Apply Build 2026 brand theme extracted from build.microsoft.com.
6. Host on GitHub Pages at `walkthenose75/microsoft-build-2026-explorer`.
7. Document everything with OpenSpec, including comprehensive source index.

## Success Criteria

- ✅ Page displays all 303 announcements across 22 categories within 2 seconds.
- ✅ Users can filter to any category in one click.
- ✅ Search narrows results in real time as the user types.
- ✅ Keynote video is embedded and accessible with one click.
- ✅ All 303 URLs resolve to official Microsoft domains only.
- ✅ Status badges render correctly for GA, Preview, Wave 1, and other statuses.
- ✅ Page renders correctly at mobile (320px) and desktop (2560px) widths.
- ✅ GitHub Pages deploys and serves the page successfully.
