# Quickstart: validating the 10-module course

Run from the repository root (`/home/guillaume/www`). Scenarios map to
the spec's success criteria; contracts are in `contracts/`.

## Prerequisites

```sh
source .venv/bin/activate        # numpy, pandas, openpyxl, scipy present
quarto --version                 # 1.4.x (drafts supported)
```

## V1 — The repository renders (SC-009, FR-040)

```sh
quarto render teaching/data-description --quiet
```

**Expected**: exit 0, no "file not found" warnings. (Today this fails or
warns because the sidebar lists `session-*.qmd` files that no longer
exist — the first delivery step fixes it.)

## V2 — Dataset invariants hold (SC-003, FR-024–FR-027)

```sh
python specs/010-data-description-10-modules/verify_dataset.py
```

**Expected**: prints `OK` for each invariant in `data-model.md` §2 and
prints the recomputed statistics for both franchises. Fails if Harbour
days 1–30 differ from the legacy CSV (mean 628.34, $s$ 137.09, $Q_1$
506.60 on `daily_revenue_eur`).

## V3 — Quoted numbers recompute (SC-003)

For each module: pick three numbers from the worked example, recompute
them with the Excel steps on the same page using `wandering-fork.xlsx`.
**Expected**: all match to the printed precision.

## V4 — Module contract (SC-002, SC-001)

```sh
python specs/010-data-description-10-modules/check_modules.py
```

**Expected** per module: all headings from the contract present in
order; time plan sums to 180; ≥ 1 collapsible `.callout-caution`;
further-reading table has an OpenStax and a Khan Academy row; demo block
or `TODO:` present; total across modules 1,800.

## V5 — Fidelity (SC-004, FR-039)

Open `specs/010-data-description-10-modules/fidelity-record.md`.
**Expected**: every theory block, worked example, exercise and demo from
the old session pages has a row marked `migrated`, `adapted` or
`dropped` (with a reason).

## V6 — No orphans or old links (SC-009, FR-041)

```sh
grep -rn "session-[0-9][0-9]" teaching/data-description _quarto.yml || echo "none"
find teaching/data-description -name "session-*.qmd" -o -name "excel-worksheet*.qmd"
```

**Expected**: `none` and no files listed.

## V7 — Drafts stay hidden until publish (SC-009, FR-037)

With `draft: true` in `modules/_metadata.yml`:

```sh
quarto render --quiet && grep -c "module-0" docs/teaching/data-description/index.html
```

**Expected**: modules render blank and are absent from the sidebar and
search index. After removing the flag and rewriting `index.qmd`, the
same check shows all ten modules linked.

## V8 — Demos (SC-008)

```sh
quarto preview teaching/data-description/modules/module-03.qmd
```

Open M3, M5 and M9 in a browser. **Expected**: histogram bin slider,
boxplot builder and scatter/regression demo each load and respond; M1,
M2, M4, M7, M8, M10 show a `TODO:` callout where no demo exists.

## V9 — Navigation depth (SC-010)

From `index.qmd`, reach each of M1–M10, the dataset page, the glossary
and the function page in ≤ 2 clicks.

## V10 — External references (SC-007, FR-043)

- OpenStax: section titles and numbers match the PDF table of contents
  (`pdftotext -f 1 -l 12 -layout introductory-business-statistics-2e_-_WEB.pdf -`).
- Khan Academy: open each unit link in a browser (cannot be automated;
  the site is client-rendered). Record the date in each module's
  further-reading table.

## V11 — Beginner pilot (SC-005, SC-006, SC-011)

After publish to a test audience: time the M2 Excel lab with a student
who has never used a PivotTable; collect mock-exam scores after M9.
**Expected**: ≥ 90% finish M2's lab in 60 min; ≥ 80% score ≥ 60% on the
mock exam.

## Tooling note

`verify_dataset.py`, `check_modules.py` and `fidelity-record.md` are
authored during implementation (see `/speckit-tasks`). They live in the
feature directory and are not part of the site build.
