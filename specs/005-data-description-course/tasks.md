# Tasks: Data Description Course (MS03-001-G)

**Input**: Design documents from `/specs/005-data-description-course/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`,
`contracts/`, `quickstart.md`, `wandering-fork-dataset.csv` (all present)

**Tests**: Not requested in the spec — this is a static content feature.
Verification is done via `quickstart.md` render/manual checks, folded
into User Story 3 and the Polish phase below.

**Organization**: Tasks are grouped by user story (US1/US2/US3 from
`spec.md`) to enable independent authoring and verification.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1/US2/US3)
- Exact file paths are included in every description

## Path Conventions

Single Quarto content course, flat under `teaching/data-description/`
(no per-block subfolders), per `plan.md`'s Structure Decision. All
`.qmd` files use front matter `lang: en` and `draft: true` until Polish
task T034.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare the course directory, tooling, and reference data
before any lesson content is authored.

- [X] T001 [P] Create `teaching/data-description/_metadata.yml` with
  `lang: en` and a comment noting navigation is registered
  authoritatively in the root `_quarto.yml` (mirror the wording in
  `teaching/mathematical-fundamentals/_metadata.yml`)
- [X] T002 [P] Copy `teaching/mathematical-fundamentals/_extensions/quarto-ext/shinylive`
  into `teaching/data-description/_extensions/quarto-ext/shinylive`
  (per `research.md` §5 / `plan.md` Project Structure)
- [X] T003 [P] Install `python-pptx` and `python-docx` into the project
  `.venv` (`pip install python-pptx python-docx`); do **not** commit
  `.venv` (constitution: "Python env MUST NOT be committed")
- [X] T004 Run the one-time extraction pass (`research.md` §1) over the
  three `teaching/data-description/ressources/` Moodle archives using
  `python-pptx`/`python-docx`/`openpyxl`, skipping non-lesson artifacts
  per `research.md` §7 (`Forum_*`, `*.html`, `URL_*`, `shared/`,
  `overviewfiles/`); write per-session scratch notes to `/tmp/` (not
  committed) for use while authoring T010–T021
- [X] T005 [P] Re-run the "Wandering Fork" dataset generation script and
  diff its output against the committed
  `specs/005-data-description-course/wandering-fork-dataset.csv` to
  confirm it still reproduces the exact statistics verified in
  `data-model.md` (mean 628.34, std dev 137.09, $Q_1$=506.60,
  $Q_3$=729.99, $r$=0.621) before any session cites them

**Checkpoint**: Course skeleton tooling ready; source content readable;
canonical dataset re-verified.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared files every session depends on (syllabus/glossary
skeletons, warm-up data, navigation) MUST exist before Phase 3 begins.

**⚠️ CRITICAL**: No session content may be authored until this phase is
complete.

- [X] T006 Create `teaching/data-description/index.qmd` skeleton (front
  matter only — `title: "Data Description"`, `subtitle: "MS03-001-G |
  Business School"`, `lang: en`, `draft: true` — plus empty section
  headers) per `contracts/syllabus-page.md`
- [X] T007 [P] Create `teaching/data-description/glossary.qmd` skeleton
  (front matter — `title: "Glossary"`, `subtitle: "Data Description"`,
  `lang: en`, `draft: true` — plus an empty table with columns
  Notation | Name | Plain-language definition | Pronunciation (Greek
  only) | Introduced in) per `contracts/glossary-page.md`
- [X] T008 [P] Author the Sessions 1–2 warm-up dataset — a small,
  originally-authored 6-item product-price list (name, unit price,
  quantity) unrelated to "The Wandering Fork" — and append it as a
  "Warm-up dataset (Sessions 1–2)" section in
  `specs/005-data-description-course/data-model.md`, per FR-006's
  allowance for a simpler pre-case-study dataset
- [X] T009 Add the `data-description` sidebar block to `_quarto.yml`,
  grouped into Part I (Sessions 1–2), Part II (Sessions 3–9), Part III
  (Sessions 10–12), listing `index.qmd`, `glossary.qmd`, and all 12
  `session-NN.qmd` files (per `plan.md` Project Structure and
  constitution Principle II) — depends on T006/T007 existing so no nav
  entry 404s even while draft

**Checkpoint**: Foundation ready — all 12 session-authoring tasks in
Phase 3 can now start (in parallel, if staffed).

---

## Phase 3: User Story 1 - Learner works through one complete session (Priority: P1) 🎯 MVP

