---

description: "Task list for feature 016 — interactive surendettement map"
---

# Tasks: Interactive Surendettement Map

**Input**: Design documents from `/specs/016-interactive-surendettement-map/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: No TDD/unit-test tasks — the spec defines validation via the runnable quickstart.md scenarios (SC-001…SC-010), the `04_validate.py` data-contract script, and the `quarto render` gate (research R8). Each story phase therefore ends with a Validate task that runs the relevant quickstart checks.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Most widget work lives in the single `{ojs}` block of `posts/overindebtedness/index.qmd`, so story tasks are sequential within that file; [P] marks tasks in different files that can run in parallel.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Build-time dependency and the front-matter fix that the render gate needs.

- [X] T001 [P] Build-time geometry verified (research R3): Quarto OJS loads d3/Inputs from cdn.jsdelivr.net at runtime (confirmed on quarto-ojs-runtime.js), so the documented fallback is used — Python-precomputed SVG paths in `posts/overindebtedness/index.qmd`, pure-stdlib OJS widget (no d3/Inputs/Plot import). No new dependency added; `requirements.txt` unchanged.
- [X] T002 [P] Fix the broken front-matter `image:` path in `posts/overindebtedness/index.qmd` from `../../assetsoverindebtedness.jpg` to `../../assets/posts/overindebtedness.jpg` (FR-019)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Data-pipeline fix (dynamic year range + 2018 attempt), the `ojs_define` payload chunk, and the widget CSS. No user-story work can begin until this phase is complete.

**⚠️ CRITICAL**: US1–US4 all depend on the payload chunk (T007) and the corrected dataset (T006); US2 additionally depends on the 2018 fix (T003–T005).

- [X] T003 [P] Edit the BdF block in `posts/overindebtedness/scripts/01_download.py`: make the year range dynamic, fix the broken `synthese_*.pdf` download URL (current files are HTML error pages), re-fetch « Le surendettement en 2018 », and extract the department table with `pdfplumber` per `contracts/bdf-2018-source.md` section B (FR-001)
- [X] T004 [P] Edit `posts/overindebtedness/scripts/02_clean.py`: replace the hardcoded `range(2019, 2025)` with dynamic earliest-detected-year + latest-complete-year (12 monthly observations) detection (FR-001/FR-002)
- [X] T005 [P] Extend/verify `posts/overindebtedness/scripts/04_validate.py` coverage checks for the dynamic year range; it must pass with the new range and log any 2018 gap in `coverage_report.csv` (research R8)
- [X] T006 Run the pipeline `01_download.py → 02_clean.py → 03_merge.py → 04_validate.py` from `posts/overindebtedness/` and verify `data/processed/analytical_dataset.csv` covers `[2018 or 2019] → latest complete year` × 96 departments; `04_validate.py` exits 0 (SC-005, quickstart §1)
- [X] T007 Add a Python build chunk in `posts/overindebtedness/index.qmd` that produces `od_geo` (TopoJSON via `topojson`, prequantize 1e4, properties reduced to `{code, nom}`), `od_indicators` (6 indicators with `key/label/unit/source/millesime/decimals/varies_by_year`), and `od_data` (`[{code, nom, years, rang, delta_n1, z}]`, `null` for missing), exposed via `ojs_define(...)` per `contracts/ojs-payload.md`; on missing inputs emit a visible warning cell and empty structures (contract failure behavior)
- [X] T008 [P] Verify at first render of `posts/overindebtedness/index.qmd` that `d3.feature`, `d3.geoConicConformal`, and `d3.scaleQuantile` exist in Quarto 1.10's bundled OJS d3; if not, document the fallback to Python-precomputed SVG paths in `posts/overindebtedness/index.qmd` (research R3 verification task)
- [X] T009 [P] Add the `od-*` widget classes (`.od-map`, `.od-tooltip`, `.od-panel`, `.od-legend`, `.od-badge`, `.od-table`, controls row, top-5 labels, « données manquantes » neutral style) to `assets/custom.scss` (FR-018, research R6); no inline `style=` or `<style>` block in the `.qmd`

**Checkpoint**: Foundation ready — dataset covers the dynamic range, payload chunk is defined, widget styles exist. User-story implementation can now begin.

---

## Phase 3: User Story 1 — Reader sees the territorial level of over-indebtedness (Priority: P1) 🎯 MVP

**Goal**: The cartography section shows one interactive map of metropolitan France with all 96 departments colored by the latest-year filing rate (per 10,000 inhabitants), with legend, source, year, tooltip, and keyboard/screen-reader support.

**Independent Test**: Render the page with JS enabled; inspect the default map — 96 polygons colored, legend with units, title, source and year visible; hover shows the tooltip; Tab reaches every polygon (quickstart §3, SC-001/SC-002/SC-009).

### Implementation for User Story 1

- [X] T010 [US1] Rewrite the cartography section of `posts/overindebtedness/index.qmd`: remove the four static choropleth Python chunks and add the single `{ojs}` explorer block rendering the default view — 96 polygons via `d3.feature(od_geo, …)` + `d3.geoPath` + `d3.geoConicConformal` (parallels [44, 49], `fitSize` to a responsive viewBox) (research R4), colored by latest-year `suren` rate with `d3.scaleQuantile` 6 classes + ColorBrewer YlOrRd (FR-003/FR-004, R5); display legend with class ranges + unit « dépôts / 10 000 hab. », title, source « Banque de France », year, and a data-computed caption (FR-015); prose wrapped at 80 chars (FR-021)
- [X] T011 [US1] In the same `{ojs}` block, implement the hover tooltip (FR-012): department name, code, current value with unit, rank out of 96, raw filing count `nb` (only when the variable is `suren`), change vs previous year, and z-score vs the national mean; styled via `.od-tooltip`
- [X] T012 [US1] Accessibility (FR-023, R10): SVG root `role="application"` with `aria-label`; each department `<path>` gets `tabindex="0"`, `role="button"`, and an `aria-label` (name, value, rank) recomputed on every state change; Enter pins/unpins; controls built with `Inputs.range`/`Inputs.select`/`Inputs.radio`/`Inputs.button` (keyboard-operable); add a `<details class="od-table">` listing all 96 departments' values for the current variable and year as a text alternative
- [X] T013 [US1] Validate US1: `quarto render posts/overindebtedness/index.qmd` exits 0; open `docs/posts/overindebtedness/index.html` and confirm 96/96 polygons render for the default year, legend/unit/source/year are visible, the tooltip works on hover, and every polygon is Tab-reachable with an `aria-label` (SC-001/SC-002/SC-009 partial, quickstart §3)

**Checkpoint**: User Story 1 is fully functional and testable independently — the core map renders, encodes the rate correctly, and is accessible.

---

## Phase 4: User Story 2 — Reader explores the rise year by year (Priority: P1)

**Goal**: A year slider + play button animate the map across the full dynamic range (2018→latest after the pipeline fix), and the evolution caption states the trough and rebound figures computed from the data.

**Independent Test**: Move the slider across every year and press play; the map re-colors each year without reload and the caption's trough/rebound figures match `analytical_dataset.csv` (SC-001/SC-005, quickstart §3).

### Implementation for User Story 2

- [X] T014 [US2] In the `{ojs}` block of `posts/overindebtedness/index.qmd`, add a year slider (`Inputs.range`) covering every available year in `od_data` and a play button (`Inputs.button`) that animates one year every ~800 ms; any manual slider input clears the timer (FR-009, research R9); map re-colors per year without a page reload
- [X] T015 [US2] Add the evolution caption computed programmatically from `od_data`: trough year/value and rebound to the latest year (e.g. 2020 = 108 748 → latest year value, ≈ +24 %) — no hand-typed figures (FR-002/FR-015, SC-005)
- [X] T016 [US2] Validate US2: re-run render; move the slider across the full range and press play (interrupt it with the slider); confirm the map updates each year and the caption figures match `analytical_dataset.csv` (SC-001/SC-005, quickstart §3)

**Checkpoint**: User Stories 1 and 2 both work — the default level map and the year-by-year animation.

---

## Phase 5: User Story 3 — Reader compares economic indicators and variation (Priority: P2)

**Goal**: A variable selector offers the 6 indicators and a mode toggle offers level / variation-vs-first-year / variation-vs-previous-year / rank; variation modes use a 0-centered diverging scale and label the top-5 risers and fallers.

**Independent Test**: Switch across all 6 variables × 4 modes; legend, units, source and caption update; top-5 risers/fallers labels match a ranking computed from the CSV (SC-006/SC-008, quickstart §3).

### Implementation for User Story 3

- [X] T017 [US3] Add a variable selector (`Inputs.select`) with the six indicators of FR-007 (`suren`, `chomage`, `pauvrete`, `rsa`, `locataires`, `score`; Gini excluded), each carrying its own unit/source/millesime from `od_indicators`; for indicators with `varies_by_year = false` show a `.od-badge` next to the selector with the actual source millésime (e.g. « INSEE 2021 ») and keep the year slider visible but inert (FR-022). Implemented as a native `<select class="od-select">` (pure-stdlib widget per the T001/T008 fallback — `Inputs` would load from CDN and violate FR-017/SC-004); badge `.od-badge` shows « source millésime », slider/play are disabled (visible but inert) for single-millésime indicators
- [X] T018 [US3] Add a mode toggle (`Inputs.radio`): `niveau` | `var_base` (vs first year, %) | `var_n1` (vs previous year, %) | `rang` (FR-011); level/rank modes use a quantile sequential scale, variation modes use a 0-centered diverging scale (ColorBrewer RdBu reversed so red = increase) over the symmetric extent (FR-005, R5). Implemented as a native radio group `.od-modes` (same no-CDN rationale); niveau = 6 quantile classes YlOrRd, rang = quantiles over ranks (rank 1 darkest), var_* = RdBu_r over symmetric extent max|Δ|
- [X] T019 [US3] In variation modes, label the top-5 risers and top-5 fallers directly on the map (FR-014); render missing values (`null`) with the neutral « données manquantes » `.od-*` class (FR-006). Labels are SVG `<text class="od-toplabel od-rise/od-fall">` placed at per-department centroids (`cx`/`cy` added to `od_paths` by the `od-payload` chunk); missing values keep `.od-missing`
- [X] T020 [US3] Validate US3: spot-check all 6 variables × 4 modes — legend with units, source, year and computed caption update for every state (SC-008); variation-mode top-5 labels match the ranking computed from `analytical_dataset.csv` (SC-006, quickstart §3). Validated statically + on built HTML: 24/24 indicator×mode combos have 96/96 non-null values; top-5 var_base (2019→2025, suren) identical between CSV and payload (2A, 70, 2B, 91, 68 up / 58, 10, 56, 15, 72 down); payload 171.1 KB ≤ 200 KB (SC-010); `quarto render` exits 0; cell passes `node --check`; zero CDN imports in the widget. Browser-level interaction pass still pending (headless browser blocked here)

**Checkpoint**: User Stories 1–3 work — level, animation, indicator comparison, and variation modes.

---

## Phase 6: User Story 4 — Reader pins a department and sees its trajectory (Priority: P2)

**Goal**: Clicking (or Enter on) a department pins it and opens a side panel with its full-year sparklines for the filing rate and the selected indicator; clicking again unpins.

**Independent Test**: Click any department → panel appears with two sparklines and yearly values; click another → panel updates; click again → unpins; change year/variable → panel series stay complete (quickstart §3).

### Implementation for User Story 4

- [X] T021 [US4] In the `{ojs}` block of `posts/overindebtedness/index.qmd`, implement pinning: click/Enter on a polygon sets `pinned` to that department code and opens the `.od-panel` side panel showing its full-year sparkline for the filing rate and for the currently selected indicator, with underlying yearly values; clicking the same polygon again unpins (`pinned = null`); the panel's series stay complete and the map highlight follows the pinned department when year or variable changes (FR-013). Implemented as native `click` + `keydown` (Enter/Espace) handlers calling `togglePin(code)`; `state.pinned` is the single source of truth — `render()` re-derives each path's `.od-pinned` class and `aria-pressed` from it and calls `renderPanel()`, so the map highlight and panel always follow year/variable changes (R9). Panel = `<aside class="od-panel">` inside a new flex `.od-body` wrapper (map + panel), with close button « ✕ » (Désépingler); two pure-SVG sparklines (no d3, polyline broken on `null`, per-year dots with `<title>`, current-year dot `.od-spark-now`) plus a wrapping list of yearly values `.od-spark-vals` (raw `nb` dossier counts shown only here and in the tooltip, FR-003); when the selected indicator is `suren` itself, a « même série » note is shown. Styles for `.od-body`/`.od-panel`/`.od-spark-*` added to `assets/custom.scss` (FR-018/R6); no `style=`/`<style>` in the widget; prose sentence added at ≤ 80 chars (FR-021)
- [X] T022 [US4] Validate US4: click several departments (e.g. Haute-Garonne), change the year slider and the variable, then unpin; confirm the panel appears/updates/unpins and the sparklines show the full year range (quickstart §3). Validated statically + on built HTML: `quarto render posts/overindebtedness/index.qmd` exits 0; extracted `{ojs}` block passes `node --check`; built `docs/posts/overindebtedness/index.html` contains the `togglePin`/`renderPanel`/`od-panel`/`od-spark` wiring (click + Enter handlers, `renderPanel()` call in `render()`); payload still 171.1 KB ≤ 200 KB (SC-010); dept 31 (Haute-Garonne) has the full 2019–2025 series with `suren` + `nb` in the payload so both sparklines render 7 points; `.od-spark-line` present in the compiled site CSS; no `style=`/`<style>` in the widget block; prose ≤ 80 chars. Browser-level interaction pass still pending (headless browser blocked here)

**Checkpoint**: User Stories 1–4 work — the explorer is fully interactive (explore, compare, pin).

---

## Phase 7: User Story 5 — Reader without JavaScript still gets the picture (Priority: P3)

**Goal**: A static latest-year level map remains in the section as the no-JS fallback with a note, and the post preview image `assets/posts/overindebtedness.jpg` is the trough→latest-year variation (rebound) map.

**Independent Test**: Disable JS → static hero map + note visible in the cartography section; the blog index card shows the rebound variation map (SC-003, quickstart §3).

### Implementation for User Story 5

- [X] T023 [US5] Add a static hero choropleth of the latest-year filing rate (same encoding rules FR-003–FR-006, light-theme matplotlib palette per FR-019) in the cartography section of `posts/overindebtedness/index.qmd` as the no-JS fallback, with a note pointing JS-enabled readers to the interactive explorer above (FR-016); render it as the fallback shown when the OJS payload is unavailable (contracts/ojs-payload.md failure behavior, existing `CARTO_AVAILABLE` pattern). Implemented as a new `### Carte statique de repli (sans JavaScript)` subsection after the explorer: `carto-static-setup` chunk (loads GeoJSON in EPSG:2154, merges latest-year data, computes the national trough year dynamically, `CARTO_STATIC_AVAILABLE` guard + visible warning on failure) + `fig-carto-hero` chunk (always the `suren_depot_taux` rate, 6 quantile classes sampled from YlOrRd at i/5 like the widget, `#d9d9d9` « données manquantes », legend with class ranges + unit « dépôts / 10 000 hab. », in-figure title with the dynamic year, source + « 96 départements métropolitains, DOM-TOM exclus » footer, local `plt.rc_context` with the light-theme palette of `assets/custom.scss` per FR-019) plus prose note ≤ 80 chars
- [X] T024 [US5] Add a Python chunk in `posts/overindebtedness/index.qmd` that generates the post preview image `assets/posts/overindebtedness.jpg` as the variation map from the trough year (computed from the data, 2020 in the current dataset) to the latest year, in %, diverging scale per FR-005 (FR-016). Implemented as the `carto-preview` chunk (`include: false`): per-department % change of `suren_depot_taux` trough→latest, `TwoSlopeNorm` centered on 0 over the symmetric extent with `RdBu_r` (red = hausse, R5), hatched neutral missing style, colorbar « variation (%) », title with the computed years, source + DOM-TOM footer, saved to `../../assets/posts/overindebtedness.jpg` at 150 dpi on the `$surface` background; prints the computed creux/rebound figures to the render log (2020 = 108 748 → 2025 = 148 020, +36,1 %)
- [X] T025 [US5] Validate US5: render, then disable JavaScript in the browser and confirm the static hero map and note are visible; check the blog index card preview shows the rebound variation map and that the front-matter `image:` path resolves (SC-003, quickstart §3). Validated statically + on built HTML: `quarto render posts/overindebtedness/index.qmd` exits 0; `docs/posts/overindebtedness/index.html` contains `fig-carto-hero-output-1.png`, the « Carte statique de repli (sans JavaScript) » heading + note, and the « DOM-TOM exclus » caption (the hero is a plain `<img>`, inherently visible without JS); `assets/posts/overindebtedness.jpg` regenerated (100 789 o) as the 2020→2025 diverging variation map and copied to `docs/assets/posts/overindebtedness.jpg`; front-matter `image: ../../assets/posts/overindebtedness.jpg` resolves. Browser JS-disable pass still pending (headless browser blocked here)

