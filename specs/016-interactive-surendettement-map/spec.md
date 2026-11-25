# Feature Specification: Interactive Surendettement Map — Hybrid Cartography for the overindebtedness Post

**Feature Branch**: `016-interactive-surendettement-map`

**Created**: 2026-11-20

**Status**: Draft

**Input**: User description: "Based on the brainstorming session on
the overindebtedness post (formerly posts/dataviz-bdf/), create the spec
for: format option C (hybrid —
interactive explorer plus a static hero map); fix the encoding choices
(rate-based levels, quantile classes, diverging variation scale); build
the full interactive explorer and replace the static matplotlib maps in
the cartography section; reframe the evolution by fixing the BdF API so
2018 is included; map only for now (no linked scatter)."

## Context

`posts/overindebtedness/index.qmd` (moved from `posts/dataviz-bdf/`; hero
image now `assets/posts/overindebtedness.jpg`, default site theme applies)
currently renders four static matplotlib
choropleths (over-indebtedness level, evolution, four explanatory
variables, fragility score). Two concrete defects motivate this feature:

1. The evolution map compares against a hardcoded 2018, but the
   processed dataset starts in 2019, so that map silently never renders.
2. The level map auto-switches between raw counts and a rate via a
   `median < 100` heuristic instead of a fixed, documented encoding.

The data also tells a story the current narrative misses: national
filings fell from 143,091 (2019) to a trough of 108,748 (2020) then
rebounded to 134,807 (2024) — a rise of about +24% from the trough, with
the strongest rebounds in departments such as Haute-Corse, Corse-du-Sud,
Haute-Garonne and Drôme. The interactive map should make that rise
explorable year by year.

**Explicitly out of scope**: linked map-to-scatter brushing ("map only"
decision); DOM-TOM; spatial regression models; any change to the OLS
modelling sections; the existing bivariate scatter plots stay as they are.

## Clarifications

### Session 2026-11-20

- Q: When the reader selects an indicator whose values do not change across
  years (chômage, pauvreté, part des locataires), how should the year
  slider behave? → A: Option A — the year slider and play button stay
  visible but have no effect on the map of a single-millésime indicator,
  and a badge next to the variable selector shows the indicator's actual
  source millésime (encoded as FR-022).
- Q: What level of keyboard and screen-reader support must the interactive
  SVG map provide? → A: Option A — every department polygon is
  keyboard-focusable and Enter-activatable with an `aria-label` stating
  name, value and rank; all controls are keyboard-operable; a collapsible
  data table lists the 96 departments' values for the current
  variable/year as a text alternative (encoded as FR-023).
- Q: What page-weight budget should the inlined map data respect? → A:
  Option A — total inlined map payload (geometry + data) ≤ ~200 KB:
  coordinates rounded to 3 decimals, only `code`/`nom` properties kept
  (encoded in FR-017 and SC-010).
- Q: What should the static hero/preview image show? → A: Option B — the
  in-section no-JS fallback stays the latest-year level map, and the post
  preview image (`assets/posts/overindebtedness.jpg`) is the variation map
  from the trough year to the latest year, so the rebound is visible on the
  blog index (encoded in FR-016).

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Reader sees the territorial level of over-indebtedness (Priority: P1)

A reader opens the cartography section of the overindebtedness post and
sees one map of metropolitan France where each of the 96 departments is
colored by the over-indebtedness filing rate (filings per 10,000
inhabitants) for the most recent year, with a readable legend, source
and year.

**Why this priority**: This is the core visual of the post; without it
the section has no anchor. It replaces the four static choropleths with
one clear, correctly encoded map.

**Independent Test**: Render the page with JavaScript enabled and
inspect the map in its default state: 96 departments colored, legend
with units, title, source and year visible. No other story needed.

**Acceptance Scenarios**:

1. **Given** the rendered post, **when** the cartography section loads,
   **then** the map shows all 96 metropolitan departments colored by the
   filing rate for the latest available year.