**Goal**: Every session page (1–12) is a complete, self-contained lesson
(theory → worked example → Excel reference → proof → exercises with
solutions), per `contracts/session-page.md`.

**Independent Test**: Render any single session (e.g.,
`teaching/data-description/session-07.qmd`) and confirm it presents
objectives, theory, a worked example on the correct dataset, "Using
Excel" steps, a collapsible proof, and exercises with revealable
solutions — all in English, with correctly rendered math.

### Implementation for User Story 1

- [X] T010 [P] [US1] Author `teaching/data-description/session-01.qmd`
  — Excel Fundamentals I (spreadsheet handling, cell referencing, basic
  functions) using the warm-up dataset from T008, per
  `contracts/session-page.md`'s required section order
- [X] T011 [P] [US1] Author `teaching/data-description/session-02.qmd`
  — Excel Fundamentals II (sorting, data processing); close with a
  short framing paragraph introducing "The Wandering Fork" case study
  that Session 3 will open with (FR-006)
- [X] T012 [P] [US1] Author `teaching/data-description/session-03.qmd`
  — Univariate graphical representation I (qualitative data): use the
  verified weather frequency table from `data-model.md` (Sunny 13/43.3%,
  Cloudy 12/40.0%, Rainy 5/16.7%) for the frequency table + bar/pie
  chart worked example
