# Feature Specification: Pedagogical Improvement — Mathematical Fundamentals Course

**Feature Branch**: `007-improve-math-pedagogy`

**Created**: 2026-09-13

**Status**: Draft

**Input**: User description: "Previous research agent wrote 2 markdown files
(specify-1.md and specify-2.md) to improve the pedagogical impact of
mathematical-fundamentals. Start a new specify loop to improve the course."

## Overview

The `teaching/mathematical-fundamentals/` course currently delivers sound
mathematical content across eight modules but lacks a consistent pedagogical
framework. Modules vary in structure — some begin with an opening problem,
others jump directly into theory — and none yet include diagnostic activities,
interactive exploration widgets, dedicated error-awareness sections, or
self-assessment checkpoints. The two research documents (`specify-1.md` and
`specify-2.md`) identify a clear pedagogical template and a set of interactive
simulators tailored to each module's key concept.

This feature applies that template uniformly across all eight modules, adds
one interactive exploration component per module, strengthens the course entry
point (`index.qmd`), and creates two new supporting reference pages (a formula
sheet and a learning guide). The goal is to shift the course from a collection
of correct notes into a structured learning environment where students
repeatedly diagnose, experiment, apply, and reflect.

## Clarifications

### Session 2026-09-13

- Q: Which interactive technology should the simulations use — Observable JS
  (OJS) or Shinylive Python? → A: OJS for lightweight browser-based sliders
  and reactive displays (no server required); Shinylive Python where the
  simulation genuinely benefits from Python computation. This satisfies the
  constitution's T-IV requirement (Shinylive for priority concepts) while using
  the lighter-weight OJS for the majority of simulations.
- Q: Do all eight simulations use OJS, departing from constitution T-IV
  (Shinylive-only), or should at least one use Shinylive? → A: Use OJS for
  all eight simulations AND propose a constitution amendment to generalise T-IV
  from "Shinylive" to "Shinylive or OJS", recording the amendment as a
  deliverable of this feature.
- Q: Should Module 8's mixed-method challenge be an interactive OJS component
  (click to unlock method-specific solution) or a static collapsible matching
  the exercise pattern of Modules 1–7? → A: Static collapsible — each problem
  has one callout revealing the method label and full worked solution together;
  the student is prompted to decide before expanding. No OJS logic required
  for Module 8.
- Q: Should the formula sheet list every named formula and algebraic property
  across Modules 1–7 (comprehensive) or only the formulas students invoke
  directly when solving problems (applied formulas only)? → A: Applied formulas
  only — approximately 20–25 key formulas total, one to four per module.
  Intermediate properties (e.g., fraction rules, power laws) are covered in
  the module theory sections and the glossary; they are excluded from the
  formula sheet.
- Q: Should the application questions in the Course Roadmap supplement the
  existing topic-list descriptions or replace them? → A: Supplement — keep the
  existing topic lists and add a bolded application question after each
  module's topic list. Both elements serve different needs: the topic list
  covers prerequisite checking; the question creates motivation.
- Q: Should the formula sheet be a complete reference compiled across all eight
  modules from the outset, or built incrementally per module? → A: A single
  comprehensive `formula-sheet.qmd` covering all modules, organized by module
  section. This gives students a unified revision resource rather than eight
  separate lists.

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Student follows a full module learning loop (Priority: P1)

A student opens any module page (1–8), and the page guides them through a
complete, predictable sequence: a diagnostic activity to surface what they
already know, a provocative opening problem, core theory with worked examples,
guided practice with progressive hints, an interactive simulation they can
explore, an applied business problem, a common-error section, a self-assessment
quiz, a three-point summary, and a link to the next module. They never have to
guess where the lesson is going or what they are expected to do next.

**Why this priority**: The recurring learning loop is the foundational
deliverable. A single fully-restructured module proves the template and
delivers standalone educational value; the pattern is then replicated across
the remaining seven.

**Independent Test**: Open any restructured module in the rendered site.
Confirm the page contains, in order: Diagnostic Activity, Opening Problem,
Core Concepts, Worked Example, Guided Practice (with hint and solution),
Interactive Exploration (widget present and functional), Applied Problem,
Common Errors, Check Your Understanding (five questions), Summary (three
takeaways), Independent Work, and Continue link.

