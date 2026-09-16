# Tasks: Mathematical Fundamentals RevealJS Slide Decks

**Input**: Design documents from `specs/007-math-fundamentals-slides/`

**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [data-model.md](data-model.md),
[contracts/slide-deck-format.md](contracts/slide-deck-format.md),
[quickstart.md](quickstart.md)

**Tests**: Not requested. Validation is done via `quarto render` smoke tests
and visual inspection per [quickstart.md](quickstart.md).

**Organization**: Tasks are grouped by user story. US1 (Module 1 deck) is
the MVP — it is independently completable and demonstrable before any other
story begins.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no shared-state dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths are included in every task description

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the two infrastructure prerequisites that block all slide
rendering. No user story work can begin until T001 is complete; FR stub work
requires T002.

- [x] T001 Create `assets/dark-slides.scss` with RevealJS SCSS variables
  following the schema in `specs/007-math-fundamentals-slides/data-model.md`
  (Entity 2). Required variables: `$backgroundColor`, `$mainColor`,
  `$headingColor`, `$linkColor`, `$selectionBackgroundColor`,
  `$mainFontSize`. Add `/*-- scss:defaults --*/` and `/*-- scss:rules --*/`
  section markers. Do NOT import or reference `assets/dark.scss`.

- [x] T002 Create the directory `fr/teaching/mathematical-fundamentals/`
  (including all parent directories `fr/` and `fr/teaching/` if they do not
  exist). This path must exist before any French stub files can be written.

**Checkpoint**: `assets/dark-slides.scss` exists and `fr/teaching/mathematical-fundamentals/`
directory exists. No rendering needed yet.

---

## Phase 2: Foundational (Canary Validation)

**Purpose**: Build and validate Module 1 slides as the canary before
producing the remaining 7 decks. Proves the RevealJS + SCSS approach is
correct end-to-end. All subsequent deck creation (T007–T013) follows the
pattern established here.

**⚠️ CRITICAL**: T001 must be complete before T003. T003 must pass (exit 0)
before T007–T013 begin.

- [x] T003 Create `teaching/mathematical-fundamentals/module-1-slides.qmd`
  as a complete RevealJS slide deck. Front matter per contract:
  `title: "1️⃣ Essential Mathematical Calculations for Economics and
  Management — Slides"`, `subtitle: "Mathematical Fundamentals · MS01-001-G"`,
  `lang: en`, `format: revealjs` with `theme: assets/dark-slides.scss`,
  `slide-number: true`, `progress: true`, `controls: true`,
  `transition: slide`. Required slide sections in order:
  (1) Learning Objectives (4 bullets from module-1.qmd callout-note),
  (2) Order of Operations — PEMDAS rule with `$$` formula and 1-sentence explanation,
  (3) Absolute Value — definition `|a|` and 4 key properties in a `.callout-tip`,
  (4) Powers — 6 key properties in a `.callout-tip`,
  (5) Square Root — definition and 2 properties,
  (6) Fractions — addition/subtraction, multiplication, division rules,
  (7) Percentages and Index Numbers — percentage change formula
  `$$\Delta\% = \frac{V_\text{final}-V_\text{initial}}{V_\text{initial}}\times 100$$`
  and note that successive changes multiply not add,
  (8) Proportionality Rule — formula
  `$$\frac{a}{b}=\frac{c}{x}\Rightarrow x=\frac{b\times c}{a}$$`,
  (9) Worked Example — successive discounts coat problem (€200 × 0.90 × 0.95 × 0.85)
  condensed to 3 key steps,
  (10) Summary — 3 numbered takeaways (order of operations governs; successive
  percentages multiply; always divide by initial value),
  (11) `## 📖 Full Reference` — link to `module-1.qmd` with text "See the
  complete module for theory, exercises, and interactive simulations."
  No OJS blocks. No inline style attributes.