**Checkpoint**: User Stories 1–5 work — the hybrid format is complete (interactive explorer + static fallback + preview image).

---

## Phase 8: User Story 6 — Analyst reproduces the map end to end (Priority: P3)

**Goal**: From a clean checkout, the documented pipeline + `quarto render` reproduce the same dataset, map and figures with no manual edits, and the freeze cache is committed.

**Independent Test**: Run quickstart §1–§2 from a clean environment; dataset covers `[2018 or 2019] → latest complete year` × 96; `quarto render` exits 0; `_freeze/` committed (SC-005/SC-007).

### Implementation for User Story 6

- [X] T026 [US6] Reproducibility run per `quickstart.md` §1–§2: from a clean environment run `posts/overindebtedness/scripts/01_download.py → 02_clean.py → 03_merge.py → 04_validate.py`, confirm `data/processed/analytical_dataset.csv` covers the dynamic range × 96 departments and the evolution reference year is the earliest available (dynamic, FR-002), then `quarto render posts/overindebtedness/index.qmd` exits 0 (SC-005/SC-007). Ran the four scripts with `.venv/bin/python` from `posts/overindebtedness/`: 01_download exits 0 (9/10 sources already present and skipped; the 2018 synthèse PDF fails on BdF bot protection — documented fallback), 02_clean/03_merge exit 0, 04_validate exits 0 with 0 errors; `analytical_dataset.csv` is byte-identical after the re-run (git-clean) and covers 2019–2025 × 96 = 672 rows with the 2018 gap logged in `coverage_report.csv` and the reference year dynamic (2019); `quarto render posts/overindebtedness/index.qmd` exits 0 (SC-005/SC-007)
- [X] T027 [US6] Commit the `_freeze/posts/overindebtedness/` render cache in the same commit as the `.qmd`/script changes (constitution III, FR-021) and verify the full-site `quarto render` exits 0 (constitution render gate). Full-site render: a single `quarto render` invocation needs ~330 s for 246 files, which exceeds this sandbox's 300 s command cap, and a killed run discards Quarto's staged output — so the site was rendered in coverage-complete subsets (root files, `posts/`, each `fr/teaching/*/` and `teaching/*/` directory), every invocation exiting 0 with zero « error encountered »; all 246 source files have their `docs/` HTML output present afterwards. `_freeze/posts/overindebtedness/` (incl. the new `fig-carto-hero-output-1.png`) committed in the same commit as the `.qmd` change; unrelated freeze drift (`_freeze/teaching/*`, `_freeze/posts/perceptron/*` supporting-path renames produced by the subset re-renders) reverted, and stray single-file outputs cleaned

