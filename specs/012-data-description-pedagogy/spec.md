# Feature Specification: Concrete-to-Abstract Pedagogy — Data Description Course

**Feature Branch**: `012-data-description-pedagogy`

**Created**: 2026-10-13

**Status**: Draft

**Input**: User description: "Improve the pedagogical aspect of the
data-description course with a more concrete-to-abstract approach. For
example, one thing you can change is to move Excel lab to homework
exercises in order to give more room and time for deeper in-class
comprehension of concept and mathematical notation. Start with my next
class, which is module-06.qmd."

## Overview

The `teaching/data-description/` course (10 modules × 3 hours,
undergraduate business students) currently presents each concept in an
**abstract-first** order: a formal definition or formula callout comes
first, a plain-language paraphrase follows, and the concrete numbers only
appear later in the worked example on a 30-day dataset. Each 180-minute
module also spends 30–60 minutes on an in-class **Excel lab**, which
competes for time with understanding the concepts and the mathematical
notation — the part students find hardest and cannot easily learn alone.
The written exams (midterm and final) assess concepts, calculation by
hand and interpretation, not Excel operation.

This feature restructures the in-class part of each module around a
**concrete → visual → verbal → symbolic → general** progression:
students first work with a tiny, hand-computable example drawn from the
running "Wandering Fork" case, see it as a picture, describe it in
words, and only then meet the notation, which is decoded symbol by symbol
against the numbers they have just computed. The Excel lab moves out of
the classroom into a clearly marked **homework** section on each module
page, preserving every existing Excel exercise and solution, and the
freed in-class time is reallocated to concept construction, notation
fluency and by-hand practice.

**Module 6 — Dispersion** is the pilot and the first deliverable, because
it is the next class taught. The pattern established on Module 6 is then
captured as a reusable module template and rolled out to the other
modules.

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Student builds the idea of dispersion from concrete numbers in Module 6 (Priority: P1)

A student attends Module 6. Before any formula appears, the instructor
shows two Wandering Fork trucks with the **same mean** daily revenue over
a handful of days but visibly different day-to-day behaviour, and asks
which one is riskier to run. Using small, round numbers, the student
computes the range, then fills a **deviation table** column by column —
each day's distance from the mean, the discovery that these distances
always sum to zero, squaring to remove the signs, averaging with $n-1$,
and taking the square root to return to euros. Only after the table is
complete does the page name the symbols ($x_i$, $\bar{x}$, $n$,
$\sum$, $s^2$, $s$) and show the general formula, with each symbol
explicitly pointed back to a column of the table the student just filled.
The same concrete-first sequence is used for the coefficient of
variation ("is €137 of variation a lot?") and for the shortcut formula.
The full 30-day worked example then confirms the method on real-sized
data.

**Why this priority**: Module 6 is the next class to be taught; it
delivers immediate value and serves as the proof of concept for the
whole course. Variance and standard deviation are also the most
notation-heavy concepts in Part II and the foundation for Modules 7 and 9.

**Independent Test**: Read the revised Module 6 page from top to bottom
and confirm that, for range, variance/standard deviation, coefficient of
variation and the shortcut formula, a concrete numerical activity and a
visual appear *before* the corresponding formula callout, and that every
symbol in each formula is mapped to a concrete quantity already
computed. Can be taught as a stand-alone 3-hour session.

**Acceptance Scenarios**:

1. **Given** the revised Module 6 page, **When** a student reaches the
   first formula callout for sample variance, **Then** they have already
   computed every term of that formula by hand on a small dataset of at
   most 6 values with whole-number (or near-whole) arithmetic.