- [x] T004 Smoke-test: run `quarto render teaching/mathematical-fundamentals/module-1-slides.qmd --quiet`
  and confirm exit code 0. Verify that
  `docs/teaching/mathematical-fundamentals/module-1-slides.html` is created.
  If the render fails, fix T001 or T003 before continuing.

**Checkpoint**: `module-1-slides.html` exists and renders as a RevealJS
presentation (verified by opening in browser: no navbar, no sidebar, full-screen
slide layout visible).

---

## Phase 3: User Story 1 — Instructor Delivers a Module Lecture (P1) 🎯 MVP

**Goal**: An instructor can open Module 1 slides in full-screen RevealJS and
deliver a complete lecture covering all 7 core concepts, a worked example,
and a summary — without needing the reference page.

**Independent Test**: Open
`docs/teaching/mathematical-fundamentals/module-1-slides.html` in a browser.
Advance through all slides and confirm: (a) all 7 concepts appear, each with
a `.callout-tip` formula block; (b) the worked example appears with step-by-step
calculations; (c) the Summary slide has exactly 3 numbered takeaways; (d) the
final slide has a working link to `module-1.html`.

### Implementation for User Story 1

Module 1 slide deck was created in the Foundational phase (T003/T004). The
US1 validation tasks below confirm all acceptance scenarios from the spec.

- [x] T005 [US1] Visual inspection of `docs/teaching/mathematical-fundamentals/module-1-slides.html`
  per quickstart.md Step 3 checklist: confirm RevealJS chrome (no navbar,
  slide-number indicator, progress bar, controls visible), title slide shows
  correct title and subtitle, Learning Objectives is slide 2, all 7 concept
  slides are present with rendered LaTeX (not raw `$$...$$`), Worked Example
  step-by-step is readable, Summary has 3 numbered takeaways, Reference slide
  link opens `module-1.html` correctly.

**Checkpoint**: US1 is complete and independently demonstrable. The instructor
can open `module-1-slides.html` and deliver a full Module 1 lecture.

---

## Phase 4: User Story 2 — Student Reviews Slides After Lecture (P2)

**Goal**: Students can navigate to the Module 1 slide deck from the course
site (via sidebar or module reference page), and the slide deck links back
to the full reference page for deeper study.

**Independent Test**: Navigate to
`docs/teaching/mathematical-fundamentals/index.html`, find the "Slides"
section in the left sidebar, click "Module 1 — Slides", confirm the deck
opens. Then open `docs/teaching/mathematical-fundamentals/module-1.html`
and confirm the "📊 Lecture slides" link opens `module-1-slides.html`.
Finally, from `module-1-slides.html`, click "📖 Full Reference" and confirm
it opens `module-1.html`.

### Implementation for User Story 2

- [x] T006 [US2] Edit `_quarto.yml`: insert a new `"**Slides**"` section
  into the `mathematical-fundamentals` sidebar block, between the existing
  module list and the `"**Resources**"` section. Add one entry:
  `- text: "Module 1 — Slides"` / `  href: teaching/mathematical-fundamentals/module-1-slides.qmd`.
  Use the exact YAML fragment from `specs/007-math-fundamentals-slides/data-model.md`
  (Entity 4) as the reference. Do not touch any other sidebar block.

- [x] T007 [US2] Edit `teaching/mathematical-fundamentals/module-1.qmd`:
  add the following block immediately after the opening `.callout-note`
  (Learning objectives) block and before the `## Diagnostic Activity` heading:
  `> 📊 **Lecture slides**: [View the slides for this module](module-1-slides.qmd)`.
  This is a blockquote line; do not use a callout div. Do not change any
  other content in the file.

**Checkpoint**: US2 is complete. Student can find Module 1 slides via the
sidebar and via the reference page link. The slide deck links back to the
reference page.

---

## Phase 5: User Story 3 — Consistent Coverage Across All 8 Modules (P3)

