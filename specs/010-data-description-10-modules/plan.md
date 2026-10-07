# Implementation Plan: Data Description — 10-Module Redesign

**Branch**: `010-data-description-10-modules` | **Date**: 2026-10-06 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/010-data-description-10-modules/spec.md`

## Summary

Replace the 12-session Data Description course with **10 modules × 180
minutes** for 2nd-year business students, English-only, Excel woven into
every module, on a new two-franchise "Wandering Fork" dataset (240 rows,
16 columns). The work is mostly **content migration plus authoring**:
nine of the ten modules re-use existing session text, derivations and
four existing Shinylive demos; Module 1 is new; the dataset, a data
page, an Excel-function page and a fidelity record are new.

Planning corrected three things the brainstorm got wrong (see
[research.md](./research.md)): the OpenStax section numbers (and the fact
that OpenStax has **no** box-plot, weighted-mean or scatter-plot
section), the unverifiable Khan Academy deep links, and the 120-minute
(not 180) time budget. It also found that the sidebar and live syllabus
already point at session files that no longer exist, so restoring a green
render is the first step.

**Technical approach**: static content only. Quarto `.qmd` pages under
`teaching/data-description/modules/`, one seeded Python script to
generate and verify the dataset, Quarto-native `draft: true` to keep the
course hidden until complete, then one publishing change.

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`) / Pandoc Markdown, LaTeX
math; Python 3.x in the project `.venv` for dataset generation and
checks only

**Primary Dependencies**: Quarto 1.4.537; `quarto-ext/shinylive`
(already in `teaching/data-description/_extensions/`); `numpy`, `pandas`,
`openpyxl`, `scipy` (already in `.venv`; nothing new to install); `pdftotext`
for reference checks (already available)

**Storage**: Flat files — `.qmd` sources; datasets as CSV and XLSX in
`teaching/data-description/data/`; rendered HTML in `docs/`

**Testing**: `quarto render` exit 0; `verify_dataset.py` (invariants and
recomputed statistics); `check_modules.py` (module contract, time
budget); manual browser check of three required demos; manual
Khan Academy link verification; see [quickstart.md](./quickstart.md)

**Target Platform**: Static site on GitHub Pages (`docs/` on `main`)

**Project Type**: Static teaching site (content only)

**Performance Goals**: N/A. Practical: each module page renders and loads
without broken assets; demos load lazily as elsewhere on the site

**Constraints**: English only; prose wrapped at 80 characters; no
tracking, cookies, embeds or third-party iframes; no new runtime
dependency; pages hidden until the course is complete; module page
structure fixed by the contract

**Scale/Scope**: 10 modules, 1 syllabus, 3 reference pages (dataset,
glossary, Excel functions), ~4 data files, ~2,900 lines of existing
session text to migrate

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1.*

- [x] **I. Content-First** — Every page is a `.qmd`; datasets are
  downloadable resources, not pages. No raw HTML in `docs/`.
- [x] **II. Navigation registered** — Sidebar contract lists every page;
  old session entries removed (see
  `contracts/dataset-and-navigation-contract.md`).
- [x] **III. Reproducible** — Demos run client-side; no executed cells
  planned, so no `_freeze/` change. If a module adds an executed cell,
  its freeze entry is committed.
- [x] **IV. Privacy-First** — Khan Academy is linked, never embedded;
  demos run in the browser; datasets are invented. No analytics added.
- [x] **V. Styling contained** — No `style=` or `<style>` in modules.
  *Precedent note*: the existing Shinylive apps style their own iframe
  (`ui.tags.style`) because `assets/dark.scss` cannot reach inside the
  app; this is carried over unchanged from feature 005.
- [ ] **VI. Bilingual parity** — **Deviation, justified**: English only
  now; French deferred by design decision 5. See Complexity Tracking.

*Teaching pages:*

- [x] **T-I. Content Fidelity** — Fidelity record maps every old block
  (FR-039); drops need a reason.
- [x] **T-II. Pedagogical Structure** — Contract fixes theory → example
  → exercises.
- [x] **T-III. Audience language** — Contract requires a plain-language
  sentence after every formula.
- [x] **T-IV. Interactive demos** — M3, M5, M9 required (existing demos
  migrated); other priority concepts carry `TODO:` callouts.
- [x] **T-V. Glossary** — `modules/glossary.qmd` updated per module;
  "Introduced in" column switched to modules.
- [x] **T-VI. Proof** — A collapsible derivation is assigned to every
  module including M10 (data-model §1).
