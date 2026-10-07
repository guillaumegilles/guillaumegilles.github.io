# Feature Specification: Data Description — 10-Module Redesign

**Feature Branch**: `010-data-description-10-modules`

**Created**: 2026-10-06

**Status**: Draft

**Input**: User description: "Build specification based on
`teaching/data-description/brainstorm-10-modules.md`. The 7 open design
questions are answered; there is still a lot to work on, as the unmarked
next steps suggest."

## Overview

The Data Description course (`teaching/data-description/`, MS03-001-G)
currently ships as 12 session pages (`session-01.qmd` … `session-12.qmd`,
specified in `specs/005-data-description-course/`). The first two sessions
are a stand-alone Excel block; the rest cover descriptive statistics.

This feature **supersedes the 12-session structure of feature 005** with
**10 modules of 3 hours each (30 h total)** for **2nd-year business-school
students**. The redesign is driven by a brainstorm document and seven
design decisions made by the course owner:

| # | Decision | Consequence for this spec |
|---|---|---|
| 1 | Excel is a **woven** skill, not a dedicated block | No Excel-only module; each module introduces the spreadsheet skills its statistics need |
| 2 | Kurtosis is **conceptual only** | No kurtosis formula or Excel function is required |
| 3 | Weighted mean stays **inside Module 4** | No separate enrichment page |
| 4 | Time series / index numbers are **left for the next course** | Out of scope; Module 10 only signposts them |
| 5 | **All-English** course; French translation added once the course is complete | English is the only authored language in this feature |
| 6 | Interactive demos only for the **hardest visualisations** | Demos are required for a short list of modules, not every module |
| 7 | **Add a second franchise** and **expand the dataset** (more variables, more days) for M8–M10 | A new, larger running dataset is a deliverable |

The running case study **"The Wandering Fork"** (a fictional food-truck
business) is retained, with original invented data. The course remains
Excel-based for computation.

### Module plan

| M | Title | Main OpenStax IBS 2e reference |
|---|---|---|
| 1 | What is statistics? Data types and measurement | Ch. 1 |
| 2 | Organising qualitative data: frequency tables and charts | Ch. 2 (§2.1–2.2) |
| 3 | Organising quantitative data: histograms and cumulative curves | Ch. 2 (§2.2) |
| 4 | Measures of central tendency (incl. weighted mean) | Ch. 2 (§2.3) |
| 5 | Measures of position: quartiles, percentiles, boxplot | Ch. 2 (§2.3–2.4) |
| 6 | Measures of dispersion: variance, standard deviation, CV | Ch. 2 (§2.7) |
| 7 | Shape of distributions: skewness (kurtosis conceptual) | Ch. 2 (§2.6) |
| 8 | Bivariate analysis I: contingency tables and scatter plots | Ch. 2 (§2.5), Ch. 13 (§13.1) |
| 9 | Bivariate analysis II: covariance, correlation, regression | Ch. 13 (§13.1–13.4) |
| 10 | Synthesis, review, and mock exam | Ch. 2 and Ch. 13 review |

The OpenStax section numbers above come from the brainstorm and MUST be
verified against the actual PDF during planning (see Assumptions).

### Mapping from the current 12 sessions

| Current session | Destination |
|---|---|
| S1 Excel I (cell referencing, basic functions) | Woven into M1 and M2 |
| S2 Excel II (sorting, PivotTables, PivotCharts) | Woven into M2, M3 and M8 |
| S3 Qualitative graphical | M2 |
| S4 Quantitative graphical | M3 |
| S5 Position indicators | M5 |
| S6 Central tendency | M4 |
| S7 Dispersion | M6 |
| S8 Shape | M7 |
| S9 Univariate synthesis | End of M7 (short synthesis) |
| S10 Bivariate graphical | M8 |
| S11 Bivariate numerical | M9 |
| S12 Bivariate synthesis and mock exam | M10 |

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Student completes one module end to end (Priority: P1)

A 2nd-year business student opens a module page and, in one 3-hour
sitting, reads a business question, learns the concept, follows a worked
example on the Wandering Fork data, reproduces it in Excel, and checks
their own work against collapsible solutions.

**Why this priority**: A single complete module is the smallest unit that
delivers teaching value and is the template for the other nine.

**Independent Test**: Take any one finished module. A student with the
prerequisites can reach every module learning objective using only that
page, the shared dataset, and the linked resources, in about 180 minutes.

**Acceptance Scenarios**:

1. **Given** a module page, **When** a student reads it top to bottom,
   **Then** they meet in order: a business question, learning objectives,
   theory, worked examples, an Excel section, and exercises with
   collapsible solutions.
