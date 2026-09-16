# Implementation Plan: Data Description Course (MS03-001-G)

**Branch**: `006-data-description-course` | **Date**: 2026-09-12 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/005-data-description-course/spec.md`

## Summary

Deliver a complete, English-language, 15-file Quarto course under
`teaching/data-description/`: a syllabus (`index.qmd`), a glossary
(`glossary.qmd`), and 12 session pages (`session-01.qmd` …
`session-12.qmd`) grouped into three parts (Excel Fundamentals →
Univariate Data Treatment → Bivariate Data Treatment). Content is
faithfully derived from the three `ressources/` Moodle archives at the
level of concepts, formulas, worked-example structure, and difficulty —
but **not** at the level of literal figures: the running case study is
renamed **"The Wandering Fork"** and driven by an originally-authored,
statistically-verified 30-day dataset (this plan's `wandering-fork-dataset.csv`)
so every session reuses identical, internally consistent numbers. Four
priority concepts get Shinylive interactive demos; all 15 files carry
`draft: true` until the whole course is complete, then flip to published
together; Session 12 closes with an original mock-exam section.

**Technical approach**: This is a static content feature — no application
code. The deliverables are `.qmd` sources rendered by Quarto to `docs/`,
plus one Python extraction pass (run once, ad hoc, not committed as a
build step) over the binary source archives to recover exact source text
before authoring each session. The build gate is `quarto render` exiting
0 with correct math rendering, no broken links, and all four required
Shinylive demos functioning in the browser.

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`) + Pandoc Markdown; LaTeX
math (`$...$` / `$$...$$`); Python 3.11 (project `.venv`) for one-time,
non-shipped source-extraction scripts

