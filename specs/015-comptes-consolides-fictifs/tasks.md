---

description: "Task list for the fictitious consolidated accounts (French GAAP) course red thread"
---

# Tasks: Fictitious Consolidated Accounts (French GAAP) — Course Red Thread

**Input**: Design documents from `/specs/015-comptes-consolides-fictifs/`

**Prerequisites**: plan.md (required), spec.md (user stories US1–US5), research.md (R1–R8), data-model.md, contracts/dataset-files-contract.md, quickstart.md

**Tests**: Not requested as TDD test tasks; each phase's independent test is the corresponding quickstart.md validation step (the spec's acceptance scenarios map 1:1 to quickstart steps).

**Organization**: Tasks are grouped by user story (US1–US5 from spec.md, in priority order) so each story is an independently testable increment.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: User story this task belongs to ([US1]…[US5]); Setup/Foundational/Polish phases have no story label
- Exact file paths are given in every task

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the directories and pin the tooling before any content work.

- [X] T001 Create directories `scripts/financial-analysis/`, `fr/teaching/financial-analysis/donnees/fichiers/`, and `teaching/financial-analysis/donnees/`
- [X] T002 [P] Create `requirements.txt` at repo root pinning `openpyxl==3.1.5` (already present in `.venv`; file does not exist yet) per AGENTS.md venv convention
- [X] T003 [P] Verify the fictitious SIREN for Groupe AUBÉPINE SA is a 9-digit number not assigned to a real company (web search of the SIREN registry); record the chosen value in `scripts/financial-analysis/dataset_params.py` (R4)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: The single-source dataset. Nothing publishable exists until this phase completes.

**⚠️ CRITICAL**: No user story work can begin until T010–T012 are done.

- [X] T010 Write `scripts/financial-analysis/dataset_params.py`: every figure of Groupe AUBÉPINE — mère AUBÉPINE SA + filiales IG (AUBÉPINE NORD SAS 75%, AUBÉPINE SUD SAS 80%, VERGER Export SARL 60%) + associé MEE (TERROIR PARTENAIRES SA 30%), postes bilan/CR/flux for N-2, N-1, N in k€, dates d'acquisition + prix des titres, opérations intragroupe (vente avec marge en stock, prêt, créance/dette, dividendes) — per data-model.md entities and R4
- [X] T011 Implement `scripts/financial-analysis/generate-dataset.py`: derive all consolidated statements from dataset_params.py by construction (bilan équilibré, résultat tie, flux tie — data-model.md validation rules); emit (a) `aubepine-consolide.xlsx` via openpyxl with sheets `Périmètre`, `Bilan`, `Compte de résultat`, `Annexe`, `Flux` (columns N-2/N-1/N, contract §1), (b) `aubepine-consolide.pdf`, (c) markdown table fragments for the `.qmd` pages, (d) corrigé figures; implement `--check` mode (re-read Excel, assert all invariants, exit 0/1, contract §3); deterministic output (normalized zip timestamps)
- [X] T012 Run `python scripts/financial-analysis/generate-dataset.py` then `--check`; both MUST exit 0 (quickstart steps 1–2, SC-001). Fix params until green.

**Checkpoint**: Foundation ready — generator is green, artifacts exist.

---

## Phase 3: User Story 1 — Student accesses the complete dataset (Priority: P1) 🎯 MVP

**Goal**: The fictitious group's full French-GAAP consolidated accounts (bilan, CR, annexe, flux; N-2..N) are published on the site and downloadable, clearly labelled fictitious.

**Independent Test**: quickstart steps 1, 2, 4, 5, 6 — generator green, both trees render exit 0, sidebar section present in EN+FR, Excel/PDF downloadable from `docs/`, disclaimer on every page.

- [X] T020 Create the 6 FR pages under `fr/teaching/financial-analysis/donnees/`: `index.qmd` (présentation, périmètre, disclaimer "Données fictives — usage pédagogique uniquement" en prose simple, note d'usage de l'IA visible, dérivation `.callout-caution` T-VI), `bilan-consolide.qmd`, `compte-de-resultat.qmd`, `annexe.qmd`, `flux-tresorerie.qmd`, `telechargements.qmd` — front matter with `title`, `abstract`, `date-modified` (not `date`); tables pasted from the generator's markdown fragments
- [X] T021 [P] Create the 6 EN stub pages under `teaching/financial-analysis/donnees/` (same file names): title + "Translation in progress" + link to the FR page; no `lang:` override (Principle VI)
- [X] T022 Register the new sidebar section "Fil rouge — Groupe AUBÉPINE" (FR) / "Red thread — AUBÉPINE Group" (EN) in `_quarto.yml` in BOTH `fr-financial-analysis` and `en-financial-analysis` blocks, appended after existing sections; `index.qmd` stays first (T-VIII)
- [X] T023 Copy generated `fichiers/aubepine-consolide.xlsx` and `aubepine-consolide.pdf` into `fr/teaching/financial-analysis/donnees/fichiers/` and link them with relative paths from `telechargements.qmd` (contract §1–2, R1)
- [X] T024 Render gate: `quarto render fr/teaching/financial-analysis --quiet` and `quarto render teaching/financial-analysis --quiet` both exit 0; verify `docs/fr/teaching/financial-analysis/donnees/fichiers/` contains the Excel and PDF and that sidebar links resolve (quickstart steps 4–5)

