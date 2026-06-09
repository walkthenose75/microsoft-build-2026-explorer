# Design: Interactive Build 2026 Explorer

## Architecture Overview

The application is a **single self-contained HTML file** with zero external dependencies, no build step, and no server. All CSS, JavaScript, and data (388 announcements) are inlined. No runtime fetch is required — the page renders instantly from embedded data.

```
┌─────────────────────────────────────────────────────┐
│                    index.html                        │
│  ┌──────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Inlined  │  │  Inlined JS  │  │  Inlined CSS  │  │
│  │  HTML     │  │  (data +     │  │  (Build 2026  │  │
│  │ (shell)  │  │   renderer)  │  │   theme)      │  │
│  └──────────┘  └──────┬───────┘  └───────────────┘  │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │  ALL_CATEGORIES  │                     │
│              │  (388 inline    │                     │
│              │   announcements)│                     │
│              └────────┬────────┘                     │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │  detectStatus() │                     │
│              │  + render()     │                     │
│              └─────────────────┘                     │
└─────────────────────────────────────────────────────┘
        ↓ Deployed via GitHub Pages
  walkthenose75.github.io/microsoft-build-2026-explorer/
```

## Data Architecture

### Inline Data Model

All 388 announcements are stored as a JavaScript constant `ALL_CATEGORIES`:

```javascript
const ALL_CATEGORIES = [
  {
    id: 'hardware-infrastructure',
    emoji: '🏗️',
    title: 'Hardware & Infrastructure',
    description: 'Core infrastructure services...',
    subcategories: [
      {
        name: 'Compute and hardware',
        announcements: [
          {
            title: 'Azure Cobalt 200 VMs',
            url: 'https://azure.microsoft.com/...',
            description: 'Arm-based VMs...'
          },
          // ...
        ]
      },
      // ...
    ]
  },
  // ... 26 more categories
];
```

### Category Metadata

`CATEGORY_META` provides emoji, accent color, and label for each of the 27 categories:

| Category | Emoji | Color |
|----------|-------|-------|
| Hardware & Infrastructure | 🏗️ | #F59E0B (amber) |
| Apps & Development | 🔧 | #10B981 (emerald) |
| Data & Analytics | 📊 | #3B82F6 (blue) |
| AI & Agents | 🤖 | #8B5CF6 (purple) |
| Security & Governance | 🔒 | #EF4444 (red) |
| Power Apps | ⚡ | #742774 (purple) |
| Power Automate | 🔄 | #0066FF (blue) |
| Copilot Studio | 🤖 | #00B7C3 (teal) |
| Power BI | 📊 | #F2C811 (gold) |
| Power Pages | 🌐 | #6264A7 (indigo) |
| Power Platform Admin | ⚙️ | #008272 (teal-dark) |
| Dataverse | 🗄️ | #00A4EF (sky) |
| Microsoft 365 Copilot | 🧠 | #6264A7 (indigo) |
| Agent 365 | 🤝 | #107C10 (green) |
| Microsoft Foundry | 🏭 | #0078D4 (azure) |
| D365 Finance & Operations | 💰 | #002050 (navy) |
| D365 Sales | 📈 | #004B50 (dark-teal) |
| D365 Customer Service | 🎧 | #8661C5 (violet) |
| D365 Field Service | 🔧 | #498205 (olive) |
| D365 Business Central | 🏢 | #00188F (royal) |
| D365 Contact Center | 📞 | #E3008C (pink) |
| D365 Customer Insights | 📣 | #FF8C00 (orange) |
| Developer Tools | 💻 | #0078D4 (azure) |
| Windows Platform | 🪟 | #0078D4 (azure) |
| Microsoft Teams | 💬 | #6264A7 (indigo) |
| Azure AI Services | 🧠 | #0078D4 (azure) |
| Microsoft Entra | 🔐 | #0078D4 (azure) |

### Status Badge Detection

`detectStatus(title, description, url)` auto-detects announcement status in priority order:

1. **Private Preview** → purple badge
2. **Open Source** → green badge
3. **Experimental** → orange badge
4. **Coming Soon** → yellow badge
5. **Limited Access** → blue badge
6. **GA / Generally Available** → green badge
7. **Preview / Public Preview** → blue badge
8. **URL contains `release-plan/2026wave1`** → amber "Wave 1" badge
9. **No match** → no badge (clean card)

