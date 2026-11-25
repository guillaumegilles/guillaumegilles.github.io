# Phase 0 Research — Interactive Surendettement Map (016)

All findings below were verified against the repo and, where marked *live*,
against the Banque de France WebStat API on 2026-11-20. Each entry follows
Decision / Rationale / Alternatives considered.

## R1 — Where does 2018 come from? (FR-001/FR-002)

**Decision**: Make the year range fully dynamic in `02_clean.py` (today it
is hardcoded to `range(2019, 2025)`): earliest year = min year present in
the downloaded data, latest year = latest *complete* year (12 monthly
observations). Additionally attempt to add 2018 by parsing the official BdF
annual synthesis PDF (« Le surendettement en 2018 »), re-downloaded from a
correct banque-france.fr URL. If the 2018 table cannot be extracted, the
explorer falls back to 2019 as reference year (spec edge case) — the
rebound story (2020 trough → latest year) is unaffected.

**Rationale**: *Live check of the WebStat `observations` dataset*: the
series `IFI.M.Dxx.SUREN.DEPOT` (96 departments, the exact keys used by
`01_download.py`) start at **2019-01** (verified for D01; the local
`data/raw/bdf/surendettement_api.csv` confirms min 2019-01, max 2026-04,
8,448 rows). Guessed annual series keys (`IFI.A./IFI.Y./IFI.` variants) all
return 0 records, and the catalog full-text search surfaces no dedicated
pre-2019 surendettement dataset. So the API floor is 2019; the only
authoritative 2018 source at department level is the annual synthesis PDF.
Note the raw `synthese_*.pdf` files currently in `data/raw/bdf/` are HTML
error pages, not PDFs — the PDF download in the pipeline must be fixed as
part of this task. Also note the API now reaches 2026-04, so the latest
*complete* year after the fix is 2025, not 2024.

**Alternatives considered**: (a) hardcode 2018 from the old report —
rejected, violates FR-002 (no hand-typed data) and raw-data immutability;
(b) use only 2019+ and drop the 2018 goal — kept as fallback, not primary,
because the spec explicitly asks for the 2018 attempt; (c) scrape the
WebStat web UI — rejected, the ODS API already used is the supported path.

## R2 — How does Python pass data to the `{ojs}` block?

**Decision**: Use Quarto's `ojs_define(...)` inside a Python chunk of
`index.qmd` to expose three variables to the OJS block: `od_geo` (TopoJSON
object), `od_data` (records array), `od_indicators` (indicator metadata).
Quarto 1.10.19 is installed and supports `ojs_define` in Python chunks.

**Rationale**: keeps everything inlined in the rendered HTML (FR-017, zero
runtime requests), works with `freeze: auto` (the Python chunk result is
cached in `_freeze/`), and needs no extra files published to `docs/` (the
post's `data/` directory is currently NOT copied to `docs/`, so fetching
at runtime would 404 anyway).

**Alternatives considered**: `FileAttachment("data/…")` — would require
publishing the data files as site resources and a runtime same-origin fetch;
rejected because it adds moving parts and the payload is small enough to
inline. Hand-writing JSON into the `.qmd` — rejected, violates
FR-002/FR-026-style rules (figures generated programmatically, raw data not
hand-edited).

## R3 — Geometry encoding and the ≤ ~200 KB budget (FR-017, SC-010)

**Decision**: Inline the department geometry as **TopoJSON with
prequantization 1e4** (~4-decimal degrees), produced at build time by the
Python `topojson` package from `data/geo/departements.geojson` with
properties reduced to `{code, nom}`. Client-side, decode with
`d3.feature(topo, topo.objects.<layer>)` from the d3 bundle that Quarto
ships in OJS. Measured sizes: TopoJSON 1e4 = **83 KB**; GeoJSON rounded to
3 decimals = 220 KB (over budget alone). Data table ≈ 30 KB. Total ≈ 115 KB
≤ 200 KB.

**Rationale**: TopoJSON deduplicates shared borders and quantizes
coordinates, which is what actually fits the budget; `d3` v7's default
bundle re-exports d3-topojson, so `d3.feature` is available without any CDN
import (a jsdelivr `import … from "topojson-client"` would violate the
privacy rule — runtime third-party request).

**Alternatives considered**: GeoJSON rounded to 3 dp (220 KB — exceeds the
~200 KB budget); precomputed SVG path strings in Python (~150–220 KB, and
kills pan/zoom flexibility); adding `topojson-client` via Observable import
(rejected — CDN request, privacy).

**Verification task for implementation**: confirm `d3.feature` exists in
Quarto 1.10's bundled d3 at first render; if not, fall back to
Python-precomputed SVG paths (documented fallback, still ≤ 200 KB at 2
decimals).

