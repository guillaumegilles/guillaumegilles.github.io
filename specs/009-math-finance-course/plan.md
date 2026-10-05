# Implementation Plan: Cours de Mathématiques Financières (M1)

**Branch**: `009-math-finance-course` | **Date**: 2026-10-04 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/009-math-finance-course/spec.md`

**Note**: This plan was produced by the `/speckit-plan` command.

## Summary

Create a complete French financial mathematics course for M1 business-school students
at `fr/teaching/mathematics-finance/`, built from the detailed pedagogical outline in
`teaching/mathematical-finance/index.qmd`. The deliverable is **6 new `.qmd` files**
(index/syllabus, 3 day-modules, glossaire, formulaire) plus `_metadata.yml`, sidebar
registration in `_quarto.yml`, and three OJS interactive demos (one per day).
An English stub at `teaching/mathematical-finance/` is also updated so that the
bilingual parity requirement is satisfied. No new Quarto extensions or runtime
dependencies are needed — OJS is natively supported.

## Technical Context

**Language/Version**: Quarto Markdown (`.qmd`) with YAML front matter; Quarto CLI
(version already installed in project).

**Primary Dependencies**: Quarto (sole content pipeline); `assets/dark.scss` (HTML
theme); OJS (natively supported by Quarto, used for all three interactive demos);
no new extensions required.

**Storage**: Filesystem — 6 new `.qmd` files under
`fr/teaching/mathematics-finance/`; 1 new `_metadata.yml` under that directory;
edits to `_quarto.yml` (sidebar blocks for EN and FR); minor update to the existing
`teaching/mathematical-finance/index.qmd` (promote to proper EN syllabus or add stub
notice).

**Testing**: `quarto render` exit code 0; manual link-follow audit of the French
sidebar; visual check that OJS demos load without errors; verify all internal links
in `index.qmd` resolve to correct pages.

**Target Platform**: GitHub Pages (static HTML output in `docs/`).

**Project Type**: Quarto website (static site).

**Performance Goals**: N/A — static site; rendering time is not a user-facing metric.

**Constraints**:
- No new runtime dependencies (no R, no npm packages, no new Quarto extensions).
- `quarto render` must exit 0 before any commit touching `.qmd` sources or `_quarto.yml`.
- Both EN and FR render targets must pass (Principle VI + Development Workflow gate).
- All custom styling in `assets/dark.scss` only (Principle V).
- No inline `style=` attributes or `<style>` blocks (Principle V).
- Interactive demos: OJS only (no Shinylive needed — all computations are pure arithmetic).

**Scale/Scope**: 6 French `.qmd` files + 1 `_metadata.yml` + `_quarto.yml` sidebar
changes + 1 English stub update.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Content-First** — All French pages are `.qmd` sources rendered by Quarto;
  no direct HTML in `docs/`. OJS blocks are native Quarto syntax.
- [x] **II. Navigation registered** — A new `fr-mathematics-finance` sidebar block
  will be added to `_quarto.yml` covering all 6 French pages. The existing
  `teaching/mathematical-finance/index.qmd` currently has no sidebar registration
  — an `en-mathematics-finance` sidebar block will be added simultaneously.
  _Note_: the current EN `index.qmd` is rendered but has no sidebar; this feature
  corrects that violation as part of scope.
- [x] **III. Reproducible** — French `.qmd` files contain no Python computation
  requiring re-execution; `_freeze/` entries produced by `quarto render` will be
  committed alongside source changes.
- [x] **IV. Privacy-First** — OJS demos compute values from user-controlled sliders
  using pure arithmetic; no external calls, no cookies, no analytics.
- [x] **V. Styling contained** — No inline styles or `<style>` blocks. All theme
  adjustments (if any) go in `assets/dark.scss` only.
- [x] **VI. Bilingual parity** — This feature creates the FR course. The existing EN
  `teaching/mathematical-finance/index.qmd` already renders (it is the raw course
  plan). It will be refactored into a proper EN syllabus stub with `lang: en` and a
  "translation in progress / cours disponible en français" notice. Full EN course
  pages are out of scope for this feature (see Assumptions in spec); the stub
  satisfies the parity rule.
- [x] **T-I. Content Fidelity** — All canonical theory (formulas, examples, exercises)
  from `teaching/mathematical-finance/index.qmd` is preserved and structured into the
  FR pages. No content is removed; it is reorganised.
- [x] **T-II. Pedagogical Structure** — Each module follows: intuition économique →
  représentation (ligne du temps) → formalisation mathématique → décision managériale →
  exercices (N1/N2/N3) with collapsible solutions.
- [x] **T-III. Audience language** — French prose targets M1 business-school students.
  Every formula is followed by a plain-language explanation.
- [x] **T-IV. Interactive demos** — One OJS demo per day-module (capitalisation vs
  actualisation / prix obligataire vs taux / VAN et TRI). Remaining priority concepts
  are marked with `TODO:` `.callout-important` blocks.
- [x] **T-V. Glossary** — `fr/teaching/mathematics-finance/glossaire.qmd` lists all
  symbols and terms introduced across the three modules.
- [x] **T-VI. Proof** — Each module includes at least one collapsible formal derivation
  (`.callout-caution` with `collapse="true"`).
- [x] **T-VII. Visual intuition** — Geometric interpretations are surfaced: time line
  diagrams for capitalisation/actualisation, convexity discussion for bond price-rate
  relationship, NPV curve crossing zero for IRR.
- [x] **T-VIII. Course syllabus** — `fr/teaching/mathematics-finance/index.qmd` is the
  course syllabus, is the first entry in the FR sidebar block, and contains a
  Recommended Literature section with author/title/edition/publisher for all 5
  references.

## Project Structure

### Documentation (this feature)

```text
specs/009-math-finance-course/
├── plan.md          ← this file
├── research.md      ← Phase 0 output
├── data-model.md    ← Phase 1 output
├── quickstart.md    ← Phase 1 output
├── contracts/       ← Phase 1 output (URL + page structure contracts)
└── tasks.md         ← Phase 2 output (speckit-tasks — NOT created here)
```

### Source files (repository root)

```text
_quarto.yml                                   ← sidebar blocks added (EN + FR)

teaching/mathematical-finance/
├── index.qmd                                 ← refactored: EN stub/syllabus, lang: en
└── image.jpg                                 ← kept as-is

fr/teaching/mathematics-finance/
├── _metadata.yml                             ← sets lang: fr for all FR pages
├── index.qmd                                 ← FR syllabus (T-VIII compliant)
├── module-01.qmd                             ← Journée 1 : valeur temps, annuités
├── module-02.qmd                             ← Journée 2 : emprunts, obligations
├── module-03.qmd                             ← Journée 3 : VAN, TRI, risque
├── glossaire.qmd                             ← Glossaire central (T-V)
└── formulaire.qmd                            ← Formulaire de référence (10 formules)
```

**Structure Decision**: Folder-per-language as mandated by Principle VI. All French
content is self-contained under `fr/teaching/mathematics-finance/`. File naming
follows the established `module-NN.qmd` pattern from `fr/teaching/mathematical-fundamentals/`.

## Complexity Tracking

> No Constitution Check violations — table omitted.
> The only pre-existing violation (EN `index.qmd` has no sidebar registration) is
> corrected as part of this feature's scope.
