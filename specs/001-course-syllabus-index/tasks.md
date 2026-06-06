---
description: "Task list for Course Syllabus Index Pages"
---

# Tasks: Course Syllabus Index Pages

**Input**: Design documents from `specs/001-course-syllabus-index/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/,
quickstart.md (all present)

**Tests**: No automated test framework exists for this Quarto site and none was
requested. Validation is `quarto render` exiting 0 plus the grep structural
checks in `quickstart.md`. No test tasks are generated.

**Organization**: Tasks are grouped by user story (US1 P1, US2 P2, US3 P3) for
independent implementation and delivery.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1 / US2 / US3 (setup, foundational, polish carry no story label)

## Path Conventions

Quarto content site. Work is confined to:
- `teaching/<course>/index.qmd` (6 syllabi to amend)
- `fr/teaching/<course>/index.qmd` (3 new French stubs — EN-authored courses)
- `_quarto.yml` (sidebar registrations/fixes)
- `assets/dark.scss` (referenced only; not edited)

Courses & authored language: `inseec-finance` (fr), `ece-proba` (fr),
`essca-stat` (en), `mathematical-analysis` (fr), `ai-papers` (en), `ai-dev` (en).

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish a clean baseline before editing content.

- [X] T001 Activate `.venv` and capture a baseline full render: run
  `source .venv/bin/activate && quarto render` from repo root and record the
  current exit code / failing pages so regressions introduced by this feature
  are distinguishable from pre-existing ones.
- [X] T002 Re-read `specs/001-course-syllabus-index/contracts/syllabus-template.md`
  and `data-model.md` to confirm the canonical structure (front matter, session
  outline table, literature table profiles) every syllabus must match.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Shared `_quarto.yml` navigation must be correct before any syllabus
counts as "published / first sidebar entry" (Principle II, T-VIII).

**⚠️ CRITICAL**: Complete before user-story phases.

- [X] T003 Fix the dangling `ece-proba` sidebar block in `_quarto.yml`: replace
  `teaching/statistics-probability/index.qmd` with the real
  `teaching/ece-proba/index.qmd`. The
  `- section: teaching/statistics-probability/univariate.qmd` entry references a
  **non-existent file** used only as a group label — convert it to a plain text
  section title (e.g. `- section: "Une variable"`) keeping its existing
  `contents:` list of `teaching/ece-proba/univariate-*.qmd` pages. Do **not**
  hunt for a `univariate.qmd` file; none exists.
- [X] T004 Audit `_quarto.yml` and confirm each course block lists its own
  `teaching/<course>/index.qmd` as the FIRST item (blocks: `inseec-finane`,
  `ece-proba`, `decision-making`, `mathematical-analysis`, `ai-papers`,
  `ai-dev`). Note any block where the index is not first; do not reorder
  session entries beyond moving the index to first position.

**Checkpoint**: Navigation is consistent; syllabus amendments can begin.

---

## Phase 3: User Story 1 — Student finds the course reading list (Priority: P1) 🎯 MVP

**Goal**: Every course syllabus shows a session-outline table and a Recommended
Literature table, with compliant front matter, as the first sidebar entry.

**Independent Test**: Navigate to each `teaching/<course>/` page; it renders a
description, a `| # | Session | Topics Covered |` table, and a Recommended
Literature table with ≥1 row containing author/title/edition/publisher (or
author/title/year/venue for papers).

> Each task below edits one independent file → all are [P]. Each task MUST:
> (1) set front matter (`title`, `lang`, `date-modified`; remove any
> `format:`/`theme:` override); (2) ensure an **Overview/description** paragraph
> **and a "Learning Objectives" list** are present (FR-002) — add them if
> missing; (3) add the session-outline table (links resolving to existing
> session files — locality-independent); (4) add the Recommended Literature
> table per the contract. Wrap prose at 80 chars.

- [X] T005 [P] [US1] Amend `teaching/essca-stat/index.qmd`: remove the per-file
  `format.html.theme: cosmo` override and `toc` block, replace `date: today`
  with `date-modified`, add `lang: en`; add a session-outline table linking the
  15 sessions at `sessions/session-01.qmd … session-15.qmd`; add a Recommended
  Literature table (book profile).
