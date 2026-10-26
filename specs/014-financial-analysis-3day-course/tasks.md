# Tasks: Financial Analysis — 3-Day Intensive Course (18 h)

**Input**: Design documents from `/specs/014-financial-analysis-3day-course/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No test suite is requested. Validation is the scripted checks and
render gate in `quickstart.md` (tasks T047 and T048).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: can run in parallel (different files, no dependency on an unfinished task)
- **[Story]**: user story from spec.md (US1–US5)

## Path Conventions

- `FR/` = `fr/teaching/financial-analysis/` (canonical French course)
- `EN/` = `teaching/financial-analysis/` (English mirror)
- Block durations (minutes) are fixed in research.md R2; do not re-derive them.
- Prose wraps at 80 columns. No `style=` or `<style>`. Callouts only for
  definitions (`note`), formulas (`tip`), proofs (`caution`), one
  common-mistakes block (`warning`), `TODO:` (`important`).

---

## Phase 1: Setup

- [x] T001 Confirm with the owner that French content moves back to `FR/` (research R1). Record the answer at the top of research.md. If declined, stop and re-plan paths.
- [x] T002 Record the pre-change state in `specs/014-financial-analysis-3day-course/baseline.md`: durations of the 9 quests (1h30, 2h, 2h, 2h, 2h, 2h30, 2h, 2h, 3h), XP values (100, 150, 200, 150, 150, 200, 150, 150, 250) and the list of files under `EN/` (including binaries).
- [x] T003 [P] Write `specs/014-financial-analysis-3day-course/scripts/check-timetable.sh` that sums the "Duration (min)" column per day in a `planning.qmd` and fails unless each day = 360 and the total = 1080 (contract section 2).
- [x] T004 [P] Write `specs/014-financial-analysis-3day-course/scripts/check-parity.sh` that fails when a `.qmd` under `FR/` has no mirrored path under `EN/`, or an `EN/` page other than `index.qmd` and `planning.qmd` lacks "Translation in progress".
- [x] T005 [P] Write `specs/014-financial-analysis-3day-course/scripts/check-conventions.sh` implementing quickstart section 5 (no `style=`, `.callout-important` titles start with `TODO:`, every `#exr-` followed by a folded `<details class="answer">`, one `.callout-caution` per quest).

---

## Phase 2: Foundational (blocks all user stories)

**Purpose**: repair publishing state so every later page lands in the right place.

- [x] T006 Relocate the French course with `git mv` from `EN/` to `FR/` (all `.qmd`, `modules/`, `exercices/`, `assets/`, `image.jpg`, source PDFs/DOCX/PPTX/MP4/PNG). Do not touch files already deleted in the working tree under `FR/` beyond reconciling them with the move. Keep existing names (FR-019).
- [x] T007 Delete the generated orphan `EN/exercices/examen-1h.html` (Principle I). Leave empty `new/` and `old/` out of the move.
- [x] T008 Create the English root course folder `EN/` with `modules/` and `exercices/` subfolders and confirm `teaching/_metadata.yml` (`lang: en`) and `fr/teaching/_metadata.yml` (`lang: fr`) apply; remove any `lang:` repeated in moved files.
- [x] T009 Replace the broken `inseec-finane` sidebar block in `_quarto.yml` with two blocks, `en-financial-analysis` and `fr-financial-analysis`, ordered per contract section 4 (index, planning, evaluation, Day 1/2/3 groups, reference group, glossaire, exams, instructor group). List only pages that exist after T006; the new pages are added as they are created.
- [x] T010 Verify `quarto render fr/teaching/financial-analysis --quiet` exits 0 after the move and old URLs under `modules/` and `exercices/` still resolve.

**Checkpoint**: French pages render under `/fr/…`; sidebars point to real files.

---

## Phase 3: User Story 1 — Instructor delivers from a minute-by-minute plan (P1) 🎯 MVP

**Goal**: three timetables summing to exactly 6 h per day.
**Independent test**: `check-timetable.sh` passes on `FR/planning.qmd`; a colleague reads Day 1 and states what to teach and when.

