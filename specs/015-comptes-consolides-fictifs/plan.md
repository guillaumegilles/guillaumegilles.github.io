# Implementation Plan: Fictitious Consolidated Accounts (French GAAP) — Course Red Thread

**Branch**: `015-comptes-consolides-fictifs` | **Date**: 2026-11-04 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/015-comptes-consolides-fictifs/spec.md`

## Summary

Create one **fictitious industrial group** (decision Q1: new group, STRATFIN
stays as the simplified Quest 2 workshop) with **complete French-GAAP
consolidated statements for 3 fiscal years N-2, N-1, N** — bilan (modèle
normal), compte de résultat (par nature), annexe, tableau des flux de
trésorerie (decision Q2) — published **as consolidated statements only**
(decision Q3: no per-entity individual accounts) — and reuse it as the red
thread ("fil rouge") across the case studies of `financial-analysis`.

Technical approach (see [research.md](research.md)):

1. **Single-source generator**: one deterministic Python script
   (`scripts/financial-analysis/generate-dataset.py`, openpyxl already in
   `.venv`) holds every figure of the group in one parameter file and emits
   the Excel workbook, the PDF and the markdown tables of the `.qmd` pages.
   Consistency (balanced bilans, tied results, coherent comparatives, FR-003)
   holds **by construction**, and a `--check` mode re-verifies it (SC-001).
2. **Publication**: new `donnees/` section under
   `fr/teaching/financial-analysis/` (one page per statement + group
   presentation), registered in the FR sidebar of `_quarto.yml`; EN stubs
   under `teaching/financial-analysis/donnees/`; downloadable Excel/PDF sit
   next to the pages so Quarto copies them to `docs/`.
3. **Teacher key**: `enseignant/corrige-<groupe>.qmd` + the generator's
   parameter file is the source of truth (FR-007, SC-004).
4. **Fil rouge**: Quest 2 (consolidation), Quest 3 (diagnostic), the BdF
   ratio pages and the exams link to the dataset (FR-008).
5. **Transparent anti-AI-copy measures** (FR-009, SC-005): visible AI-use
   note on the dataset and evaluation pages, seeded per-student variants via
   `generate-dataset.py --seed <id>`; **no hidden prompt injection anywhere**.

## Technical Context

**Language/Version**: Quarto (existing project version), Markdown with LaTeX
math; Python 3 in `.venv` (openpyxl 3.1.5 confirmed installed) for the
offline generator/checker scripts. French primary, English stubs.

**Primary Dependencies**: Quarto only for rendering; openpyxl for Excel
output. No new runtime dependency; nothing added to `requirements.txt`.

**Storage**: Files — `.qmd` sources + generated Excel/PDF resources under
`fr/teaching/financial-analysis/donnees/`, copied to `docs/` by Quarto.
No database.

**Testing**: `quarto render` MUST exit 0 for EN and FR trees; generator
`--check` mode (exit 0 = consistent, SC-001); variant determinism test
(same seed → identical file hash, FR-009); EN/FR parity check; manual
read-through of SC-003 (all BdF ratio inputs present).

**Target Platform**: Static site on GitHub Pages (`docs/`).

**Project Type**: Static documentation/course site (content project) plus
offline data-generation scripts (no server-side component).

**Performance Goals**: N/A for content. Dataset generation (all years, all
outputs) SHOULD complete in < 5 s locally.

**Constraints**: Constitution gates below; no cookies/tracking (IV); no
hidden text or prompt-injection content in any published file (FR-009,
SC-005); navigation only in `_quarto.yml` (II); styling only in
`assets/custom.scss` if needed (V); 80-column prose wrap; `_freeze/` is NOT
touched (no Python blocks inside `.qmd` pages — tables are static markdown
generated once by the script, so `freeze: auto` has nothing to cache).

**Scale/Scope**: 1 group (parent + 3 filiales en intégration globale + 1
participation en mise en équivalence), 3 exercices (N-2..N), ~6 new FR pages
+ 6 EN stubs + 1 teacher page, 2 scripts (generator/checker + variant mode
in the same script), 1 Excel + 1 PDF per year-set, edits to ~4 existing
pages to add fil-rouge links.

## Constitution Check

*GATE: checked before Phase 0 research; re-checked after Phase 1 design (both
checks below pass with the ACTIONs resolved inside this feature).*

| Gate | Status | Notes |
|---|---|---|
| I. Content-First | PASS | All new pages are `.qmd`; Excel/PDF are resources of those pages, never hand-written HTML in `docs/`. |
| II. Navigation registered | **ACTION** | New sidebar section "Fil rouge — <groupe>" added to BOTH `en-financial-analysis` and `fr-financial-analysis` blocks in `_quarto.yml`; EN entries point to stub pages. |
| III. Reproducible | PASS | No Python execution blocks in `.qmd` pages → no freeze entries created or deleted. Generator output is deterministic (seeded). |
| IV. Privacy-First | PASS | Static files only; no scripts, no tracking. Explicitly: no hidden prompt-injection text (SC-005 verified by inspection + grep in quickstart). |
| V. Styling contained | PASS | Tables and plain prose only; the "données fictives" disclaimer is plain prose (callout roles are reserved); no new CSS needed. |
| VI. Bilingual parity | **ACTION** | Every new FR page gets an EN stub with "Translation in progress" + link to FR, mirroring the existing convention. |
| T-I Content Fidelity | PASS | Purely additive: existing quest pages are edited only to add a link to the dataset; nothing removed. |
| T-II Pedagogical Structure | **ACTION** | New dataset pages ordered presentation → bilan → CR → annexe → flux → téléchargement; existing quests keep theory → example → exercise order. |
| T-III Audience language | PASS | Plain-language disclaimer and notes; every accounting term explained on first use. |
| T-IV Interactive demos | **ACTION** | One OJS demo (student picks a ratio, sees it computed from the dataset) on the dataset index page; if not built in time, a `.callout-important` `TODO:` marks the gap. |
| T-V Glossary | **ACTION** | Consolidation terms used on the new pages (intégration globale, écart d'acquisition, intérêts minoritaires, mise en équivalence) MUST be present in `glossaire.qmd`; add missing ones. |
| T-VI Proof | **ACTION** | The dataset index page includes one `.callout-caution` derivation: why the consolidated bilan stays balanced after eliminations (reuse the Q2 proof, adapted). |
| T-VII Visual intuition | PASS | Not forced; the flux statement table serves as the visual. |
| T-VIII Syllabus | PASS | `index.qmd` remains the first sidebar entry; the new section is appended after the existing sections. |

No unjustified violations: every ACTION is resolved within this feature, so
Complexity Tracking is empty. Re-check after Phase 1: all gates still PASS
with the same resolutions (see data-model.md and contracts/).

## Project Structure

### Documentation (this feature)

```text
specs/015-comptes-consolides-fictifs/
├── spec.md
├── plan.md                  # this file
├── research.md              # Phase 0 output
├── data-model.md            # Phase 1 output
├── quickstart.md            # Phase 1 output
├── contracts/
│   └── dataset-files-contract.md   # Phase 1 output
├── checklists/requirements.md
└── tasks.md                 # created by /speckit-tasks (NOT by /speckit-plan)
```

### Source Code (repository root)

```text
_quarto.yml                                # EDIT: new "Fil rouge" sections (EN + FR sidebars)