2. **Given** a formula in the theory section, **When** the student reads
   it, **Then** a plain-language sentence explains what it computes and
   why a manager would care.
3. **Given** the Excel section, **When** the student follows it step by
   step on the shared dataset, **Then** they obtain the same numbers as
   the worked example.
4. **Given** the exercises, **When** the student attempts one before
   expanding its solution, **Then** both a by-hand and an in-Excel
   variant are available for each module's core skill.

---

### User Story 2 - Student follows the whole course on one running case (Priority: P2)

A student works through Modules 1 to 10 in order. Results from earlier
modules (frequency tables, mean, standard deviation) are reused later, and
the second franchise lets them compare two businesses in the bivariate
and synthesis modules.

**Why this priority**: Continuity across modules is what turns ten
lessons into a course, but it requires the P1 module template first.

**Independent Test**: Starting from the dataset alone, a student can
reproduce every number quoted in any module, and the numbers quoted in
later modules are consistent with those in earlier ones.

**Acceptance Scenarios**:

1. **Given** the shared dataset, **When** a student recomputes any
   statistic quoted in any module, **Then** it matches the published
   value.
2. **Given** Module 8, 9 or 10, **When** the student reads the exercises,
   **Then** they compare the two franchises on at least one qualitative
   and one quantitative relationship.
3. **Given** a module that reuses an earlier result, **When** the student
   follows the cross-reference, **Then** it leads to the module that
   defined that result.

---

### User Story 3 - Student prepares for exams with Module 10 (Priority: P2)

Near the end of the course, a student uses Module 10 to run a complete
descriptive analysis on a fresh dataset and sit an original mock exam in
the same format as the real exams (MCQ plus short answer).

**Why this priority**: The mock exam is the course's main self-assessment
tool and the one place all modules come together.

**Independent Test**: A student who has not read Modules 1 to 9 in detail
can still identify, from the mock exam solutions, which module to revise
for each question they missed.

**Acceptance Scenarios**:

1. **Given** the mock exam, **When** the student completes it in the
   allotted time, **Then** every item has a worked solution and points to
   the module that teaches the underlying skill.
2. **Given** the synthesis walkthrough, **When** the student follows it,
   **Then** it covers variable typing, frequency tables, charts,
   position, centre, dispersion, shape, and the bivariate steps in a
   sensible order.
3. **Given** the common-pitfalls list, **When** the student reads it,
   **Then** it includes at least: unequal-width histogram heights,
   $n$ versus $n-1$, correlation versus causation, and $r$ versus $R^2$.

---

### User Story 4 - Instructor migrates from 12 sessions to 10 modules safely (Priority: P3)

The instructor needs the new structure to replace the old one without
losing canonical theory, worked examples or exercises, without leaving
dead links, and without publishing a half-finished course.

**Why this priority**: It protects existing work, but only matters once
modules exist.

**Independent Test**: Compare the old session pages with the new modules
using the mapping table: every canonical item is either present in its
destination module or listed as deliberately dropped with a reason.

**Acceptance Scenarios**:

1. **Given** the old session pages, **When** the migration is complete,
   **Then** a content-fidelity record shows where each theory block,
   worked example and exercise went (or why it was dropped).
2. **Given** the site navigation, **When** the migration is complete,
   **Then** the sidebar lists exactly the syllabus, 10 modules and the
   glossary, and no old session page remains reachable.
3. **Given** the course is not finished, **When** the site is built,
   **Then** unfinished pages are not publicly visible.

---

### User Story 5 - Student finds the right outside resource (Priority: P3)

A student who is stuck on a concept wants a free video or chapter that
covers it, without hunting through a textbook or a video library.

**Why this priority**: Supplementary resources improve the course but do
not block it.

**Independent Test**: From any module page, a student reaches a relevant
textbook chapter and Khan Academy lesson in one click each.

**Acceptance Scenarios**:

1. **Given** a module page, **When** the student opens its further
   reading section, **Then** it lists the matching OpenStax section(s)
   and Khan Academy lesson(s) with a short note on what each covers and
   its approximate duration.
2. **Given** a listed external link, **When** the student follows it,
   **Then** it leads to the intended lesson.

---

### Edge Cases

- **Time budget error in the brainstorm.** The brainstorm's budget table
  totals 120 min per module (20 h overall), not 180 min (30 h). This spec
  uses a corrected 180-min budget (see FR-004); the brainstorm table must
  not be treated as authoritative.
- **Existing worked examples assume 30 days.** Hand computation on 30
  observations is a feature (quartiles, grouped tables). The expanded
  dataset MUST still offer a 30-day subset so existing examples remain
  valid and hand-computable.
