# Quickstart: Validate the 3-Day Course

Run from the repository root (`/home/guillaume/www`). Details of formats:
[contracts/course-pages-contract.md](contracts/course-pages-contract.md);
entities: [data-model.md](data-model.md).

## Prerequisites

- Quarto installed; `.venv` not required (no Python blocks).
- On branch `014-financial-analysis-3day-course`.

## 1. Render both language trees

```sh
quarto render fr/teaching/financial-analysis --quiet
quarto render teaching/financial-analysis --quiet
```

Expected: exit 0 for both, no warnings about missing links or unknown
cross-references. Before the full-site render gate, run `quarto render`
once more for the whole site.

## 2. Timetable sums (SC-001, SC-006 support)

For each `planning.qmd` (FR and EN), sum the "Duration (min)" column of
each day's table.

Expected: 360, 360, 360 and 1 080 total; EN rows identical to FR rows
(Block, Start, Duration).

## 3. Coverage (SC-002)

Check that the nine quest files and the six reference files each appear
in `planning.qmd` or `annexes/inventaire-sources.qmd`.

Expected: no missing file.

## 4. Parity (SC-008)

For every `.qmd` under `fr/teaching/financial-analysis/`, the mirrored
path exists under `teaching/financial-analysis/`.

Expected: no missing counterpart; only `index.qmd` and `planning.qmd` are
full translations, the rest contain "Translation in progress".

## 5. Constitution checks

- No `style=` or `<style>` in the course files.
- `.callout-important` only with a `TODO:` title; no `.callout-note` used
  for prerequisites or tasks.
- Every exercise is `#exr-…` with a folded `<details class="answer">`.
- Every quest has one `.callout-caution` derivation.
- Glossary linked in the sidebar; syllabus lists literature with
  editions.
- Prose wrapped at 80 columns.

## 6. Assessment arithmetic (SC-007)

From `evaluation.qmd`, compute the final grade for XP = 900 and exam =
12/20: `0.4 × (900 / 1500 × 20) + 0.6 × 12 = 4.8 + 7.2 = 12.0`, level =
Stratège Financier.

Expected: the page states the same result in under 2 minutes of reading.

## 7. Human read-throughs

- Instructor pilot (SC-003): a colleague prepares Day 1 from the pages in
  under 2 hours.
- Student check (SC-004): 10 questions about days, preparation and
  deliverables answered from the home page, ≥ 90 % correct.
- Concept-order pass (SC-005): each day read once looking for a concept
  used before being introduced.

## 8. Navigation and switcher

Open the rendered site (`quarto preview`): every course page is reachable
from its sidebar, the language switcher goes between mirrored pages, and
the old URLs under `modules/` and `exercices/` still resolve.
