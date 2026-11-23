# Contract: BdF surendettement source — WebStat API + 2018 fallback

Producer: `posts/overindebtedness/scripts/01_download.py` (BdF block) and
`02_clean.py`. Consumer: `data/processed/surendettement.csv` →
`analytical_dataset.csv` → the map payload (contracts/ojs-payload.md).

## A. WebStat ODS API (primary, monthly 2019-01 → present)

- Endpoint: `https://webstat.banque-france.fr/api/explore/v2.1/catalog/datasets/observations/exports/csv/`
- Auth: header `Authorization: Apikey <BDF_APIKEY>` (key already embedded in
  `01_download.py`, extracted from the public webstat JS bundle).
- Query params: `where=series_key IN ("IFI.M.D01.SUREN.DEPOT", … 96 keys)`,
  `select=series_key,time_period,obs_value`, `order_by=series_key,time_period`,
  `delimiter=;`. No time filter — the export returns the full history.
- Output: `data/raw/bdf/surendettement_api.csv` (fields
  `series_key;time_period;obs_value`; verified min period **2019-01**, max
  2026-04 at research time).
- Cleaning (`02_clean.py`): `annee = int(time_period[:4])`; sum monthly
  `obs_value` per (dep_code, annee); keep only **complete years** (12
  months) and the earliest detected year — i.e. replace the current
  hardcoded `range(2019, 2025)` with a dynamic range (FR-001/FR-002).
- Output schema (unchanged): `dep_code, dep_nom, annee, suren_depot_nb,
  source_url, source_millesime`.

## B. 2018 fallback (annual synthesis PDF)

- The WebStat API has **no pre-2019** SUREN.DEPOT records (verified live,
  research R1), so 2018 can only come from the official annual synthesis
  (« Le surendettement en 2018 », banque-france.fr). The
  `data/raw/bdf/synthese_2018.pdf` file currently on disk is an HTML error
  page — the download URL must be fixed and the file re-fetched.
- Extraction: `pdfplumber` (already in `.venv`) parses the department-level
  table of dossiers déposés; rows are appended to `surendettement.csv` as
  `annee = 2018` with `source_millesime = "2018"` and
  `source_url` = the PDF URL.
- If the PDF is unavailable or the table is not parseable: the pipeline
  MUST log the gap in `coverage_report.csv` and continue with 2019 as the
  earliest year (spec edge case); the explorer then uses 2019 as reference
  year (FR-002 dynamic reference).

## C. Invariants

1. Raw files under `data/raw/` are never hand-edited; all transformation in
   versioned scripts (spec FR-001 / 001-spec FR-009).
2. `suren_depot_nb` = integer count of dossiers déposés; the rate
   `suren_depot_taux` (per 10,000 inhabitants) is derived in `03_merge.py`
   and is the only value mapped as a level (FR-003).
3. After the fix, `surendettement.csv` covers
   `[earliest detected → latest complete year] × 96` departments
   (expected 2019–2025 via API, 2018–2025 if the PDF fallback succeeds).
