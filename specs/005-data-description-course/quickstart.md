# Quickstart: Validating the Data Description Course

This guide validates the feature end-to-end once implementation is
complete (or incrementally, per file). It does not duplicate the content
requirements — see `spec.md` for functional requirements and
`contracts/` for the required structure of each page type.

## Prerequisites

- Quarto CLI installed (matches the version used elsewhere in the repo)
- Project `.venv` active with `python-pptx`, `python-docx` added (one-time,
  for source extraction — see `research.md` §1); `pandas`/`numpy`/`openpyxl`
  already present
- Branch `006-data-description-course` checked out

## 1. Regenerate/inspect the canonical dataset (optional — already verified)

```sh
python3 -c "import pandas as pd; df = pd.read_csv('specs/005-data-description-course/wandering-fork-dataset.csv'); print(df.describe())"
```

Expected: 30 rows; `daily_revenue_eur` mean ≈ 628.34, std ≈ 137.09
(matches `data-model.md`).

## 2. Render a single session while iterating

```sh
quarto render teaching/data-description/session-05.qmd --quiet
```

Expected: exits 0; no LaTeX/math warnings; output HTML contains the
expected `##` headings from `contracts/session-page.md` in order.

## 3. Render the whole course

```sh
quarto render teaching/data-description/ --quiet
```

Expected: exits 0 for all 15 files (index, glossary, 12 sessions).

## 4. Render the full site (regression check)

```sh
quarto render
```

Expected: exits 0; no new broken links reported; `docs/` updated;
`scripts/update-profile-readme.sh` post-render hook runs without error.

## 5. Manual verification checklist (maps to Success Criteria)

- [ ] Open `teaching/data-description/index.qmd` output — syllabus shows
  3-part session table, assessment scheme, Recommended Literature
  (SC-001, T-VIII)
- [ ] Click through all 12 session links from the index — no dead links
  (SC-008, SC-009)
- [ ] Open `glossary.qmd` output — every symbol used in any session
  appears with a definition (SC-007)
- [ ] Open the 4 sessions containing a Shinylive demo — each app loads
  and responds to input in the browser (SC-006)
- [ ] Spot-check 3 sessions' worked examples against
  `data-model.md`'s verified statistics — numbers match exactly (SC-004)
- [ ] Confirm every `.qmd` file has `lang: en` and (until complete)
  `draft: true` (FR-005, FR-017)
- [ ] Confirm Session 12 contains the original mock-exam section
  (FR-018) and it does not reproduce verbatim source exam text
- [ ] Grep the rendered course for any of the source's proprietary
  figures/case-study name ("Food Truck") to confirm none leaked in
  (SC-004)

## 6. Flip to published (final step, once all of the above pass)

Remove `draft: true` from all 15 files in a single change (FR-017), add
the `data-description` sidebar block to `_quarto.yml` if not already
present, then re-render the full site and commit `docs/` + `_freeze/`
(if any) together with the source changes, per the constitution's
render gate.
