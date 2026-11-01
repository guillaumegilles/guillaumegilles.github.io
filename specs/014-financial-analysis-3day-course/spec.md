# Feature Specification: Financial Analysis — 3-Day Intensive Course (18 h)

**Feature Branch**: `014-financial-analysis-3day-course`

**Created**: 2026-10-26

**Status**: Draft

**Input**: User description: "used materials in teaching/financial-analysis
to create a 3 days courses (6 hours each day for a total of 18 hours of
content)."

## Context

`teaching/financial-analysis/` already holds a large set of raw
materials: a syllabus outline (`index.qmd`) announcing three days of three
"quests", nine quest worksheets (`modules/01…09`), reference pages on the
Banque de France (BdF) methodology (performance, financial structure,
liquidity, rating, formulas), two exams, and many source documents (PDF,
DOCX, PPTX). They were produced piece by piece and do not yet add up to a
coherent, deliverable 18-hour course:

- Stated quest durations do not match 6 h per day. Most quests are 2 h,
  Quest 6 is 2 h 30 and Quest 9 is 3 h, so Day 2 and Day 3 overrun and
  Day 1 is uncertain.
- Reference pages (liquidity, structure, performance, BdF rating) are not
  placed in any day's timetable, so it is unclear when students learn the
  theory the quests assume.
- Both exams (1 h and 3 h 30) are larger than any slot in the plan.
- Preparatory work, grading and XP are scattered across pages.

This feature turns those materials into one **ready-to-teach 3-day
course**: a timetable accounting for every minute of the 18 hours, the
content to teach in each block, and the supporting pages for students and
the instructor.

## Clarifications

### Session 2026-10-26

- Q: Should the 3-day course replace the existing quest pages or be built
  as a separate set of pages next to them? → A: Edit the existing quest
  and reference pages in place, and rewrite `index.qmd` as the 3-day
  course home page.
- Q: Should reference theory be taught live in class or given as pre-reading?
  → A: Hybrid: a short live theory segment (20–30 min) opens each quest,
  and the reference page is the pre-reading.
- Q: Are the 1 h and 3 h 30 exams inside or outside the 18 h? → A: Both
  stay outside the 18 h, in a separate session; in-course assessment uses
  boss cases and XP only.
- Q: Do XP and levels count toward the final grade? → A: Yes: XP counts
  for a stated share of the final grade and the separate exam counts for
  the rest (default share 40 % XP / 60 % exam, adjustable by the owner).
- Q: Full English translation or labelled stubs? → A: Full translation of
  the home page and timetable only; every other page is a labelled stub
  linking to the French version.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Instructor delivers the course from a minute-by-minute plan (Priority: P1)

An instructor opens the course and sees, for each of the three days, a
timetable of exactly 6 hours of teaching. Each block states its start and
duration, its learning goal, the materials to use, and the activity
students perform. The three days add up to exactly 18 hours.

**Why this priority**: Without a reliable timetable the course cannot be
taught. Everything else (student pages, assessment) hangs off it.

**Independent Test**: Add up the block durations for each day and for the
course. Then have a colleague who has not seen the materials read Day 1 and
state what they would teach and when.

**Acceptance Scenarios**:

1. **Given** the course schedule, **When** the instructor adds the block
   durations of any one day, **Then** the total is exactly 6 h of
   teaching, with breaks listed separately and not counted.
2. **Given** the course schedule, **When** the instructor adds the three
   days, **Then** the total is exactly 18 h.
3. **Given** any block in the timetable, **When** the instructor looks at
   it, **Then** it names the source material (existing page or document)
   it uses, so nothing needs to be searched for.
4. **Given** a block that mixes theory and practice, **When** the
   instructor reads it, **Then** theory comes first, followed by a worked
   example, then the student exercise (existing pedagogical order).

---

### User Story 2 - Student follows a coherent 3-day journey (Priority: P1)

A student reads the course home page and understands, before Day 1, what
they will learn each day, what to prepare, what they must hand in, and how
they will be assessed. During each day they can find the page for the
current block in one click and never meet a concept used before it has
been introduced.

**Why this priority**: Equal to Story 1: the course has two audiences and
it is only usable if both can navigate it.

**Independent Test**: Give the home page to a student and ask them, without
help, to list the day-by-day content, the preparatory work for Day 2, and
how the final grade is computed.

**Acceptance Scenarios**:

1. **Given** the course home page, **When** a student reads it, **Then**
   they see the three days, the blocks of each day with their durations,
   and the learning goals of each day.
2. **Given** a block that uses a formula or method (for example the
   leverage effect, free cash flow or the recurring net result),
   **When** the student opens it, **Then** that formula or method has been
   taught in an earlier block or in the same block before it is applied.
3. **Given** the course home page, **When** a student looks for the
   preparatory work of a day, **Then** it is listed with the day it is due
   and its expected effort.
4. **Given** the course home page, **When** a student wants to look up a
   formula, **Then** a single reference page collects all formulas used
   across the three days.

---

### User Story 3 - Course content fits the time without losing the core (Priority: P2)

