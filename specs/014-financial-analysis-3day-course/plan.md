# Implementation Plan: Financial Analysis — 3-Day Intensive Course (18 h)

**Branch**: `014-financial-analysis-3day-course` | **Date**: 2026-10-26 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/014-financial-analysis-3day-course/spec.md`

## Summary

Turn the existing `financial-analysis` materials into one deliverable
18-hour course (3 days × 360 teaching minutes) by **editing the existing
pages in place** (clarification Q1). The work is editorial, not code:

1. Rebalance the nine quests to fixed block durations that sum to exactly
   360 min per day (the current durations total 19 h and are uneven; see
   [research.md](research.md) R2).
2. Open every quest with a 20–30 min live theory segment fed by the
   existing reference pages as pre-reading (Q2).
3. Add the missing course-level pages: full timetable, assessment scheme
   (40 % XP / 60 % exam, Q4), glossary, instructor guides per day, and a
   source inventory. Exams stay outside the 18 h (Q3).
4. Repair the publishing state: the French content currently sits at the
   English root, language is wrongly inherited, and the sidebar points to a
   page that does not exist (R1, R6).
5. Bring all pages in line with the constitution (callout roles, exercise
   blocks, folded answers, derivations, glossary).
6. Provide EN counterparts: full translation of home page + timetable,
   labelled stubs for everything else (Q5).

## Technical Context

**Language/Version**: Quarto (existing project version), Markdown with
LaTeX math; French primary, English secondary.

**Primary Dependencies**: Quarto only. Optional Observable JS (`{ojs}`)
blocks for demos; no Python needed, so no Shinylive and no freeze impact.

**Storage**: Files — `.qmd` sources, rendered to `docs/` (committed).

**Testing**: `quarto render` must exit 0 for EN and FR; scripted
timetable-sum check and page-parity check (see
[quickstart.md](quickstart.md)); manual read-through (SC-003/004/005).

**Target Platform**: Static site on GitHub Pages.

**Project Type**: Static documentation/course site (content project).

**Performance Goals**: N/A (content). Each page must render without
errors; no page-weight target beyond existing norms.

**Constraints**: 80-column prose wrap; styling only in `assets/dark.scss`;
no tracking; navigation only in `_quarto.yml`; no content deleted without
a recorded note (FR-007); existing URLs keep working (FR-019).

**Scale/Scope**: ~9 quest pages + 6 reference pages + 2 exams edited;
~9 new FR pages (planning, evaluation, glossaire, 3 instructor days,
inventory, plus rewritten index); ~20 EN pages (2 full, rest stubs).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|---|---|---|
| I. Content-First | PASS | All pages are `.qmd`; the stray `teaching/financial-analysis/exercices/examen-1h.html` is a generated orphan and is removed (R6). |
| II. Navigation registered | **ACTION** | `_quarto.yml` has no valid financial-analysis sidebar (`teaching/inseec-finance/index.qmd` does not exist, id typo `inseec-finane`). Fixed in this feature (R6). |
| III. Reproducible | PASS | No computational blocks → no freeze entries created or deleted. |
| IV. Privacy-First | PASS | Only static content; OJS demos run client-side without tracking. External links are plain hyperlinks. |
| V. Styling contained | **ACTION** | Existing quests use `.callout-note` for "Prérequis" and `.callout-important` for "Travail préparatoire"/boss notes, which violates the callout roles. Converted to plain markup (R7). Any new style goes in `assets/dark.scss`. |
| VI. Bilingual parity | **ACTION** | French content is at the EN root and inherits `lang: en`. Relocated to `fr/` (R1); EN root gets full/stub pages (Q5). |
| T-I Content Fidelity | PASS (tracked) | Cuts recorded in the change log per FR-007 (R2, R8). |
| T-II Pedagogical Structure | **ACTION** | Quests must follow theory → worked example → exercise with folded answers; live theory segment added (Q2). |
| T-III Audience language | PASS | Plain-language explanation required next to every formula in `formules.qmd`. |
| T-IV Interactive demos | **ACTION** | Demos: leverage effect (Q4) and 3-year projection (Q8) in OJS; other gaps marked `TODO:` callouts (R9). |
| T-V Glossary | **ACTION** | New `glossaire.qmd` linked from the sidebar (R10). |
| T-VI Proof | **ACTION** | One derivation (`.callout-caution`) per quest/session (R9). |
| T-VII Visual intuition | PASS | Applied where natural (leverage slope, DuPont tree, cash waterfall); not forced elsewhere. |
| T-VIII Syllabus | **ACTION** | `index.qmd` first in sidebar; Recommended Literature table exists but editions are "N/A" and must be filled. |

No unjustified violations: every ACTION is resolved within this feature,
so Complexity Tracking is empty. The gate is re-checked after Phase 1
below.

## Project Structure

### Documentation (this feature)

```text
specs/014-financial-analysis-3day-course/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── course-pages-contract.md
├── checklists/requirements.md
└── tasks.md              # created by /speckit-tasks
```

### Source Code (repository root)

```text
_quarto.yml                                  # EN + FR sidebars (fixed)
assets/dark.scss                             # only if a new style is needed

fr/teaching/financial-analysis/              # canonical French course
├── index.qmd                                # rewritten: home/syllabus
├── planning.qmd                             # NEW: full timetable (FR-018)
├── evaluation.qmd                           # NEW: XP, levels, grade (FR-011)
├── glossaire.qmd                            # NEW (T-V)
├── enseignant/
│   ├── jour-1.qmd  jour-2.qmd  jour-3.qmd   # NEW: instructor guides (FR-009)
│   └── (01-temple-bilans-enseignant.qmd folded into jour-1)
├── annexes/inventaire-sources.qmd           # NEW (FR-014)
├── modules/
│   ├── 01…09-*.qmd                          # EDITED: rebalanced quests
│   ├── banque-france*.qmd performances.qmd
│   ├── structure-fi.qmd liquidite.qmd       # EDITED: pre-reading pages
│   └── formules.qmd                         # EDITED: single formula page
├── exercices/examen-1h.qmd examen-final.qmd # kept; marked outside 18 h
└── (source PDFs/DOCX/PPTX: inventory only)

teaching/financial-analysis/                 # English counterpart
├── index.qmd  planning.qmd                  # full translation
└── …every other page as a labelled stub
```

**Structure Decision**: French is the canonical teaching language, so the
course lives under `fr/teaching/financial-analysis/` (as it was in `HEAD`
before the working copy moved it), with the English mirror at
`teaching/financial-analysis/`. This follows the folder-per-language rule
and the directory-level `lang:` in `_metadata.yml`. See research R1.

## Complexity Tracking

*No constitution violations remain to justify.*

## Post-Design Constitution Re-check

After Phase 1 (data model, contract, quickstart): all ACTION gates have an
owning requirement and a validation step in `quickstart.md`. No new
violations introduced. PASS.
