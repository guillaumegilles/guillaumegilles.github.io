# Feature Specification: Data Description Course (MS03-001-G)

**Feature Branch**: `005-data-description-course`

**Created**: 2026-09-12

**Status**: Draft

**Input**: User description: "@teaching/data-description/ — the directory contains resources already to inspire and build upon it. Design a thorough specification to develop the course."

## Overview

`teaching/data-description/` currently contains only a `ressources/`
subdirectory with three exported Moodle course archives (a 2024/25 French
run, a 2024/25 English run, and a newer block-structured bilingual export)
plus bilingual syllabus files (`syllabus-en.qmd`, `syllabus-fr.qmd`). No
Quarto course pages exist yet. This is the ESSCA **MS03-001-G "Data
description"** course: a 30-hour, 4-ECTS, Semester-3 seminar that teaches
the first stage of data analysis — numerical summaries and graphical
representation of data — as the direct successor to
`teaching/mathematical-fundamentals/` (MS01) and `teaching/mathematical-analysis/`
(MS02), and the direct prerequisite to `teaching/decision-making-stat/` (MS04,
Inferential Statistics), which already exists on the site and even
references "Data Description" as a refresher in its own Session 6.

The source archives show a stable pedagogical structure across all three
Moodle exports and both syllabus languages: **Excel Fundamentals** (2
sessions, 6h) → **Univariate Data Treatment** (graphical representation,
position indicators, central tendency/dispersion/asymmetry indicators — 3
sessions, 18h) → **Bivariate Data Treatment** (2 sessions, 6h). The
legacy Moodle exports additionally enumerate 12 individually numbered
teaching sessions (Session 1–12), each with animation slides, a written
summary, exercises (with/without solutions), practical-work Excel
workbooks, and — from Session 3 onward — a running case study
("Study case – Missions – Session N") that supplies the dataset used
for graphical, positional, dispersion, and bivariate exercises across
the rest of the course. This feature reuses that case study's business
scenario and pedagogical structure but not its proprietary figures: the
running case is renamed **"The Wandering Fork"** and re-authored with
original, invented data (see Clarifications). Assessment is a Midterm Exam
(35%, 45 min) and a Final Exam (65%, 90 min), both individual written
exams with an MCQ component, plus 20h of personal work per the syllabus.

This feature delivers a **complete, coherent, English-language Quarto
course** under `teaching/data-description/`, faithfully derived from
these source archives and syllabi, structured as a syllabus
(`index.qmd`), a glossary (`glossary.qmd`), and 12 session pages
(`session-01.qmd` … `session-12.qmd`) grouped into three parts, following
the same authoring conventions already established by the sibling
courses `teaching/mathematical-fundamentals/` and `teaching/decision-making-stat/`
and required by the project constitution.

## Clarifications

### Session 2026-09-12

- Q: Should the spec's references to the sibling course use the new
  path `teaching/decision-making-stat/`, or does the on-disk rename
  from `teaching/essca-stat/` not reflect a final decision yet? → A:
  **The rename is final.** All references in this spec use
  `teaching/decision-making-stat/` (the current on-disk name, front
  matter title "Decision Making Statistics — S04"); its Session 6 is
  still the "Data Description" refresher referenced by FR-016 and the
  Edge Cases below.
- Q: Should the course reproduce the exact figures/text of ESSCA's
  proprietary teaching materials (the case-study data, exam questions,
  official answer keys), or should the case study and exercises be
  paraphrased/re-numbered into originally-authored content merely
  inspired by the source? → A: **Paraphrase/re-author (Option B).** The
  course preserves the source's pedagogical structure, formulas, and
  difficulty level, but the running case study is renamed to "The
  Wandering Fork" with entirely original, invented data values; exam
  questions and official answer keys from the source are never
  reproduced verbatim. Fidelity (FR-003, SC-004) is therefore judged on
  concept/structure/difficulty coverage, not numeric matching against
  the source archives.
- Q: Should the 15 new pages be marked `draft: true` and built
  incrementally out of public view, or published session-by-session as
  each one is finished? → A: **`draft: true` on all 15 files until the
  whole course is complete (Option A)**, then flipped to published
  together in one change, mirroring the existing precedent on
  `teaching/decision-making-stat/index.qmd` (see FR-017).
- Q: Should Session 12 include practice exam-style questions modeled on
  the source's Midterm/Final exam format, or stay a purely conceptual
  revision summary? → A: **Include an original mock-exam-style section
  (Option A)** — mixed MCQ and short-answer items using "The Wandering
  Fork" data, consistent with the no-verbatim-source-exam rule already
  agreed above (see FR-018).