**Acceptance Scenarios**:

1. **Given** a student opens a module page, **When** they reach the top,
   **Then** they encounter a Diagnostic Activity with two to four prerequisite
   questions and a collapsible answer block before any theory is presented.
2. **Given** a student reads the Diagnostic Activity, **When** they continue,
   **Then** they find an Opening Problem — a provocative business or economics
   question — that motivates the module's central concept.
3. **Given** a student reaches the Guided Practice section, **When** they
   attempt an exercise, **Then** they can expand a hint before seeing the full
   solution, ensuring progressive rather than immediate disclosure.
4. **Given** a student reaches the Interactive Exploration section, **When**
   they adjust a slider or parameter, **Then** the output updates reactively
   and follow-up interpretation questions ask them to explain what they observe.
5. **Given** a student reaches the Check Your Understanding section, **When**
   they read the five questions, **Then** the questions cover at least one
   calculation, one conceptual, one applied, and one error-diagnosis question.
6. **Given** a student reaches the end of a module, **When** they read the
   Summary, **Then** it presents exactly three key takeaways, followed by an
   Independent Work list and a Continue link to the next module.

---

### User Story 2 — Student uses the course entry page as a learning hub
(Priority: P2)

A student arrives at the course home (`index.qmd`) and immediately understands
how to navigate the course, what to prepare before each module, and how to
study effectively. The page provides a "Start Here" checklist, a callout
explaining the six-step module learning sequence, the course roadmap with
application questions, a self-monitoring progress checklist, and links to the
formula sheet and learning guide.

**Why this priority**: The entry page frames the whole learning experience.
Without a learner-oriented entry point, students treat the modules as isolated
notes rather than a connected progression. This depends on individual modules
existing but adds the course-level orientation layer.

**Independent Test**: Open `index.qmd` in the rendered site. Confirm the page
contains: a welcome callout, a "Start Here" step list, a "How to study each
module" tip callout, a Course Roadmap with at least one application question
per module, and a Learning Progress checklist.

**Acceptance Scenarios**:

1. **Given** a student opens the course home, **When** they read the top of
   the page, **Then** they find a welcome callout summarising what the course
   will help them do.
2. **Given** a student reads the "Start Here" section, **When** they follow
   the steps, **Then** each step links to a real resource (syllabus, learning
   guide, glossary, formula sheet).
3. **Given** a student reads the Course Roadmap, **When** they look at each
   module entry, **Then** they find a bolded application question that
   contextualises the module's relevance to economics, finance, or management.
4. **Given** a student uses the Learning Progress checklist, **When** they
   tick completed modules, **Then** they can track their own progress across
   all eight modules without needing external tools.

---

### User Story 3 — Student uses the formula sheet and learning guide as revision
resources (Priority: P3)

A student preparing for an assessment opens `formula-sheet.qmd` to find every
formula introduced across Modules 1–7 organised by module, with each formula
labelled with a plain-language description of what it computes. They also open
`learning-guide.qmd` to find advice on how to study each module, how to keep
an error log, and a suggested revision schedule.

**Why this priority**: The formula sheet and learning guide are supporting
resources that multiply the value of the modules already present. They depend
on the modules being complete but can be authored alongside Module 1
restructuring.

**Independent Test**: Open `formula-sheet.qmd` in the rendered site. Confirm
it lists formulas for all seven content modules (1–7), each with a label and
plain-language description. Open `learning-guide.qmd` and confirm it includes
study advice, error-log guidance, and a revision schedule.

**Acceptance Scenarios**:

1. **Given** a student opens the formula sheet, **When** they look up any
   formula covered in the course, **Then** they find it listed under the
   correct module section with its name and what it calculates in plain
   language.
2. **Given** a student opens the learning guide, **When** they read the error
   log section, **Then** they understand how to record errors, their causes,
   and preventive rules.
3. **Given** a student uses the formula sheet during revision, **When** they
   apply a formula to a problem, **Then** the plain-language description is
   sufficient to confirm they have selected the right formula without
   re-reading the full module.

---

### Edge Cases

