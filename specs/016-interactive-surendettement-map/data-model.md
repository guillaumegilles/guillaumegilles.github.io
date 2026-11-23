# Phase 1 Data Model — Interactive Surendettement Map (016)

Source of truth: `specs/016-interactive-surendettement-map/spec.md`
(Key Entities) + `posts/overindebtedness/data/processed/analytical_dataset.csv`.

## Entities

### Département
- `code`: 2-character INSEE code, zero-padded string, includes `2A`/`2B`
  (Corse). Primary key. 96 values (métropole only; DOM-TOM excluded).
- `nom`: display name (from GeoJSON properties).
- Relationship: 1 département → N observations (one per millésime).

### Millésime
- `annee`: integer year. After the pipeline fix (FR-001/FR-002) the range is
  **dynamic**: earliest detected year (target 2018 via the BdF synthèse PDF,
  API floor 2019) → latest *complete* year (12 monthly observations; 2025
given the API currently reaches 2026-04). Stored as `annee` in the dataset.

### Indicateur cartographique
One per selectable variable (FR-007). Metadata table, inlined as
`od_indicators`:

| key | label (FR) | unit | source | millésime behavior |
|-----|-----------|------|--------|--------------------|
| `suren` | Taux de dépôt de dossiers | dépôts / 10 000 hab. | Banque de France | varies by year |
| `chomage` | Taux de chômage | % | INSEE TCRD | single millésime (constant across years) → badge (FR-022) |
| `pauvrete` | Taux de pauvreté | % | INSEE FiLoSoFi | single millésime → badge |
| `rsa` | Part allocataires RSA | % | DREES | varies by year |
| `locataires` | Part ménages locataires | % | INSEE RP | single millésime → badge |
| `score` | Score de fragilité | z-score composite | computed (0.3/0.3/0.2/0.2) | varies by year |

Derived per (département, millésime) at build time: `rang` (rank 1–96 among
non-null values), `delta_n1` (% change vs previous year), `z` (z-score vs
national mean of the year), and for `suren` only: `nb` (raw filing count,
tooltip/panel only — never the mapped color, FR-003).

### Mode d'affichage (FR-011)
`niveau` | `var_base` (vs first year, %) | `var_n1` (vs previous year, %)
| `rang`. Level/rank modes use a quantile sequential scale (FR-004);
variation modes use a 0-centered diverging scale (FR-005).

### Géométrie départementale
- Source: `posts/overindebtedness/data/geo/departements.geojson`
  (96 Polygon features, properties `code`/`nom`).
- Build-time transform: properties reduced to `{code, nom}`, coordinates
  quantized via TopoJSON prequantize 1e4 (R3) → inlined as `od_geo`.
- Client-side: `d3.feature(od_geo, od_geo.objects.<layer>)` → GeoJSON
  features → `d3.geoPath` with `d3.geoConicConformal` (R4).

### Carte hero statique (FR-016)
Two static matplotlib figures rendered by the existing Python pipeline:
1. in-section no-JS fallback — latest-year `suren` level map;
2. preview image `assets/posts/overindebtedness.jpg` — variation map
   trough year → latest year (diverging, trough computed from data).

### Score de fragilité
Unchanged composite: `0.3·z_chômage + 0.3·z_pauvreté + 0.2·z_RSA +
0.2·z_locataires`, recomputed if inputs change; reused as the `score`
indicator.

## Inlined payload schema (build-time contract)

Exposed to OJS via `ojs_define` (see `contracts/ojs-payload.md`):

```jsonc
od_geo:        TopoJSON object, objects.<layer>.geometries[].properties = {code, nom}
od_indicators: [{key, label, unit, source, millesime, decimals, varies_by_year}]
od_data:       [{code, nom, years: {"2019": {suren: 18.1, nb: 1216, chomage: 5.5, …}, …},
                 rang: {"2019": {suren: 12, …}}, delta_n1: {…}, z: {…}}]
```

- `null` (not missing string) marks absent values → neutral
  « données manquantes » style (FR-006).
- All values rounded for display (`decimals` per indicator); ranks/deltas/z
  computed at build time from full precision.

## Widget state model (FR-009…FR-014, FR-022/023)

Single reactive state: `{year, indicator, mode, pinned}`.
- `year`: integer in detected range; no-op for indicators with
  `varies_by_year = false` (FR-022 badge shows `millesime`).
- `indicator`: one of the 6 keys (FR-007).
- `mode`: one of 4 (FR-011).
- `pinned`: department code or `null`; Enter/click toggles (FR-013).
Transitions: any control change recomputes color scale domain (quantile of
current mode), legend, caption figures (computed, FR-015), tooltip/aria
labels (FR-012/FR-023) and the pin panel sparklines. Play = programmatic
year increments that any manual input cancels (R9).

## Validation rules (enforced by 04_validate.py + build chunk)

1. Exactly 96 distinct `code` values, matching the GeoJSON codes 1:1
   (including 2A/2B).
2. Every (code, year) has `suren` non-null for all years in range.
3. Rates are per 10,000 inhabitants; raw `nb` never used as color (FR-003).
4. Years within [earliest detected, latest complete]; no partial year.
5. Inlined payload (od_geo + od_data + od_indicators serialized) ≤ 200 KB
   (SC-010), measured on built HTML.
6. No third-party URLs anywhere in the widget code (FR-017, SC-004).