**Goal**: All 8 modules have a working RevealJS slide deck (EN) and a French
stub, all are registered in the sidebar, and all render without errors.

**Independent Test**: Run
`for n in 1 2 3 4 5 6 7 8; do quarto render teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet && echo "OK $n"; done`
and confirm 8 "OK" lines. Then run
`for n in 1 2 3 4 5 6 7 8; do quarto render fr/teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet && echo "FR OK $n"; done`
and confirm 8 "FR OK" lines. Open the course index and confirm the Slides
section lists all 8 modules.

### Implementation for User Story 3 — English Slide Decks (Modules 2–7)

Create each file following the same front matter contract as T003
(`title`, `subtitle`, `lang: en`, `format: revealjs`, `theme: assets/dark-slides.scss`,
`slide-number: true`, `progress: true`, `controls: true`, `transition: slide`).
All [P] tasks operate on distinct files and can run in parallel.

- [x] T008 [P] [US3] Create `teaching/mathematical-fundamentals/module-2-slides.qmd`.
  Title: `"2️⃣ Mastering Equations for Better Decision-Making — Slides"`.
  Learning objectives from module-2.qmd. Concept slides (4):
  (1) Expanding — distributivity rule with example,
  (2) Factoring — common factor extraction with example,
  (3) Notable Identities — `$(a+b)^2$`, `$(a-b)^2$`, `$(a+b)(a-b)$` in a `.callout-tip`,
  (4) First-Degree Equations — isolation method, balance rule.
  Worked Example: break-even point calculation.
  Summary: 3 takeaways. Reference link to `module-2.qmd`.

- [x] T009 [P] [US3] Create `teaching/mathematical-fundamentals/module-3-slides.qmd`.
  Title: `"3️⃣ Curve Analysis in Economics and Management — Slides"`.
  Learning objectives from module-3.qmd. Concept slides (4):
  (1) Reading a Graph — intercepts, slope, sign from a Cartesian plane,
  (2) Equation of a Line — `$y = ax + b$`, slope and y-intercept interpretation,
  (3) Systems of Equations — substitution and elimination methods,
  (4) Inequalities — solution sets, graphical interpretation.
  Worked Example: intersection of two pricing/cost models.
  Summary: 3 takeaways. Reference link to `module-3.qmd`.

- [x] T010 [P] [US3] Create `teaching/mathematical-fundamentals/module-4-slides.qmd`.
  Title: `"4️⃣ Introduction to Financial-Mathematics Tools — Slides"`.
  Learning objectives from module-4.qmd. Concept slides (3):
  (1) Numerical Sequences — index notation `$(u_n)_{n\geq 0}$`, general term,
  (2) Arithmetic Sequences — common difference `$d$`, general term
  `$u_n = u_0 + nd$`, sum formula,
  (3) Geometric Sequences — common ratio `$q$`, general term
  `$u_n = u_0 \times q^n$`, sum formula.
  Worked Example: savings or loan scenario modelled as a sequence.
  Summary: 3 takeaways. Reference link to `module-4.qmd`.

- [x] T011 [P] [US3] Create `teaching/mathematical-fundamentals/module-5-slides.qmd`.
  Title: `"5️⃣ Application of Financial Mathematics — Slides"`.
  Learning objectives from module-5.qmd. Concept slides (2):
  (1) Simple Interest — formula `$C_n = C_0(1 + nt)$`, linear growth,
  (2) Compound Interest — formula `$C_n = C_0(1+t)^n$`, exponential growth,
  capitalisation frequency effect.
  Worked Example: compare two investment vehicles over 5 years.
  Summary: 3 takeaways (key difference: linear vs. exponential growth).
  Reference link to `module-5.qmd`.