**Checkpoint**: All six user stories are independently functional and the pipeline is reproducible end to end.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Full acceptance sweep and regression/style gates that span all stories.

- [X] T028 [P] Full quickstart validation sweep (quickstart §3) against the built `docs/posts/overindebtedness/index.html`: all SC-001…SC-010 — measure the serialized `od_geo`+`od_data`+`od_indicators` payload in the built HTML is ≤ 200 KB (SC-010), and confirm via the browser devtools Network tab that the widget initiates zero requests to third-party hosts while interacting (SC-004, FR-017). Static sweep on the built HTML + payload vs CSV: SC-010 payload 171,2 KB ≤ 200 KB PASS; SC-001 od_paths=96, od_data=96, years 2019–2025 PASS; SC-008 6 indicators (suren/chomage/pauvrete/rsa/locataires/score) + 4 modes (niveau/var_base/var_n1/rang) present in the widget script PASS; SC-005 payload trough 2020 = 108 748, latest 2025 = 148 020, rebound +36,1 %, identical to `analytical_dataset.csv` PASS; SC-006 top-5 risers (2A, 70, 2B, 91, 68) and fallers (58, 10, 56, 15, 72) of var_base match the CSV ranking PASS; SC-004 zero `http(s)://` occurrences in the OJS payload + widget script region (only the page's own canonical `ggilles.dev` URL injected by Quarto) PASS; SC-009 `tabindex`/`aria-label`/`role="button"`/`aria-pressed`/`.od-table` `<details>`/tooltip/panel wiring present in the widget script PASS; SC-003 hero `<img>` + note + DOM-TOM caption in static HTML, preview jpg in `assets/` and `docs/assets/` PASS. Browser-level interaction pass (slider/tooltip/Network tab) still pending — headless browser blocked here
- [X] T029 [P] Regression and style gates: confirm the EDA/OLS/bivariate-scatter sections above the cartography section are unchanged vs the pre-feature render (FR-020); prose in the modified `posts/overindebtedness/index.qmd` wraps at 80 characters (FR-021); the `.qmd` contains no inline `style=` attribute and no page-level `<style>` block for the widget (FR-018); a DOM-TOM exclusion note is present on the map (spec edge cases); all map UI text is in French. Verified: `git diff HEAD` on the `.qmd` is a single insertion hunk at the cartography section (`@@ -1870,6 +1870,212 @@`) — EDA/OLS/scatter untouched (FR-020); zero prose lines > 80 chars in the added section outside code fences (41 pre-existing > 80 lines elsewhere left alone per FR-020) (FR-021); no HTML `style=` attribute and no `<style>` block in the `.qmd` (the only `style=` matches are matplotlib `linestyle=`/`style="italic"` kwargs) (FR-018); « DOM-TOM exclus » in the widget source line, the hero fig-cap and the preview-image footer; all widget UI strings French (Niveau / Variation vs … / Rang / Lire l'animation / Pause / Désépingler / données manquantes)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **User Stories (Phase 3–8)**: All depend on Foundational completion; proceed in priority order (P1 → P2 → P3): US1, US2 (both P1), then US3, US4 (P2), then US5, US6 (P3)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Starts after Foundational — no dependency on other stories; builds the `{ojs}` explorer skeleton that US2–US4 extend in the same block
- **User Story 2 (P1)**: Depends on US1's explorer block and on the Foundational 2018 pipeline fix (T003–T006)
- **User Story 3 (P2)**: Extends US1/US2's explorer with selector + mode toggle — same `{ojs}` block, sequential after US2
- **User Story 4 (P2)**: Extends the same explorer with pinning — sequential after US3
- **User Story 5 (P3)**: Adds the static hero fallback + preview image in the same `.qmd` — independent of US2–US4 logic but shares the file, so sequential after US4
- **User Story 6 (P3)**: Validates the whole pipeline + render gate; depends on all prior phases for the final end-to-end run

### Within Each User Story

- Core implementation before validation
- The Validate task at the end of each story phase MUST pass before moving to the next story
- Story complete before moving to the next priority

### Parallel Opportunities

- Phase 1: T001 and T002 are [P] (different files: `requirements.txt` vs `index.qmd` front matter)
- Phase 2: T003, T004, T005, T008, T009 are [P] (different files: `01_download.py`, `02_clean.py`, `04_validate.py`, a render-time d3 check, `assets/custom.scss`); T006 (pipeline run) and T007 (payload chunk) follow once T003–T005 land
- Phase 9: T028 and T029 are [P] (independent read-only validation sweeps over the built HTML and sources)
- Different user stories share `posts/overindebtedness/index.qmd`, so story phases run sequentially, not in parallel

---

## Parallel Example: Foundational Phase

```bash
# Launch all independent Foundational file edits together:
Task: "Edit the BdF block in posts/overindebtedness/scripts/01_download.py …"        # T003
Task: "Edit posts/overindebtedness/scripts/02_clean.py: dynamic range …"              # T004
Task: "Extend/verify posts/overindebtedness/scripts/04_validate.py …"                 # T005
Task: "Verify d3.feature/geoConicConformal/scaleQuantile in Quarto's bundled d3 …"    # T008
Task: "Add od-* widget classes to assets/custom.scss …"                               # T009
# Then, once those land, run the pipeline (T006) and add the ojs_define chunk (T007)
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2, both P1)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL — blocks all stories)
3. Complete Phase 3: User Story 1 (default level map + tooltip + accessibility)
4. Complete Phase 4: User Story 2 (year slider + play + computed caption)
5. **STOP and VALIDATE**: render the post and run quickstart §3 checks SC-001/SC-002/SC-005/SC-009
6. Commit with `_freeze/` — this is the shippable MVP: the interactive level map and the year-by-year rebound animation

### Incremental Delivery

1. Setup + Foundational → foundation ready
2. Add US1 + US2 → validate → commit (MVP!)
3. Add US3 → validate → commit (indicator comparison + variation)
4. Add US4 → validate → commit (pin panel)
5. Add US5 → validate → commit (no-JS fallback + preview image)
6. Add US6 → validate → commit (reproducibility + freeze)
7. Polish (Phase 9): full SC sweep, payload/network gates, regression checks

### Parallel Team Strategy

With multiple developers, Phase 1 and the [P] tasks of Phase 2 can be split across files; user-story phases share `index.qmd` and should be done sequentially by one developer (or split by clearly separated `{ojs}` cells if coordinated).

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps each task to a user story for traceability
- Each user story is independently completable and testable via its Validate task
- Validation is by quickstart.md scenarios + `04_validate.py` + `quarto render` exit 0 — no unit-test framework is introduced (research R8)
- Commit after each task or logical group, with `_freeze/` in the same commit as `.qmd` changes (constitution III)
- Stop at each checkpoint to validate the story independently before proceeding
- Avoid: vague tasks, cross-story dependencies that break independence, hand-edited raw data or hand-typed figures (FR-001/FR-002)

---

## Implementation Notes (MVP: phases 1–4, T001–T016, 2026-11-22)

Verified decisions that adjust the original task wording:

- **T001/T008 — geometry transport**: Quarto 1.10.19's OJS runtime resolves
  `d3`/`Inputs`/`Plot` from `https://cdn.jsdelivr.net/npm/` **at runtime**
  (`dependency("d3","7.8.5","dist/d3.min.js")` in `quarto-ojs-runtime.js`;
  confirmed by rendering a probe page — no local bundle). That violates
  FR-017/SC-004 for this widget, so the documented research-R3 fallback is
  used: **Python-precomputed SVG paths** (EPSG:2154 → viewBox 1000 px,
  `simplify(800)` + integer coords) inlined via `ojs_define`, and a
  **pure-stdlib OJS widget** (only the local `html` builtin — zero CDN
  imports, zero runtime third-party requests). No `topojson` dependency
  added; `requirements.txt` unchanged. Payload measured on built HTML:
  **168.9 KB ≤ 200 KB** (SC-010).
- **T007 — `ojs_define` emission**: a Python chunk with `include: false`
  does NOT emit the `<script type="ojs-define">` block (verified with a
  probe render). The `od-payload` chunk therefore uses `echo: false` +
  `output: false`, which does emit it.
- **T003/T004 — 2018**: API floor confirmed at 2019-01. The BdF
  `/system/files/` endpoints return 404/403 from this environment (bot
  protection), so the best-effort PDF download fails and the spec's
  documented fallback applies: pipeline logs the 2018 gap in
  `coverage_report.csv` (`annee_*` rows + warning) and the reference year
  is dynamic (2019). Dynamic range after fix: **2019–2025 × 96 = 672 rows**
  (was 2019–2024). `04_validate.py` exits 0.
- **T015 — caption figures** computed from the payload at data level:
  trough 2020 = 108 748 dossiers, latest 2025 = 148 020, rebound +36.1 %
  (2024 = 134 807 per the spec; the range now extends to 2025 because the
  API reaches 2026-04, so 2025 is the latest complete year).
- **Render gate**: `quarto render posts/overindebtedness/index.qmd` exits 0;
  `_freeze/posts/overindebtedness/` regenerated. The full-site
  `quarto render` (246 files) exceeds this environment's 120 s command cap
  and was interrupted mid-run; the collateral partial outputs were
  reverted (`git checkout -- docs/` + removal of untracked strays), so the
  working tree contains only the intended MVP changes. Run the full-site
  render before committing.
- Browser-level checks (SC-001/002/004/009 interactive: slider, tooltip,
  keyboard tab-order, network panel) could not be executed here (headless
  Chromium/Node are policy-blocked); the widget cell was statically
  validated instead (balanced syntax, no external URLs, all controls
  present). Worth a manual pass per quickstart §3.