scripts/financial-analysis/
├── generate-dataset.py                    # NEW: single-source generator + --check + --seed
└── dataset_params.yml (or .py module)    # NEW: every figure of the fictitious group

fr/teaching/financial-analysis/
├── donnees/                               # NEW: the fictitious group dataset
│   ├── index.qmd                          # presentation, périmètre, disclaimer, AI-use note, OJS demo
│   ├── bilan-consolide.qmd                # bilan N-2..N (tables generated by the script)
│   ├── compte-de-resultat.qmd             # CR N-2..N
│   ├── annexe.qmd                         # principes, écarts d'acquisition, opérations intragroupe, minoritaires
│   ├── flux-tresorerie.qmd                # tableau des flux N-2..N
│   ├── telechargements.qmd                 # links to Excel/PDF + variant notice
│   └── fichiers/
│       ├── <groupe>-consolide-N.xlsx      # generated (openpyxl)
│       └── <groupe>-consolide-N.pdf       # generated
├── enseignant/
│   └── corrige-<groupe>.qmd               # NEW: teacher key (all figures + ratios)
└── modules/02-archives-consolidees.qmd, 03-detective-diagnostic.qmd,
    banque-france*.qmd, performances.qmd, structure-fi.qmd, liquidite.qmd,
    exercices/examen-*.qmd               # EDITED: add fil-rouge links only

teaching/financial-analysis/
└── donnees/                               # NEW: EN stubs mirroring fr/.../donnees/
    └── *.qmd                              # stub: "Translation in progress" + link to FR
```

**Structure Decision**: content lives in the existing course tree
(`fr/teaching/financial-analysis/donnees/`) because the dataset is course
material, not a site-wide asset; the generator lives in `scripts/` next to
the existing post-render script, not in the course tree, so it never ships
to `docs/`.

## Complexity Tracking

Empty — no constitution gate requires an unjustified violation; all ACTION
items above are resolved inside this feature.