- [X] T013 [P] [US1] Author `teaching/data-description/session-04.qmd`
  — Univariate graphical representation II (quantitative data): use the
  verified `daily_revenue_eur` class frequency table from
  `data-model.md` ([400,500[=6, [500,600[=6, [600,700[=8, [700,800[=7,
  [800,900[=3) for histogram/frequency-polygon/cumulative-frequency;
  include the required Shinylive histogram/frequency-distribution demo
  (FR-008a) seeded with this data
- [X] T014 [P] [US1] Author `teaching/data-description/session-05.qmd`
  — Position indicators: quartiles/percentiles/boxplot, quoting the
  verified exclusive-method values from `data-model.md`
  ($Q_1$=506.60, $Q_2$=643.63, $Q_3$=729.99, $IQR$=223.39, fences
  171.52/1065.07, zero outliers); include the required Shinylive
  boxplot-from-quartiles demo (FR-008b)
- [X] T015 [P] [US1] Author `teaching/data-description/session-06.qmd`
  — Central tendency: mean ($\bar{x}$=628.34), median ($Me$=643.63),
  and grouped mode ($Mo\approx666.67$ from modal class [600,700[) per
  `data-model.md`; add a `.callout-important TODO:` marking the
  mode/central-tendency concept as a future demo candidate beyond the
  4 required in FR-008
- [X] T016 [P] [US1] Author `teaching/data-description/session-07.qmd`
  — Dispersion: range (478.97), sample variance ($s^2$=18,793.33),
  sample std. dev. ($s$=137.09), CV (21.82%) per `data-model.md`;
  include the required Shinylive central-tendency-and-dispersion
  calculator demo (FR-008c)
- [X] T017 [P] [US1] Author `teaching/data-description/session-08.qmd`
  — Asymmetry/shape: skewness (+0.034, near-symmetric with very mild
  right skew) per `data-model.md`, explaining what a near-zero skew
  means; add a `.callout-important TODO:` marking skewness as a future
  demo candidate beyond the 4 required in FR-008
- [X] T018 [P] [US1] Author `teaching/data-description/session-09.qmd`
  — Univariate practical-work synthesis: an Excel walkthrough recapping
  Sessions 3–8's indicators, recomputed end-to-end on "The Wandering
  Fork" `daily_revenue_eur` column
- [X] T019 [P] [US1] Author `teaching/data-description/session-10.qmd`
  — Bivariate graphical representation: contingency table (`weather` ×
  `daily_revenue_eur` class) and scatter plot of `temperature_c` vs.
  `daily_revenue_eur` using the raw rows in
  `wandering-fork-dataset.csv`
- [X] T020 [P] [US1] Author `teaching/data-description/session-11.qmd`
  — Bivariate numerical summaries: covariance (252.81), correlation
  $r$=0.621, $r^2$=0.386, and the regression line
  $\widehat{\text{revenue}} = -22.01 + 28.71 \times \text{temperature\_c}$
  per `data-model.md`; include the required Shinylive
  scatter-plot-and-correlation demo (FR-008d)
- [X] T021 [US1] Author `teaching/data-description/session-12.qmd` —
  Bivariate practical-work synthesis recapping Sessions 10–11, plus an
  originally-authored mock-exam section (mixed MCQ + short-answer, on
  "The Wandering Fork" data, revealable solutions) mirroring the
  Midterm/Final Exam format (FR-018); author last, after T010–T020, so
  the mock exam can safely reference results already established in
  earlier sessions
- [X] T022 [US1] Consolidate every symbol/formula introduced in
  T010–T021 into `teaching/data-description/glossary.qmd` (notation,
  plain-language definition, pronunciation guide for Greek letters,
  introducing session) per `contracts/glossary-page.md` — depends on
  T010–T021; touches the shared glossary file, so not parallelizable

**Checkpoint**: All 12 sessions + glossary are complete and each is
independently testable per the Independent Test above.

---

## Phase 4: User Story 2 - Learner follows the whole course and the running case study (Priority: P2)

**Goal**: The syllabus, session outline, and cross-session "Wandering
Fork" narrative connect into one navigable course ending in exam-prep
guidance.

**Independent Test**: From `index.qmd`, follow every session link in
order; confirm "The Wandering Fork" case study escalates coherently from
Session 3 onward and Session 12 closes with exam preparation.

### Implementation for User Story 2

- [X] T023 [P] [US2] Fill in full content for
  `teaching/data-description/index.qmd` (course description, curriculum
  placement noting MS01/MS02 prerequisites and the MS04
  `teaching/decision-making-stat/` refresher link, learning objectives,
  the 3-part session outline table linking all 12 sessions, assessment
  scheme — Midterm 35%/45min + Final 65%/90min — personal work 20h, and
  the Recommended Literature section from the source syllabi) per
  `contracts/syllabus-page.md` — depends on T010–T021 for final session
  titles/topics
- [X] T024 [P] [US2] Review `session-03.qmd` through `session-12.qmd`
  (T012–T021) for narrative continuity — confirm each session's opening
  paragraph explicitly references the prior session's "Wandering Fork"
  finding before introducing its own mission — and fix phrasing where a
  session restarts the narrative instead of building on it
- [X] T025 [US2] Render the full course
  (`quarto render teaching/data-description/ --quiet`) and manually
  click through every link from `index.qmd` to confirm 0 broken links
  and correct title/topic alignment with the syllabus (SC-008, SC-009)

**Checkpoint**: The course is fully navigable end-to-end with a coherent
running case study.

---

## Phase 5: User Story 3 - Instructor verifies fidelity and constitution compliance (Priority: P3)

**Goal**: Confirm the finished course matches source concepts/structure
without reproducing proprietary figures, and satisfies every
constitution teaching-page requirement.

**Independent Test**: Pick any session, cross-check its formulas and
structure against the matching source material, confirm glossary
coverage, and confirm required proofs/demos are present.

### Implementation for User Story 3

- [X] T026 [P] [US3] Cross-check each of `session-01.qmd`–`session-12.qmd`
  against its mapped source folder (the table in `research.md` §2) to
  confirm every concept in that source session appears in the rendered
  page (SC-003) with no silently dropped topic from FR-004
- [X] T027 [P] [US3] Grep the rendered course
  (`teaching/data-description/*.qmd` and `docs/teaching/data-description/`)
  for the source's proprietary case name ("Food Truck") and any figures
  from `The Food Truck.xlsx`/`The Food Truck_EN.xlsx` to confirm zero
  leakage of proprietary content (SC-004)
- [X] T028 [P] [US3] Verify `glossary.qmd` (T022) lists 100% of the
  mathematical symbols/formulas actually used across `session-01.qmd`
  through `session-12.qmd`, with a pronunciation guide on every Greek
  letter (SC-007)
- [X] T029 [P] [US3] Verify every session file has at least one collapsible
  (`collapse="true"`) proof/derivation (T-VI) and at least one surfaced
  geometric/visual intuition passage (T-VII), per `contracts/session-page.md`
- [X] T030 [P] [US3] Run `quarto preview` and manually confirm all 4
  required Shinylive demos (T013, T014, T016, T020) load and respond to
  input in the browser; confirm the two `TODO:` gaps (T015, T017) are
  present and correctly labeled `.callout-important` (SC-006)

**Checkpoint**: Fidelity and constitution compliance are verified across
the whole course.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final regression checks and the draft→published flip.

- [X] T031 [P] Run `quarto render` for the full site and fix any broken
  links or math-rendering warnings surfaced outside
  `teaching/data-description/` (regression check, SC-005)
- [X] T032 Run the full manual verification checklist in `quickstart.md`
  §5 end-to-end and record results
- [X] T033 Remove `draft: true` from all 15 files
  (`index.qmd`, `glossary.qmd`, `session-01.qmd`–`session-12.qmd`)
  together, in a single change, only after T023–T032 all pass (FR-017;
  SC-001 must be met first — no empty/placeholder pages)
- [X] T034 Re-render the full site after the draft flip and commit
  `docs/` (and any new `_freeze/` entries, though none are expected per
  `plan.md`) together with the source changes, per the constitution's
  render gate

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Setup (T003 must finish before
  T004; T001/T002/T005 are independent) — BLOCKS Phase 3
- **User Story 1 (Phase 3)**: Depends on Foundational completion (T006–T009)
- **User Story 2 (Phase 4)**: Depends on User Story 1 completion (needs
  final session content for T023/T024)
- **User Story 3 (Phase 5)**: Depends on User Story 1 completion (needs
  finished sessions to verify); may run in parallel with Phase 4 since
  neither writes to the other's files
- **Polish (Phase 6)**: Depends on Phases 3, 4, and 5 all passing

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational — no dependency on
  US2/US3
- **User Story 2 (P2)**: Needs US1's session files to exist first
  (reads their titles/content); not independently authorable before US1
- **User Story 3 (P3)**: Needs US1's session files to exist first (it is
  a verification pass over them); can run in parallel with US2

### Within Phase 3

- T010–T020 are mutually independent (different files) and fully
  parallelizable
- T021 (Session 12) should come after T010–T020 (soft narrative
  dependency — the mock exam references established results)
- T022 (glossary consolidation) depends on T010–T021 and is not
  parallelizable (single shared file)

### Parallel Opportunities

- T001, T002, T003, T005 (Setup) can all run in parallel
- T007, T008 (Foundational) can run in parallel with each other (not
  with T006/T009, which touch shared routing files close in sequence)
- T010–T020 (11 of the 12 session files) can all run in parallel
- T026–T030 (User Story 3 verification tasks) can mostly run in
  parallel with each other and with Phase 4

---

## Parallel Example: User Story 1

```bash
# Launch all independent session-authoring tasks together:
Task: "Author teaching/data-description/session-01.qmd — Excel Fundamentals I"
Task: "Author teaching/data-description/session-03.qmd — Univariate graphical representation I"
Task: "Author teaching/data-description/session-05.qmd — Position indicators"
Task: "Author teaching/data-description/session-07.qmd — Dispersion"
Task: "Author teaching/data-description/session-10.qmd — Bivariate graphical representation"
# ...continue for the remaining independent session files (T010-T020)
# Session 12 (T021) and the glossary consolidation (T022) run after.
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL — blocks all session work)
3. Complete Phase 3: User Story 1 (all 12 sessions + glossary)
4. **STOP and VALIDATE**: Render and read through 2–3 sessions
   independently per the Independent Test
5. Course is now internally complete but still `draft: true`

### Incremental Delivery

1. Setup + Foundational → foundation ready
2. User Story 1 → 12 sessions + glossary complete → validate
   independently (still draft)
3. User Story 2 → syllabus + narrative continuity + link check → validate
4. User Story 3 → fidelity + constitution compliance verification →
   validate
5. Polish → full regression render → flip `draft: true` off → publish

### Parallel Team Strategy

With multiple authors:

1. Everyone completes Setup + Foundational together (fast, ~4 tasks)
2. Once Foundational is done, split the 12 sessions in Phase 3 across
   authors (T010–T020 are independent files); one author reserves
   Session 12 (T021) for last and the glossary consolidation (T022)
3. Two authors then split Phase 4 (syllabus/continuity) and Phase 5
   (fidelity/compliance verification) in parallel, since neither writes
   to the other's files
4. Converge on Phase 6 together for the final render and draft flip

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- All numeric values quoted in Phase 3 tasks come from the
  already-verified `data-model.md` — do not recompute or re-invent them
  (FR-006)
- Commit after each task or logical group
- Stop at any checkpoint (end of Phase 2, 3, 4, 5) to validate
  independently before continuing
- Avoid: inventing new "Wandering Fork" numbers, reproducing verbatim
  source exam content, skipping the `contracts/session-page.md` section
  order