- [x] T012 [P] [US3] Create `teaching/mathematical-fundamentals/module-6-slides.qmd`.
  Title: `"6️⃣ Functions Useful in Economics and Management — Slides"`.
  Learning objectives from module-6.qmd. Concept slides (3):
  (1) Functions — definition, domain of definition, forbidden values
  (`$f: x \mapsto f(x)$`),
  (2) Usual Functions — affine `$f(x)=ax+b$`, polynomial `$f(x)=ax^2+bx+c$`,
  logarithm `$\ln$`, exponential `$e^x$` — each with a sketch description,
  (3) Second-Degree Equations — discriminant `$\Delta = b^2-4ac$`, root
  formula `$x = \frac{-b\pm\sqrt{\Delta}}{2a}$`.
  Worked Example: determine which function best models a given phenomenon.
  Summary: 3 takeaways. Reference link to `module-6.qmd`.

- [x] T013 [P] [US3] Create `teaching/mathematical-fundamentals/module-7-slides.qmd`.
  Title: `"7️⃣ Introduction to Optimization — Slides"`.
  Learning objectives from module-7.qmd. Concept slides (3):
  (1) Average Rate of Change — formula
  `$\frac{f(b)-f(a)}{b-a}$`, geometric meaning as slope of secant,
  (2) Instantaneous Rate / Derivative — intuitive limit definition,
  derivative of `$f(x)=ax^2+bx+c$` is `$f'(x)=2ax+b$`,
  (3) Finding Extrema — set `$f'(x)=0$`, sign table, interpret max/min in context.
  Worked Example: find the price or quantity that maximises profit.
  Summary: 3 takeaways. Reference link to `module-7.qmd`.

### Implementation for User Story 3 — Module 8 Revision Deck

Module 8 depends on the content of Modules 1–7 being established (T008–T013).

- [x] T014 [US3] Create `teaching/mathematical-fundamentals/module-8-slides.qmd`.
  Title: `"8️⃣ Revision and Final-Exam Preparation — Slides"`.
  This is a cross-module revision deck — NOT a repeat of any single module.
  Learning objectives from module-8.qmd (identify method, connect concepts,
  practise mixed problems). Slide structure:
  (1) Module 1 Recap — key formula: percentage change `$\Delta\%$` + 1 takeaway,
  (2) Module 2 Recap — key formula: notable identity `$(a+b)^2$` + 1 takeaway,
  (3) Module 3 Recap — key formula: line equation `$y=ax+b$` + 1 takeaway,
  (4) Module 4 Recap — key formulas: arithmetic `$u_n=u_0+nd$` and
  geometric `$u_n=u_0 q^n$` + 1 takeaway,
  (5) Module 5 Recap — key formulas: simple `$C_0(1+nt)$` vs compound
  `$C_0(1+t)^n$` + 1 takeaway,
  (6) Module 6 Recap — discriminant formula `$\Delta=b^2-4ac$` + 1 takeaway,
  (7) Module 7 Recap — derivative rule + 1 takeaway,
  (8) Method Identification — table mapping problem type to module/method
  (scenario → tool),
  (9) Exam Strategy — timing tips, error-check routine, formula sheet usage.
  Summary: "Choose the right tool — no chapter label." Reference link to `module-8.qmd`.

### Implementation for User Story 3 — French Stub Decks

All FR stubs follow the schema from data-model.md (Entity 3): `lang: fr`,
`format: revealjs`, `theme: assets/dark-slides.scss`, `slide-number: true`.
Body: `## 🚧 Traduction en cours` slide + `.callout-note` with link to EN counterpart.
Link path from `fr/teaching/mathematical-fundamentals/` to EN:
use `../../teaching/mathematical-fundamentals/module-N-slides.qmd`.
All [P] tasks operate on distinct files and can run in parallel.

- [x] T015 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-1-slides.qmd`.
  Title: `"1️⃣ Calculs Mathématiques Essentiels — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-1-slides.qmd`.

- [x] T016 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-2-slides.qmd`.
  Title: `"2️⃣ Maîtriser les Équations — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-2-slides.qmd`.