2. **Given** the default view, **when** the reader hovers any
   department, **then** a tooltip shows the department name, the rate,
   its rank out of 96, the raw filing count, the change vs the previous
   year, and its z-score vs the national mean.
3. **Given** the default view, **when** the reader reads the legend and
   caption, **then** the unit (filings per 10,000 inhabitants), the
   source (Banque de France) and the year are all stated.

---

### User Story 2 — Reader explores the rise year by year (Priority: P1)

A reader moves a year slider (or presses play) from 2018 to 2024 and
watches the map animate, seeing the 2020 trough followed by the rebound
in filings through 2024.

**Why this priority**: "The rise of over-indebtedness filings" is the
post's headline story; the animation is what makes it legible. This
story requires the BdF download fix (2018) to cover the full period.

**Independent Test**: With the pipeline re-run including 2018, move the
slider across all years and press play; verify the map updates each
year and the caption states the trough and rebound figures.

**Acceptance Scenarios**:

1. **Given** the explorer, **when** the reader moves the year slider,
   **then** the map re-colors without a page reload for every year
   2018–2024.
2. **Given** the explorer, **when** the reader presses play, **then** the
   map animates chronologically and can be interrupted by moving the
   slider.
3. **Given** the full 2018–2024 series, **when** the reader reads the
   evolution caption, **then** the trough year/value and the rebound to
   the latest year are stated and were computed programmatically from
   the dataset (no hand-typed figures).

---

### User Story 3 — Reader compares economic indicators and variation (Priority: P2)

A reader switches the map to an economic indicator (unemployment rate,
poverty rate, RSA share, renter share, fragility score) and to a
variation mode (vs 2018 or vs previous year, in %) to identify which
departments drove the recent rise and where vulnerability concentrates.

**Why this priority**: This is what links filings to economic conditions
at department level — the post's research question — and the variation
mode is the only view that reveals the post-2020 risers (Corsica,
Haute-Garonne, Drôme, …).

**Independent Test**: Switch variable and mode controls; verify the map,
legend, units and caption update accordingly and top risers/fallers are
labeled.

**Acceptance Scenarios**:

1. **Given** the variable selector, **when** the reader picks each of
   unemployment, poverty, RSA, renter share and fragility score,
   **then** the map re-colors with that indicator's own unit, source and
   year in the legend/caption.
2. **Given** a variation mode vs the first year, **when** the reader
   selects it, **then** the scale is diverging around zero and the top 5
   risers and top 5 fallers since that year are labeled on the map.
3. **Given** the variation vs previous year mode, **when** the reader
   selects it at a given year, **then** each department shows its
   year-over-year change in %.

---

### User Story 4 — Reader pins a department and sees its trajectory (Priority: P2)

A reader clicks a department (e.g. Haute-Garonne) and a side panel
pins it, showing its 2018–2024 sparkline for filings and for the
currently selected indicator, with the underlying values.

**Why this priority**: Pinning turns the map from a static picture into
a per-territory investigation tool, at low cost once tooltips exist.

**Independent Test**: Click any department; verify the panel appears
with two sparklines and values; click another department; verify the
panel updates; click again to unpin.

**Acceptance Scenarios**:

1. **Given** the explorer, **when** the reader clicks a department,
   **then** a panel pins that department and shows its yearly series
   (2018–2024) for the filing rate and the selected indicator.
2. **Given** a pinned department, **when** the reader changes the year
   slider or the variable, **then** the panel's series stay complete and
   the map highlight follows the pinned department.
3. **Given** a pinned department, **when** the reader clicks it again,
   **then** the panel unpins.

---

### User Story 5 — Reader without JavaScript still gets the picture (Priority: P3)

A reader with JavaScript disabled still sees a static map of the filing
rate for the latest year, and a social-media crawler fetching the post's
preview image (`assets/posts/overindebtedness.jpg`) gets the rebound
variation map (trough → latest year).

**Why this priority**: Hybrid format decision: the interactive explorer
replaces the in-section static maps, but one static hero map remains for
the og:image and the no-JS fallback. Not blocking the interactive core.

