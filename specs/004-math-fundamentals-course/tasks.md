# Tasks: Complete English Course — Mathematical Fundamentals and Data Analysis

**Input**: Design documents from `/specs/004-math-fundamentals-course/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Not requested. This is a static Quarto content feature; verification is
done via `quarto render` (exit 0), link checks, and source-fidelity review rather
than automated code tests. No test tasks are generated.

**Organization**: Tasks are grouped by user story so each can be implemented and
verified independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1 = complete module content; US2 = whole-course navigation/framing;
  US3 = source-fidelity verification
- All paths are relative to repo root `/home/guillaume/www/`

## Path Conventions

- Course sources: `teaching/mathematical-fundamentals/`
- Reference archives (read-only): `teaching/mathematical-fundamentals/MS01-001-G_Fondamentaux*/`
- Site nav: `_quarto.yml`; rendered output: `docs/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create missing files and shared scaffolding.

- [X] T001 [P] Create `teaching/mathematical-fundamentals/module-8.qmd` skeleton (front matter with `title`, `lang: en`, `abstract`, `date`, `keywords`, and `code-links` to Syllabus + module-1…module-8) per `specs/004-math-fundamentals-course/contracts/module-page.md`
- [X] T002 [P] Create `teaching/mathematical-fundamentals/glossary.qmd` skeleton (front matter + themed section headings) per `specs/004-math-fundamentals-course/contracts/glossary-page.md`
- [X] T003 [P] Extract reference text/numbers from source decks and handouts into a scratch note (using `python-pptx` / `pdftotext`) to support fidelity while authoring; keep archives unmodified (`teaching/mathematical-fundamentals/MS01-001-G_Fondamentaux*/`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Normalize conventions every module must share before content authoring.

**⚠️ CRITICAL**: Complete before starting per-module content (Phase 3).

- [X] T004 Normalize front matter across `teaching/mathematical-fundamentals/module-1.qmd`…`module-8.qmd`: English `title`, `lang: en`, `abstract`, `date`, and a consistent `code-links` block (Syllabus + Module 1–8) so cross-navigation is uniform (FR-011)
- [X] T005 [P] Confirm the callout-semantics and LaTeX conventions to apply everywhere (note=definitions, tip=formulas, warning=caveats, important=exam/`TODO:` demo gaps, caution+collapse=exercises/proofs; all math LaTeX) as defined in `specs/004-math-fundamentals-course/research.md` Decisions 4–7 — record as a short authoring checklist comment in each empty module file

**Checkpoint**: Conventions fixed — module content authoring can begin in parallel.

---

## Phase 3: User Story 1 - Complete, English module end-to-end (Priority: P1) 🎯 MVP

**Goal**: Every module (1–8) is a self-contained English lesson: objectives →
introduction → theory → ≥1 collapsible derivation → multiple worked examples →
static exercises with revealable solutions, at Module 1 depth, using LaTeX and
constitution-compliant callouts.

**Independent Test**: Open any one module page after rendering; confirm it has
objectives, theory, a collapsible derivation, worked examples, and exercises with
revealable solutions — all in English with correct math — faithful to its source
deck.

**MVP note**: Completing **T006 (Module 1)** alone satisfies the US1 independent
test and is the minimal shippable slice; the full story requires all eight.

- [X] T006 [P] [US1] Author `teaching/mathematical-fundamentals/module-1.qmd` — translate to English; convert all Unicode/HTML math to LaTeX; keep concepts (order of operations, absolute value, powers, square roots, fractions, percentages/index, proportionality); convert the `shinylive` quizzes to static exercises in `.callout-caution collapse="true"`; add ≥1 collapsible derivation (successive-discount factor); add `.callout-important` `TODO:` demo-gap markers; verify results against source (SC-002, SC-003, SC-004, T-VI)
- [X] T007 [P] [US1] Author `teaching/mathematical-fundamentals/module-2.qmd` — complete & translate; cover factoring, expanding, notable identities, solving first-degree equations; migrate `.callout-tip` "Solution" blocks to `.callout-caution collapse="true"`; add derivation of $(a+b)^2=a^2+2ab+b^2$; preserve all existing worked results (SC-003, SC-004, T-VI)
- [X] T008 [P] [US1] Author `teaching/mathematical-fundamentals/module-3.qmd` — rewrite the repeated slide-outline dumps into coherent English prose; cover Cartesian plane, equation of a line, systems of first-degree equations (graphical + algebraic), first-degree inequalities and systems, synthesis (logistics/budget) exercise; add derivation of two-line intersection by substitution; surface graphical intuition (T-VII, SC-003)
- [X] T009 [P] [US1] Author `teaching/mathematical-fundamentals/module-4.qmd` from the Module 4 deck/handout — numerical sequences (definition, sum of terms, sense of variation), arithmetic sequences, geometric sequences, savings/loan examples; add derivation of the sum of the first $n$ terms; add `TODO:` demo-gap marker (SC-003, SC-004, T-VI)
- [X] T010 [P] [US1] Author `teaching/mathematical-fundamentals/module-5.qmd` from the Module 5 deck — simple interest, compound interest, combined approach, inverse problems, unit/period conversion, synthesis exercise; add derivation of $C_n = C_0(1+i)^n$ (SC-003, SC-004, T-VI)
- [X] T011 [P] [US1] Author `teaching/mathematical-fundamentals/module-6.qmd` from the Module 6 deck — single-variable function (domain, forbidden values, sign, variation, parity), usual functions (affine, degree-2 polynomial, square root, logarithm, exponential), second-degree equations; add derivation of quadratic roots/discriminant; surface graph intuition (SC-003, T-VI, T-VII)
- [X] T012 [P] [US1] Author `teaching/mathematical-fundamentals/module-7.qmd` from the Module 7 deck — average & instantaneous rate of change, intuitive derivative, application to affine and degree-2 functions, optimization (max/min); add derivation of the derivative of $f(x)=x^2$ from the average rate of change; tangent-slope intuition (SC-003, T-VI, T-VII)
- [X] T013 [P] [US1] Author `teaching/mathematical-fundamentals/module-8.qmd` — revision & final-exam preparation aligned to Modules 1–7 and `EF 2025-2026 correction FR.pdf`; include mixed worked examples (functions, systems, financial math) with collapsible solutions and one representative exam-style derivation (FR-008, T-VI)

**Checkpoint**: All eight modules are complete, English, and independently readable.

---

## Phase 4: User Story 2 - Navigate the whole course, syllabus to exam prep (Priority: P2)

**Goal**: A connected course — English syllabus with recommended literature, a
glossary, and working sidebar navigation from index through all eight modules.

**Independent Test**: From the index page, follow every module link, the glossary,
and the exam-prep module; confirm each destination exists, is in English, and the
syllabus matches each module's topic/sequence.

- [X] T014 [US2] Rewrite `teaching/mathematical-fundamentals/index.qmd` fully in English; keep the 8-module outline with links and dates; rewrite the "Lecture recomandé" list into a **Recommended Literature** section with author, title, edition, and publisher for each entry (FR-010, T-VIII); set `lang: en`
- [X] T015 [US2] Populate `teaching/mathematical-fundamentals/glossary.qmd` with every symbol/formula introduced in Modules 1–8 (FR↔EN term, LaTeX notation, plain-English definition) per `contracts/glossary-page.md` (T-V)
- [X] T016 [US2] Add a `mathematical-fundamentals` sidebar block to `_quarto.yml` listing `index.qmd` first, then `module-1.qmd`…`module-8.qmd`, then `glossary.qmd` (constitution §II, §T-VIII; FR-008a)
- [X] T017 [US2] Reconcile `teaching/mathematical-fundamentals/_metadata.yml` so its local sidebar does not conflict with the authoritative `_quarto.yml` registration
- [X] T018 [US2] Verify every syllabus module link, glossary link, and per-module `code-links` entry resolves (SC-006, SC-007)

**Checkpoint**: Full course navigable end-to-end from the syllabus.

---

## Phase 5: User Story 3 - Verify fidelity to source materials (Priority: P3)

**Goal**: Confirm each module preserves source concepts, examples, and results, and
that no untranslated French learner-facing prose remains.

**Independent Test**: Pick any module and cross-check its concept list and results
against the source PPTX/PDF; confirm complete coverage and matching results.

- [X] T019 [P] [US3] Concept-coverage audit: for each module 1–8, tick every concept in `specs/004-math-fundamentals-course/research.md` Decision 3; add any missing concept to the module (SC-003)
- [X] T020 [P] [US3] Result-fidelity audit: cross-check worked-example and exercise results in each module against the corresponding source deck/handout/exam; correct any divergence (SC-004)
- [X] T021 [P] [US3] English-only audit: scan `module-*.qmd` and `index.qmd` for untranslated French learner-facing prose (per `quickstart.md` heuristic) and fix (SC-002)

**Checkpoint**: All modules verified faithful and fully English.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final build, rendering integrity, and delivery.

- [ ] T022 Run `quarto render` (full site) and fix any broken math or render errors until it exits 0 (SC-005)
- [ ] T023 [P] Confirm callout semantics are consistent across all modules (note/tip/warning/important/caution-collapse) and no inline `style=`/`<style>` blocks were introduced (constitution §V)
- [ ] T024 [P] Confirm 80-character prose wrapping and `lang: en` front matter on all new/edited `.qmd` files (constitution workflow, §VI)
- [ ] T025 Commit regenerated `docs/` (and any `_freeze/` updates) alongside sources in the same commit (constitution §III)
- [ ] T026 Run the `quickstart.md` validation checklist end-to-end (SC-001 through SC-007) and record results

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately.
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories.
- **US1 (Phase 3)**: Depends on Foundational. Modules are independent of each other.
- **US2 (Phase 4)**: T015 (glossary content) and T018 (link check) depend on US1
  modules existing; T014/T016/T017 can begin once files exist (after Setup) but are
  best finalized after US1.
- **US3 (Phase 5)**: Depends on US1 (and US2 for link/nav aspects).
- **Polish (Phase 6)**: Depends on all desired stories being complete.

### User Story Dependencies

- **US1 (P1)**: Independent — each module stands alone. This is the MVP.
- **US2 (P2)**: Frames/links US1 output; glossary and link-verification need US1 done.
- **US3 (P3)**: Verification layer over US1/US2.

### Within Each Story

- US1: front matter (Phase 2) → theory → derivation → worked examples → exercises,
  per module.
- US2: syllabus + glossary content → nav registration → link verification.
- US3: coverage → results → language audits.

### Parallel Opportunities

- Setup tasks T001–T003 run in parallel.
- **All eight module tasks T006–T013 run in parallel** (different files).
- US3 audits T019–T021 run in parallel.
- Polish T023/T024 run in parallel.

---

## Parallel Example: User Story 1 (the bulk of the work)

```bash
# After Phase 2, author all eight modules in parallel (different files):
Task: "Author module-1.qmd (T006)"
Task: "Author module-2.qmd (T007)"
Task: "Author module-3.qmd (T008)"
Task: "Author module-4.qmd (T009)"
Task: "Author module-5.qmd (T010)"
Task: "Author module-6.qmd (T011)"
Task: "Author module-7.qmd (T012)"
Task: "Author module-8.qmd (T013)"
```

---

## Implementation Strategy

### MVP First (User Story 1, one module)

1. Phase 1: Setup (create `module-8.qmd`, `glossary.qmd` skeletons).
2. Phase 2: Foundational (normalize front matter + conventions).
3. Phase 3: Complete **Module 1 (T006)** → render → validate independently → demo.

### Incremental Delivery

1. Setup + Foundational → ready.
2. US1 module by module → each renders and reads independently (MVP grows).
3. US2 → syllabus, glossary, navigation → full course browsing.
4. US3 → fidelity/language audits.
5. Polish → full render, docs commit, quickstart validation.

### Parallel Team Strategy

After Foundational, different authors can each take one or more of T006–T013
(one file each, no conflicts), while another prepares the syllabus/glossary (US2).

---

## Notes

- [P] tasks = different files, no dependencies.
- No automated tests (content feature); the render gate + fidelity audits are the
  acceptance mechanism.
- Two constitution deviations apply (see `plan.md` Complexity Tracking): bilingual
  parity deferred (English-only per user request) and Shinylive demos replaced by
  `.callout-important` `TODO:` markers.
- Commit after each module or logical group; keep `docs/`/`_freeze/` in sync
  (constitution §III).