- [X] T006 [P] [US1] Amend `teaching/inseec-finance/index.qmd`: prepend a YAML
  front-matter block (`title`, `lang: fr`, `date-modified`) — none exists today;
  ensure an Overview + Learning Objectives are present. For the session outline:
  this course currently has **no session pages registered** in its sidebar, so
  the outline table MAY list planned sessions **without links** (Topics Covered
  filled in); links are added later when session pages exist. Add a Recommended
  Literature table (book profile, French finance references). Note: T011's link
  check does not apply to link-less planned-session rows here.
- [X] T007 [P] [US1] Amend `teaching/ece-proba/index.qmd`: add `lang: fr` to
  front matter (keep existing `title`/`date-modified`); add a session-outline
  table linking the `teaching/ece-proba/*.qmd` session files registered in the
  `ece-proba` sidebar block; add a Recommended Literature table (book profile).
- [X] T008 [P] [US1] Amend `teaching/mathematical-analysis/index.qmd`: add
  `lang: fr` (keep existing dates); add a session-outline table linking the
  `teaching/mathematical-analysis/*.qmd` module files; add a Recommended
  Literature table (book profile).
- [X] T009 [P] [US1] Amend `teaching/ai-papers/index.qmd`: add `date-modified`
  and `lang: en`; remove the stray draft placeholder block (the `::: ` raw-notes
  list); add a session-outline table linking the `teaching/ai-papers/*.qmd`
  pages; add a Recommended Literature table using the **paper profile**
  (`| Author(s) | Title | Year | Publication Venue |`, FR-009).
- [X] T010 [P] [US1] Amend `teaching/ai-dev/index.qmd`: add `lang: en` (keep
  existing `title`/`date-modified`); add a session-outline table linking the
  `teaching/ai-dev/*.qmd` pages; add a Recommended Literature table (paper /
  online-resource profile as appropriate).
- [X] T011 [US1] Render-verify US1: run
  `quarto render teaching/<course>/index.qmd --quiet` for all six courses and
  confirm each exits 0 and shows both tables. Fix any broken outline links
  (must resolve to existing files).

**Checkpoint**: All six syllabi are complete, compliant, and first in their
sidebar — MVP delivered.

---

## Phase 4: User Story 2 — Instructor updates the reading list (Priority: P2)

**Goal**: The literature list is a single authoritative, self-contained table in
each `index.qmd` so an instructor can edit it without touching any session file.

**Independent Test**: Edit one course's literature table, run
`quarto render teaching/<course>/index.qmd --quiet`; the change appears and no
other file required modification.

- [ ] T012 [US2] In each `teaching/<course>/index.qmd`, ensure the
  Recommended Literature section is self-contained (no `{{< include >}}` of
  external files, no cross-file references) and add a short maintainer HTML
  comment above the table documenting the column profile (book vs paper) so
  future edits stay consistent. (Edits all six files as one uniform unit — not
  parallelizable against the per-file US1 tasks.)
- [ ] T013 [US2] Verify the edit-in-isolation property: modify a single row in
  one course's literature table, render only that file, confirm success, then
  revert the test edit. Confirm no session file or other course was touched.

**Checkpoint**: Literature lists are maintainable in one place per course.

---

## Phase 5: User Story 3 — French-language visitor reads the syllabus (Priority: P3)

**Goal**: Each EN-authored syllabus has a reachable French stub counterpart so
`fr/teaching/<course>/` never 404s. (FR-authored courses are deferred to the
language-normalization feature — out of scope here.)

**Independent Test**: Navigate to `fr/teaching/<course>/` for the three
EN-authored courses; each shows the source title, a French "traduction en cours"
callout, and a working backlink to the EN syllabus.

- [ ] T014 [P] [US3] Create `fr/teaching/essca-stat/index.qmd` stub: front
  matter `title` (source course title), `lang: fr`; a `.callout-note`
  "Traduction en cours / Translation in progress" block; a Markdown backlink to
  `../../../teaching/essca-stat/index.qmd`.
- [ ] T015 [P] [US3] Create `fr/teaching/ai-papers/index.qmd` stub (same pattern;
  backlink to `../../../teaching/ai-papers/index.qmd`).
- [ ] T016 [P] [US3] Create `fr/teaching/ai-dev/index.qmd` stub (same pattern;
  backlink to `../../../teaching/ai-dev/index.qmd`).