**Independent Test**: Render the page, disable JavaScript, and verify
the static hero map and an explanatory note are visible; check that
`assets/posts/overindebtedness.jpg` is regenerated from the latest year.

**Acceptance Scenarios**:

1. **Given** JavaScript disabled, **when** the cartography section is
   viewed, **then** a static choropleth of the latest-year filing rate
   plus a note pointing to the interactive version (for JS-enabled
   readers) are displayed.
2. **Given** the rendered site, **when** the post card is previewed,
   **then** the preview image is the trough→latest-year variation
   (rebound) map.

---

### User Story 6 — Analyst reproduces the map end to end (Priority: P3)

An analyst re-runs the data pipeline (now including 2018 from the BdF
WebStat API) and `quarto render`, and gets the same map and figures
without manual edits.

**Why this priority**: Reproducibility is a standing project principle;
the 2018 gap must be fixed in the versioned scripts, not by hand.

**Independent Test**: Run the documented pipeline from a clean checkout
(`posts/overindebtedness/scripts/`: download → clean → merge → validate →
render); verify the dataset covers 2018–2024 × 96 departments and the
render exits 0.

**Acceptance Scenarios**:

1. **Given** a clean environment, **when** the documented pipeline runs,
   **then** the surendettement series covers 2018–2024 for all 96
   departments and the evolution view uses the earliest year
   dynamically.
2. **Given** the pipeline outputs, **when** `quarto render` runs on the
   post, **then** it exits 0 and the committed freeze cache lets CI
   render without re-executing Python.

---

### Edge Cases

- What happens with variables that have a single source millésime?
  → Confirmed in the current dataset: chômage, pauvreté (FiLoSoFi) and
  renter share (RP) are constant across 2019–2024 for all 96 departments.
  The year slider has no effect on their map and a badge shows the actual
  source millésime (FR-022).
- What happens when a department has no value for a variable/year? →
  The polygon gets a distinct neutral "données manquantes" style and the
  tooltip says so; it is excluded from ranks.
- How are Corse codes 2A/2B handled? → Same zero-padded code matching as
  today; both must render.
- What if the 2018 BdF fetch still fails after the fix? → The explorer
  falls back to the earliest available year and prints a visible
  warning; the pipeline reports the gap in the coverage report.
- What if JavaScript is disabled? → Static hero map + note (User Story
  5).
- What about narrow screens? → The map scales (responsive viewBox) and
  the controls stack vertically; tooltips become tap-to-show.
- What about DOM-TOM? → Excluded, with an explicit note on the map.
- What happens if the reader presses play while dragging the slider? →
  The animation pauses and the manual position wins.
- The Gini index (~20% coverage) is excluded from the variable selector.

## Requirements *(mandatory)*

### Functional Requirements

#### Data pipeline (BdF API fix)

- **FR-001**: The Banque de France WebStat download MUST be extended to
  fetch the 2018 filings by department (and to detect the earliest year
  actually published), so the analytical dataset covers 2018–2024 × 96
  metropolitan departments. All transformation MUST happen in the
  versioned scripts; raw files MUST NOT be edited by hand.
- **FR-002**: Every evolution view MUST compute its reference year
  dynamically as the earliest available year (no hardcoded year), and
  the trough/rebound figures quoted in the text MUST be computed
  programmatically from the dataset.

#### Encoding fixes

- **FR-003**: Level maps MUST always encode the **rate** (filings per
  10,000 inhabitants); raw filing counts MUST appear only in tooltips
  and the pinned panel, never as the mapped color.
- **FR-004**: Level classification MUST use quantile (or equivalent
  Jenks) classes, 5 to 7 classes, and the legend MUST show the class
  ranges with units.
- **FR-005**: Variation modes (vs reference year, vs previous year) MUST
  use a diverging color scale centered on 0 (percent change).
- **FR-006**: Color palettes MUST be colorblind-safe and adapted to the
  page theme; missing data MUST have a distinct neutral style labeled
  "données manquantes".
