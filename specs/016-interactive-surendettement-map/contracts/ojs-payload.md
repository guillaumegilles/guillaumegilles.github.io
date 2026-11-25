# Contract: Python build chunk → `{ojs}` explorer (ojs-payload)

Build-time, in-page contract. Producer: a Python chunk in
`posts/overindebtedness/index.qmd` (runs at render, cached in `_freeze/`).
Consumer: the single `{ojs}` block of the cartography section. Transport:
Quarto `ojs_define(...)` — variables become OJS cells; everything is
serialized into the rendered HTML (no runtime fetch, FR-017).

## Variables exposed

| OJS variable | Type | Content | Source |
|---|---|---|---|
| `od_geo` | object (TopoJSON) | `objects.<layer>.geometries[]` with `properties: {code, nom}` only; prequantize 1e4 | `data/geo/departements.geojson` via `topojson` |
| `od_indicators` | array of objects | `{key, label, unit, source, millesime, decimals, varies_by_year}` for the 6 indicators of FR-007 | spec data-model.md |
| `od_data` | array of objects | `[{code, nom, years: {<year>: {<indicatorKey>: value, nb?: rawCount}}, rang: {<year>: {<key>: rank}}, delta_n1: {…}, z: {…}}]` | `data/processed/analytical_dataset.csv` |

## Rules

1. `code` is a zero-padded 2-char string (`"01"`, `"2A"`); join key with
   geometry `properties.code`.
2. Missing value = JSON `null` (never `""`, never omitted silently).
3. `nb` (raw filings) exists only under the `suren` indicator and is used
   only in tooltip/panel text (FR-003).
4. `millesime` on an indicator = its actual source year when
   `varies_by_year` is false (FR-022 badge); for varying indicators it is
   the current `year` at render of each state (client-side).
5. Serialized size of (`od_geo` + `od_data` + `od_indicators`) MUST be
   ≤ 200 KB in the built HTML (SC-010); measured plan estimate ≈ 115 KB.
6. No URLs, no functions, no Dates — plain JSON values only.
7. Client-side decoding MUST use the d3 bundle shipped with Quarto
   (`d3.feature`, `d3.geoPath`, `d3.geoConicConformal`, `d3.scaleQuantile`);
   no `import` from CDNs (FR-017).

## Failure behavior

- If `analytical_dataset.csv` or the GeoJSON is missing at render time, the
  Python chunk MUST emit a visible warning cell and `ojs_define` empty
  structures; the OJS block MUST render the static fallback note instead of
  crashing (mirrors the existing `CARTO_AVAILABLE` pattern in index.qmd).