- [x] T011 [US1] Create `FR/planning.qmd` with one table per day using exactly the columns "Block | Start (min) | Duration (min) | Goal | Sources | Cut first" and the block ids, starts and durations of research R2 (Day 1: D1-B1 15, D1-B2 110, D1-B3 100, D1-B4 135; Day 2: D2-B1 120, D2-B2 105, D2-B3 135; Day 3: D3-B1 100, D3-B2 110, D3-B3 140, D3-B4 10). Each row names its source pages (US1 scenario 3).
- [x] T012 [US1] In `FR/planning.qmd` add, under each table, a "Pauses" list (two 15 min breaks and a 60 min lunch, not counted) and a header sentence stating 360 min of teaching per day and 1080 min total.
- [x] T013 [US1] In `FR/planning.qmd` add per block the order theory → worked example → exercise (T-II), with the live-theory minutes of research R4 (25, 25, 25, 25, 20, 25, 20, 25, 30).
- [x] T014 [US1] Run `check-timetable.sh FR/planning.qmd`; fix until 360/360/360/1080.
- [x] T015 [P] [US1] Create `FR/enseignant/jour-1.qmd` (instructor guide for Day 1): pacing per block, answer key pointers, expected pitfalls, "what to cut first" per block. Fold the content of `FR/modules/01-temple-bilans-enseignant.qmd` into it (keep every item; T-I) and leave a one-line redirect page at the old path so the URL keeps working.
- [x] T016 [P] [US1] Create `FR/enseignant/jour-2.qmd` with the same structure for Day 2 (D2-B1…D2-B3).
- [x] T017 [P] [US1] Create `FR/enseignant/jour-3.qmd` with the same structure for Day 3 (D3-B1…D3-B4), including the fallback list of public annual reports (research R5).
- [x] T018 [US1] Add `planning.qmd` and the three instructor pages to the `fr-financial-analysis` sidebar in `_quarto.yml`; render and check each is reachable.

**Checkpoint**: MVP — the course has a valid 18 h timetable and instructor guides.

---

## Phase 4: User Story 2 — Student follows a coherent 3-day journey (P1)

**Goal**: a home page that tells the whole story; no concept used before it is taught.
**Independent test**: 10-question home-page check ≥ 90 %; formulas page covers all three days.

- [x] T019 [US2] Rewrite `FR/index.qmd` (keep the title, intro, RNCP list and the 6-step table; fix the Quête-to-day mapping): per day show narrative goal, blocks with durations (link to `planning.qmd`), prerequisites, preparatory work with expected effort ≤ 45 min per evening, and end-of-day deliverable (FR-008). Convert the `.callout-important` "Travail préparatoire" boxes to plain headings and lists (R7).
- [x] T020 [US2] In `FR/index.qmd` replace the "Plan des séances" table by the corrected timetable summary, add the statement that the 1 h and 3 h 30 exams are outside the 18 h, and update the "Correspondance Compétences RNCP — Quêtes" table to the final blocks (FR-013).
- [x] T021 [US2] In `FR/index.qmd` fill the Recommended Literature table with editions. Where an edition cannot be verified, write "édition à vérifier" and list it in `baseline.md`; do not invent values (T-VIII).
- [x] T022 [P] [US2] Edit `FR/modules/formules.qmd` into the single formula page (FR-010): every formula used on the three days with a plain-language explanation; formulas in `.callout-tip`. Add the leverage formula, DuPont, RNR ≈ ¾ × RCAI, FPNR, FRNG/BFR, FTA/CA, FTD, EV/EBITDA, WACC, carbon intensity.
- [x] T023 [P] [US2] Create `FR/glossaire.qmd`: every acronym and symbol (ROCE, ROE, RNR, RCAI, FPNR, FRNG, BFR, FTA, FTD, EV, EBITDA, WACC, DPEF, CSRD, FIBEN, IFRS, PCG…) with a plain-language definition. Link it in the sidebar (T-V).
- [x] T024 [P] [US2] Edit reference pages `FR/modules/banque-france.qmd`, `performances.qmd`, `structure-fi.qmd`, `liquidite.qmd`, `banque-france-cotation.qmd`: add at the top a "Pré-lecture" line stating which quest uses it and the reading time (R4); convert any non-conforming callouts.
- [x] T025 [US2] Add a 1-page "Les trois états financiers" primer as pre-reading for Q1 in `FR/modules/etats-financiers.qmd` (short, plain language) and register it in the sidebar reference group.
- [x] T026 [US2] Concept-order pass: read Day 1, 2, 3 in order and list in `baseline.md` every concept used before it is introduced; fix each by moving a definition or adding a pre-reading link (SC-005).

