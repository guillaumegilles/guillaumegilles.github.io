# Implementation Plan: Complete English Course — Mathematical Fundamentals and Data Analysis

**Branch**: `004-math-fundamentals-course` | **Date**: 2026-07-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/004-math-fundamentals-course/spec.md`

## Summary

Deliver a complete, English-language, eight-module Quarto course under
`teaching/mathematical-fundamentals/`, faithfully derived from the source
archives (`MS01-001-G_Fondamentaux` and `MS01-001-G_Fondamentaux-26`: slide
decks, student handouts, final exam) and the existing partial drafts. Each
module is developed to the depth of the current Module 1 (full lesson prose,
multiple worked examples, sizeable exercise banks), uses LaTeX math throughout,
and presents all exercises as static revealable solutions (no interactive
runtime widgets). The work also brings the course into line with the project
constitution by adding a glossary, a collapsible derivation per module, an
English Recommended Literature section, constitution-compliant callout
semantics, and proper `_quarto.yml` navigation registration.

**Technical approach**: This is a static content feature — no application code.
The deliverables are `.qmd` source files rendered by Quarto to `docs/`. The
build gate is `quarto render` exiting 0 with correct math rendering and no
broken links.

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`) + Pandoc Markdown; LaTeX math
(`$...$` / `$$...$$`) — Quarto 1.x

**Primary Dependencies**: Quarto CLI; native math rendering (KaTeX/MathJax as
configured by the site); `quarto-ext/shinylive` extension (present in the course
`_extensions/`, but interactive demos are intentionally deferred — see
Complexity Tracking); Quarto callout blocks (`.callout-*`)

**Storage**: Flat files — `.qmd` sources under
`teaching/mathematical-fundamentals/`; rendered HTML committed to `docs/`;
computation cache (if any) under `_freeze/`

**Testing**: `quarto render` MUST exit 0; manual/scripted link check across the
syllabus and eight modules; visual verification of math rendering and
collapsible solutions

**Target Platform**: Static site served by GitHub Pages from `docs/` on `main`

**Project Type**: Static documentation/teaching site (Quarto) — content only, no
runtime backend

**Performance Goals**: N/A (static pages). Practical goal: each module page
renders and loads without broken assets.

**Constraints**: Source prose wraps at 80 characters; all math in LaTeX; no
inline `style=` / `<style>`; no tracking/cookies; callout semantics per
constitution §V; content in English (learner-facing)

**Scale/Scope**: 1 syllabus (`index.qmd`) + 8 module files (`module-1.qmd` …
`module-8.qmd`, of which `module-8.qmd` is new) + 1 `glossary.qmd`; ~8 source
slide decks + handouts + final exam as reference inputs

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

- [x] **I. Content-First** — All deliverables are `.qmd` sources; HTML is
  generated into `docs/`. No hand-written HTML. **PASS**
- [~] **II. Navigation registered** — The course is currently registered only in
  a local `_metadata.yml` (partial) and is **absent from `_quarto.yml`**. Plan
  adds a proper `mathematical-fundamentals` sidebar block to `_quarto.yml`
  (authoritative) listing the index, all eight modules, and the glossary. This
  supersedes/reconciles the spec's clarification wording that referenced
  `_metadata.yml`. **PASS (after implementation)**
- [x] **III. Reproducible** — Regenerated `docs/` and any `_freeze/` entries are
  committed with the source changes. No incidental freeze deletions. **PASS**
- [x] **IV. Privacy-First** — Pure static content; no scripts, cookies, embeds,
  or third-party calls introduced. Removing the `shinylive` runtime blocks
  further reduces client-side code. **PASS**
- [x] **V. Styling contained** — No CSS/SCSS changes required; if any are needed
  they go in `assets/dark.scss`. Callout usage follows the constitution table
  (note=definitions, tip=formulas, warning=caveats, important=exam/critical,
  caution+collapse=exercises/proofs). Legacy `.callout-tip` solution blocks are
  migrated to `.callout-caution collapse="true"`. **PASS**
- [~] **VI. Bilingual parity** — No `fr/` tree exists anywhere in the repo and no
  language switcher is implemented site-wide; the site is English-only in
  practice today. The user explicitly requested English content. French
  counterparts for this course are **deferred** (documented in Complexity
  Tracking) as a pre-existing, cross-cutting gap out of this feature's scope.
  `lang: en` front matter WILL be set on all new/edited course files. **DEVIATION
  (justified & deferred)**