**Checkpoint**: US1 fully functional and testable independently — dataset is live and downloadable.

---

## Phase 4: User Story 2 — Instructor reuses the group across case studies (Priority: P1)

**Goal**: The same fictitious group is the red thread of the course: every case study that needs accounts links to it instead of inventing figures.

**Independent Test**: `grep -l "donnees/index.qmd"` over the edited files lists all of them (quickstart step 6); both trees still render exit 0.

- [ ] T030 [P] [US2] Add one plain-prose link to `../donnees/index.qmd` in `fr/teaching/financial-analysis/modules/02-archives-consolidees.qmd` (FR-008; no other edit, T-I)
- [ ] T031 [P] [US2] Add the same link in `fr/teaching/financial-analysis/modules/03-detective-diagnostic.qmd`
- [ ] T032 [P] [US2] Add the same link in the BdF reference pages `fr/teaching/financial-analysis/modules/performances.qmd`, `structure-fi.qmd`, `liquidite.qmd`, `banque-france.qmd`
- [ ] T033 [P] [US2] Add the same link in `fr/teaching/financial-analysis/exercices/examen-final.qmd` (and `examen-1h.qmd` if it uses accounts)
- [ ] T034 [US2] Add a one-line mention of the fil rouge in `fr/teaching/financial-analysis/index.qmd` and `planning.qmd`
- [ ] T035 [US2] Re-render both trees (exit 0) and run the grep check of quickstart step 6

**Checkpoint**: US1 + US2 both work independently; the dataset is referenced everywhere it is needed.

---

## Phase 5: User Story 3 — Student works from the dataset at the required depth (Priority: P2)

**Goal**: Published consolidated statements only (owner decision 2026-11-04): the annexe documents every intragroup operation, and all BdF ratio inputs are present for 3 years.

**Independent Test**: quickstart step 7 — compute all BdF ratios (performance, structure, liquidité) for N-2..N from the downloaded Excel alone, zero missing inputs (SC-003); render exit 0.

- [ ] T040 [US3] Complete `fr/teaching/financial-analysis/donnees/annexe.qmd` from generator output: principes comptables (CRC 99-02, IG/MEE), périmètre, écarts d'acquisition per filiale, opérations intragroupe with amounts (vente + marge en stock, prêt, créance/dette, dividendes), intérêts minoritaires bilan + résultat (FR-004)
- [ ] T041 [US3] Complete `flux-tresorerie.qmd` with the tableau des flux N-2..N (méthode indirecte)
- [ ] T042 [US3] Add the OJS ratio demo on `donnees/index.qmd` (student picks a ratio, it computes from the dataset; `{ojs}` block, `currentColor`, per AGENTS.md convention); if not built, mark a `.callout-important` with `TODO:` (T-IV)
- [ ] T043 [P] [US3] Ensure `fr/teaching/financial-analysis/glossaire.qmd` lists intégration globale, mise en équivalence, écart d'acquisition, intérêts minoritaires; add missing entries (T-V)
- [ ] T044 [US3] Run the ratio-coverage validation (quickstart step 7) and record the computed ratios in the corrigé params for later diff (SC-003)

**Checkpoint**: US3 independently verified — analysis depth works from the published dataset alone.

---

## Phase 6: User Story 4 — Teacher has a complete answer key (Priority: P2)

**Goal**: `enseignant/corrige-aubepine.qmd` reproduces every published figure; SC-004 holds.

**Independent Test**: quickstart step 8 — recompute from dataset_params.py and diff against published tables and corrigé; diff MUST be empty (SC-004).

- [ ] T050 [US4] Generate `fr/teaching/financial-analysis/enseignant/corrige-aubepine.qmd`: all figures, écarts d'acquisition, minoritaires, eliminated intragroup ops, consolidated statements, and the BdF ratios per year
- [ ] T051 [P] [US4] Create EN stub `teaching/financial-analysis/enseignant/corrige-aubepine.qmd` and register both corrigé pages in the "Instructor" sidebar sections of `_quarto.yml` (EN + FR)
- [ ] T052 [US4] Run quickstart step 8; fix params until the recomputed-vs-published diff is empty

**Checkpoint**: US4 verified — grading is mechanical and consistent.

---

## Phase 7: User Story 5 — Transparent per-student variants (Priority: P3)

**Goal**: Seeded per-student Excel variants deter AI copy-paste, with a visible notice; no hidden content anywhere (SC-005).

**Independent Test**: quickstart step 3 — same seed → identical hash, different seeds → different files, every variant passes `--check`; quickstart step 6 grep finds no hidden text.