### Session 2026-09-12 (self-resolved from strong site precedent)

- Q: Should the course be authored bilingually (EN+FR) from day one, or
  English-first with French deferred? → A: **English-first at the
  repository root** (`teaching/data-description/`), matching the two
  most recent precedents (`teaching/decision-making-stat/` and the
  `004-math-fundamentals-course` feature). Full French parity
  (Constitution Principle VI) is a pre-existing, cross-cutting gap
  affecting most of the site and is explicitly deferred, documented
  below as a justified deviation — not silently dropped. The bilingual
  source archives remain available in `ressources/` to support a future
  French translation feature.
- Q: The source is 100% Excel-based (Block 1 is literally "Handling
  Excel"); does this satisfy or conflict with Constitution T-IV
  (priority concepts MUST have a Shinylive interactive demo)? → A: Both.
  Excel remains the tool of record for fidelity — each session documents
  the exact Excel functions/steps used in the source materials (e.g.,
  `MEDIAN`, `MODE.SNGL`, `VAR.S`, `STDEV.S`, `QUARTILE.EXC`, `CORREL`) in
  a reference table — while the priority numeric/graphical concepts
  (frequency distribution & histogram, boxplot from quartiles, central
  tendency & dispersion computation, scatter plot & correlation) also
  get a Shinylive interactive demo per T-IV, so learners can explore the
  concept independent of spreadsheet software. Concepts not yet given a
  demo are marked with a `.callout-important` `TODO:` per the
  constitution's own escape hatch.
- Q: Should the site mirror the legacy Moodle "Session 1…12" granularity,
  or consolidate into 3 pages matching the syllabus's 3 blocks? → A:
  **Keep the 12-session granularity** (`session-01.qmd` …
  `session-12.qmd`), consistent with the sibling course
  `teaching/decision-making-stat/` (which uses one file per teaching
  session, not per block) and because each of the 12 legacy sessions maps to a
  distinct, non-redundant set of source slides, exercises, and practical
  work. The 3 syllabus blocks are preserved as **Parts** (a grouping
  displayed in the syllabus table and as `##` part headers in the
  sidebar), not as separate files.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner works through one complete session (Priority: P1)

A business-school student opens any session page (1 through 12) and
works through a self-contained lesson: a short recap of why the topic
matters for data-driven decisions, explicit learning objectives, plain-
language theory with definitions and formulas, a worked example using
the running "The Wandering Fork" case data (or a simple warm-up dataset
for the Excel-fundamentals sessions), the exact Excel steps/functions
used to reproduce the result, and a set of practice exercises with
collapsible solutions — everything in English.

**Why this priority**: This is the core learner-facing deliverable. One
fully realized session already proves the content pattern and delivers
standalone educational value.

**Independent Test**: Render the site and open one session (e.g.,
Session 7, dispersion indicators). Confirm it presents objectives,
theory, a worked example on "The Wandering Fork" (or equivalent)
dataset, the Excel steps to reproduce it, and exercises with revealable
solutions — all in English, with correctly rendered math and no broken
layout.

**Acceptance Scenarios**:

1. **Given** a rendered session page, **When** the learner reads the
   introduction and objectives, **Then** they understand what the
   session covers and what they will be able to compute/interpret
   afterward, in English.
2. **Given** a worked example, **When** the learner reads it, **Then**
   it uses a concept and dataset consistent with the source materials and
   shows a step-by-step solution with a stated numerical result.
3. **Given** an Excel-based concept, **When** the learner reads the
   "Using Excel" callout/table, **Then** the exact function name(s) and
   steps needed to compute the result are shown.
4. **Given** an exercise with a hidden solution, **When** the learner
   expands it, **Then** a correct, verifiable answer is revealed.
5. **Given** any mathematical expression on the page, **When** the page
   renders, **Then** the notation displays correctly with no broken
   markup.

---

### User Story 2 - Learner follows the whole course and the running case study (Priority: P2)

A student starts at the syllabus, follows the three parts in order
(Excel Fundamentals → Univariate Data Treatment → Bivariate Data
Treatment), and tracks how "The Wandering Fork" business case
accumulates new questions from session to session (first descriptive tables, then
distribution shape, then position indicators, then dispersion, then
relationships between two variables), arriving at the final session with
exam-preparation guidance for the Midterm and Final Exam.

**Why this priority**: A connected, navigable course — not isolated
notes — with a coherent case-study narrative is what makes the material
usable as an actual course and builds the intuition the follow-on
Inferential Statistics course (`decision-making-stat`) assumes.

**Independent Test**: From the index page, follow every session link in
order; confirm "The Wandering Fork" case study reappears with escalating
questions from Session 3 onward, the syllabus's assessment section
matches the weighting/duration described in each session, and the final
session provides revision/exam-prep content.

**Acceptance Scenarios**:

1. **Given** the index/syllabus page, **When** the learner reads it,
   **Then** the course description, three-part outline, schedule,
   assessment scheme (Midterm 35% / Final 65%), personal-work load (20h),
   and Recommended Literature are all presented in English.
2. **Given** the session list on the index page, **When** the learner
   clicks each link, **Then** they reach the corresponding session, whose
   title and topic match the syllabus description and part grouping.
3. **Given** Sessions 3 through 12, **When** the learner reads the
   worked examples, **Then** "The Wandering Fork" case study data and
   narrative persist and build on prior sessions rather than restarting.
4. **Given** the final session (12), **When** the learner opens it,
   **Then** it provides a revision summary and an original mock-exam
   section (mixed MCQ and short-answer, on "The Wandering Fork" data)
   whose format mirrors the Midterm/Final Exam structure described in
   the syllabus, with revealable solutions.

---

### User Story 3 - Instructor verifies fidelity and constitution compliance (Priority: P3)

The course owner compares each finished session against the
corresponding source slide deck, practical-work workbook, and exercise
correction file to confirm concepts, formulas, structure, and difficulty
were preserved (while numeric values and the case study were originally
authored per the Clarifications), and separately checks that the
glossary, proofs, and interactive demos required by the project
constitution are present.

**Why this priority**: Fidelity and constitution compliance are
correctness/quality guarantees layered on top of the content produced in
P1/P2; they are essential to trust the deliverable but not required for
a single session to already be useful.

**Independent Test**: Pick any session, cross-check its formulas,
worked-example structure, and exercise difficulty against the matching
source PPTX/XLSX/correction file (not the numeric values, which are
originally authored), confirm the glossary lists every symbol introduced
in that session, and confirm at least one collapsible proof/derivation
is present.

**Acceptance Scenarios**:

1. **Given** a session's source slide deck and practical-work
   correction file, **When** the instructor compares them, **Then**
   every concept, formula, and exercise type in the source appears in
   the rendered session, and no proprietary source figures, case-study
   data, or verbatim exam content have been reproduced.
2. **Given** the completed course, **When** the instructor scans
   `glossary.qmd`, **Then** every mathematical symbol/formula introduced
   in any session (e.g., $\bar{x}$, $Me$, $Mo$, $Q_1$, $Q_3$, $\sigma$,
   $s$, $CV$, skewness, $\text{Cov}(X,Y)$, $r$) is listed with notation,
   plain-language definition, and pronunciation guide where relevant.
3. **Given** any session, **When** the instructor checks for a proof or
   derivation, **Then** at least one collapsible (`collapse="true"`)
   derivation of a central formula is present.
4. **Given** the priority concepts identified in Requirements below,
   **When** the instructor checks for interactive demos, **Then** each
   either has a working Shinylive demo or a `.callout-important` `TODO:`
   marker documenting the gap.

---

### Edge Cases

- **Duplicate/overlapping Moodle exports**: Three separate archives exist
  (`Cours_Description_de_donnes_2425` FR, `Course_Data_description_EN_2425`
  EN, and a newer block-structured `Course_MS03-001-G_Data_descri...`
  bilingual export). Where they overlap, the newer/more complete version
  is authoritative and no source concept is dropped; older duplicates are
  reference-only.
- **Non-machine-readable binary sources**: Slide decks (`.pptx`), student
  handouts/PW documents (`.docx`), and workbooks (`.xlsx`) cannot be
  parsed by the standard project tooling used to draft this spec. The
  planning phase MUST account for a conversion/extraction step (e.g.,
  opening with an Office-compatible tool or a Python
  `python-pptx`/`python-docx`/`openpyxl` script) to recover exact source
  text, formulas, and numeric results before authoring each session.
- **Original case-study data must stay internally consistent**: because
  "The Wandering Fork" uses invented figures rather than the source's
  `The Food Truck.xlsx`/`The Food Truck_EN.xlsx` workbooks, all invented
  values MUST be computed once and reused consistently across every
  session that references them (no silently-changing numbers for the
  same fact from one session to the next).
- **Locale-dependent Excel function names**: French Excel uses localized
  function names (e.g., `MOYENNE`, `ECART.TYPE`) while English Excel uses
  `AVERAGE`, `STDEV.S`, etc. All "Using Excel" content MUST standardize on
  English Excel function names regardless of which source archive a
  screenshot/step came from.
- **Missing correction files for some legacy sessions**: A few legacy
  session numbers have exercises without a published correction (e.g.,
  "Exercises – without solution"); these become practice exercises with
  instructor-authored (self-consistent, clearly derivable) solutions
  rather than omitted content.
- **MCQ / "adaptive learning path" quizzes**: The source repeatedly
  references Moodle-hosted MCQ "Improvement path" quizzes that cannot be
  reproduced as live Moodle quizzes on a static site. These become static
  self-check quizzes (question + options + revealable feedback) within
  the relevant session, matching the pattern already used in
  `teaching/decision-making-stat/session-01.qmd`.
- **Non-lesson archive items**: Forum pages, external "Syllabus" URLs,
  `index.html`/`about.html` Moodle shell pages, and "shared"/"overviewfiles"
  folders are structural Moodle artifacts, not lesson content, and MUST
  NOT be treated as required source material.
- **Prerequisite/successor cross-references**: The course must reference
  its prerequisites (`teaching/mathematical-fundamentals/`,
  `teaching/mathematical-analysis/`) and acknowledge that
  `teaching/decision-making-stat/` (Inferential Statistics) assumes this
  course's content as a refresher (its own Session 6), without
  duplicating that course's material.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The course MUST provide a syllabus at
  `teaching/data-description/index.qmd` containing: a course description
  and learning objectives, a prerequisites note (MS01
  Mathematical Fundamentals, MS02 Mathematical Analysis), a session
  outline table grouped into three parts (Part I — Excel Fundamentals:
  Sessions 1–2; Part II — Univariate Data Treatment: Sessions 3–9; Part
  III — Bivariate Data Treatment: Sessions 10–12) linking every session
  file, the assessment scheme (Midterm Exam 35% / Final Exam 65%,
  individual written exams with MCQ component, durations as stated in
  the syllabus), the expected personal-work load (20h), and a
  Recommended Literature section listing author(s), title, edition, and
  publisher for each reference from the source syllabi.
- **FR-002**: The course MUST provide 12 session files
  (`session-01.qmd` … `session-12.qmd`) under `teaching/data-description/`,
  each following the mandatory pedagogical order: theory → worked
  example(s) → exercises with collapsible solutions.
- **FR-003**: Content MUST be faithfully derived from the source
  materials in `teaching/data-description/ressources/` (both syllabi and
  all three Moodle archives) at the level of concepts, formulas, worked-
  example structure, exercise types, and difficulty; no source concept
  listed in the syllabus organization section may be silently dropped.
  Per the Clarifications below, exact proprietary figures, case-study
  data, and verbatim exam content MUST NOT be reproduced — numerical
  values and the case-study identity are originally authored.
- **FR-004**: Session topics MUST cover, at minimum, across the three
  parts: (Part I) spreadsheet handling, cell referencing, basic
  functions, sorting and data processing; (Part II) frequency
  tables and graphical representation of qualitative/quantitative data
  (bar chart, pie chart, histogram, frequency polygon, cumulative
  frequency), position indicators (quantiles, quartiles, percentiles,
  boxplot), central tendency indicators (mean, median, mode), dispersion
  indicators (range, variance, standard deviation, coefficient of
  variation), and asymmetry/shape indicators (skewness); (Part III)
  bivariate graphical representation (contingency table, scatter plot,
  conditional distributions) and bivariate numerical summaries
  (covariance, correlation coefficient, and an introduction to the
  least-squares regression line).
- **FR-005**: All learner-facing content (prose, headings, objectives,
  examples, exercise prompts, solutions, tables, captions) MUST be
  written in English; `lang: en` MUST be set in every new file's front
  matter.
- **FR-006**: A recurring, originally-authored case study, "The
  Wandering Fork" (a fictional food-truck business inspired by, but not
  reproducing, the source's case), MUST be used as the running
  dataset/narrative for worked examples and exercises from Session 3
  onward, with each session's "mission" building on the data and
  questions introduced in prior sessions rather than restarting with an
  unrelated dataset. All numerical values for "The Wandering Fork" MUST
  be invented (not copied from `The Food Truck.xlsx`/`The Food Truck_EN.xlsx`)
  and kept internally consistent across sessions. Sessions 1–2 (Excel
  Fundamentals) MAY use a simpler warm-up dataset before the case study
  is introduced.
- **FR-007**: For every statistical concept covered, the corresponding
  session MUST include a "Using Excel" reference (table or callout)
  naming the exact English-locale Excel function(s) or steps used to
  compute it (e.g., `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `VAR.S`, `STDEV.S`,
  `QUARTILE.EXC`, `CORREL`, sort/filter operations), consistent with the
  Excel-centric nature of the source materials.
- **FR-008**: The following priority concepts MUST each have a
  Shinylive (`{shinylive-python}`) interactive demo: (a) frequency
  distribution and histogram construction, (b) quartiles/percentiles and
  boxplot construction, (c) mean/median/mode and dispersion (variance,
  standard deviation) computation on a sample the learner can edit, and
  (d) scatter plot and correlation coefficient. Any additional priority
  concept without a demo MUST be marked with a `.callout-important`
  `TODO:` block per the project constitution's escape hatch.
- **FR-009**: Exercises MUST use static, revealable solutions
  (collapsible callouts); MCQ-style self-check quizzes carried over from
  the source "adaptive learning path" MUST be reproduced as static
  question/options/feedback blocks, not live Moodle-dependent quizzes.
- **FR-010**: The course MUST maintain a `glossary.qmd` listing every
  mathematical symbol and formula introduced in any session, each with
  its notation, a plain-language definition, and — for Greek letters
  (e.g., $\sigma$, $\mu$) — a pronunciation guide; it MUST be linked from
  the course sidebar.
- **FR-011**: Each session MUST include at least one collapsible
  (`collapse="true"`) formal proof or step-by-step derivation of its
  central formula or result (e.g., the shortcut/computational formula
  for variance, the rank formula for a quartile, the bounds of the
  correlation coefficient $-1 \le r \le 1$).
- **FR-012**: Wherever a concept has a geometric or visual
  interpretation, it MUST be surfaced (e.g., the boxplot as a picture of
  the five-number summary, variance as an average squared distance from
  the mean, correlation as related to the angle/alignment of points
  around a trend line).
- **FR-013**: The site navigation (`_quarto.yml` sidebar) MUST register
  the index page, the glossary, and all 12 sessions grouped by the three
  parts, so learners can reach every page from course navigation.
- **FR-014**: Non-lesson archive artifacts (forum pages, external
  syllabus URLs, Moodle shell HTML, duplicate exports) MUST NOT be
  presented as required course lessons; the binary source files
  (`.pptx`/`.docx`/`.xlsx`) remain reference-only inputs under
  `ressources/` and are not published directly.
- **FR-015**: The completed course MUST render successfully
  (`quarto render` exits 0) as part of the existing site build, with
  correctly rendered mathematical notation and no broken internal links.
- **FR-016**: The syllabus and/or an early session MUST note the
  course's place in the curriculum: successor to Mathematical
  Fundamentals (MS01) and Mathematical Analysis (MS02); prerequisite
  refresher for Inferential Statistics (`teaching/decision-making-stat/`, MS04).
- **FR-017**: All 15 files (syllabus, glossary, 12 sessions) MUST carry
  `draft: true` in their front matter while the course is under
  construction, consistent with the existing precedent on
  `teaching/decision-making-stat/index.qmd`. The course sidebar block
  MUST still be registered in `_quarto.yml` per Principle II while
  draft. Draft status MUST be removed from all 15 files together, in a
  single change, only once every file satisfies SC-001 (no empty or
  placeholder pages) — partial publication of an incomplete course MUST
  NOT occur.
- **FR-018**: Session 12 MUST include an originally-authored mock-exam
  section (a mix of MCQ and short-answer items, using "The Wandering
  Fork" data) whose format and difficulty mirror the Midterm/Final Exam
  structure described in the syllabus, with revealable solutions; it
  MUST NOT reproduce verbatim questions or answer keys from the source
  exam files, per the Clarifications above.

### Key Entities *(include if feature involves data)*

- **Course**: The "Data Description" (MS03-001-G) offering; attributes
  include title, description, prerequisites, three-part schedule,
  assessment scheme, personal-work load, and recommended reading.
  Represented by `index.qmd`.
- **Part**: One of three thematic groupings (Excel Fundamentals,
  Univariate Data Treatment, Bivariate Data Treatment) that organizes
  sessions in the syllabus table and sidebar; not a separate file.
- **Session**: One of 12 self-contained lesson pages; attributes include
  title, part, learning objectives, theory, worked example(s), Excel
  reference, exercises with solutions, and (where applicable) an
  interactive demo. Maps to one or more legacy Moodle session folders
  (slides, summary, exercises, practical work).
- **Case Study ("The Wandering Fork")**: The recurring, originally-
  authored dataset and business narrative (a fictional food-truck
  business's sales/customer data, inspired by but not copied from the
  source's case study) used for worked examples and exercises from
  Session 3 onward; accumulates new questions/data as the course
  progresses.
- **Exercise**: A practice item within a session; attributes include the
  prompt, optional real-world ("The Wandering Fork" or warm-up) context,
  and a revealable correct solution/result.
- **Glossary Term**: An entry in `glossary.qmd`; attributes include
  notation/symbol, plain-language definition, pronunciation guide (for
  Greek letters), and the session(s) where it is introduced.
- **Source Material**: An authoritative reference input (slide deck,
  student handout, practical-work workbook, exercise correction, exam,
  syllabus) from `ressources/`, used to guarantee fidelity but not
  published directly.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 15 deliverable pages (1 syllabus + 1 glossary + 12
  sessions) contain complete content — 0 empty or placeholder pages.
- **SC-002**: 100% of learner-facing text across the course is in
  English.
- **SC-003**: Every topic listed in the source syllabus's three-block
  organization section appears in at least one session (100% topic
  coverage against the syllabus).
- **SC-004**: 100% of worked examples and exercises use the same
  concept, formula, and difficulty level as the matching source
  material, while using originally-authored ("The Wandering Fork")
  data rather than the source's proprietary figures (0 proprietary
  source figures, case-study data, or verbatim exam content reproduced).
- **SC-005**: The course renders with 0 broken mathematical expressions
  and 0 build/render errors.
- **SC-006**: At least 4 priority concepts (per FR-008) have a working
  Shinylive demo; any remaining priority-concept gap carries a tracked
  `TODO:` callout (0 undocumented gaps).
- **SC-007**: Every mathematical symbol/formula used in any session
  appears in `glossary.qmd` (100% glossary coverage).
- **SC-008**: A learner can navigate from the syllabus through all 12
  sessions to the exam-preparation content in Session 12 without
  encountering an empty, placeholder, or broken-link page.
- **SC-009**: Every session link on the index page and every
  cross-session navigation link resolves to an existing, correct session
  page (0 broken links).

## Assumptions

- The three-part structure (Excel Fundamentals / Univariate Data
  Treatment / Bivariate Data Treatment) from the syllabus is authoritative
  for grouping; the 12-session granularity from the legacy Moodle exports
  is authoritative for file structure, matching the convention already
  used by the sibling course `teaching/decision-making-stat/`.
- Where the three source archives disagree on details, the newest,
  most complete archive (`Course_MS03-001-G_Data_descri..._.2013698`,
  block-structured, bilingual) is preferred, followed by the English
  2024/25 export, then the French 2024/25 export, for any concept present
  in more than one — for structure and difficulty only; numeric values
  themselves are always originally authored per the Clarifications.
- The deliverable is the set of Quarto files (index, glossary, 12
  sessions) under `teaching/data-description/`; the `ressources/`
  archives remain unmodified reference inputs and are not published
  directly.
- English-first authoring at the repository root is accepted per the
  two most recent site precedents; full French parity (Constitution
  Principle VI) is deferred as a documented, justified deviation, not a
  silent omission — consistent with how `001-course-syllabus-index` and
  `004-math-fundamentals-course` handled the same tension.
- Excel remains the tool of record referenced throughout (per source
  fidelity), supplemented — not replaced — by Shinylive demos for the
  priority concepts identified in FR-008, per the constitution's T-IV
  escape hatch for tracked gaps.
- Binary source files (`.pptx`, `.docx`, `.xlsx`) require an extraction
  step (e.g., a Python script using `python-pptx`/`python-docx`/`openpyxl`,
  or manual opening) during the planning/implementation phase, since they
  are not directly readable by the standard project tooling used to
  author this specification; this spec's content mapping relies on the
  syllabus text, file/session naming, and the already-rendered
  `teaching/decision-making-stat/` and `teaching/mathematical-fundamentals/`
  precedents for structure and depth.
- The recommended-reading list may remain bibliographic (original titles
  unchanged) even where the original works are French-language, matching
  the source syllabus bibliography.
