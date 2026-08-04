# Phase 0 — Research: Complete English Course (Mathematical Fundamentals)

All spec clarifications were resolved during `/speckit.clarify` (session
2026-07-23). This document records the design decisions needed to execute the
plan, plus the authoritative mapping from source materials to modules.

## Decision 1 — Content source of truth per module

**Decision**: Treat the full `MS01-001-G_Fondamentaux` archive as the primary
source (it contains all eight decks, student handouts, and the final exam). Use
`MS01-001-G_Fondamentaux-26` (2026 partial export: Modules 2–4) as the newer
overlay: where a concept or example appears in both, prefer the -26 version;
never drop a concept present in either.

**Rationale**: -26 is the more recent revision but only partial; the full
archive guarantees complete coverage including Modules 5–8 and the exam.

**Alternatives considered**: Using -26 alone (rejected: incomplete); merging
verbatim (rejected: risks duplication and contradictory numbering).

## Decision 2 — Source → module mapping

| Module | Title (EN) | Primary source deck | Handout / extra |
|---|---|---|---|
| 1 | Essential mathematical calculations for economics & management | `Module 1 - Calculs mathématiques … ETUDIANT.pptx` | existing `module-1.qmd` draft |
| 2 | Mastering equations for better decision-making | `Module 2 - Maîtrise des équations …` (both archives) | `Module 2 … ETUDIANTS.pdf`; existing draft |
| 3 | Curve analysis in economics & management | `Module 3 - Analyse des courbes …` (both archives) | `Module 3 … ETUDIANTS.pdf`; existing draft |
| 4 | Introduction to financial-mathematics tools | `Module 4 - Introduction mathématiques financières …` | `Module 4 … ETUDIANTS.pdf` |
| 5 | Application of financial mathematics | `Module 5 - Application mathématiques financières …` | — |
| 6 | Functions useful in economics & management | `Module 6 - Présentation des fonctions …` | — |
| 7 | Introduction to optimization | `Module 7 - Introduction à l'optimisation …` | — |
| 8 | Revision & final-exam preparation | `Module 8 - Révisions …` (two exports) | `EF 2025-2026 correction FR.pdf` |

**Rationale**: Confirmed by extracting each deck's "Plan du module" slide via
`python-pptx`. Non-lesson archive items (forums, syllabus URL redirects,
duplicate exports) are references only, per FR-014.

## Decision 3 — Module concept coverage (from deck plans)

- **M1**: order of operations, absolute value, powers, square roots, fractions,
  percentages & index numbers, proportionality rule.
- **M2**: algebraic transformations — factoring, expanding, notable identities,
  solving first-degree equations.
- **M3**: graphical representation, Cartesian plane, equation of a line, systems
  of first-degree equations (graphical + algebraic), first-degree inequalities,
  systems of inequalities, synthesis exercise (logistics/budget).
- **M4**: numerical sequences (definition, sum of terms, sense of variation,
  EXCEL), arithmetic sequences, geometric sequences.
- **M5**: simple interest, compound interest, combined approach, inverse
  problems, unit/period conversion, EXCEL, synthesis exercise.
- **M6**: single-variable function (domain, forbidden values, sign, variation,
  parity), usual functions (affine, degree-2 polynomial, square root,
  logarithm, exponential), second-degree equations, EXCEL.
- **M7**: average rate of change, instantaneous rate of change / intuitive
  derivative, application to affine and degree-2 polynomial functions,
  optimization (max/min), EXCEL, synthesis exercise.
- **M8**: revision across functions, systems of equations, and financial math,
  aligned to the final-exam correction.

**Rationale**: These lists become the per-module acceptance target for SC-003
(100% concept coverage). "EXCEL application" slides are represented as short
prose notes/examples (no spreadsheet embed required).

## Decision 4 — Mathematical notation

