# Implementation Plan: Concrete-to-Abstract Pedagogy — Data Description

**Branch**: `012-data-description-pedagogy` | **Date**: 2026-10-13 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/012-data-description-pedagogy/spec.md`

## Summary

Re-sequence the in-class part of each Data Description module from
abstract-first (formula → paraphrase → numbers) to a **concrete → visual
→ verbal → symbolic** micro-cycle (*Try it → See it → Say it → Write it
→ Notation decoder*), move every Excel lab into a **Homework — Excel
lab** section at the end of the page, and spend the freed ~50 minutes on
concept construction, notation fluency and by-hand practice, closed by
an exit check.

**Module 6 (Dispersion) is the pilot**, due before the next class. It
uses two hand-friendly trucks with the same €620 mean (Truck A: s = 20,
Truck B: s = 200 — verified in [research.md](./research.md) R2), a
deviation table that makes "deviations sum to zero" the motivation for
squaring and for $n-1$, an OJS two-truck figure that reveals dots →
deviations → squares step by step, and
notation decoders for every formula. All theory callouts, the worked
example values, derivation, demo and all six existing exercises are
kept; the three Excel exercises become Homework 1–3.

**Technical approach**: content-only edits to `.qmd` files; one `{ojs}`
step-reveal figure; a v2 module contract and a v2 structure
checker for revised modules; then a module template, a syllabus update
and the rollout to Modules 7–10 in teaching order.

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`), LaTeX math; Observable
JS (Quarto `{ojs}`) for the figure; Python 3 in `.venv` for the checker

**Primary Dependencies**: Quarto 1.10.19; `quarto-ext/shinylive`
(existing demo, unchanged); Quarto's built-in OJS runtime with
Observable Plot and Inputs (already used in
`teaching/mathematical-fundamentals/`); `numpy` for number checks.
Nothing new to install

**Storage**: Flat files — `.qmd` sources, `_freeze/` cache, rendered
`docs/`

**Testing**: `check_modules_v2.py` (contract v2), v1 checker for
unrevised modules, NumPy number check, `quarto render` exit 0, manual
browser walkthrough — see [quickstart.md](./quickstart.md)

**Target Platform**: Static site on GitHub Pages (`docs/`)

**Project Type**: Static teaching site (content only)

**Performance Goals**: N/A; the OJS figure renders client-side in
under a second (no WebAssembly, unlike the Shinylive demo)

**Constraints**: Module 6 ready before the next class; English only;
prose ≤ 80 chars; no new callout types or styles; no tracking or new
runtime; no removal of existing content (T-I); worked-example numbers
unchanged

**Scale/Scope**: 1 pilot module (~420 lines), then 4 modules (7–10);
1 glossary, 1 syllabus, 1 template, 1 contract, 1 checker, 1 fidelity
record. Modules 1–5 out of scope

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1.*

- [x] **I. Content-First** — Only existing `.qmd` files edited; the
  template, contract and fidelity record are spec documents, not pages.
- [x] **II. Navigation registered** — Homework stays on the module
  page. The only `_quarto.yml` change is the new `fr-data-description`
  sidebar block that registers the French stubs (FR-021).
- [x] **III. Reproducible** — The OJS figure runs in the browser; no
  executed cell, so no `_freeze/` change (R3).
- [x] **IV. Privacy-First** — OJS runtime is the same one already used
  on the site; a task verifies no third-party CDN request (R3).
- [x] **V. Styling contained** — New elements reuse existing callout
  semantics (R4); no SCSS change, no `style=`, no `<style>`. The figure's
  colours are Plot options (chart content, not page CSS).
- [x] **VI. Bilingual parity** — Resolved by FR-021: one French stub
  page per English module page under
  `fr/teaching/data-description/modules/` ("Contenu en préparation" +
  link to the English page), registered in a new `fr-data-description`
  sidebar block. Full translation stays out of scope, as the principle
  allows.

*For teaching pages only:*

- [x] **T-I. Content Fidelity** — Nothing removed; moves and renumbering
  tracked in `fidelity-record.md` (data-model §4).
- [x] **T-II. Pedagogical Structure** — Theory → worked example →
  exercises kept; concrete activities live inside Theory and introduce
  each concept before use (contract v2).
- [x] **T-III. Audience language** — Strengthened: "In plain words" line
  plus a notation decoder for every formula.
- [x] **T-IV. Interactive demos** — Module 6 Shinylive demo kept as is.
- [x] **T-V. Glossary** — Adds $x_i$, $\sum_{i=1}^{n}$ (with
  pronunciation) and $x_i-\bar{x}$ (R10).
- [x] **T-VI. Proof** — Collapsible shortcut-formula derivation kept.
- [x] **T-VII. Visual intuition** — Strengthened: the OJS figure's
  third step draws each squared deviation as a square, so variance is
  seen as squared distance (area) before the formula.
- [x] **T-VIII. Course syllabus** — `index.qmd` edited (module pattern,
  personal work); Recommended Literature and first sidebar position
  untouched. No inline div-toggle bilingual patterns used.

**Post-design re-check (after Phase 1, revised after /speckit-analyze)**:
all gates pass. VI is now satisfied by the French stubs (FR-021)
instead of being carried as a deviation.

## Project Structure

### Documentation (this feature)

```text
specs/012-data-description-pedagogy/
├── plan.md                         # this file
├── research.md                     # Phase 0
├── data-model.md                   # Phase 1
├── quickstart.md                   # Phase 1
├── contracts/
│   └── module-page-contract-v2.md  # Phase 1
├── checklists/requirements.md      # /speckit-specify
├── spec.md
├── check_modules_v2.py             # authored in implementation
├── fidelity-record.md              # authored in implementation
├── module-template.md              # authored in implementation (US3)
└── tasks.md                        # /speckit-tasks (not created here)
```

### Source (repository root)

```text
teaching/data-description/
├── index.qmd                       # syllabus: one sentence now (M6),
│                                   # full wording with template (US3)
└── modules/
    ├── module-06.qmd               # PILOT — restructured (US1, US2)
    ├── module-07.qmd               # rollout + first homework debrief
    ├── module-08.qmd               # rollout
    ├── module-09.qmd               # rollout
    ├── module-10.qmd               # rollout: Excel replicate → homework
    └── glossary.qmd                # + x_i, Σ (Module 4), x_i − x̄ (Module 6)
fr/teaching/data-description/
├── index.qmd                       # existing stub + link to EN
└── modules/                        # NEW: 13 French stubs (FR-021)
_quarto.yml                         # + fr-data-description sidebar block

docs/teaching/data-description/...  # rendered output, committed
```

**Structure Decision**: Single static Quarto site. Content edits stay in
the existing course directory; the only new pages are the French stubs
and their sidebar block. Spec
artefacts (checker, template, fidelity record) live in the feature
directory, like feature 010's.

## Delivery phases

| Phase | Scope | Deadline driver | Spec |
|---|---|---|---|
| A | v2 checker + Module 6 restructure + glossary + fidelity record + one syllabus sentence | Next class (Module 6) | US1, US2 |
| B | Module 7: debrief row (fallback edit if the full revision is late, R8), then full revision | Module 7 class | US2 FR-019, US4 |
| C | Module template + full syllabus wording | Before Module 8 revision | US3 |
| D | Modules 8, 9, 10 in teaching order | Each module's class | US4 |

Each phase ends with the quickstart checks and a commit including
`docs/` and `_freeze/`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|

| Two module contracts coexist during rollout (v1, v2) | Modules are revised one at a time ahead of each class | Changing all modules at once is impossible before the next class; editing the v1 checker would break checks on unrevised modules |