The instructor wants each existing quest and reference topic to be
rebalanced so it fits its slot, without dropping the central theory, worked
examples and exercises that make the course valuable.

**Why this priority**: This is the editorial work that makes Story 1 true.
It depends on the timetable (Story 1), so it follows it.

**Independent Test**: For each of the nine quests and each reference
topic, check that it appears in the timetable, that its core theory,
worked example and exercise are still present, and that its activity can
realistically be finished in its slot.

**Acceptance Scenarios**:

1. **Given** the nine existing quests, **When** the course is complete,
   **Then** each of them appears in exactly one block, with a duration
   that matches the time its activity needs.
2. **Given** a quest that currently runs longer than its slot (for
   example the 3 h final quest), **When** it is rebalanced, **Then** the
   removed or shortened parts are listed (moved to optional extension,
   homework, or cut) and the central concept is still taught.
3. **Given** the reference pages on performance, financial structure,
   liquidity and BdF rating, **When** the course is complete, **Then**
   each is listed as pre-reading for the quest that depends on it and
   taught in that quest's opening live theory segment.

---

### User Story 4 - Assessment and progress fit inside the 18 hours (Priority: P2)

The instructor and students know how learning is assessed during the three
days (XP, end-of-day "boss" case, levels) and what is done with the
existing exams, so that grading is clear and nothing assessed is missing
from the timetable.

**Why this priority**: Assessment is part of the existing identity of the
course, but the course can be taught without it being re-specified.

**Independent Test**: Take one student's hypothetical results and compute
their final level and grade from the published rules only.

**Acceptance Scenarios**:

1. **Given** the published assessment rules, **When** the maximum XP of
   all activities is added up, **Then** the total is consistent with the
   thresholds of the four levels and converts to the stated XP share of
   the final grade.
2. **Given** each end-of-day boss case, **When** it appears in the
   timetable, **Then** its time slot, deliverable and grading criteria are
   stated.
3. **Given** the existing 1 h and 3 h 30 exams, **When** the course is
   complete, **Then** each is explicitly marked as outside the 18 h, and
   the 18 h timetable has no hidden assessment time.

---

### User Story 5 - Course is available in French and English (Priority: P3)

A French-speaking cohort and an English-speaking reader each find the
complete course in their language, as the site requires for every page.

**Why this priority**: The site's bilingual rule applies to every page, but
the primary teaching language (French) must be right first.

**Independent Test**: For every new or changed page, check that its
counterpart exists in the other language (full translation or a stub with
a notice and a link).

**Acceptance Scenarios**:

1. **Given** any page of the course in one language, **When** the reader
   switches language, **Then** they reach its counterpart: a full
   translation for the home page and timetable, or a clearly labelled
   "translation in progress" stub for every other page.
2. **Given** the course timetable, **When** it is read in either language,
   **Then** the durations and block order are identical.

---

### Edge Cases

- A block runs over: each block names what to cut or defer first when time
  is short, so the day still ends at 6 h.
- A day starts with unprepared students: the plan states what the
  preparatory work enables and a fallback (short in-class catch-up) so
  later blocks are not blocked.
- A student joins on Day 2 or Day 3 only: each day lists its prerequisites
  so they can see what they need to have read.
- Materials in the folder that are not used (duplicate files, exam
  variants, third-party PDFs): they are listed as "not part of the 18 h"
  rather than silently ignored.
- Real company annual reports used for the tournament may change year to
  year: the plan states how the data is obtained, so the exercise survives
  a new report edition.
- Group size varies (3–5 students per team, as in the existing quests):
  timings state what changes for a smaller or larger cohort.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The course MUST define exactly three teaching days of 6 h
  each (360 minutes of teaching per day, 1 080 minutes in total). Breaks
  are shown but not counted.
- **FR-002**: Each day MUST be a sequence of blocks, each with a start
  offset, a duration, a learning goal, the source materials and the
  student activity.
- **FR-003**: The durations of all blocks of a day MUST add up to exactly
  360 minutes, and the three days to exactly 1 080 minutes.
- **FR-019**: The course MUST be built by editing the existing quest and
  reference pages in place (no parallel copy of the course), and by
  rewriting the course home page (`index.qmd`) as the 3-day course home
  page. Existing page addresses MUST keep working.
- **FR-004**: All nine existing quests MUST be placed in the timetable,
  keeping the Day 1 / Day 2 / Day 3 grouping of the current syllabus,
  with durations adjusted so each day equals 6 h.
- **FR-005**: The reference topics (BdF method overview, performance,
  financial structure, liquidity, BdF rating, formula sheet) MUST be
  listed as pre-reading for the quest that first uses them, AND each quest
  MUST open with a live theory segment of 20–30 minutes counted within
  its block duration, so a student who did not prepare can still follow.
- **FR-006**: Each block MUST follow the pedagogical order of theory,
  then worked example, then exercise with the solution available
  separately from the statement.
- **FR-007**: For every block whose duration changes from the current
  materials, the course MUST record what was shortened, moved or removed,
  and why. Core theory, worked examples and exercises MUST NOT be deleted.