- **FR-007**: The variable selector MUST offer: filing rate,
  unemployment rate, poverty rate, RSA share, renter share, fragility
  score. The Gini index MUST NOT be offered in the selector (the six
  indicators answer the research questions; Gini stays in the EDA
  section).

#### Interactive explorer (replaces the static maps in the cartography section)

- **FR-008**: The four static choropleth figures in the cartography
  section MUST be replaced by a single interactive map explorer
  implemented as a native Observable JS (`{ojs}`) block, plus one static
  hero map (see FR-016).
- **FR-009**: The explorer MUST provide a year slider covering every
  available year (2018–2024 after FR-001) and a play button that animates
  the years chronologically; manual slider input MUST interrupt the
  animation.
- **FR-010**: The explorer MUST provide a variable selector with the six
  indicators of FR-007.
- **FR-011**: The explorer MUST provide a mode toggle: level | variation
  vs first year (%) | variation vs previous year (%) | rank.
- **FR-012**: Hovering a department MUST show a tooltip with: name, code,
  current value with unit, rank out of 96, raw filing count when the
  variable is the filing rate, change vs previous year, and z-score vs
  the national mean for the current year.
- **FR-013**: Clicking a department MUST pin it and open a side panel
  with its 2018–2024 sparkline for the filing rate and for the selected
  indicator, with underlying yearly values; clicking again unpins.
- **FR-014**: Variation modes MUST label the top 5 risers and top 5
  fallers directly on the map.
- **FR-015**: Every explorer state (variable × mode × year) MUST display:
  a descriptive title, a legend with units, the data source and year, and
  a one-line interpretive caption. The caption figures MUST be computed
  from the data, not hand-typed.
- **FR-022**: For indicators whose values are constant across years
  (single source millésime — currently chômage, pauvreté and renter
  share), the year slider and play button MUST remain visible but MUST
  NOT change the map, and a badge next to the variable selector MUST
  show the indicator's actual source millésime (e.g. « INSEE 2021 »).
- **FR-023**: The map MUST be fully operable by keyboard and exposed to
  screen readers: every department polygon MUST be focusable and
  Enter-activatable with an `aria-label` stating name, value and rank;
  all controls (year slider, play, variable selector, mode toggle)
  MUST be keyboard-operable; and a collapsible data table MUST list the
  96 departments' values for the current variable and year as a text
  alternative.

#### Static hero map and fallback

- **FR-016**: A static choropleth of the latest-year filing rate (same
  encoding rules FR-003–FR-006) MUST remain in the section as the no-JS
  fallback with a note. In addition, a static variation map (trough year
  → latest year, in %, diverging scale per FR-005) MUST be generated as
  the post's preview image (`assets/posts/overindebtedness.jpg`); the
  trough year MUST be computed from the data (2020 in the current
  dataset).

#### Site rules (constitution)

- **FR-017**: The map MUST NOT initiate any runtime network request to
  third-party hosts: no tile servers, no CDN, no analytics. Geometry and
  the panel dataset MUST be inlined into the rendered page at build time
  (from the versioned data files), so the widget works offline and
  tracking-free. To keep the page light, geometry coordinates MUST be
  rounded to 3 decimals and only `code`/`nom` properties kept, so the
  total inlined map payload (geometry + data) stays ≤ ~200 KB.
- **FR-018**: Widget styling MUST use CSS classes through the site's
  single styling entry point; the `.qmd` MUST NOT contain inline
  `style=` attributes or page-level `<style>` blocks for the widget.
- **FR-019**: The post front matter MUST reference existing files so the
  render gate passes: the current `image: ../../assetsoverindebtedness.jpg`
  path is broken (missing `posts/`) and MUST be corrected to
  `../../assets/posts/overindebtedness.jpg`. The post now uses the site's
  default light theme, so the static hero map MUST be styled for that
  theme (the dark «blackboard» matplotlib palette no longer matches the
  page).