- **Module 8 (revision)**: Module 8 has no new theory. Its Interactive
  Exploration section is a static mixed-method challenge: six to eight
  unlabelled problems drawn from across Modules 1–7, each with a single
  collapsible callout that reveals the method label and full worked solution
  together. Students are prompted to decide which method applies before
  expanding. No OJS code is used in Module 8; the section is static,
  consistent with the exercise format of the other modules.
- **Module 1 existing interactive TODO**: Module 1 already has a
  `.callout-important` TODO marker for an interactive quiz. The OJS percentage-
  change simulator replaces this placeholder, resolving the open TODO.
- **Existing hint/solution structure**: Several modules already use collapsible
  callouts for solutions. Where hint/solution pairs are already present, they
  are preserved and used as the Guided Practice section; where only a solution
  callout exists, a hint callout is inserted before it.
- **Module completion order**: Module 1 is restructured first as the template
  proof. Modules 2–7 follow using the confirmed template. Module 8 is authored
  last, after Modules 1–7 are stable.
- **OJS and Shinylive coexistence**: Both OJS blocks and `{shinylive-python}`
  blocks can exist on the same page in Quarto. The specification does not
  require one per page to use only one technology.
- **Formula sheet currency**: If a module is later revised to add a new
  formula, `formula-sheet.qmd` must be updated in the same edit to maintain
  consistency.

## Requirements *(mandatory)*

### Functional Requirements

**Module template (applies to all eight modules):**

- **FR-001**: Every module MUST open with a **Diagnostic Activity** section
  containing two to four prerequisite questions and a collapsible answer block,
  placed before any theory content.
- **FR-002**: Every module MUST include an **Opening Problem** section
  immediately after the Diagnostic Activity, presenting a single business,
  finance, or economics scenario and a provocative question that the module's
  central concept resolves. The student MUST be prompted to write down a
  prediction before continuing.
- **FR-003**: Every module MUST include a **Core Concepts** section presenting
  definitions and rules, each accompanied by a plain-language explanation of
  what the concept computes and why it matters in context (per constitution
  T-III).
- **FR-004**: Every module MUST include at least one fully **Worked Example**
  with every step explicitly justified and the result stated.
- **FR-005**: Every module MUST include a **Guided Practice** section with a
  multi-step exercise, a collapsible hint, and a collapsible complete solution
  — in that order, so the student encounters the hint before the solution.
- **FR-006**: Every module MUST include an **Interactive Exploration** section
  containing at least one reactive simulation (OJS or Shinylive Python) whose
  inputs map to the module's key concept, followed by two to four
  interpretation questions asking the student to explain the observed behaviour.
- **FR-007**: Every module MUST include an **Applied Problem** section
  presenting a finance, economics, or management scenario with a dataset or
  decision context drawn from the source materials.
- **FR-008**: Every module MUST include a **Common Errors** section using a
  `.callout-warning` block that names at least one typical error for the
  module's topic, shows the incorrect and correct workings side by side, and
  explains why the error occurs.
- **FR-009**: Every module MUST include a **Check Your Understanding** section
  with exactly five short questions covering at minimum: one calculation
  question, one conceptual question, one applied question, and one
  error-diagnosis question.
- **FR-010**: Every module MUST end with a **Summary** of exactly three key
  takeaways, followed by an **Independent Work** list and a **Continue** link
  to the next module (or to the revision page for Module 8).
- **FR-011**: Every interactive simulation MUST be followed by interpretation
  questions that require the student to reason about the output, not merely
  observe it (e.g., "Can you explain why…?" or "Find the input that makes…").
- **FR-012**: Each concept in the Core Concepts section SHOULD appear in at
  least two of the four representation forms (verbal, symbolic, numerical,
  graphical) where applicable, to support multiple-representation learning.

**Per-module interactive simulations:**

- **FR-013**: Module 1 MUST include an OJS percentage-change simulator with
  sliders for initial value, increase rate, and decrease rate, displaying the
  value after increase, final value, and overall change. This resolves the
  existing `TODO` interactive placeholder.