- [x] T017 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-3-slides.qmd`.
  Title: `"3️⃣ Analyse des Courbes — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-3-slides.qmd`.

- [x] T018 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-4-slides.qmd`.
  Title: `"4️⃣ Outils de Mathématiques Financières — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-4-slides.qmd`.

- [x] T019 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-5-slides.qmd`.
  Title: `"5️⃣ Application des Mathématiques Financières — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-5-slides.qmd`.

- [x] T020 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-6-slides.qmd`.
  Title: `"6️⃣ Fonctions Utiles en Économie et Gestion — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-6-slides.qmd`.

- [x] T021 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-7-slides.qmd`.
  Title: `"7️⃣ Introduction à l'Optimisation — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-7-slides.qmd`.

- [x] T022 [P] [US3] Create `fr/teaching/mathematical-fundamentals/module-8-slides.qmd`.
  Title: `"8️⃣ Révision et Préparation à l'Examen — Diapositives"`. `lang: fr`.
  Link to `../../teaching/mathematical-fundamentals/module-8-slides.qmd`.

### Implementation for User Story 3 — Sidebar and Reference Page Completion

- [x] T023 [US3] Edit `_quarto.yml`: extend the `"**Slides**"` section added
  in T006 to include entries for Modules 2–8 (one entry per module, same
  format as Module 1). Also add a new French sidebar block
  `id: fr-mathematical-fundamentals` mirroring the EN block structure, with
  a `"**Diapositives**"` section listing all 8 FR stub entries
  (`href: fr/teaching/mathematical-fundamentals/module-N-slides.qmd`).
  Do not alter any other sidebar block.

- [x] T024 [P] [US3] Edit `teaching/mathematical-fundamentals/module-2.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-2-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T025 [P] [US3] Edit `teaching/mathematical-fundamentals/module-3.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-3-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T026 [P] [US3] Edit `teaching/mathematical-fundamentals/module-4.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-4-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T027 [P] [US3] Edit `teaching/mathematical-fundamentals/module-5.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-5-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T028 [P] [US3] Edit `teaching/mathematical-fundamentals/module-6.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-6-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T029 [P] [US3] Edit `teaching/mathematical-fundamentals/module-7.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-7-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

- [x] T030 [P] [US3] Edit `teaching/mathematical-fundamentals/module-8.qmd`:
  add `> 📊 **Lecture slides**: [View the slides for this module](module-8-slides.qmd)`
  immediately after the opening `.callout-note` block and before
  `## Diagnostic Activity`. No other changes.

**Checkpoint**: All 8 EN decks, 8 FR stubs, full sidebar, and all reference
page links are in place. US3 is complete.

---

## Phase 6: Polish & Validation

**Purpose**: End-to-end verification that the complete feature renders
correctly and all acceptance criteria are met.

- [x] T031 Run full site render: `quarto render --quiet`. Confirm exit code 0.
  If errors appear, fix the offending file(s) before proceeding to T032.

- [x] T032 [P] Run all 8 EN deck renders individually and confirm all pass
  per quickstart.md Step 5. Command:
  `for n in 1 2 3 4 5 6 7 8; do quarto render teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet && echo "OK $n"; done`

- [x] T033 [P] Run all 8 FR stub renders individually and confirm all pass
  per quickstart.md Step 8. Command:
  `for n in 1 2 3 4 5 6 7 8; do quarto render fr/teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet && echo "FR OK $n"; done`

- [x] T034 Visual inspection of all 8 EN decks per quickstart.md Steps 3–7:
  verify RevealJS chrome, title, all concept slides, worked example, summary,
  reference link, sidebar link, and module-page link all work correctly for
  each module.

- [x] T035 Verify bilingual stub navigation per quickstart.md Step 8: open
  each FR stub, confirm "🚧 Traduction en cours" notice, and confirm the
  "version anglaise" link opens the EN slide deck correctly.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately.
  T001 and T002 are independent of each other [P].