---

## Phase 5: User Story 3 — Content fits the time without losing the core (P2)

**Goal**: each quest fits its block; nothing core is lost; every change is logged.
**Independent test**: each of the nine quests has theory, worked example, exercise, one derivation, demo or TODO, and a change-log row.

Quest edits touch different files and can run in parallel. For each, use
the block minutes in research R2 and R9 (derivation and demo) and the
cut list in R2. Apply the quest-page order in contract section 3.

- [x] T027 [P] [US3] Edit `FR/modules/01-temple-bilans.qmd` to 110 min (theory 25): update duration text (currently 1h30), convert prerequisite callout, make exercises `#exr-` blocks with folded answers, add derivation (balance sheet identity and cash link) in `.callout-caution`, add `TODO:` demo callout, add cut-first note.
- [x] T028 [P] [US3] Edit `FR/modules/02-archives-consolidees.qmd` to 100 min (theory 25): trim one intragroup elimination case into the optional extension; derivation of elimination entries; `TODO:` demo; exercises and folded answers.
- [x] T029 [P] [US3] Edit `FR/modules/03-detective-diagnostic.qmd` to 135 min including the Day 1 boss (theory 25): derivation RNR ≈ ¾ × RCAI; exercises and folded answers; `TODO:` demo; cut-first note.
- [x] T030 [P] [US3] Edit `FR/modules/04-arenes-rentabilite.qmd` to 120 min (theory 25): derivation ROE = ROCE + (ROCE − i) × D/E in `.callout-caution`; formulas as `.callout-tip`; add an OJS leverage-effect slider demo (pure JavaScript, no Python); exercises and folded answers.
- [x] T031 [P] [US3] Edit `FR/modules/05-cartographes-modele-eco.qmd` to 105 min (theory 20): derivation linking canvas margin to EBIT margin; `TODO:` demo; convert callouts; exercises and folded answers.
- [x] T032 [P] [US3] Edit `FR/modules/06-conseil-sages.qmd` to 135 min including the Day 2 boss (theory 25): merge Step 5 into the boss presentation; derivation EV/EBITDA to equity bridge; `TODO:` demo; exercises and folded answers; move the "pièges" section to the single `.callout-warning`.
- [x] T033 [P] [US3] Edit `FR/modules/07-veilleurs-marche.qmd` to 100 min (theory 20): shared fiche template, 4-minute pitches; derivation of IFRS 16 effect on EBITDA and debt; `TODO:` demo.
- [x] T034 [P] [US3] Edit `FR/modules/08-architectes-strategie.qmd` to 110 min (theory 25): derivation FCF = EBITDA − tax − capex − ΔBFR; add an OJS three-year projection demo; exercises and folded answers.
- [x] T035 [P] [US3] Edit `FR/modules/09-gardiens-extra-financier.qmd` to 140 min including the final boss (theory 30): move Step 4 (WACC adjustment) and the 1.5-page report to a clearly labelled take-home extension; derivation of the ESG discount-rate adjustment; replace the "3h" header; `TODO:` demo; folded answers.
- [x] T036 [US3] In each of `FR/enseignant/jour-1.qmd`, `jour-2.qmd`, `jour-3.qmd` add the "Journal des modifications" table (block, previous minutes, new minutes, what changed, destination, reason) for the quests of that day, using `baseline.md` values (FR-007).
- [x] T037 [US3] Verify no theory, worked example or exercise was removed: compare each quest against `git diff HEAD` and list any removal in the change log with its destination (SC-006).

---

## Phase 6: User Story 4 — Assessment fits inside the 18 hours (P2)

**Goal**: one assessment page consistent with the timetable.
**Independent test**: quickstart section 6 (XP 900, exam 12/20 → 12.0, Stratège Financier).