- [x] **T-VII. Visual intuition** — Contract section 8; variance as
  squared distance, regression as best-fit line.
- [x] **T-VIII. Course syllabus** — `index.qmd` stays first in the
  sidebar and gains OpenStax and Khan Academy in Recommended Literature
  (contract §4).

**Post-design re-check (after Phase 1)**: unchanged. No new violation
introduced by the data model or contracts. Only VI remains a justified
deviation.

## Project Structure

### Documentation (this feature)

```text
specs/010-data-description-10-modules/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── module-page-contract.md
│   └── dataset-and-navigation-contract.md
├── checklists/requirements.md
├── spec.md
├── verify_dataset.py        # authored in implementation
├── check_modules.py         # authored in implementation
├── fidelity-record.md       # authored in implementation
└── tasks.md                 # /speckit-tasks (not created here)
```

### Source (repository root)

```text
_quarto.yml                          # sidebar block rewritten
teaching/data-description/
├── index.qmd                        # syllabus (rewritten last)
├── image.jpg
├── data/
│   ├── wandering-fork.csv           # new, 240 rows
│   ├── wandering-fork.xlsx          # new
│   ├── payroll-skew.csv             # new
│   └── lakeside-bakery.csv          # new
├── modules/
│   ├── _metadata.yml                # draft: true (removed at publish)
│   ├── module-01.qmd … module-10.qmd
│   ├── dataset.qmd                  # new
│   ├── glossary.qmd                 # exists; updated
│   └── excel-functions.qmd          # new (from the .txt)
├── _extensions/quarto-ext/shinylive # exists
└── ressources/                      # unchanged (source archives, syllabi)
```

Removed during migration: `modules/session-04…12.qmd`,
`modules/excel-worksheet.qmd`, `modules/excel-worksheet-2.qmd`,
`modules/Excel_functions_English_French.txt`. `AGENTS.md`'s Spec Kit
pointer is updated to this plan.

**Structure Decision**: Single Quarto course directory, following the
owner's in-progress `modules/` layout and the sibling courses'
conventions; no application code, no new top-level directories except
`data/`.

## Delivery phases

Ordered by dependency. `/speckit-tasks` turns these into tasks.

| Phase | Goal | Depends on | Output |
|---|---|---|---|
| **A. Stabilise** | Make the site render again | — | Sidebar rewritten to the module list; `_metadata.yml` with `draft: true`; `module-01.qmd` renamed `module-02.qmd`; `quarto render` exit 0 |
| **B. Dataset** | Generate and verify data | — (parallel with A) | `data/*`, `verify_dataset.py`, `dataset.qmd`; figures table for later modules |
| **C. Shell** | Shared pages | A | `excel-functions.qmd`, glossary updated, fidelity-record skeleton, `check_modules.py` |
| **D1. Modules 1–3** | Organise data | B, C | M1 (new), M2 (from old S3 + Excel), M3 (from S4 + histogram demo) |
| **D2. Modules 4–7** | Summarise one variable | D1 | M4 (S6 + weighted mean), M5 (S5 + boxplot demo), M6 (S7 + demo), M7 (S8 + S9 + conceptual kurtosis) |
| **D3. Modules 8–10** | Two variables, synthesis | D2, B | M8 (S10), M9 (S11 + demo), M10 (S12 rebuilt on Lakeside data, mock exam) |
| **E. Verify** | Quality gates | D1–D3 | Quickstart V1–V10 passed; fidelity record complete; Khan Academy links opened by owner |
| **F. Publish** | One-change release | E | Remove `draft: true`; rewrite `index.qmd` (outline, assessment, literature); delete old files; `quarto render`; commit `docs/` |

D1, D2 and D3 can each be split across authors because modules touch
disjoint files; the glossary is the only shared file (append-only).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| Constitution VI — no French counterpart pages | Design decision 5: the course is authored in English first and translated once finished. Same accepted deviation as features 004 and 005. | Writing stub FR pages for 14 pages now adds noise that will be overwritten by the real translation; a stub-only approach also needs the language switcher routes, which are out of scope for a content rewrite. A follow-up feature will add FR parity. |

## Open items for the owner (not blockers for tasks)

1. Open each Khan Academy unit link in a browser and confirm (Phase E).
2. Confirm midterm = M1–M5 and final = M1–M10 (research §6).
3. Confirm the franchise names **Harbour** and **Campus** (cosmetic).
4. `index.qmd` is live with dead links today; decide whether a quick
   interim fix is wanted before publish (plan assumes not).
