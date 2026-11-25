# Quickstart — Validate the interactive surendettement map end to end

Feature 016. Prerequisites: Python 3.11 venv at repo root with
`pip install -r requirements.txt` (now including `topojson`), Quarto ≥ 1.4
(1.10.19 installed), network access for the one-time data download.

## 1. Reproduce the data pipeline (SC-005, US6)

```bash
cd posts/overindebtedness
python scripts/01_download.py    # BdF API + 2018 PDF attempt + INSEE/DREES
python scripts/02_clean.py       # dynamic complete-year range
python scripts/03_merge.py
python scripts/04_validate.py    # must pass; check coverage_report.csv
```

Expected: `data/processed/analytical_dataset.csv` covers
`[2018 or 2019] → 2025` × 96 departments for `suren_depot_*` (2018 only if
the synthèse PDF parsed — otherwise the coverage report logs the gap and
the range starts at 2019). No manual edits to raw files.

## 2. Render the post (SC-007, FR-019/FR-021)

```bash
cd /home/guillaume/www
quarto render posts/overindebtedness/index.qmd
# must exit 0; then render the site gate if touching shared files:
quarto render
```

Expected: exit 0, no console errors when opening
`docs/posts/overindebtedness/index.html`, front-matter `image:` points to
an existing `assets/posts/overindebtedness.jpg`, and the post's `_freeze/`
entry is committed with the change.

## 3. Validate the explorer against the success criteria

Open `docs/posts/overindebtedness/index.html` in a browser:

| Check | SC | How |
|---|---|---|
| 96/96 departments render for every year | SC-001 | move the year slider across the full range; count polygons (or check no « données manquantes » for `suren`) |
| Controls update the map without reload; tooltip on all 96 | SC-002 | switch variable × mode × year; hover each region |
| No-JS fallback + preview image | SC-003 | disable JS: static latest-year map + note visible; blog index card shows the rebound variation map |
| Zero third-party requests from the widget | SC-004 | devtools Network tab while interacting: no requests leaving the origin |
| Trough/rebound caption matches data | SC-005 | compare caption figures with `analytical_dataset.csv` (e.g. 2020 = 108,748; latest year value; % rebound) |
| Top-5 risers/fallers labels | SC-006 | variation-vs-base mode; labels match a ranking computed from the CSV |
| Every state has title/legend+units/source+year/caption | SC-008 | spot-check all 6 variables × 4 modes |
| Keyboard + screen reader | SC-009 | Tab through all 96 polygons; each `aria-label` states name/value/rank; open the collapsible data table |
| Payload size | SC-010 | in the built HTML, measure the serialized `od_geo`+`od_data`+`od_indicators` ≤ 200 KB |

## 4. Regression checks

- The EDA/OLS/scatter sections above the cartography section are unchanged
  (FR-020): compare rendered output before/after for those sections.
- `quarto render` of the full site exits 0 (constitution render gate).

## References

- Spec: `specs/016-interactive-surendettement-map/spec.md`
- Data model: `data-model.md` — payload schema and validation rules
- Contracts: `contracts/ojs-payload.md`, `contracts/bdf-2018-source.md`
- Research decisions: `research.md` (R1: API floor 2019-01; R3: TopoJSON 83 KB)