*Teaching pages:*
- [x] **T-I. Content Fidelity** — Source theory, worked examples, and exercises
  are preserved; existing draft answers retained. **PASS**
- [x] **T-II. Pedagogical Structure** — Every module follows theory → worked
  examples → exercises with collapsible solutions. **PASS**
- [x] **T-III. Audience language** — Plain English for business students; every
  formula gets a prose explanation. **PASS**
- [~] **T-IV. Interactive demos** — Spec clarification mandates static-only
  exercises and conversion of Module 1's `shinylive` quizzes to static form,
  which conflicts with "priority concepts MUST have a Shinylive demo." Reconciled
  via the escape hatch T-IV itself provides: each priority concept without a demo
  is marked with a `.callout-important` `TODO:` block, keeping gaps trackable.
  **DEVIATION (justified; gaps tracked per T-IV)**
- [x] **T-V. Glossary** — A new `glossary.qmd` (FR↔EN terms, notation, plain
  definitions) is created and added to the sidebar. **PASS (after implementation)**
- [x] **T-VI. Proof** — Each module includes at least one collapsible derivation
  (`.callout-caution collapse="true"`), e.g., sum of an arithmetic/geometric
  series, compound-interest formula, the discriminant, or the derivative of a
  quadratic from the rate of change. **PASS (after implementation)**
- [x] **T-VII. Visual intuition** — Geometric/graphical intuition surfaced where
  applicable (lines, feasible regions, function graphs, tangent slope as
  derivative). **PASS**
- [x] **T-VIII. Course syllabus** — `index.qmd` exists at the course root, is the
  first sidebar entry, and its Recommended Literature section is rewritten in
  English with author, title, edition, and publisher for each reference. **PASS
  (after implementation)**

**Gate result**: PASS with two justified deviations (VI bilingual parity
deferred; T-IV interactive demos replaced by tracked TODO callouts). See
Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/004-math-fundamentals-course/
├── plan.md              # This file
├── research.md          # Phase 0 — decisions & source→module mapping
├── data-model.md        # Phase 1 — content entities & module coverage matrix
├── quickstart.md        # Phase 1 — how to build & verify the course
├── contracts/
│   ├── module-page.md   # Required structure of a module page
│   ├── syllabus-page.md # Required structure of index.qmd
│   └── glossary-page.md # Required structure of glossary.qmd
└── checklists/
    └── requirements.md  # Spec quality checklist (from /speckit.specify)
```

### Source Code (repository root)

```text
teaching/mathematical-fundamentals/
├── _metadata.yml        # Local metadata; reconciled with _quarto.yml nav
├── index.qmd            # Syllabus (EN) — + English Recommended Literature
├── module-1.qmd         # Essential mathematical calculations (translate+extend)
├── module-2.qmd         # Mastering equations (translate+complete)
├── module-3.qmd         # Curve analysis (rewrite outline dumps into prose)
├── module-4.qmd         # Financial-math tools: numerical sequences (author)
├── module-5.qmd         # Application of financial math: interest (author)
├── module-6.qmd         # Functions in economics/management (author)
├── module-7.qmd         # Introduction to optimization (author)
├── module-8.qmd         # Revision & final-exam prep (NEW)
├── glossary.qmd         # NEW — FR↔EN glossary of symbols/terms
└── MS01-001-G_Fondamentaux*/   # Reference source archives (unmodified)

_quarto.yml              # ADD: mathematical-fundamentals sidebar block
docs/                    # Regenerated HTML output (committed)
```

**Structure Decision**: Single Quarto content course. One `.qmd` per module
(8 modules) plus syllabus and glossary, all under
`teaching/mathematical-fundamentals/`. Navigation is registered authoritatively
in `_quarto.yml`. No application source tree applies (content-only feature).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| **VI. Bilingual parity deferred** (no `fr/` counterparts, no language switcher) | User explicitly requested English-only content; the entire site currently has no `fr/` tree or switcher, so adding a lone FR course would be inconsistent and out of scope | Creating FR stubs for just this course would neither satisfy site-wide parity nor the user's request; a proper bilingual rollout is a separate cross-cutting feature |
| **T-IV. Shinylive demos replaced by `TODO:` callouts** | Spec clarification (session 2026-07-23) mandates static-only exercises and conversion of Module 1's interactive quizzes to static form (reliable rendering, privacy, lighter pages) | Keeping/adding `shinylive` blocks contradicts the accepted clarification; T-IV explicitly permits marking demo gaps with a `.callout-important` `TODO:` block, so gaps stay tracked without runtime widgets |
