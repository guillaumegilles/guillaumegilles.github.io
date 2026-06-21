# Feature Specification: Giscus Retro Blackboard Theme Integration

**Feature Branch**: `003-giscus-theme-integration`

**Created**: 2026-06-19

**Status**: Draft

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Seamless Visual Integration of the Comment Section (Priority: P1)

A blog reader scrolls to the bottom of a post and finds the comments and reactions widget. The widget looks like a natural part of the page — same dark surface tones, same chalk-coloured text, same retro terminal aesthetic — instead of appearing as a jarring white or generic-dark block.

**Why this priority**: The current giscus widget uses one of giscus's built-in light or dark themes, which clashes with the custom Retro Blackboard palette. This is the most visible pain point and the core reason this feature exists.

**Independent Test**: Open any published post page. Scroll to the comments section. Verify that the giscus widget background, text colour, and border style are visually consistent with the surrounding page content — without implementing any other story.

**Acceptance Scenarios**:

1. **Given** a visitor loads any post page, **When** the giscus widget finishes loading, **Then** the widget container uses one of the board surface colours (`#0D1610`–`#2F4636`) as its background — never white or a generic off-theme dark.
2. **Given** the giscus widget is visible, **When** the visitor reads comment text and metadata, **Then** all text renders in the chalk palette (`#D2CCC0` / `#EAE6DC` / `#7E8F82`), consistent with the page body text.
3. **Given** the giscus widget is visible, **When** the visitor looks at section borders or dividers inside the widget, **Then** they use the board-lighter border tone (`#2F4636`) — not a colour from the default giscus stylesheet.

---

### User Story 2 — Themed Interactive Elements (Priority: P2)

A visitor wants to react to a post (thumbs up, heart, etc.) or click "Sign in to comment". All interactive elements — emoji reaction buttons, submit buttons, links — use phosphor-green (`#5BDB6D`) as the primary accent, matching the site-wide link and primary colour.

**Why this priority**: Interactive affordances are the second most visible mismatch after backgrounds. Buttons and links in the default giscus theme use GitHub's blue (`#0969DA`), which is completely absent from the Retro Blackboard palette.

**Independent Test**: Load a post page in a browser while logged in to GitHub via giscus. Verify that reaction buttons, hover states, and the sign-in link all show the phosphor-green accent without any other theming change having been made.

**Acceptance Scenarios**:

1. **Given** the visitor views reaction emoji buttons, **When** they hover over or focus a button, **Then** the highlight or focus ring appears in phosphor-green (`#5BDB6D`), not blue or any other off-palette colour.
2. **Given** the visitor is not signed in, **When** the "Sign in with GitHub to comment" prompt is visible, **Then** the sign-in call-to-action uses phosphor-green as its primary colour.
3. **Given** the visitor submits a reaction, **When** the selected-state indicator is shown, **Then** it uses phosphor-green fill/border to confirm the active state.

---

### User Story 3 — Themed Comment Composition Area (Priority: P3)

A signed-in visitor writes a comment. The text area, Markdown preview, and submit button all look native to the Retro Blackboard theme: dark input fields, chalk-toned placeholder text, phosphor-green submit button, monospace font in the preview area.

**Why this priority**: The comment form is only visible after sign-in, so it affects fewer visitors than the read-only widget view. However, inconsistent styling during the act of writing is jarring for engaged users.

**Independent Test**: Sign in via giscus on a post page and open the comment composition form. Verify styling without any page reload.

**Acceptance Scenarios**:

1. **Given** a signed-in visitor opens the comment editor, **When** they view the text input area, **Then** the textarea background is a board surface tone, the border is `#2F4636`, and placeholder text is chalk-dim (`#7E8F82`).
2. **Given** the visitor switches to Markdown preview mode, **When** rendered content is displayed, **Then** code spans use the IBM Plex Mono font and the `#A8D8A0` terminal-green colour, consistent with the page's inline code style.
3. **Given** the visitor is ready to submit, **When** they view the submit button, **Then** it is styled with a phosphor-green background and board-darkest (`#0D1610`) text — matching the site's primary button convention.

---

### Edge Cases