- **FR-014**: Module 2 MUST include an OJS break-even simulator with inputs
  for fixed cost, variable cost per unit, and selling price per unit,
  displaying revenue, total cost, profit, and the break-even quantity.
- **FR-015**: Module 3 MUST include an OJS line-intersection explorer with
  sliders for slope and intercept of two lines, displaying the graph and the
  algebraic intersection point.
- **FR-016**: Module 4 MUST include an OJS sequence explorer with inputs for
  the initial term, common difference (arithmetic), and common ratio
  (geometric), displaying both sequences side by side for a user-selected
  number of terms.
- **FR-017**: Module 5 MUST include an OJS compound-interest calculator with
  inputs for principal, annual interest rate, number of periods, and
  capitalisation frequency, displaying simple-interest value, compound-interest
  value, and cumulative interest, with a bar or line chart of value over time.
- **FR-018**: Module 6 MUST include an OJS function-family explorer allowing
  the student to select a function type (affine, quadratic, exponential,
  logarithmic) and adjust its parameters, with the graph updating to show
  domain, intercepts, and sense of variation.
- **FR-019**: Module 7 MUST include an OJS profit-maximisation simulator where
  the student moves a quantity slider to observe total revenue, total cost, and
  profit, then compares the observed maximum to the derivative-based optimum.
- **FR-020**: Module 8 MUST include a static mixed-method challenge in its
  Interactive Exploration section, presenting six to eight unlabelled problems
  drawn from across Modules 1–7. Each problem MUST use a single collapsible
  `.callout-caution` block that reveals both the method label and the full
  worked solution together. The section MUST prompt the student to identify the
  appropriate method before expanding. No OJS reactive code is used; this
  section is static.

**Course entry point (`index.qmd`):**

- **FR-021**: `index.qmd` MUST include a **Welcome** callout at the top of the
  page summarising what the course enables students to do (five bullet points).
- **FR-022**: `index.qmd` MUST include a **Start Here** numbered section with
  five preparation steps, each linking to a real resource page (syllabus,
  learning guide, diagnostic activity, glossary, formula sheet).
- **FR-023**: `index.qmd` MUST include a **How to study each module** tip
  callout describing the six-step module learning sequence (Diagnose →
  Understand → Observe → Practise → Experiment → Apply).
- **FR-024**: Each module entry in the Course Roadmap MUST retain its existing
  topic-list description AND add a bolded application question immediately
  after the topic list, contextualising the module's relevance to economics,
  finance, or management. The application question MUST NOT replace the topic
  list.
- **FR-025**: `index.qmd` MUST include a **Learning Progress** checklist with
  one tick-box entry per module that students can use to track their progress.

**Supporting reference pages:**

- **FR-026**: A `formula-sheet.qmd` MUST be created, organised by module
  (Modules 1–7), listing only the formulas students invoke directly when
  solving problems (applied formulas) — approximately one to four formulas per
  module, totalling roughly 20–25 entries across the sheet. Intermediate
  algebraic properties (fraction rules, power laws, notable identities as
  definitions) are excluded; they are covered in module theory sections and the
  glossary. Each entry MUST include the formula in LaTeX and a one-sentence
  plain-language description of what it computes.
- **FR-027**: A `learning-guide.qmd` MUST be created, providing: how to
  prepare for each module, the recommended study sequence for a single session,
  guidance on maintaining an error log (what to record, how to use it), and a
  suggested weekly revision schedule across the eight-module course.
- **FR-028**: Both `formula-sheet.qmd` and `learning-guide.qmd` MUST be
  registered in the course sidebar in `_quarto.yml`.

**Constitution compliance:**

- **FR-029**: All new sections MUST use the callout semantics defined in the
  constitution: `.callout-note` for definitions, `.callout-tip` for key
  formulas and shortcuts, `.callout-warning` for common errors and caveats,
  `.callout-important` for exam-critical rules, `.callout-caution` for
  exercises (with `collapse="true"` for solutions).
- **FR-030**: All mathematics in new and revised sections MUST use LaTeX
  (`$...$` inline, `$$...$$` display). Any residual Unicode or HTML math
  notation encountered during restructuring MUST be converted.
