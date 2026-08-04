# Phase 1 — Data Model: Course Content Entities

This feature has no runtime data store. The "data model" describes the content
entities the course is composed of, their required fields, relationships, and
validation rules (mapped to functional requirements and success criteria).

## Entity: Course

Represents the whole offering; realized by `index.qmd`.

| Field | Description | Rule |
|---|---|---|
| title | "Mathematical Fundamentals and Data Analysis" | English (FR-002) |
| presentation | General description & objectives | English; matches source syllabus |
| competencies | Targeted competencies (2.3, 5.2) | English |
| schedule | Ordered list of 8 modules with dates | Links resolve (FR-011, SC-006) |
| assessment | Continuous control 50% + final exam 50% | Preserved from source |
| workload | Expected personal work (≈50 h) | English |
| literature | Recommended reading | Each entry: author, title, edition, publisher (T-VIII) |
| lang | Content language | `en` |

**Validation**: Must be first sidebar entry; must contain a Recommended
Literature section (T-VIII) — otherwise course is "incomplete/unpublished".

## Entity: Module

Eight instances (`module-1.qmd` … `module-8.qmd`). Each maps to one source deck.

| Field | Description | Rule |
|---|---|---|
| id | 1–8 | unique |
| title | Module title | English (FR-002) |
| date | Scheduled session date | preserved from syllabus |
| objectives | Learning objectives | `.callout-note`; English (FR-004) |
| introduction | Motivation in econ/management context | English (FR-004, FR-013) |
| concepts | Definitions & rules | cover all source-deck concepts (FR-005, SC-003) |
| worked_examples | ≥ multiple fully worked examples | step-by-step + stated result (FR-004, FR-004a) |
| derivation | ≥1 collapsible proof/derivation | `.callout-caution collapse="true"` (T-VI) |
| exercises | Exercise bank w/ revealable solutions | static; results agree w/ source (FR-012, SC-004) |
| demo_gaps | Priority concepts lacking a demo | `.callout-important` `TODO:` (T-IV) |
| nav_links | Cross-module code-links | resolve to existing pages (FR-011) |
| lang | `en` | required |

**State/lifecycle** (per module authoring):
`empty/front-matter-only → drafted → translated-to-EN → concept-complete →
render-clean`. A module is "done" only at `render-clean` with SC-003/SC-004 met.

**Current starting state**:

| Module | Starting state | Work required |
|---|---|---|
| 1 | drafted (FR, Unicode math, shinylive) | translate → LaTeX → static exercises → add derivation |
| 2 | drafted (mixed FR/EN, `.callout-tip` solutions) | translate → migrate callouts → complete equations section |
| 3 | drafted (outline dumps) | rewrite prose → add examples/derivation → translate |
| 4–7 | front-matter only | author in full from decks/handouts |
| 8 | absent | create new revision/exam-prep module |

## Entity: Exercise

A practice item inside a module.

| Field | Description | Rule |
|---|---|---|
| prompt | Question text | English; LaTeX math |
| context | Optional real-world framing | econ/finance/management (FR-013) |
| solution | Revealable correct answer/result | `.callout-caution collapse="true"`; matches source (SC-004) |

## Entity: Glossary Term

Rows in the new `glossary.qmd`.

| Field | Description | Rule |
|---|---|---|
| term_en | English term | required |
| term_fr | French equivalent | required (FR↔EN bridge, matches site pattern) |
| notation | Symbol/notation if any | LaTeX |
| definition | Plain-language definition | English; audience-appropriate (T-III) |

**Validation**: Every mathematical symbol/formula introduced in any module MUST
appear here (T-V). Linked from the sidebar.

## Entity: Source Material (reference only)

Authoritative inputs; never published as lessons (FR-014).

| Field | Description |
|---|---|
| kind | slide deck (PPTX) / handout (PDF) / final exam (PDF) / syllabus |
| module_ref | which module it feeds (see research.md Decision 2) |
| archive | `MS01-001-G_Fondamentaux` or `…-26` |

## Relationships

- Course **1—8** Module (ordered).
- Module **1—N** Exercise; Module **1—≥1** Derivation.
- Module **N—1** Source Material (primary deck) plus optional handout/exam.
- Course/Modules **N—1** Glossary (shared).

## Coverage matrix (acceptance target)

For each module, SC-003 requires every concept in research.md Decision 3 to
appear. SC-004 requires every worked/exercise result that also exists in the
source to match. These two per-module checks are the core "done" tests and feed
directly into task generation.