- What happens when the custom theme stylesheet is temporarily unavailable (e.g., during a deploy)? The widget should still load using a fallback appearance rather than breaking the page layout.
- What happens if a visitor's browser blocks third-party iframes or GitHub assets? The comment section should fail gracefully — no broken layout, no JavaScript errors — and ideally show a brief "Comments unavailable" message in place of the widget.
- What happens on very small screens (≤375 px wide)? The widget must remain readable and not overflow the page column; horizontal scroll must not be introduced by the widget.
- What happens when giscus updates its internal HTML structure? The theme file targets stable CSS custom properties published in giscus's theming API, so minor structural changes should not break the theme.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The giscus widget on all post pages MUST render using a custom theme that replaces the default giscus light/dark appearance with colours drawn exclusively from the Retro Blackboard design tokens.
- **FR-002**: Widget backgrounds MUST use board surface colours (`#0D1610`, `#152119`, `#1C2E22`, `#253A2C`, or `#2F4636`).
- **FR-003**: All text content inside the widget (comments, metadata, labels, timestamps) MUST render in the chalk palette (`#D2CCC0` primary, `#EAE6DC` emphasis, `#7E8F82` secondary/muted).
- **FR-004**: All interactive elements (reaction buttons, links, submit controls, sign-in prompt) MUST use phosphor-green (`#5BDB6D`) as their primary accent colour; no blue (`#0969DA` or similar) from the default GitHub palette must remain visible.
- **FR-005**: Hover and focus states on interactive elements MUST use a phosphor-green highlight or glow consistent with the site's existing link-hover style.
- **FR-006**: The widget border and divider colours MUST use the board-lighter tone (`#2F4636`), providing a low-contrast separation consistent with the rest of the page.
- **FR-007**: Monospace text inside the widget (code snippets in comments) MUST use the IBM Plex Mono font family, matching the page's code block convention.
- **FR-008**: The custom theme MUST be applied before the widget becomes visible to the user to prevent a flash of the default (off-palette) styles.
- **FR-009**: The giscus configuration in `posts/_metadata.yml` MUST point to the custom theme resource; no per-post front matter changes should be required.
- **FR-010**: The custom theme resource MUST be version-controlled alongside the site source and deployed as part of the normal site build.

### Key Entities

- **Custom theme stylesheet**: A standalone CSS file containing only giscus-targeted style overrides using the Retro Blackboard design tokens. It is referenced by the giscus configuration and injected into the giscus iframe at load time.
- **Design tokens**: The canonical set of colour and typography values defined in `assets/dark.scss` (board surfaces, chalk text, accent colours, font families) that both the page theme and the giscus theme must share.
- **Giscus configuration**: The metadata block in `posts/_metadata.yml` (and/or `_quarto.yml`) that controls which GitHub repository, theme, and settings giscus uses on post pages.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A visitor looking at any post page cannot visually distinguish the giscus widget container from the surrounding page surface — the widget's background and text colours fall within the same Retro Blackboard palette used by the rest of the page.
- **SC-002**: Zero instances of GitHub-default blue, white, or off-palette colours are visible anywhere in the giscus widget during normal viewing on post pages.
- **SC-003**: All reaction buttons, links, and interactive controls in the widget show a phosphor-green accent on hover/focus; no other accent colour family appears.
- **SC-004**: The widget is fully readable at all viewport widths ≥ 320 px without introducing horizontal scroll or layout overflow.
- **SC-005**: The themed widget loads without a visible flash of default (off-palette) styling on a standard broadband connection.
- **SC-006**: The custom theme file is deployed as part of the normal site build with no additional manual steps required.

---

## Assumptions

- The site is dark-only; no light/dark mode toggle exists and no light-mode variant of the giscus theme is required.
- The giscus widget will remain configured in `posts/_metadata.yml` (repo, category, etc.); this feature changes only the visual theme parameter.
- The custom theme stylesheet will be hosted as a static asset within the same repository and served at a stable, publicly accessible URL (required by giscus's custom-theme mechanism, which fetches and injects the CSS into its iframe).
- giscus's published CSS custom properties and stable class names are used as styling targets; the theme file does not rely on undocumented or ephemeral internal selectors.
- Browser support matches the existing site baseline — modern evergreen browsers; no IE11 compatibility is needed.
- No changes to GitHub Discussions settings, giscus app permissions, or repository configuration are required; this feature is styling-only.
- Performance impact of adding one additional small CSS file fetch (the custom theme) is acceptable.