## R4 — Map projection

**Decision**: client-side `d3.geoConicConformal()` with parallels [44, 49]
centered on mainland France (the standard conformal choice for France
métropolitaine), `fitSize` to a responsive viewBox.

**Rationale**: no extra dependency, resolution-independent (vector), and
Corse renders acceptably with a small inset offset if needed.

**Alternatives considered**: preprojecting in Python (geopandas, EPSG:2154)
and inlining SVG paths — kept as fallback (R3); equirectangular — rejected,
visibly distorts northern France.

## R5 — Color scales and classification (FR-004/FR-005/FR-006)

**Decision**: levels use `d3.scaleQuantile` with 6 classes over the 96
values and a ColorBrewer **YlOrRd** sequential interpolator; variation modes
use a diverging scale centered exactly on 0 (ColorBrewer **RdBu**, reversed
so red = increase) over the symmetric extent; rank mode = quantile over
ranks. Missing values get a dedicated neutral class styled in
`custom.scss` and labeled « données manquantes ». Palettes are
colorblind-considerate (YlOrRd/RdBu are the standard safe choices) and chosen
for the site's light theme.

**Rationale**: quantile classes avoid the empty-class problem of equal
intervals on skewed rates; a 0-centered diverging scale is the honest
encoding for % change (FR-005).

**Alternatives considered**: Jenks natural breaks (no bundled implementation
in d3 — would need a hand-rolled algorithm, rejected for complexity); fixed
class breaks (rejected — not comparable across variables/years).

## R6 — Widget styling vs constitution V (FR-018)

**Decision**: all widget chrome (controls row, tooltip, pin panel, legend,
badge, collapsible table, top-5 labels) uses dedicated classes prefixed
`od-` added to `assets/custom.scss`. The `.qmd` contains no `style=`
attribute and no `<style>` block. d3 sets SVG `fill`/`stroke` as presentation
attributes — these are not `style=` properties and are unavoidable for a
choropleth; everything else goes through classes.

**Rationale**: constitution V names `assets/custom.scss` as the single
styling entry point; keeping widget CSS there also lets the site theme
light/dark variants apply.

**Alternatives considered**: inline styles inside OJS `html` template
literals — used by some existing teaching pages, but rejected here because
the constitution forbids inline `style=` and FR-018 commits to classes.

## R7 — OJS in a blog post (constitution tech-stack scope note)

**Decision**: implement the explorer as a native `{ojs}` block in the post,
as explicitly requested (spec FR-008) and consistent with AGENTS.md ("Use
`{ojs}` blocks … for interactive demos"). Recorded as a justified deviation
in plan.md's Complexity Tracking.

**Rationale**: OJS adds no runtime dependency, no tracking, and no
server-side state; it is the only interactive mechanism the site supports.

**Alternatives considered**: static maps only; Python-generated animation —
both rejected in the brainstorm (see plan.md Complexity Tracking).

## R8 — Testing / validation approach

**Decision**: no unit-test framework is introduced. Validation = (a)
`scripts/04_validate.py` data-contract checks (extended to the dynamic year
range), (b) the runnable scenarios in `quickstart.md` mapped one-to-one to
SC-001…SC-010 (manual + browser devtools checks), (c) the render gate
`quarto render` exit 0 with committed `_freeze/`.

**Rationale**: matches repo practice (the 001 pipeline validated via coverage
reports, not pytest) and the constitution's render gate.

**Alternatives considered**: adding pytest + Playwright — rejected as
heavier than the repo's conventions and as a new dependency surface.

## R9 — Play animation behavior (FR-009)

**Decision**: play advances one year every ~800 ms via the slider's
programmatic update; any manual slider input clears the timer (spec edge
case: manual position wins).

**Rationale**: reuses the single source of truth (the year state), so map,
legend, caption, tooltip and pin panel can never disagree.

## R10 — Accessibility implementation (FR-023)

**Decision**: SVG root gets `role="application"` with an `aria-label`;
each department `<path>` gets `tabindex="0"`, `role="button"`, and an
`aria-label` recomputed on every state change (name, value, rank); Enter
pins/unpins; focus shows the same tooltip as hover. Controls use
`Inputs.range` / `Inputs.select` / `Inputs.radio` / `Inputs.button` (all
keyboard-operable natively). A `<details class="od-table">` lists all 96
departments' values for the current variable/year.

**Rationale**: satisfies FR-023 with built-in OJS widgets (no custom focus
management) and gives screen-reader users the full data, not just the map.

**Alternatives considered**: aria-label on the SVG only (rejected — values
would be invisible to screen readers); visual-only map (rejected in
clarify Q2).