- **Students with no Excel experience.** With Excel woven in, Module 1 and
  2 MUST give a self-contained "first steps" path so a beginner is not
  lost before the first function.
- **French Excel locale.** Students may run a French-locale Excel;
  function names differ. The existing English/French function list MUST
  stay available and be linked from every Excel section.
- **Quartile conventions.** Excel offers inclusive and exclusive quartile
  functions that give different values on small samples. The course MUST
  state which one it uses and warn that textbook and Excel values can
  differ.
- **Population versus sample notation.** Descriptive course, but
  Excel exposes `.P` and `.S` variants. The course MUST explain which is
  used and why, without developing inference.
- **Mid-migration state.** The working tree currently holds a
  `module-01.qmd` that still contains the old Session 3 title and
  content, and the glossary and Excel function list have been moved into
  `modules/`. Planning MUST reconcile these rather than assume a clean
  start.
- **Partial delivery.** If only some modules are finished, none are
  published until the whole course is complete.
- **No-reproduction rule.** Khan Academy and OpenStax content MUST be
  linked and summarised, never copied wholesale, and OpenStax material
  that is reused MUST be attributed under its licence.

## Requirements *(mandatory)*

### Functional Requirements

**Structure and scope**

- **FR-001**: The course MUST consist of exactly 10 modules, in the order
  and with the titles in the Module plan above, plus a syllabus and a
  glossary.
- **FR-002**: Each module MUST be designed for 180 minutes of contact
  time, and the course total MUST be 1,800 minutes (30 hours).
- **FR-003**: The course MUST cover descriptive statistics only. Time
  series, index numbers, probability distributions, and inferential
  methods MUST NOT be taught; Module 10 MUST signpost time series as
  "next course" content.
- **FR-004**: Each module MUST specify a time budget summing to 180
  minutes across theory, Excel lab and exercises. Module 10 MUST reserve
  at least 90 minutes for the mock exam and debrief.

**Module content template**

- **FR-005**: Every module MUST open with a business question and a list
  of measurable learning objectives.
- **FR-006**: Every module MUST present theory first, then worked
  examples, then exercises with collapsible solutions, in that order.
- **FR-007**: Every formula MUST be paired with a plain-language
  explanation of what it computes and why it matters in business.
- **FR-008**: Every module MUST include at least one collapsible
  derivation or step-by-step justification of its central formula or
  concept.
- **FR-009**: Wherever a concept has a geometric or visual reading
  (variance as squared distance, correlation as direction of
  association, regression as best-fit line), it MUST be shown.
- **FR-010**: Every module MUST include an Excel section listing the
  exact English-locale functions and menu steps used, with a link to the
  English/French function reference.
- **FR-011**: Every module MUST offer, for its core skill, both a by-hand
  exercise and an in-Excel exercise.
- **FR-012**: Every module MUST end with a "Further reading" section that
  lists matching OpenStax IBS 2e section(s) and Khan Academy lesson(s),
  each with a one-line note and approximate duration.
- **FR-013**: Every module MUST define its new symbols and terms in the
  glossary, with notation, a plain definition, and — for Greek letters —
  a pronunciation guide.

**Module-specific content**

- **FR-014**: Excel skills MUST be introduced in the module where the
  statistics first need them, following the plan: spreadsheet basics and
  variable typing in M1; counting functions and basic charts in M2;
  binning, histograms and PivotTable grouping in M3; central-tendency
  functions in M4; quartile and boxplot tools in M5; variance and
  standard-deviation functions in M6; skewness in M7; cross-tabulation
  and scatter charts in M8; correlation and regression in M9.
- **FR-015**: Module 1 MUST cover: descriptive versus inferential
  statistics, population versus sample, variable types, and the four
  levels of measurement, and MUST introduce the running dataset.
- **FR-016**: Module 3 MUST teach unequal-width class histograms using
  density, and MUST explain the half-open class convention.
- **FR-017**: Module 4 MUST cover arithmetic mean, grouped mean, weighted
  mean, median, mode, and when each is appropriate, including the effect
  of skewness and outliers.
- **FR-018**: Module 5 MUST cover quartiles, percentiles, IQR, the
  five-number summary, the 1.5 × IQR outlier rule, boxplot construction
  and reading, and side-by-side boxplots for group comparison.
- **FR-019**: Module 6 MUST cover range, variance and standard deviation
  (population and sample), grouped variance, and coefficient of
  variation, and MUST show how to compare the risk of two businesses.