- **Phase 2 (Foundational)**: T003 depends on T001. T004 depends on T003.
  T004 must pass before T008–T014 begin.
- **Phase 3 (US1)**: T005 depends on T004 (verified T003 output).
- **Phase 4 (US2)**: T006–T007 depend on T004. T006 and T007 are independent [P].
- **Phase 5 (US3)**:
  - T008–T013 depend on T004 and can run in parallel with each other [P],
    except T014 (Module 8) which depends on T008–T013 being established
    as reference.
  - T015–T022 (FR stubs) depend on T002 only; independent of T008–T014 [P].
  - T023 depends on T008–T022 (all decks and stubs must exist before
    registering them all in the sidebar).
  - T024–T030 depend on T008–T014 (each reference page link requires the
    corresponding slide deck to exist) and are independent of each other [P].
- **Phase 6 (Polish)**: All Phase 5 tasks must be complete. T031 should run
  first; T032–T035 can follow in parallel after T031 passes.

### User Story Dependencies

- **US1 (P1)**: Can complete after Phase 1 + Phase 2. No dependency on US2 or US3.
- **US2 (P2)**: Can complete after US1 (T003/T004). Extends US1 with navigation.
- **US3 (P3)**: Can begin (for decks T008–T013) after Phase 2 (T004 passes).
  FR stubs (T015–T022) can begin after T002.

### Parallel Opportunities

```
Phase 1:   T001 ║ T002   (independent files)
Phase 2:   T001 → T003 → T004
Phase 3:   T004 → T005
Phase 4:   T004 → T006 ║ T007
Phase 5:   T008 ║ T009 ║ T010 ║ T011 ║ T012 ║ T013  (after T004)
           T014 (after T008–T013)
           T015 ║ T016 ║ T017 ║ T018 ║ T019 ║ T020 ║ T021 ║ T022  (after T002)
           T023 (after T008–T022)
           T024 ║ T025 ║ T026 ║ T027 ║ T028 ║ T029 ║ T030  (after T008–T014)
Phase 6:   T031 → T032 ║ T033 ║ T034 ║ T035
```

---

## Implementation Strategy

### MVP First (User Story 1 — Module 1 Only)

1. Complete Phase 1 (T001, T002)
2. Complete Phase 2 (T003, T004)
3. Complete Phase 3 (T005)
4. **STOP and VALIDATE**: Open `docs/teaching/mathematical-fundamentals/module-1-slides.html`
   in a browser. The instructor can use this deck to deliver Module 1.
5. Demo to stakeholders if needed — this is a working MVP.

### Incremental Delivery

1. Complete MVP (US1) → instructor has Module 1 slides
2. Add US2 (T006–T007) → students can find and navigate Module 1 slides
3. Add US3 (T008–T030) → all 8 modules covered, FR stubs in place
4. Run validation (Phase 6) → full site renders clean

### Parallel Agent Strategy

With multiple agents:
- **Agent A**: T001 (SCSS) → T003 → T004 → T005 → T008–T013 (sequential EN decks)
- **Agent B**: T002 (FR dir) → T015–T022 (FR stubs, all parallel)
- **Agent C** (after T004): T006–T007, T023–T030 (navigation edits)
- All agents converge at T031 (full site render).

---

## Notes

- [P] tasks = different files, no dependencies — safe to parallelize
- [Story] label maps each task to its user story for traceability
- The Module 1 deck (T003) is the pattern for all other decks. Implement T003
  carefully; it is the reference implementation.
- Never use `{ojs}`, `{shinylive-python}`, or `{python}` blocks in slide files.
- Never add inline `style=` attributes or `<style>` blocks to slide files.
- After T031 (full render), commit `docs/` and `_freeze/` in the same commit
  as the source changes per the Development Workflow in the constitution.
- The pre-existing Constitution VI gap (reference pages lack FR counterparts)
  is out of scope. Do not attempt to fix it in this feature.