- **FR-020**: Linked map↔scatter brushing is OUT of scope; the existing
  bivariate scatter section MUST remain unchanged.
- **FR-021**: Prose in the modified `.qmd` MUST wrap at 80 characters;
  `quarto render` MUST exit 0 and the `_freeze/` cache MUST be committed
  with the source changes.

### Key Entities *(include if feature involves data)*

- **Département**: geographic unit of analysis; 96 metropolitan
  departments, identified by 2-character INSEE code (including 2A/2B);
  DOM-TOM excluded.
- **Millésime**: reference year of a data point; after FR-001 the range
  is 2018–2024 for the surendettement series.
- **Indicateur cartographique**: a mappable variable with unit, source
  and millésime(s): filing rate (per 10,000 inhabitants), unemployment
  rate (%), poverty rate (%), RSA share (%), renter share (%),
  fragility score (z-score composite).
- **Mode d'affichage**: level | variation vs first year | variation vs
  previous year | rank.
- **Géométrie départementale**: the GeoJSON polygon per department,
  inlined into the page with rounded coordinates and only code/nom
  properties.
- **Carte hero statique**: the single static choropleth kept for og:image
  and no-JS fallback.
- **Score de fragilité**: existing composite
  (0.3×z_chômage + 0.3×z_pauvreté + 0.2×z_RSA + 0.2×z_locataires), reused
  unchanged as one of the selectable indicators.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The interactive map renders 96/96 departments for every
  year 2018–2024, verifiable by moving the slider to each year.
- **SC-002**: Changing year, variable or mode updates the map without a
  page reload, and every department polygon shows a tooltip on hover
  (manual check across all 96).
- **SC-003**: With JavaScript disabled, the static hero map and its note
  are visible in the cartography section, and the post's preview image is
  the rebound variation map (trough → latest year).
- **SC-004**: The browser's network panel shows zero requests to
  third-party hosts initiated by the map widget.
- **SC-005**: After re-running the pipeline, the surendettement series
  contains 2018–2024 × 96 rows, and the evolution caption's trough and
  rebound figures match the dataset (e.g. trough 2020 at 108,748
  filings, 2024 at 134,807, ≈ +24%).
- **SC-006**: The top-5 risers/fallers labeled in variation mode match
  the ranking computed from the analytical dataset.
- **SC-007**: `quarto render` on the post exits 0, the rendered page
  produces no console errors, and `_freeze/` is committed.
- **SC-008**: Every explorer state shows title, legend with units, source
  and year, and a data-generated caption (spot-check all 6 variables × 3
  modes).
- **SC-009**: All 96 department polygons are reachable by keyboard tab
  order and expose name/value/rank via `aria-label`; the collapsible data
  table shows the current variable and year for all 96 departments.
- **SC-010**: The inlined map payload in the rendered page (geometry +
  panel data) is ≤ 200 KB, measured on the built HTML.

## Assumptions

- The post remains in French; all map labels, controls, tooltips and
  captions are in French, consistent with the existing page.
- The interactive widget uses a native `{ojs}` block with d3 / Observable
  Plot (available by default in Quarto), per the site's convention for
  interactive demos; the static hero map stays in the existing Python
  (matplotlib/geopandas) pipeline so the preview-image workflow
  (`assets/posts/overindebtedness.jpg`) is unchanged.
- Confirmed against the current dataset: chômage, poverty (FiLoSoFi) and
  renter share (RP) are constant across 2019–2024 for all 96 departments
  — they are single-millésime indicators carried forward, handled per
  FR-022.
- The existing OLS/EDA sections and the bivariate scatter plots are
  untouched; only the cartography section and the BdF download script
  change.
- The post exists only in the English `posts/` tree (there is no
  `fr/posts/` counterpart today), so no translation stub is required by
  this feature.
- The post now renders with the site's default theme (`assets/custom.scss`)
  after the move to `posts/overindebtedness/`; widget styles go into the
  single styling file as classes (FR-018), and palettes are adapted to the
  light theme (FR-006, FR-019).