**Primary Dependencies**: Quarto CLI; `quarto-ext/shinylive` extension
(copied into `teaching/data-description/_extensions/`, mirroring
`teaching/mathematical-fundamentals/_extensions/`); Quarto callout blocks
(`.callout-*`); `python-pptx` and `python-docx` (NEW, `.venv`-only,
**not committed** per constitution — needed to read the `.pptx` slide
decks and `.docx` handouts in `ressources/`, which are not otherwise
machine-readable); `pandas`/`numpy`/`openpyxl` (already present in
`.venv`, used to read source `.xlsx` workbooks and to generate/verify the
"Wandering Fork" dataset's statistics)

**Storage**: Flat files — `.qmd` sources under `teaching/data-description/`;
the original "Wandering Fork" dataset committed once as
`specs/005-data-description-course/wandering-fork-dataset.csv` (canonical
source of truth for every session's numbers); rendered HTML committed to
`docs/`; no `_freeze/` entries expected (no executed code cells — Shinylive
runs client-side WASM, not at render time)

**Testing**: `quarto render` MUST exit 0; manual link check across the
syllabus, glossary, and 12 sessions; visual verification of math
rendering, collapsible solutions, and the 4 Shinylive demos in a browser;
cross-check of every worked-example/exercise result against the
statistics already verified in `data-model.md` (no hand arithmetic)

**Target Platform**: Static site served by GitHub Pages from `docs/` on
`main`

**Project Type**: Static documentation/teaching site (Quarto) — content
only, no runtime backend

**Performance Goals**: N/A (static pages). Practical goal: each session
page renders and loads without broken assets; Shinylive WASM bundles load
without blocking page render (lazy per existing site convention).

**Constraints**: Source prose wraps at 80 characters; all math in LaTeX;
no inline `style=`/`<style>`; no tracking/cookies; callout semantics per
constitution §V; all learner-facing content in English; case-study
figures MUST be original and internally consistent (FR-006); all 15
files carry `draft: true` until complete (FR-017); no verbatim
reproduction of source exam content (FR-018)

**Scale/Scope**: 1 syllabus + 1 glossary + 12 session files + 1
`_extensions/quarto-ext/shinylive/` copy + 1 new `_quarto.yml` sidebar
block + 1 canonical dataset CSV (already generated and verified in this
plan) + 4 Shinylive demo blocks + ~3 Moodle archives as reference-only
inputs (never published)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

- [x] **I. Content-First** — All deliverables are `.qmd` sources; HTML is
  generated into `docs/`. No hand-written HTML. **PASS**
- [x] **II. Navigation registered** — Plan adds a new `data-description`
  sidebar block to `_quarto.yml` (the site's only authoritative nav
  source) listing the index, all 12 sessions grouped by part, and the
  glossary. **PASS (after implementation)**
- [x] **III. Reproducible** — No executed code cells are planned (Shinylive
  is client-side WASM, not rendered server-side), so no `_freeze/` entries
  are expected. The one-time Python extraction scripts are ad hoc
  (run from `.venv`, not part of the Quarto build) and produce no
  committed computation cache. **PASS**
- [x] **IV. Privacy-First** — Pure static content; the Shinylive extension
  is the same self-hosted, tracking-free component already vetted for
  `teaching/mathematical-fundamentals/`. No cookies, analytics, or
  third-party calls introduced. **PASS**
- [x] **V. Styling contained** — No CSS/SCSS changes required. Callout
  usage follows the constitution table (note = definitions, tip =
  formulas, warning = caveats, important = exam tips/TODO gaps,
  caution+collapse = exercises/proofs/solutions). **PASS**
- [~] **VI. Bilingual parity** — No `fr/` tree exists anywhere in the repo
  and no language switcher is implemented site-wide. Per the spec's
  Clarifications, this feature is English-first at the repository root,
  matching the two most recent precedents
  (`teaching/decision-making-stat/`, `004-math-fundamentals-course`).
  French parity for this course is **deferred**, documented here as a
  pre-existing, cross-cutting gap, not silently dropped (see Complexity
  Tracking). `lang: en` WILL be set on all 15 new files. **DEVIATION
  (justified & deferred, consistent with prior precedent)**

*Teaching pages:*
- [x] **T-I. Content Fidelity** — Per the spec's Clarifications, fidelity
  is scoped to concepts/formulas/structure/difficulty, not literal
  source figures (FR-003). Every topic in the syllabus's three blocks is
  covered (FR-004); nothing is silently dropped. **PASS (clarified
  scope)**
- [x] **T-II. Pedagogical Structure** — Every session follows theory →
  worked examples → exercises with collapsible solutions (FR-002).
  **PASS**
- [x] **T-III. Audience language** — Plain English for business students;
  every formula gets a prose explanation; a "Using Excel" reference
  accompanies every statistical concept (FR-007). **PASS**
- [x] **T-IV. Interactive demos** — 4 priority concepts (frequency
  distribution/histogram, quartiles/boxplot, central tendency &
  dispersion, scatter/correlation) get Shinylive demos (FR-008); any
  further gap is marked with a `.callout-important` `TODO:`. **PASS
  (after implementation)**
- [x] **T-V. Glossary** — `glossary.qmd` lists every symbol/formula
  introduced in any session, with notation, plain-language definition,
  and pronunciation guide for Greek letters (FR-010). **PASS (after
  implementation)**
- [x] **T-VI. Proof** — Each session includes at least one collapsible
  derivation of its central formula (FR-011), e.g., the quartile rank
  formula, the variance shortcut formula, the bounds of $r$. **PASS
  (after implementation)**
- [x] **T-VII. Visual intuition** — Geometric/graphical interpretation
  surfaced per FR-012 (boxplot as the five-number summary picture,
  variance as squared distance from the mean, correlation as scatter
  alignment). **PASS**
- [x] **T-VIII. Course syllabus** — `index.qmd` is the course root,
  first sidebar entry, and includes a Recommended Literature section
  with author/title/edition/publisher per FR-001. **PASS (after
  implementation)**

**Gate result**: PASS with one justified, already-precedented deviation
(VI bilingual parity deferred). See Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/005-data-description-course/
├── plan.md                      # This file
├── research.md                  # Phase 0 — decisions & source→session mapping
├── data-model.md                # Phase 1 — content entities & the verified dataset
├── wandering-fork-dataset.csv   # Phase 1 — canonical 30-day dataset (generated & stats-verified)
├── quickstart.md                # Phase 1 — how to build & verify the course
├── contracts/
│   ├── session-page.md          # Required structure of session-NN.qmd
│   ├── syllabus-page.md         # Required structure of index.qmd
│   └── glossary-page.md         # Required structure of glossary.qmd
└── checklists/
    └── requirements.md          # Spec quality checklist (from /speckit.specify + /speckit.clarify)
```

### Source Code (repository root)

```text
teaching/data-description/
├── _metadata.yml                     # lang: en; note nav lives in _quarto.yml
├── _extensions/
│   └── quarto-ext/shinylive/         # COPIED from mathematical-fundamentals/_extensions/
├── index.qmd                         # Syllabus (draft: true until complete) — FR-001
├── glossary.qmd                      # NEW (draft: true until complete) — FR-010
├── session-01.qmd … session-02.qmd   # Part I — Excel Fundamentals
├── session-03.qmd … session-09.qmd   # Part II — Univariate Data Treatment
├── session-10.qmd … session-12.qmd   # Part III — Bivariate Data Treatment (12 = mock exam)
└── ressources/                       # Existing archives — reference-only, unmodified

_quarto.yml                # ADD: data-description sidebar block (Parts I/II/III)
docs/                       # Regenerated HTML output (committed), produced only
                             # once draft: true is removed from all 15 files together
```

**Structure Decision**: Single Quarto content course, one `.qmd` per
session (12) plus syllabus and glossary, all flat under
`teaching/data-description/` (no per-block subfolders), matching the
`teaching/decision-making-stat/` convention. Navigation is registered
authoritatively in `_quarto.yml`. The canonical "Wandering Fork" dataset
lives once in the spec's own directory (`wandering-fork-dataset.csv`) so
every session file references the same numbers instead of each
inventing its own. No application source tree applies (content-only
feature).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| **VI. Bilingual parity deferred** (no `fr/` counterpart for this course, no language switcher) | The spec's Clarifications explicitly chose English-first per the two most recent site precedents; the site has no `fr/` tree or switcher anywhere yet, so adding one lone French course here would be inconsistent and out of scope | Authoring French stubs for just this course would neither satisfy site-wide parity nor match the accepted Clarification; a proper bilingual rollout is a separate, cross-cutting feature already deferred by `001-course-syllabus-index` and `004-math-fundamentals-course` |