- **FR-020**: Module 7 MUST cover symmetric, right-skewed and left-skewed
  shapes, the ordering of mean, median and mode, at least one skewness
  coefficient, and a **conceptual-only** treatment of kurtosis (names and
  pictures; no formula, no Excel function). Module 7 MUST end with a
  short consolidated univariate review on the Wandering Fork dataset.
- **FR-021**: Module 8 MUST cover contingency tables (joint, marginal and
  conditional frequencies), reading dependence from conditional profiles,
  and scatter plots (direction, strength, form, outliers). Formal
  independence tests MUST NOT be taught.
- **FR-022**: Module 9 MUST cover covariance, Pearson correlation,
  "correlation is not causation", the least-squares line, interpretation
  of slope and intercept, $R^2$, and the limits of extrapolation, and
  MUST include reading a regression output table.
- **FR-023**: Module 10 MUST contain a full descriptive-analysis
  walkthrough on a fresh dataset, a common-pitfalls review, and an
  original mock exam mixing MCQ and short-answer items with worked
  solutions mapped back to modules.

**Running case and data**

- **FR-024**: The course MUST provide one shared, downloadable dataset
  for the Wandering Fork that extends the current one with (a) a second
  franchise, (b) more observed days, and (c) additional variables beyond
  the current eight columns, covering both qualitative and quantitative
  types, discrete and continuous.
- **FR-025**: The dataset MUST support every worked example and exercise
  in Modules 1 to 10, including at least one qualitative–qualitative
  pair and one quantitative–quantitative pair per franchise for Modules 8
  and 9, and a clear skewed variable for Module 7.
- **FR-026**: The dataset MUST include a 30-day subset suitable for hand
  computation, and every figure quoted in the modules MUST be
  reproducible from the published dataset.
- **FR-027**: The dataset MUST be entirely invented (no proprietary or
  real personal data), documented with a data dictionary stating each
  variable's name, type, unit and meaning.
- **FR-028**: Exercises on Modules 8 to 10 MUST compare the two
  franchises on at least one relationship each.
- **FR-029**: A secondary small dataset MAY be used where a module needs
  a clearly skewed or outlier-driven example (for example, a payroll
  list) not available in the main dataset.

**Interactive demonstrations**

- **FR-030**: The following concepts MUST have an interactive
  demonstration: histogram bin width (M3), boxplot construction from
  quartiles (M5), and scatter plot with fitted regression line (M9).
- **FR-031**: Other modules MAY include an interactive demonstration; any
  priority concept lacking one MUST be marked with a visible `TODO`
  notice so gaps are trackable.
- **FR-032**: Every demonstration MUST work without sign-in, without
  tracking, and on the shared dataset.

**Course shell, navigation and publishing**

- **FR-033**: The course MUST have a syllabus page that lists all 10
  modules with links, learning objectives, assessment, personal-work
  volume, and a Recommended Literature section.
- **FR-034**: Recommended Literature MUST add *Introductory Business
  Statistics, 2e* (OpenStax) and the Khan Academy Statistics and
  Probability course, each with author or provider, title, edition and
  publisher or source.
- **FR-035**: The syllabus MUST keep the existing curriculum placement
  statement (follows MS01 and MS02, precedes MS04) and the assessment
  scheme (midterm 35%, final 65%), updated to name the modules each exam
  covers.
- **FR-036**: The course sidebar MUST list the syllabus first, then the
  10 modules grouped into logical parts, then the glossary, and MUST
  contain no other pages.
- **FR-037**: All 10 modules, the syllabus changes, and the dataset page
  MUST stay hidden from the public site until the entire course is
  complete, then be published together.
- **FR-038**: The course MUST be authored in English only. French
  parity is explicitly deferred to a later feature, and this deviation
  MUST be recorded rather than silently dropped.

**Migration and fidelity**

- **FR-039**: A content-fidelity record MUST map every canonical theory
  block, worked example and exercise from the 12 old session pages to
  its place in the new modules, or mark it as deliberately dropped with
  a reason.
- **FR-040**: After migration, the 12 old session pages and their
  navigation entries MUST be gone, and no page may be orphaned or
  unreachable from the sidebar.
- **FR-041**: Cross-references between modules and to the glossary MUST
  resolve; no link may point to a removed session page.
- **FR-042**: The migration MUST reconcile the current partial state
  (the Session-3-titled `module-01.qmd`, the relocated glossary, and the
  relocated Excel function list) so there is one module file per module
  number and one glossary.

**Quality of external references**

- **FR-043**: Every Khan Academy and OpenStax reference MUST be checked
  at authoring time against the live Khan Academy site and the supplied
  PDF; references that cannot be verified MUST be removed or flagged.