Title cleanup regex strips status suffixes: `/\s*[—–-]\s*(GA|Generally Available|Preview|...)\s*$/i`

## Render Pipeline

```
init()
  └→ render({ categories: ALL_CATEGORIES, lastUpdated: '' })
       ├→ Build hero section (title, search, stats, keynote embed)
       ├→ Build sidebar nav (27 category buttons with count badges)
       └→ For each category:
            ├→ Category header (emoji, title, description, accent color)
            └→ For each subcategory:
                 └→ For each announcement:
                      ├→ detectStatus(title, desc, url) → badge
                      ├→ Clean title (strip status suffix)
                      ├→ Render card with link, badge, description
                      └→ Set data-search attribute for filtering
```

## Visual Design

### Color Palette (Build 2026 Theme — extracted from build.microsoft.com)

```
Background:       #0d1017  (deep blue-charcoal)
Surface:          #1a1f2e  (card backgrounds)
Surface hover:    #242a3d
Primary accent:   #FFB900  (Build gold)
Text primary:     #e2e5eb
Text secondary:   #8b92a5
Border:           rgba(255, 185, 0, 0.15)
Link color:       #FFB900
```

**Dark mode only** — light mode CSS preserved but toggle hidden (`style="display:none"`).

### Typography

```
Font family:  "Segoe UI", -apple-system, system-ui, sans-serif
Heading 1:    2.5rem, 700 weight
Heading 2:    1.75rem, 600 weight, category accent color
Body:         0.95rem, 400 weight
```

### Layout

```
Desktop (≥1024px):
┌──────────────────────────────────────────────────┐
│  HERO: Title + Search + Stats + Keynote          │
├──────────┬───────────────────────────────────────┤
│ SIDEBAR  │  CATEGORY SECTION (emoji + title)     │
│ (sticky) │  ┌────────┐ ┌────────┐ ┌────────┐    │
│          │  │ Card 1 │ │ Card 2 │ │ Card 3 │    │
│ 🏗️ Infra │  │ [badge]│ │        │ │ [GA]   │    │
│ 🔧 Apps  │  └────────┘ └────────┘ └────────┘    │
│ 📊 Data  │                                       │
│ 🤖 AI    │  CATEGORY SECTION                     │
│ 🔒 Sec   │  ...                                  │
│ ⚡ P.Apps│                                       │
│ ...      │                                       │
│ (27 cats)│                                       │
├──────────┴───────────────────────────────────────┤
│  FOOTER: Attribution + Source Credits            │
└──────────────────────────────────────────────────┘

Mobile (<768px):
┌─────────────────────┐
│ HERO                │
│ Search bar          │
├─────────────────────┤
│ ← Nav (scroll) →    │
├─────────────────────┤
│ ┌─────────────────┐ │
│ │ Card [Preview]  │ │
│ └─────────────────┘ │
│ ┌─────────────────┐ │
│ │ Card [GA]       │ │
│ └─────────────────┘ │
└─────────────────────┘
```

## Technology Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Framework | None (vanilla JS) | Self-contained, no build step |
| CSS | Inlined `<style>` | Single-file deployment |
| Data source | Inline JavaScript array | No runtime fetch, instant render |
| Status detection | Pattern matching (regex) | No manual tagging needed |
| Hosting | GitHub Pages | Free, serves from repo root |
| Theme | Build 2026 brand (dark only) | Extracted from build.microsoft.com |
| Source policy | Microsoft-only URLs | No LinkedIn, community blogs, or third-party sources |

## Interactivity

| Feature | Implementation |
|---------|---------------|
| **Search** | `input` event → filter cards by `data-search` attribute → toggle `display` → update count badges |
| **Category filter** | Click sidebar → toggle `data-active` on sections → update nav highlight |
| **Show All** | Reset all filters, show all 388 cards |
| **Bookmark scroll** | Click nav link → `scrollIntoView({ behavior: 'smooth' })` |
| **Active tracking** | `IntersectionObserver` highlights current category in sidebar |
| **Keyboard shortcuts** | `/` focuses search, `Escape` clears |

## Performance

- **Zero network requests** — all data inline, no fetch at page load
- No external CSS/JS/font resources (Segoe UI is a system font, falls back to system-ui)
- DOM built once, filtered via `display` toggling (no re-renders)
- Search debounced to 150ms
- ~2200 lines total, loads in <1 second