- [ ] T038 [US4] Create `FR/evaluation.qmd`: XP per activity (total 1 500), levels (< 400, 400–800, 800–1 200, > 1 200 with boundary values assigned to the lower level), boss slots and criteria, grade rule `0.4 × (XP / 1500 × 20) + 0.6 × exam` on /20, exam conversion (/50 or /100 to /20), worked example. Remove the XP/level duplicates from `FR/index.qmd` and link here.
- [ ] T039 [P] [US4] Edit `FR/exercices/examen-1h.qmd` and `examen-final.qmd`: add a visible line "Hors des 18 h du cours", convert callouts, keep every question (T-I).
- [ ] T040 [US4] Decide the commented-out badge tables in `FR/index.qmd`: restore under `evaluation.qmd` as plain tables or delete, and record the decision in `baseline.md`.
- [ ] T041 [US4] Verify the sum of quest XP in `FR/modules/*.qmd` equals 1 500 and matches `evaluation.qmd`.

---

## Phase 7: User Story 5 — French and English (P3)

**Goal**: mirrored paths; full EN home page and timetable; stubs elsewhere.
**Independent test**: `check-parity.sh` passes; EN and FR timetable values identical.

- [ ] T042 [P] [US5] Translate `FR/index.qmd` to `EN/index.qmd` in full (same blocks, durations, RNCP table, literature).
- [ ] T043 [P] [US5] Translate `FR/planning.qmd` to `EN/planning.qmd` in full; Block, Start and Duration columns identical to FR.
- [ ] T044 [US5] Generate English stubs (title, "Translation in progress", link to the French page) for every other `FR/` page listed in contract section 1: `evaluation`, `glossaire`, `modules/*` (quests, reference pages, `etats-financiers`, `formules`), `exercices/*`, `enseignant/jour-{1,2,3}`, `annexes/inventaire-sources`.
- [ ] T045 [US5] Add the English sidebar `en-financial-analysis` entries for all pages; check the navbar language switcher reaches the mirrored pages.

---

## Phase 8: Polish & Cross-Cutting

- [ ] T046 [P] Create `FR/annexes/inventaire-sources.qmd`: every non-`.qmd` file in the course folder classified `used`, `optional` or `archived` with used-in block ids (FR-014); include duplicate exam formats and the empty `new/` and `old/`. Register in sidebar (FR and EN stub).
- [ ] T047 Run all scripts (`check-timetable.sh` on both planning pages, `check-parity.sh`, `check-conventions.sh`); fix every failure.
- [ ] T048 Run `quarto render` for the whole site; it must exit 0 for FR and EN and the post-render hook must run. Commit `docs/` with the sources (constitution render gate). No freeze entries should change.
- [ ] T049 Human validation: instructor pilot for Day 1 (< 2 h preparation, SC-003) and the 10-question student check (SC-004); log results in `baseline.md`.
- [ ] T050 Update `AGENTS.md` architecture notes only if the folder layout changed from what it describes.

---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → everything else. T001 gates T006.
- **US1** (T011–T018) needs Phase 2 only. It is the MVP.
- **US2** needs Phase 2; T019–T020 reuse the timetable from US1 (after T014).
- **US3** needs T011 (block minutes) and benefits from T022/T023 (formulas, glossary); T036 needs T015–T017; T037 is last.
- **US4** needs T014 and the quest XP from US3 (T041 after T035).
- **US5** needs final FR pages: T042 after T020, T043 after T014, T044 after all FR pages exist.
- Polish after all stories.

```text
Setup → Foundational → US1 ──┬─→ US2 ──┐
                             ├─→ US3 ──┼─→ US4 ─→ US5 → Polish
                             └─────────┘
```

## Parallel Examples

- Setup scripts: T003, T004, T005 together.
- Instructor guides: T015, T016, T017 together.
- Quest edits: T027–T035 are separate files, run all nine in parallel.
- US2 reference work: T022, T023, T024 together.
- Translation: T042 and T043 together.

## Implementation Strategy

1. **MVP**: Phases 1–3 (T001–T018). Result: a valid 18 h timetable and instructor guides, rendered under `/fr/`.
2. Add US2 (home page, formulas, glossary), then US3 (quest rebalancing), then US4 (evaluation).
3. US5 (English) last, because it mirrors final French pages.
4. Render and commit after each phase; the render gate (T048) applies before any commit that touches `.qmd` or `_quarto.yml`.