- [ ] T017 [US3] Register the three French stubs in `_quarto.yml` so they are
  published per Principle II (a page absent from a sidebar is "not published")
  and never 404. Add a **new dedicated sidebar block** for the French stubs,
  e.g.:

  ```yaml
  - id: fr-teaching
    contents:
      - fr/teaching/essca-stat/index.qmd
      - fr/teaching/ai-papers/index.qmd
      - fr/teaching/ai-dev/index.qmd
  ```

  Place it alongside the other sidebar blocks. Confirm `quarto render` lists the
  three pages and introduces no dangling links. (A full per-language navbar
  switcher is out of scope — deferred to the language-normalization feature.)
- [ ] T018 [US3] Render-verify US3: run `quarto render` and confirm each
  `fr/teaching/<course>/index.qmd` renders, the backlink resolves, and no 404 is
  produced for the three French stub paths.

**Checkpoint**: Partial bilingual parity delivered for EN-authored courses.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and commit hygiene.

- [ ] T019 Run the full render gate: `quarto render` MUST exit 0 (compare
  against the T001 baseline; no new failures). Allow the post-render
  `scripts/update-profile-readme.sh` hook to run; do not suppress it.
- [ ] T020 [P] Run the `quickstart.md` structural checks (the `for f in
  teaching/*/index.qmd` grep loop) and confirm every syllabus reports `lang ok`,
  `date ok`, `literature heading ok`, `outline table ok`, and NO
  `WARN per-file theme override`.
- [ ] T021 Stage and commit the rendered output and cache alongside sources:
  `docs/` and `_freeze/` MUST be committed in the same commit as the `.qmd` and
  `_quarto.yml` changes (Principle III, Development Workflow).
- [ ] T022 Update `specs/001-course-syllabus-index/quickstart.md` "Definition of
  Done" checkboxes to reflect actual completion state.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: After Setup. T003 (ece-proba sidebar fix) BLOCKS
  US1 verification for that course and is a shared `_quarto.yml` edit.
- **US1 (Phase 3)**: After Foundational. MVP.
- **US2 (Phase 4)**: After US1 (operates on the literature tables US1 creates).
- **US3 (Phase 5)**: After US1 (stubs backlink to the completed EN syllabi).
  US3 also edits `_quarto.yml` (T017) — sequence after T003/T004 to avoid
  conflicting edits to the same file.
- **Polish (Phase 6)**: After all desired stories.

### Story Independence

- US1 is fully independent and is the MVP.
- US2 depends only on US1's literature tables existing.
- US3 depends only on US1's EN syllabi existing (for the backlinks).

### Same-file sequencing (NOT parallel)

- `_quarto.yml` is touched by T003, T004, T017 → run these sequentially.
- T011, T013, T018, T019, T020 are verification gates → run after their phase's
  edits.

### Parallel Opportunities

- US1: T005–T010 each edit a different `index.qmd` → run in parallel.
- US3: T014–T016 each create a different stub file → run in parallel.
- T012 spans all six files but is a uniform additive edit; treat as one unit.

---

## Parallel Example: User Story 1

```bash
# Six independent syllabus edits (different files):
Task: "Amend teaching/essca-stat/index.qmd (T005)"
Task: "Amend teaching/inseec-finance/index.qmd (T006)"
Task: "Amend teaching/ece-proba/index.qmd (T007)"
Task: "Amend teaching/mathematical-analysis/index.qmd (T008)"
Task: "Amend teaching/ai-papers/index.qmd (T009)"
Task: "Amend teaching/ai-dev/index.qmd (T010)"
# Then T011 verifies all six render.
```

---

## Implementation Strategy

### MVP First (User Story 1)

1. Phase 1 Setup → 2. Phase 2 Foundational (sidebar fix) →
3. Phase 3 US1 (six syllabi) → 4. STOP & VALIDATE (T011) → deploy/demo.

### Incremental Delivery

1. Setup + Foundational → navigation correct.
2. US1 → all syllabi have outline + literature tables (MVP).
3. US2 → literature lists confirmed maintainable in isolation.
4. US3 → French stubs for EN-authored courses (partial parity).
5. Polish → full render gate, structural checks, commit `docs/`+`_freeze/`.

---

## Notes

- [P] = different files, no dependencies. `_quarto.yml` edits are never [P]
  against each other.
- No test tasks (no framework; render + grep is the validation per plan).
- FR-authored courses (`inseec-finance`, `ece-proba`, `mathematical-analysis`)
  get NO counterpart and NO `en/` tree here — Principle VI is intentionally
  partial; deferred to the language-normalization feature.
- Commit after each phase; `docs/` and `_freeze/` go in the same commit as
  sources (Principle III).