- **FR-008**: The home page MUST present, for each day, its narrative
  goal, its blocks with durations, its preparatory work (with expected
  effort), its prerequisites and its end-of-day deliverable.
- **FR-009**: The course MUST provide an instructor guide per day,
  covering the answer key, expected pitfalls, suggested pacing and
  what to cut first if time runs short. Instructor-only content MUST be
  kept apart from student pages.
- **FR-010**: The course MUST provide one reference page listing every
  formula used across the three days with a plain-language explanation of
  each.
- **FR-011**: The assessment scheme (XP per activity, end-of-day boss
  cases, levels, final grade) MUST be stated once, consistent with the
  timetable, and MUST show how the total XP relates to the level
  thresholds. The final grade MUST combine an XP share and an exam share,
  with the shares stated explicitly (default 40 % XP, 60 % exam) and the
  conversion from XP to a mark defined.
- **FR-012**: The existing 1 h and 3 h 30 exams are outside the 18 h (a
  separate session). The home page MUST say so, and the timetable MUST NOT
  contain exam time; only boss cases and XP activities count as in-course
  assessment.
- **FR-013**: The syllabus MUST list the recommended literature (author,
  title, edition, publisher) and the competences targeted, with the
  competence-to-quest mapping updated to match the final timetable.
- **FR-014**: The course MUST include a "what is not in the 18 h"
  inventory so that every file in the course folder is either used,
  optional, or archived.
- **FR-015**: Every page MUST exist in French and English as per the site
  rules. The home page and the full timetable MUST be fully translated;
  every other page's English counterpart MUST be a labelled stub with a
  link to the French page.
- **FR-016**: The course pages MUST be reachable from the site navigation
  and from the course home page, with no orphan page.
- **FR-017**: Each day MUST list its interactive or hands-on activity and
  its time box. Where a priority concept has no interactive demo yet, a
  visible TODO marker MUST flag the gap.
- **FR-018**: The instructor MUST be able to see, on one page, the whole
  timetable (three days, all blocks) for printing or sharing.

### Key Entities

- **Course**: the 18 h programme; has three Days, a syllabus, an
  assessment scheme, a literature list and a competence mapping.
- **Day**: a 6 h teaching unit; has a narrative goal, prerequisites,
  preparatory work, an ordered list of Blocks and an end-of-day boss case.
- **Block**: a time-boxed unit within a day; has a duration, a learning
  goal, source materials, a theory part, a worked example, an exercise, a
  solution, a "cut first" note and an XP value.
- **Quest**: an existing worksheet (nine in total); each is delivered in
  one or more Blocks.
- **Reference topic**: a theory page (performance, structure, liquidity,
  BdF rating, formulas) that feeds one or more Blocks.
- **Assessment item**: an XP-bearing activity, a boss case or an exam,
  with a time slot, deliverable and grading criteria.
- **Source document**: a file in the course folder, classified as used,
  optional or archived.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In an audit of the timetable, 100 % of days total exactly
  6 h of teaching and the course totals exactly 18 h.
- **SC-002**: 100 % of the nine quests and of the reference topics appear
  in the timetable or in the "not in the 18 h" inventory.
- **SC-003**: A new instructor, given only the course pages, can prepare
  Day 1 in under 2 hours and says nothing is missing for the delivery.
- **SC-004**: A student reading only the home page can correctly list the
  content, preparatory work and deliverable of each day, with at least
  90 % accuracy on a 10-question check.
- **SC-005**: A pilot read-through of each day finds no block that uses a
  concept before it is introduced.
- **SC-006**: For every block shortened relative to the current material,
  100 % have a recorded note of what changed; no core theory, worked
  example or exercise is lost.
- **SC-007**: A student's final level can be computed from the published
  rules in under 2 minutes, with no ambiguity about the thresholds.
- **SC-008**: 100 % of the course pages have a French and an English
  counterpart (full or labelled stub), and the timetable is identical in
  both languages.

## Assumptions

- Because pages are edited in place, the current content is the only
  copy; any removed material is recorded per FR-007 (and remains
  recoverable from version history).
- The three-day, three-quest-per-day structure and quest order of the
  current syllabus are kept; only timings, placement of reference topics
  and content balance change.
- "6 hours per day" means teaching time. Breaks and lunch are extra and
  are listed separately.
- French is the primary teaching language (current materials), with an
  English counterpart per the site's bilingual rule.
- The course targets the same audience as today: Master of Science
  students in finance, with the same RNCP competence framework.
- The 1 h exam and the 3 h 30 final exam are outside the 18 h (confirmed
  in clarification); the 18 h timetable uses boss cases and XP for
  in-course assessment.
- Third-party documents in the folder (BdF PDFs, Vernimmen newsletters,
  slide decks) stay as reference material and are not republished beyond
  what is already on the site.
- Existing project rules apply: Quarto sources only, navigation
  registered once, callouts reserved for their defined roles, solutions
  folded, and a syllabus with recommended literature.
- The `fr/teaching/financial-analysis/` tree shows many files deleted in
  the working copy; this feature treats the English-root and French trees
  as currently in flux and does not restore or rely on deleted files.