- **FR-031**: This feature MUST deliver a proposed amendment to
  `.specify/memory/constitution.md`, updating principle T-IV to read
  "interactive demo (Shinylive Python or Observable JS)" in place of
  "Shinylive interactive demo", so that OJS-based simulations satisfy the
  constitution for future audits. The amendment MUST follow the constitution's
  governance rules (version bump to 1.5.1 PATCH, rationale recorded, date
  updated).

### Key Entities

- **Module**: One of eight lesson pages; the entity gains a standardised set
  of twelve sections through this feature.
- **Interactive Simulation**: A reactive widget (OJS or Shinylive Python)
  embedded in a module's Interactive Exploration section; inputs are sliders
  or selects, outputs are computed values or charts, and follow-up questions
  accompany it.
- **Formula Sheet**: A single-page reference listing every named formula across
  Modules 1–7, organised by module, with LaTeX notation and plain-language
  labels.
- **Learning Guide**: A single-page study-skills document covering preparation,
  the module study sequence, error-log practice, and revision scheduling.
- **Course Entry Page** (`index.qmd`): The syllabus/home page; gains a welcome
  callout, a "Start Here" section, a learning-sequence tip, enriched module
  descriptions with application questions, and a progress checklist.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All eight modules contain the twelve required sections in the
  correct order — 8 of 8 modules fully templated.
- **SC-002**: Modules 1–7 each contain a functional OJS simulation matched to
  the module's key concept (7 of 7 simulations present); Module 8 contains a
  static mixed-method challenge in place of a reactive simulation.
- **SC-003**: Every interactive simulation is followed by at least two
  interpretation questions — 0 simulations left without follow-up questions.
- **SC-004**: Every module's Guided Practice section exposes a hint callout
  before the solution callout — 0 modules where only a solution callout exists
  without a preceding hint.
- **SC-005**: `index.qmd` contains all five required elements: welcome callout,
  Start Here section, learning-sequence tip, application questions per module,
  and progress checklist.
- **SC-006**: `formula-sheet.qmd` lists formulas for all seven content modules
  (Modules 1–7) — 0 modules missing from the reference.
- **SC-007**: `learning-guide.qmd` exists and contains all four required
  subsections: preparation guidance, study sequence, error-log instructions,
  and revision schedule.
- **SC-008**: Both `formula-sheet.qmd` and `learning-guide.qmd` appear in the
  course sidebar registration in `_quarto.yml`.
- **SC-009**: The site renders with zero build errors after all changes — exit
  code 0 from `quarto render`.
- **SC-010**: A student can follow the Continue link from Module 1 through to
  Module 8 without encountering a missing link or placeholder page.
- **SC-011**: `.specify/memory/constitution.md` version is bumped to 1.5.1
  (PATCH) and T-IV wording is updated to include Observable JS as an accepted
  interactive technology alongside Shinylive Python.

## Assumptions

- The eight-module structure and all existing content (theory, worked examples,
  and exercises) are preserved; this feature restructures around existing
  content, not replaces it.
- OJS reactive simulations are used for all eight modules because they run
  entirely client-side with no CDN package loading, consistent with both the
  static GitHub Pages hosting model and the privacy-first constitution (IV).
  Shinylive Python is not used for any of the eight interactive simulations
  in this feature. This departs from constitution T-IV (which currently
  mandates Shinylive); the departure is justified by privacy constraints and
  resolved by the constitution amendment in FR-031.
- Module 1 is restructured first to validate the template; Modules 2–7 follow
  in sequence; Module 8 is authored last.
- The `specify-2.md` research document provides the canonical OJS code
  patterns for Modules 1–5; Modules 6–7 follow the same pattern adapted to
  their key concepts.
- The course is authored in English throughout (per spec-004); this feature
  does not introduce French-language content or stubs (bilingual parity for
  the teaching materials is tracked in a separate initiative).
- The formula sheet lists applied formulas only (approximately 20–25 entries
  total, one to four per module, Modules 1–7). Intermediate algebraic
  properties and definitional rules are excluded. Module 8 adds no new
  formulas.
- The learning guide is a static, prose-based page with no interactive
  components.
- `_quarto.yml` is the single source of truth for navigation (constitution
  II); any new pages must be registered there.
