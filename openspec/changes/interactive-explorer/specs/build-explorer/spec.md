# Spec: Build 2026 Interactive Explorer

## Requirements

### Requirement: Self-Contained Data

The system MUST embed all announcement data inline as JavaScript — no runtime fetch, no external dependencies.

#### Scenario: Instant render
- GIVEN a user navigates to the Build Explorer page
- WHEN the page loads
- THEN all 303 announcements render from inline `ALL_CATEGORIES` data
- AND no network requests are made for announcement data
- AND the page renders in under 2 seconds

---

### Requirement: Category Navigation

The system SHALL provide persistent navigation elements that allow users to jump directly to any of the 22 announcement categories.

#### Scenario: Click category bookmark
- GIVEN a user is viewing the page
- WHEN the user clicks a category name in the sidebar navigation
- THEN the page smooth-scrolls to that category's section
- AND the active category is visually highlighted in the navigation

#### Scenario: All categories visible by default
- GIVEN a user has just loaded the page
- WHEN no filters are active
- THEN all 22 categories and all 303 announcements are visible

---

### Requirement: Live Search

The system SHALL provide a text search input that filters announcements in real time.

#### Scenario: Search matches
- GIVEN announcements are displayed
- WHEN the user types into the search box
- THEN only announcements whose title OR description contains the search text are shown
- AND the count badges update to reflect the filtered count

#### Scenario: No matches
- GIVEN a user has typed a search query
- WHEN no announcements match
- THEN the system displays "No announcements match your search"

#### Scenario: Clear search
- GIVEN a user has an active search query
- WHEN the user clears the search box (or presses Escape)
- THEN all announcements are restored

#### Scenario: Keyboard shortcut
- GIVEN the page is loaded
- WHEN the user presses `/`
- THEN the search box receives focus

---

### Requirement: Category Filtering

The system SHALL provide toggle buttons for each category that show/hide entire category sections.

#### Scenario: Toggle category
- GIVEN all categories are visible
- WHEN the user clicks a category filter button
- THEN only that category's announcements are shown
- AND other categories are hidden

#### Scenario: Show all
- GIVEN the user has filtered to a single category
- WHEN the user clicks "Show All"
- THEN all categories and announcements are restored

---

### Requirement: Status Badges

The system SHALL auto-detect and display status badges on announcement cards.

#### Scenario: GA badge
- GIVEN an announcement title or description contains "GA" or "Generally Available"
- WHEN the card renders
- THEN a green "GA" badge appears inline after the title

#### Scenario: Preview badge
- GIVEN an announcement title or description contains "Preview" or "Public Preview"
- WHEN the card renders
- THEN a blue "Preview" badge appears inline after the title

#### Scenario: Wave 1 badge
- GIVEN an announcement URL contains `release-plan/2026wave1`
- WHEN the card renders
- THEN an amber "Wave 1" badge appears inline after the title

#### Scenario: No status
- GIVEN an announcement has no detectable status
- WHEN the card renders
- THEN no badge appears (clean card)

#### Scenario: Title cleanup
- GIVEN an announcement title ends with a status suffix (e.g., "Feature X — GA")
- WHEN the card renders
- THEN the status suffix is stripped from the display title
- AND the badge conveys the status instead

---

### Requirement: Announcement Cards

Each announcement SHALL be displayed as a card with its title (linked to the source URL), optional status badge, and a short description.

#### Scenario: Click announcement link
- GIVEN an announcement card is visible
- WHEN the user clicks the announcement title
- THEN a new browser tab opens to the official Microsoft source URL

#### Scenario: Microsoft-only URLs
- GIVEN any announcement in the explorer
- WHEN a user clicks its link
- THEN the URL resolves to an official Microsoft domain (learn.microsoft.com, devblogs.microsoft.com, techcommunity.microsoft.com, azure.microsoft.com, news.microsoft.com, blogs.microsoft.com, microsoft.com, github.blog, etc.)

---

### Requirement: Keynote Embed

The system SHALL embed the Satya Nadella Build 2026 opening keynote.

#### Scenario: Keynote visible
- GIVEN the page has loaded
- WHEN a user views the hero section
- THEN the keynote video player is embedded
- AND links to the blog post, transcript, and highlights are provided

---

### Requirement: Responsive Layout

The system SHALL render correctly on screens from 320px to 2560px wide.

#### Scenario: Mobile viewport
- GIVEN a device width under 768px
- WHEN the page renders
- THEN the navigation collapses into a horizontal scrollable bar
- AND cards stack in a single column

#### Scenario: Desktop viewport
- GIVEN a device width of 1024px or wider
- WHEN the page renders
- THEN the navigation is a sticky sidebar
- AND cards are arranged in a multi-column grid

---

### Requirement: Build 2026 Theming

The page SHALL use the Microsoft Build 2026 visual identity.

#### Scenario: Visual consistency
- GIVEN the page has loaded
- WHEN a user views the page
- THEN the page uses a dark background (#0d1017) with gold (#FFB900) accents
- AND typography is Segoe UI with clear heading hierarchy
- AND category sections use distinct accent colors with matching emoji icons
- AND dark mode is forced (no light mode toggle visible)

---

### Requirement: Attribution

The page SHALL credit Matt Hansen as inspiration and list official Microsoft sources.

#### Scenario: Attribution visible
- GIVEN the page has loaded
- WHEN a user views the footer
- THEN text reads "Inspired by Matt Hansen's Build 2026 List"
- AND additional text credits "Microsoft Learn, official blogs, & DevBlogs"
- AND the sidebar credits Matt Hansen and lists Microsoft source types