- **FR-044**: Reused OpenStax material, if any, MUST carry attribution
  consistent with its licence.

### Key Entities *(include if feature involves data)*

- **Module**: One 3-hour teaching unit with a title, business question,
  objectives, theory, worked examples, Excel section, exercises, time
  budget, and further reading.
- **Running dataset**: Daily observations for two franchises, with
  qualitative and quantitative variables, plus a 30-day hand-computable
  subset and a data dictionary.
- **Franchise**: One food-truck business within the dataset; the unit of
  comparison in Modules 8 to 10.
- **Exercise**: A question with a collapsible solution, marked by-hand or
  in-Excel and tied to a module learning objective.
- **Mock exam**: An original set of MCQ and short-answer items with
  solutions that point back to modules.
- **Further-reading entry**: A pointer to an OpenStax section or Khan
  Academy lesson with a short note and duration.
- **Glossary entry**: A symbol or term with notation, definition and,
  for Greek letters, pronunciation.
- **Fidelity record**: The mapping of old session content to new module
  content, including deliberate drops.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The course totals exactly 10 modules and 1,800 planned
  minutes, and every module's time budget sums to 180 minutes.
- **SC-002**: 100% of modules contain all of: business question,
  learning objectives, theory, worked example, Excel section, exercises
  with solutions, a collapsible derivation, and further reading.
- **SC-003**: 100% of statistics quoted in any module can be reproduced
  from the published dataset by a reviewer following the module's Excel
  steps.
- **SC-004**: 100% of canonical theory blocks, worked examples and
  exercises from the 12 old sessions appear in the fidelity record as
  either migrated or deliberately dropped with a reason.
- **SC-005**: At least 90% of students in a pilot group can complete a
  module's core by-hand and in-Excel exercises in the allotted exercise
  time.
- **SC-006**: At least 80% of pilot students score 60% or higher on the
  mock exam after finishing Modules 1 to 9.
- **SC-007**: Every module's further-reading section contains at least
  one OpenStax reference and one Khan Academy reference, and 100% of
  those references are verified valid on the date of publication.
- **SC-008**: The three required interactive demonstrations (M3, M5, M9)
  are present, and any other priority concept without a demo is marked
  with a `TODO` notice.
- **SC-009**: After publication, zero old session pages are reachable and
  zero internal links are broken.
- **SC-010**: A reviewer can navigate from the syllabus to any module,
  and to the glossary and function reference, in at most two clicks.
- **SC-011**: Beginners without prior Excel experience can complete
  Module 2's Excel lab in the allotted time using only the module page
  and the function reference.

## Assumptions

- **Audience**: 2nd-year business-school students who have completed
  MS01 and MS02 and have access to desktop Excel.
- **Replacement, not addition**: This feature supersedes the 12-session
  structure of feature 005 and its tasks; feature 005's decisions on the
  Wandering Fork name, original data, no-verbatim-source-exam rule, and
  mock-exam style are inherited unchanged.
- **Time-budget split**: The 180-minute split per module is a planning
  default (roughly 35% theory, 30% Excel lab, 35% exercises, with a short
  break inside any block); Module 10 is the exception. The per-module
  values are set in the plan.
- **Exams**: The midterm (45 min) and final (90 min) formats are
  unchanged; the midterm is assumed to cover Modules 1 to 5 and the final
  Modules 1 to 10, to be confirmed in the plan.
- **Dataset size**: The expanded dataset is assumed to hold on the order
  of 90 to 120 days per franchise; the exact count and variable list are
  design decisions for the plan, subject to FR-024 to FR-027.
- **Quartile convention**: The course picks one Excel quartile convention
  and documents it; the choice is made in the plan after checking it
  against the OpenStax method.
- **OpenStax section numbers**: The section mapping is taken from the
  brainstorm and has not been checked against the PDF; verification is
  planned work (FR-043).
- **Khan Academy links**: The brainstorm's lesson URLs were not verified
  and may have moved; verification is planned work (FR-043).
- **Site conventions**: The course follows the site's existing teaching
  standards (callout semantics, glossary, collapsible proofs, syllabus
  with literature, 80-character prose wrap, privacy-first demos) and
  stays hidden until complete, as in feature 005.
- **French**: A French version is a separate later feature; until then
  the constitution's EN/FR parity rule is knowingly not met for this
  course, as already accepted for features 004 and 005.
- **Out of scope**: Time series, index numbers, probability,
  inference, formal independence tests, kurtosis formulas, a standalone
  Excel module, and any new assessment format.