**Decision**: All math in LaTeX (`$...$` inline, `$$...$$` display). Convert
Module 1's Unicode/HTML notation (`aⁿ`, `<sub>`/`<sup>`, `×`, `÷`) to LaTeX.

**Rationale**: Clarification Q3 + constitution §V ("Math MUST use standard LaTeX
syntax"). Renders reliably; consistent across the site.

## Decision 5 — Exercises & solutions (static)

**Decision**: Exercises use static revealable solutions via
`::: {.callout-caution collapse="true"}` (constitution §V exercise semantics).
Module 1's `shinylive` quiz blocks are converted into static
question/collapsible-answer lists. No `{shinylive-python}` runtime blocks are
added.

**Rationale**: Clarification Q2. Reliable rendering, privacy-first, lighter
pages. Consistent single pattern across all eight modules.

## Decision 6 — Interactive-demo gaps (T-IV reconciliation)

**Decision**: For each priority concept that would ordinarily warrant a Shinylive
demo (e.g., quiz on order of operations, interest simulator, line/feasible-region
plotter, tangent-slope explorer), insert a `.callout-important` block labelled
`TODO:` describing the intended demo.

**Rationale**: T-IV explicitly allows marking un-built demos with a `TODO:`
`.callout-important`, keeping the gap trackable while honoring the static-only
clarification.

## Decision 7 — Callout semantics migration

**Decision**: Apply the constitution §V table consistently:

| Callout | Use |
|---|---|
| `.callout-note` | definitions, background |
| `.callout-tip` | key formulas / shortcuts |
| `.callout-warning` | caveats, common mistakes (e.g., $\lvert a+b\rvert \neq \lvert a\rvert+\lvert b\rvert$) |
| `.callout-important` | exam tips, critical rules, `TODO:` demo gaps |
| `.callout-caution` (collapse) | exercises & collapsible proofs |

Legacy `.callout-tip` "✅ Solution" blocks in Modules 2–3 are migrated to
`.callout-caution collapse="true"`.

**Rationale**: Constitution §V requires consistent callout meaning site-wide.

## Decision 8 — Required collapsible derivation per module (T-VI)

**Decision**: Each module gets at least one collapsible step-by-step derivation:
M1 percentage/successive-discount factor; M2 a notable identity
$(a+b)^2=a^2+2ab+b^2$; M3 intersection point of two lines by substitution; M4
sum of the first $n$ terms of arithmetic and geometric sequences; M5 the
compound-interest formula $C_n = C_0(1+i)^n$; M6 the quadratic
roots/discriminant; M7 the derivative of $f(x)=x^2$ from the average rate of
change; M8 one representative exam-style derivation.

**Rationale**: Satisfies T-VI without disrupting reading flow (collapsible).

## Decision 9 — Navigation & syllabus

**Decision**: Register the course in `_quarto.yml` with a
`mathematical-fundamentals` sidebar block: `index.qmd` first, then
`module-1 … module-8`, then `glossary.qmd`. Reconcile/trim the local
`_metadata.yml` sidebar so it does not conflict. Update the syllabus's
Recommended Literature to English with full bibliographic detail.

**Rationale**: Constitution §II (authoritative nav in `_quarto.yml`), §T-VIII
(syllabus + literature), and clarification Q4 (full navigability, `module-8`).

## Decision 10 — Bilingual parity (deferred)

**Decision**: Do not create `fr/` counterparts in this feature. Set `lang: en`
on all course files. Record the parity gap as a follow-up.

**Rationale**: No `fr/` tree or language switcher exists site-wide; user
requested English content. A bilingual rollout is a separate cross-cutting
effort (see plan Complexity Tracking).

## Open risks

- **Handout-only numeric details**: some exercise numbers live in the student
  PDFs, not the decks; extract from PDFs (`pdftotext`) when authoring to keep
  results faithful (SC-004).
- **Module 3 outline dumps**: the current draft contains repeated slide-outline
  bullets; these must be rewritten into coherent prose, not preserved verbatim.