2. **Given** the deviation table activity, **When** the student sums the
   deviation column, **Then** the page prompts them to notice it equals
   zero and uses that observation to motivate both squaring and the
   $n-1$ denominator ("once $n-1$ deviations are known, the last one is
   forced").
3. **Given** the sample variance formula, **When** it is displayed,
   **Then** a "notation decoder" accompanies it that reads the formula
   aloud in plain words and links each symbol to a column or cell of the
   deviation table.
4. **Given** the existing worked example values for Harbour 30-day
   revenue (range 478.97, $s^2 = 18{,}793.33$, $s = 137.09$,
   $CV = 21.82\%$), **When** the module is revised, **Then** these
   values are unchanged and still appear in the worked example.
5. **Given** the end of the in-class part, **When** the student completes
   a short exit check (3–5 quick questions), **Then** the questions test
   concept and notation (e.g., "what does $s$ measure, in words?",
   "translate this formula into a sentence") rather than tool usage.

---

### User Story 2 — Student completes the Excel lab as homework (Priority: P1)

After class, the student opens the Module 6 page and finds a clearly
separated **Homework — Excel lab** section, placed after all in-class
content. It contains the Excel function reference for the module, the
three existing Excel exercises (Campus dispersion, shortcut formula with
`SUMSQ`, payroll skew) with their collapsible solutions, step-by-step
instructions sufficient to work alone, and an estimated completion time.
The homework explicitly asks the student to verify with Excel the values
they computed by hand in class, so Excel reinforces rather than replaces
the concept.

**Why this priority**: Moving the lab out of class is what frees the
time for User Story 1; the two must ship together for Module 6.

**Independent Test**: Confirm the Module 6 time plan contains no Excel
block, that every Excel exercise and solution present before the change
is present in the homework section, and that a student who missed class
could complete the homework using only the page and the dataset.

**Acceptance Scenarios**:

1. **Given** the revised Module 6 time plan, **When** the in-class blocks
   are summed, **Then** they total 180 minutes and contain 0 minutes of
   Excel lab.
2. **Given** the pre-change Module 6 page, **When** compared to the
   revised page, **Then** Exercises 4, 5 and 6 (Excel) and their solutions
   are all present, unchanged in substance, in the homework section.
3. **Given** the homework section, **When** a student reads it,
   **Then** it states an estimated completion time and how the homework
   is followed up at the start of the next module.
4. **Given** the following module, **When** class starts, **Then** a
   short homework debrief (≤ 10 minutes) is planned in its time plan.

---

### User Story 3 — Instructor reuses a concrete-to-abstract module template (Priority: P2)

The instructor (site owner) wants to apply the same approach to the next
modules without redesigning each one from scratch. A written module
template describes the in-class sequence (hook with a business question →
concrete mini-dataset activity → visual → plain-language statement →
notation decoder → general formula → worked example on the full dataset
→ by-hand practice → exit check), the homework section structure, and
the time-plan model. The course syllabus is updated so its description of
the module pattern and of personal work matches the new structure.

**Why this priority**: Makes the Module 6 pilot repeatable and keeps the
course consistent, but is not needed to teach Module 6 next class.

**Independent Test**: Hand the template to someone unfamiliar with the
course and confirm they can identify, for any module, which blocks are
in class, which are homework, and in what order the concrete and
abstract elements appear.

**Acceptance Scenarios**:

1. **Given** the template, **When** applied to a module, **Then** each
   core concept of that module has a concrete activity preceding its
   formal definition.
2. **Given** the updated syllabus, **When** a student reads the course
   description and the personal work section, **Then** they learn that
   Excel labs are homework and that the homework fits within the
   20-hour personal-work budget.

---

### User Story 4 — Remaining modules follow the same approach (Priority: P3)

Students experience the same concrete-to-abstract progression and
homework-based Excel labs in the other modules of the course, in the
order they will be taught.

**Why this priority**: Extends the benefit to the full course; each
module can be revised and released independently, ahead of its class.

**Independent Test**: For each revised module, apply the Module 6
acceptance checks (concrete before formula, notation decoder, no Excel
block in class, all Excel exercises preserved in homework).

**Acceptance Scenarios**:

1. **Given** the rollout scope agreed in the Assumptions, **When** a
   module in scope is revised, **Then** it passes the same acceptance
   scenarios as Module 6 (User Stories 1 and 2), adapted to its concepts.
2. **Given** Module 10 (synthesis and mock exam), **When** revised,
   **Then** its "replicate the walkthrough in Excel" block becomes
   homework and the mock exam and debrief remain in class.

---

### Edge Cases

- **Students without a computer at home**: the homework section must
  state that the Excel lab can be done on any device with a spreadsheet
  application or in a campus computer room, and no in-class activity may
  depend on the homework having been done (the debrief recaps it).
- **Students who skip the homework**: in-class content and the written
  exams do not require Excel, so missing homework does not block
  understanding of the next module; the debrief briefly restates the
  key result.
- **Concrete example numbers that do not divide nicely**: the mini-dataset
  must be chosen so that the mean, deviations and $s^2$ are computable by
  hand in under 5 minutes; if the true Wandering Fork values are not
  hand-friendly, a clearly labelled simplified extract (rounded values)
  is used and linked back to the real data in the worked example.
- **Concept already defined in an earlier module** (e.g., IQR in Module
  5): it is recalled briefly on the concrete data rather than rebuilt
  from scratch.
- **Concepts without a natural geometric picture**: the visual step may
  be a table or a number line; it is never skipped silently.
- **Rounding drift in the shortcut formula**: the existing warning about
  keeping the mean unrounded is preserved and illustrated on the concrete
  example.

## Requirements *(mandatory)*

### Functional Requirements

**Module 6 in-class content (pilot)**

- **FR-001**: Module 6 MUST open with a concrete business hook comparing
  two cases with the same mean but different spread, before any
  definition or formula.
- **FR-002**: For each core concept of Module 6 — range, interquartile
  range (recall), sample variance and standard deviation, coefficient of
  variation, shortcut formula — a concrete numerical activity MUST
  precede the formal definition or formula callout.
- **FR-003**: Module 6 MUST include a deviation table on a mini-dataset
  of at most 6 values with columns for $x_i$, $x_i-\bar{x}$ and
  $(x_i-\bar{x})^2$, and a total row, that students complete by hand.
- **FR-004**: The page MUST use the observation that deviations sum to
  zero to motivate squaring and the $n-1$ denominator, in plain language,
  before the formal "Why $n-1$" remark.
- **FR-005**: Every formula callout in Module 6 MUST be accompanied by a
  notation decoder that (a) reads the formula aloud in words and (b) maps
  each symbol to a quantity in the concrete activity.
- **FR-006**: Module 6 MUST include at least two short in-class
  notation exercises: one "formula → words" and one "words → formula"
  (including reading or writing $\sum$ notation).
- **FR-007**: Module 6 MUST end its in-class part with an exit check of
  3–5 quick questions on concept and notation, with collapsible answers.
- **FR-008**: Module 6's time plan MUST total 180 minutes, contain no
  Excel lab block, and show the time allocated to concrete activities,
  notation, worked example, by-hand practice and exit check.

**Module 6 homework**

- **FR-009**: Module 6 MUST contain a clearly titled homework section,
  placed after all in-class content, holding the module's Excel function
  reference and all Excel exercises with collapsible solutions.
- **FR-010**: The homework section MUST state an estimated completion
  time and include at least one task that verifies in Excel a value
  computed by hand in class.
- **FR-011**: The homework section MUST indicate how it is followed up
  (debrief at the start of the next module).

**Content fidelity and course standards**

- **FR-012**: No existing theory, worked example, derivation, interactive
  demo, exercise or solution MAY be removed; content may be reordered,
  reworded, or moved between in-class and homework sections.
- **FR-013**: Each revised module MUST keep the course's didactic order
  of theory → worked example → exercises with collapsible solutions; the
  concrete activities live inside the theory section and introduce each
  concept before it is used.
- **FR-014**: Each revised module MUST keep at least one collapsible
  derivation and its interactive demo, and MUST surface the visual
  interpretation of its central concept (for Module 6: variance as
  average squared distance from the mean).
- **FR-015**: Any new symbol introduced (e.g., a name for a deviation)
  MUST be added to the course glossary; no notation beyond the course
  syllabus MAY be introduced without a plain-language explanation.
- **FR-016**: Highlighted blocks MUST keep the course's visual semantics
  (definitions, formulas, warnings, exercises), and each new element
  (concrete activity, notation decoder, exit check, homework) MUST use
  one consistent visual treatment across all revised modules.

**Template, syllabus and rollout**

- **FR-017**: A reusable module template MUST document the in-class
  sequence, the homework section structure and the time-plan model, using
  Module 6 as the reference example.
- **FR-018**: The course syllabus MUST be updated so that its description
  of the module pattern, its learning objectives and its personal-work
  section reflect that Excel labs are homework.
- **FR-019**: The module following each revised module MUST include a
  homework debrief of at most 10 minutes in its time plan.
- **FR-020**: The rollout MUST cover Modules 7 to 10 (still to be taught
  this term), in teaching order; Modules 1–5 (already taught) MAY be
  revised later as a separate, lower-priority pass.

**Bilingual parity (Constitution VI)**

- **FR-021**: Every English Data Description page under
  `teaching/data-description/modules/` MUST have a French counterpart at
  the mirrored path under `fr/`. Until it is translated, that counterpart
  is a stub in French with a "translation in progress" notice and a link
  to the English page, and the stubs are reachable from a French course
  navigation. Translating the content is out of scope.

### Key Entities

- **Module page**: one 3-hour session; contains an in-class part
  (hook, theory with concrete activities, worked example, by-hand
  exercises, exit check) and a homework part (Excel lab).
- **Concrete activity**: a short, hand-computable task on a mini-dataset
  (≤ 6 values) drawn from or simplified from the Wandering Fork case,
  placed before a concept's formal definition.
- **Notation decoder**: a plain-language reading of a formula that links
  each symbol to a quantity in the concrete activity.
- **Exit check**: 3–5 quick concept/notation questions closing the
  in-class part.
- **Homework — Excel lab**: Excel function reference, Excel exercises
  with solutions, estimated time, and follow-up mention.
- **Module template**: the documented pattern applied to every revised
  module.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In revised modules, 0 minutes of in-class time are
  allocated to Excel lab, and 100% of the former Excel-lab minutes are
  reallocated to concrete activities, notation work and by-hand practice
  (Module 6: at least 45 minutes; Module 10: its former 30 minutes).
- **SC-002**: In revised Module 6, 100% of formula callouts are preceded
  by a concrete activity and accompanied by a notation decoder.
- **SC-003**: 100% of the Excel exercises and solutions existing before
  the change are still available in the revised modules (none lost).
- **SC-004**: At the Module 6 exit check, at least 80% of students can
  explain in one sentence what the standard deviation measures, and at
  least 70% can compute the sample variance of a 5-value dataset by hand.
- **SC-005**: A student can complete each module's Excel homework in at
  most 60 minutes, keeping total homework within the 20-hour
  personal-work budget stated in the syllabus.
- **SC-006**: On the final exam, the share of students making the
  "common mistakes" listed in Module 6 (wrong denominator, forgetting the
  square root, comparing standard deviations across units) is lower than
  in the previous cohort, as judged by the instructor.

## Assumptions

- **Rollout scope**: Module 6 is delivered first (before the next class);
  Modules 7–10 follow in teaching order; Modules 1–5, already taught this
  term, are out of scope for this feature and may be revised later.
- **Exams are unchanged**: the midterm and final remain written with an
  MCQ component and do not assess Excel operation, so moving Excel to
  homework does not affect assessment.
- **Students bring calculators** to class; no computer is needed in class
  once the Excel lab is moved to homework. The instructor may still show
  a brief (≤ 5 minutes) Excel verification on screen, which is not a lab.
- **Homework is self-checked** via the collapsible solutions and the
  next-module debrief; it is not graded.
- **Homework stays on the module page** (separate section) rather than on
  a separate page, so navigation and sidebar registration are unchanged.
- **Dataset values are unchanged**: the Wandering Fork dataset and the
  verified statistics from the previous feature
  (`specs/010-data-description-10-modules/`) remain the reference; any
  hand-friendly mini-dataset is a labelled simplification.
- **Language and translation**: modules are authored in English. French
  stub pages are in scope (FR-021) to satisfy Constitution VI; full
  French translation of the modules is out of scope. The existing French
  course index stub is kept and also gets the link to the English
  version.
- **Pedagogical basis**: the approach follows the
  concrete–pictorial–abstract progression and the principle of
  introducing notation only after the idea it names is understood.