- [ ] T060 [US5] Implement `--seed <id> --out <dir>` in `generate-dataset.py`: deterministic shifts of the documented postes only (CA VERGER, stock AUBÉPINE NORD, marge intragroupe, dividende NORD — R5), re-derive all statements, run `--check` on the variant before writing
- [ ] T061 [US5] Run quickstart step 3 (determinism + variant hashes + variant `--check` all green)
- [ ] T062 [P] [US5] Add the visible AI-use policy in plain prose to `fr/teaching/financial-analysis/evaluation.qmd` and the variant notice to `donnees/telechargements.qmd` (R8; no callout — roles reserved, Principle V)
- [ ] T063 [US5] Run the SC-005 audit: `grep -rE "​|﻿|<!--" docs/fr/teaching/financial-analysis/donnees/` after a full render MUST be clean, plus manual inspection of each new page (quickstart step 6)

**Checkpoint**: US5 verified — variants work, policy visible, zero hidden content.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Full-site validation before merge.

- [ ] T070 Run the complete quickstart.md end-to-end (steps 1–8) and record the output
- [ ] T071 Full render gate: `quarto render --quiet` exit 0 for the whole site; confirm `_freeze/` untouched (no Python blocks in `.qmd` pages, Principle III)
- [ ] T072 [P] EN/FR parity check: every `fr/teaching/financial-analysis/donnees/*.qmd` has a stub at `teaching/financial-analysis/donnees/` and vice versa (quickstart step 5)
- [ ] T073 [P] Confirm no styling was added outside `assets/custom.scss` (Principle V) — expected: no change at all
- [ ] T074 Commit `docs/` and sources together per the render gate; optional hook `/speckit-git-commit`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: no dependencies — start immediately
- **Foundational (Phase 2)**: depends on Phase 1 — BLOCKS all user stories (pages need the generated fragments)
- **User stories (Phases 3–7)**: depend on Phase 2; proceed in priority order US1 → US2 → US3 → US4 → US5, or in parallel if staffed (US2 touches only existing module files, US3 only `donnees/` + glossaire, US4 only `enseignant/`, US5 only the script + evaluation/telechargements pages — no file conflicts between stories except `donnees/index.qmd` shared by US1/US3: do T020 before T042)
- **Polish (Phase 8)**: depends on all chosen stories being complete

### User Story Dependencies

- **US1 (P1)**: after Phase 2 only — no dependency on other stories. **MVP = Phases 1–3.**
- **US2 (P1)**: after Phase 2 — edits only existing course pages; independent of US3–US5
- **US3 (P2)**: after US1's T020 (shares `donnees/` pages); adds depth, does not break US1/US2
- **US4 (P2)**: after Phase 2 — independent files (`enseignant/`)
- **US5 (P3)**: after Phase 2 — independent files (script + evaluation/telechargements)

### Within Each User Story

- Core artifact before pages that consume it (T010→T011→T012 in Phase 2)
- Generation before registration before render (T020→T022→T024 in US1)
- Story complete and validated at its checkpoint before moving to the next priority

### Parallel Opportunities

- Phase 1: T002 and T003 are [P]
- US2: T030–T033 are [P] (four different module/exercice files)
- US3: T043 is [P] relative to T040/T041 (glossaire is a different file)
- US4: T051 is [P] relative to T050
- US5: T062 is [P] relative to T060/T061
- Different stories can be worked in parallel by different people once Phase 2 is green, as long as `donnees/index.qmd` edits (T020 then T042) are sequenced

## Parallel Example: User Story 2

```text
Task: "Add fil-rouge link in fr/teaching/financial-analysis/modules/02-archives-consolidees.qmd"   (T030)
Task: "Add fil-rouge link in fr/teaching/financial-analysis/modules/03-detective-diagnostic.qmd"    (T031)
Task: "Add fil-rouge link in performances.qmd, structure-fi.qmd, liquidite.qmd, banque-france.qmd"  (T032)
Task: "Add fil-rouge link in exercices/examen-final.qmd"                                            (T033)
```

## Implementation Strategy

### MVP First (User Story 1 only)

1. Complete Phase 1 (Setup) and Phase 2 (Foundational: params + generator green)
2. Complete Phase 3 (US1: pages, sidebar, downloads, render gate)
3. **STOP and VALIDATE**: run quickstart steps 1, 2, 4, 5, 6 — dataset live and downloadable
4. Commit (`/speckit-git-commit`) — this is the mergeable MVP

### Incremental Delivery

1. Setup + Foundational → generator green
2. US1 → dataset published (MVP)
3. US2 → red thread wired into quests/exams
4. US3 → analysis depth + OJS demo + glossary
5. US4 → teacher key
6. US5 → seeded variants + visible policy + SC-005 audit
7. Phase 8 → full quickstart + full render + parity

Each story adds value without breaking previous ones; every checkpoint is independently testable via quickstart.md.

---

## Notes

- [P] tasks touch different files and have no dependency on incomplete tasks
- [USx] labels map tasks to spec.md user stories for traceability
- No TDD test tasks: tests were not requested in the spec; validation is via quickstart.md steps recorded at each checkpoint
- The generator (`generate-dataset.py` + `dataset_params.py`) is the single source of truth: never hand-edit generated tables, Excel, PDF or corrigé figures (R3)
- Forbidden: any hidden text or prompt-injection content in published files (FR-009, SC-005) — audited at T063
- Commit after each phase checkpoint, not only at the end
