# Feature Specification: 3-Day Lecture Slide Deck for the Financial Analysis Course

**Feature Branch**: `014-financial-analysis-slides`

**Created**: 2026-10-18

**Status**: Draft

**Input**: User description: "From inseec-analyse-financiere.pptx create a slide deck in fr/teaching/financial-analysis for a 3 day course on financial analysis. You can add material from all files inside fr/teaching/financial-analysis. Take your time to review all the materials available (quite a lot)."

**Evidence**: [sources.md](sources.md) inventories the 74 files in the course folder, says what each contributes, and lists the conflicts (C1–C9 below refer to its §4) the deck must resolve.

**Related**: Spec `013-improve-financial-analysis` (course coherence). Moving the course to `fr/` settles that spec's question on which language is canonical: French.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - The instructor delivers each course day from the deck (Priority: P1)

The instructor opens the deck for the current day on a projector and teaches from it from opening to wrap-up. It has the day's agenda and objectives, theory slides, worked examples, in-class exercise briefs, short breaks to check understanding, and a recap. Apart from the answer-key documents named on the exercise slides, the instructor needs no other file during the session.

**Why this priority**: This is the purpose of the feature. Today the only deck (102 slides) covers the Banque de France and the six-step consolidated-accounts method only. It has no fundamentals, no exercises, no day structure, and 25 slides that are just pictures of a 2017 institutional presentation.

**Independent Test**: Open the deck for any one day in presentation mode, go through every slide, and check that the day can be taught from start to finish. Agenda, objectives, all planned topics, at least one worked example per topic block, the exercise briefs and a recap must all be there, in teaching order.

**Acceptance Scenarios**:

1. **Given** the instructor opens the deck for Day N (one deck per day), **When** they show the first slides, **Then** the day's agenda (with timings) and 3–6 learning objectives are visible.
2. **Given** a theory block (e.g. bilan fonctionnel, RNR, FPNR), **When** the instructor reaches its end, **Then** a worked numeric example follows before any exercise that uses the concept.
3. **Given** the deck reaches an exercise, **When** it is shown, **Then** the slide gives the case name, the task, the data needed (or where to find it), the team format and the time allowed.
4. **Given** the end of a day, **When** the instructor shows the last slides, **Then** a recap of the day's key points and a preview of the next day appear.
5. **Given** the three decks together, **When** the instructor adds up the planned timings of non-optional blocks, **Then** each day totals 6 hours and the course totals 18 hours.

---

### User Story 2 - Content from the original deck is kept, corrected and up to date (Priority: P2)

Everything still useful in `inseec-analyse-financiere.pptx` is in the new deck. The content is corrected where sources conflict and updated where facts have changed since the deck was made.

**Why this priority**: The original deck is the user's chosen basis. It contains the course's backbone (the Banque de France six-step method). It also contains errors and outdated facts students would memorise: the old cote de crédit scale (C2), the 2/3 vs 3/4 tax-rate inconsistency (C1), and superseded regulatory references (C7).

**Independent Test**: A reviewer compares each original text slide with the new deck. Each one is either present, merged into another slide, or listed as deliberately dropped with a reason. Every number, scale and regulation on the new slides matches the most recent source in the folder or a verified current official source.

**Acceptance Scenarios**:

1. **Given** any of the original deck's text slides on the cotation and the six steps, **When** a reviewer looks for its content in the new deck, **Then** it is found or the coverage map records why it was dropped.
2. **Given** a slide on the cote de crédit, **When** a student reads it, **Then** it shows the current 22-position scale (1+ … 6-, 7, 8, P, 0) with labels, and states that 1+ to 4+ are eligible. If the old scale appears, it is clearly labelled as the pre-2022 scale.
3. **Given** the RNR and CAFr slides, **When** a student reads them, **Then** both use the same, current tax-rate convention, and the slide says when to use the actual tax charge instead.
4. **Given** any figure that depends on the year (firm counts, distribution, thresholds, horizon, X threshold), **When** it is shown, **Then** its source and date are displayed on the slide.
5. **Given** the 19 image-only "Découvrir la Banque de France" slides, **When** the new deck covers this topic, **Then** it does so in a few readable slides with current facts (missions, role in the Eurosystem, why the BdF rates companies), optionally with the short official video.
6. **Given** an image-only slide whose content is still needed (consolidation scope, goodwill decomposition, deferred-tax examples, qualitative profile grid, SWOT), **When** it is rebuilt, **Then** its content is readable as slide text or a table, not a low-resolution picture.

---

### User Story 3 - Material from the other course files fills the gaps (Priority: P3)

The deck adds what the original lacks, using the other files in the folder:

- fundamentals: bilan, compte de résultat, SIG, CAF, bilan fonctionnel, FRNG/BFR/TN, ratios
- rentabilité and effet de levier
- the in-class cases that already have answer keys
- recent real-world "focus" boxes: Orpéa and IFRS 16, Casino and the debt/EBE threshold, gross vs net debt

**Why this priority**: Students cannot follow the six-step analysis of consolidated accounts without the fundamentals. The folder already holds teaching material and answer keys for them (COURS M1, ratio handout, formula sheet, CONCOURSMANIA/LECTRA case, cases CP1–CP4, Vernimmen letters). Reusing it gives a complete course without writing from scratch.

**Independent Test**: Map each topic in the deck to its source file. Every topic the course needs has a source or is marked as newly written. Every in-class exercise used in the deck has an existing or newly written answer key.

**Acceptance Scenarios**:

1. **Given** the fundamentals block, **When** it is taught, **Then** it covers SIG, CAF (both methods), bilan fonctionnel with the main retraitements (crédit-bail), FRNG, BFR, TN and the core ratios, each with one definition used consistently across the deck (C6).
2. **Given** each in-class case (CONCOURSMANIA/LECTRA, CP1 SWOT, CP2 RNR, CP3 FPNR, CP4 endettement), **When** it appears in the deck, **Then** it sits right after the theory it needs, and its data are available to students.
3. **Given** a focus box from a real company, **When** it is shown, **Then** it names the company, the year, the source and the lesson for the analyst in one or two sentences.
4. **Given** a file in the folder judged irrelevant, duplicate or outdated (e.g. the AI position paper, the older Séminaire deck, the 2017 accounting news), **When** the coverage map is read, **Then** the file is listed with the reason it was not used.

---

### User Story 4 - Students revise with the same deck after class (Priority: P4)

After each day, a student opens the day's deck on the course site and reviews it. From each slide block they can reach the matching course web page (theory page, quest, formula sheet).

**Why this priority**: The slides become a revision aid at almost no extra cost. Linking back to the web pages keeps the web pages as the reference and the slides as the lecture support, as for the other courses on the site.

**Independent Test**: From the course home page, a student reaches each day's deck in two clicks or fewer. Every "for more" link in the deck opens an existing course page.

**Acceptance Scenarios**:

1. **Given** the course home page, **When** a student looks for the slides, **Then** each day's deck is listed and opens in the browser without a download.
2. **Given** a slide block, **When** the student follows its link to the course, **Then** it opens the matching page.
3. **Given** a slide containing a formula, **When** a student reads it after class, **Then** the formula is followed by a one-line plain-language explanation of what it measures.

---

### Edge Cases

- **Facts that can't be confirmed**: some facts in the folder disagree (default rates for the new scale, the X threshold of 20/21/23 months, the current consolidation thresholds). They are checked against current official sources (FR-014a). If no official source settles a fact, the slide shows the most recent folder value with its date and an instructor-facing "à vérifier" marker, and never presents it as current.
- **Missing case data**: the CONCOURSMANIA/LECTRA statements are not in the énoncé. They are retrieved from the companies' published 2016 accounts (FR-017a). If a statement can't be found, the case uses the figures it can reconcile with the answer key, and the slide says so. The exam's annex 2 is image-only but out of scope here.
- **Answer keys use outdated assumptions**: the existing keys use a 33⅓ % tax rate. The answer-key documents used in class must be recomputed with the convention taught, or the exercise slide must state that the key uses the old rate.
- **A day runs short or long**: the deck must mark which blocks are optional or can be cut, so the instructor can adjust without breaking prerequisites.
- **Third-party material**: BdF institutional images, BdF videos and Vernimmen excerpts are third-party content. They are rebuilt, linked or briefly quoted with a source, never embedded as-is (FR-022). If an official video link cannot be found, the slide gives the video's title and publisher so the instructor can find it.
- **Reading on a small screen**: wide tables (cote d'activité, consolidation methods, liquidity risk matrix) must stay readable when a student reviews the deck on a laptop.

## Requirements *(mandatory)*

### Functional Requirements

**Structure and delivery**

- **FR-001**: The course MUST have exactly three lecture decks, one per course day, each usable on its own.
- **FR-002**: Each day's slides MUST open with an agenda with timings and 3–6 measurable learning objectives, and MUST close with a recap and a preview of the next day.
- **FR-003**: The days MUST follow the original deck's progression, extended with fundamentals:
  - **Day 1**: fundamentals (reading the bilan and compte de résultat, SIG, CAF, bilan fonctionnel, FRNG/BFR/TN, ratios, rentabilité and effet de levier).
  - **Day 2**: the Banque de France and its cotation, groups and consolidation, steps 1–3 (environnement and SWOT with a short Business Model Canvas input block, examen critique, performances and RNR).
  - **Day 3**: steps 4–6 (structure financière and FPNR, liquidité, décision de cotation), short input blocks for regulatory watch and ESG, the real-case focus boxes and a wrap-up.
- **FR-003a**: Each topic block MUST point to the quest from the published syllabus (`modules/01…09`) that serves as its in-class activity, where one fits. The three quests with no matching block MUST each get a short input block of 3–5 slides: Business Model Canvas (Q5), placed with step 1 on Day 2; regulatory watch (Q7) and ESG/extra-financial reporting (Q9), both on Day 3. Each input block MUST state the quest's goal, give the minimum concepts needed to start it, and link to the quest page.
- **FR-004**: Each day MUST be planned for 6 hours of teaching (reference schedule 9:00–12:00 and 13:30–16:30), 18 hours in total. Each day's agenda timings MUST add up to 6 hours, excluding optional blocks. Blocks that would push a day past 6 hours MUST be marked optional or cuttable.
- **FR-005**: Within each topic block, slides MUST follow the order: concept → formula with plain-language explanation → worked example → exercise brief.

**Content from the original deck (inseec-analyse-financiere.pptx)**

- **FR-006**: The new deck MUST cover all still-valid content of the original's parts 2 and 3. That includes the cotation: purpose, cotation vs notation, « à dire d'expert », legal basis (OEEC, ICAS), what is analysed, information sources, indicateur dirigeant. It also includes the group and consolidation basics and all six analysis steps with their phases and indicators.
- **FR-007**: The original's part 1 (19 image-only institutional slides) MUST be condensed into at most 5 readable slides with current facts.
- **FR-008**: Content currently held in images and still needed MUST be rebuilt as readable slide content: SWOT grid, legal organisation chart, goodwill decomposition, deferred-tax examples, qualitative profile grid, cote d'activité and cote de crédit tables, distribution of firms by cote.
- **FR-009**: A coverage map MUST record, for each original slide, where its content now lives or why it was dropped.

**Accuracy and currency**

- **FR-010**: Cotation slides MUST use the current 22-position cote de crédit scale and the current cote d'activité thresholds, with eligible grades identified. Any pre-2022 scale shown MUST be labelled as historical.
- **FR-011**: RNR and CAFr MUST use one consistent tax-rate convention, matching the current French corporate tax rate. Each slide MUST state when to use the actual tax charge instead (C1).
- **FR-012**: Each ratio and aggregate MUST have exactly one definition across the deck, matching the course formula sheet. Where the sources disagree (C6), the chosen definition is recorded in the coverage map.
- **FR-013**: Year-dependent figures (firm counts, distributions, thresholds, default rates, horizons) MUST show their source and date. Outdated regulatory references MUST be updated or labelled as historical (C7).
- **FR-014**: Old-scale default rates MUST NOT be presented as applying to the current scale (C3).
- **FR-014a**: Facts that are missing, outdated or conflicting in the folder MUST be verified against current official sources (Banque de France, Légifrance, ANC, IFRS Foundation) and cited on the slide with publisher and date. This covers at least: default rates for the current scale, the cote X threshold, the rating horizon, the number of rated firms, consolidation thresholds, the accounting rules replacing CRC 99-02, and whether proportional consolidation is still allowed. The coverage map MUST record each verified fact, its source and the date it was checked.

**Material from the other files**

- **FR-015**: The deck MUST include a fundamentals block: bilan and compte de résultat reading, SIG, CAF by both methods, bilan fonctionnel with the crédit-bail retraitement, FRNG/BFR/TN and their ratios. It is sourced from the lecture notes, ratio handout and formula sheet in the folder.
- **FR-016**: The deck MUST include rentabilité économique and financière and the effet de levier, with the leverage identity derived step by step.
- **FR-017**: The deck MUST include exercise briefs for the existing cases that have answer keys: CONCOURSMANIA/LECTRA, CP1 SWOT, CP2 RNR, CP3 FPNR, CP4 endettement retraité. Each brief is placed after the theory it needs, with readable data.
- **FR-017a**: For the CONCOURSMANIA/LECTRA case, the 2016 bilan and compte de résultat of both companies MUST be retrieved from their published annual accounts and given to students as readable tables, with the source cited. The existing answer key is kept. Any gap between the retrieved figures and the key's totals MUST be recorded in the coverage map and fixed in the key or flagged on the exercise slide.
- **FR-018**: The deck MUST include at least three "focus" boxes from recent real cases in the folder (e.g. Orpéa and IFRS 16, Casino and the 6× dette/EBE threshold, gross vs net debt in France). Each box names its source and date.
- **FR-019**: The deck MUST include a short "what changed" slide on lease accounting (IFRS 16) linked to the off-balance-sheet retraitement, and a mention of the extra-financial reporting shift (DPEF → CSRD).
- **FR-020**: The coverage map MUST list every file in the folder as used, partly used or not used, with a reason. The not-used files include duplicates, outdated items and the misplaced AI paper.

**Solutions and audience**

- **FR-021**: The decks MUST NOT contain exercise solutions. Each exercise brief MUST name the answer-key document the instructor uses (existing corrigé or newly written key). The coverage map MUST list, for each exercise, its answer key and whether that key matches the tax-rate convention taught.
- **FR-022**: The decks MUST NOT embed third-party images or videos. Content from Banque de France documents and presentations MUST be rebuilt as original text, tables or diagrams, each with a source line (publisher and year). The two BdF videos MUST be linked to their official public location, not embedded. Vernimmen material MUST be limited to short quoted figures or ideas with a citation (letter number and date).

**Site integration**

- **FR-023**: Each day's slides MUST be reachable from the course home page and listed in the course navigation.
- **FR-024**: Each topic block MUST link to the matching course web page (theory page, quest or formula sheet). Every link MUST resolve.
- **FR-025**: The deck MUST be in French. The English side of the site MUST offer a "translation in progress" stub that links to the French deck.
- **FR-026**: Slide styling MUST match the site's existing lecture decks (same look, slide numbers, progress indicator).

### Key Entities

- **Course day**: one of three days; has an agenda, timings, objectives, topic blocks, exercises and a recap.
- **Topic block**: a teaching unit, such as a step of the BdF method or a fundamentals topic. It has concepts, formulas, worked examples, a link to its web page, and an optional flag.
- **Slide**: a unit of the deck. It has a role (agenda, theory, formula, example, exercise brief, focus, recap) and an optional source and date for its figures.
- **Exercise**: a case brief with data, task, team format, duration, prerequisite blocks and an answer key.
- **Focus box**: a real-company illustration with company, year, source and lesson.
- **Source file**: a file in the course folder, with its type, vintage, verdict (core / supporting / outdated / duplicate / irrelevant) and the slides that use it.
- **Coverage map**: records the source of each slide, what happened to each original slide, the definition chosen where sources conflict, and why unused files were left out.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In a dry run, the instructor teaches each of the three days from its deck, opening no other file except the answer-key documents named on the exercise slides, within ±15 minutes of the 6-hour day.
- **SC-002**: 100 % of the original deck's text slides on cotation and the six steps are accounted for in the coverage map, and 100 % of the folder's files have a verdict.
- **SC-003**: A fact-check of every number, scale and regulatory reference finds zero figures presented as current that are outdated, and zero conflicting definitions of the same ratio across the deck.
- **SC-004**: Zero slides consist only of an unreadable picture of text. Every rebuilt table is readable from the back of a classroom and on a laptop screen.
- **SC-005**: Every topic block has at least one worked example. Every exercise in the deck names an existing answer-key document, and zero solutions appear in the public decks.
- **SC-006**: Students reach any day's deck from the course home page in two clicks or fewer, and every deck-to-course link opens an existing page.
- **SC-007**: At least 80 % of students answering the end-of-course survey say the slides helped them follow the class and revise.

## Assumptions

- Audience: INSEEC MSc finance students (four programmes listed in the syllabus) with basic accounting knowledge. The course is taught in French over three in-person days of 6 hours each (18 hours), as stated in the syllabus.
- The Banque de France six-step analysis of consolidated accounts stays the course backbone, as in the original deck and the syllabus.
- The slides are the in-class lecture support. The existing web pages (theory pages, quests, formula sheet) stay the reference.
- The existing exams (`examen-1h`, `examen-final`, `Exam INSEEC`) are not rewritten in this feature. The deck may include one exam-briefing slide.
- Existing case answer keys are reused. Where they rely on the 33⅓ % tax rate, the figures are recomputed or flagged.
- The current French corporate tax rate (25 %) and the BdF scale in force since 2022 are the reference for "current". Facts not found in the folder, or outdated there, are verified against current official sources while the deck is being written (FR-014a). This requires web access during writing.
- The two short BdF videos in the folder are shown in class from their official public location.
- Learner-facing improvements to the web pages (glossary, navigation fixes, etc.) are covered by spec 013. This feature only adds the links the slides need.

## Clarifications

### Session 2026-10-18

- Q: Which storyline should the days follow? → A: Hybrid (option C). The days follow the original deck's progression, extended with fundamentals (Day 1 fundamentals; Day 2 BdF, cotation, consolidation, steps 1–3; Day 3 steps 4–6, cotation decision, focus cases). Each block points to the matching syllabus quest as its in-class activity (FR-003, FR-003a).
- Q: How should the slides be split? → A: One deck per day, 3 decks (FR-001).
- Q: Where do exercise solutions live? → A: Not in the slides. The instructor uses the answer-key documents, and each exercise slide names its key (FR-021, SC-001, SC-005).
- Q: How should the decks handle third-party material (BdF images, BdF videos, Vernimmen excerpts)? → A: Rebuild everything as original text, tables and diagrams with a source line; link to the official videos rather than embedding them; only short quoted Vernimmen figures with citation (FR-022).
- Q: Should facts missing or outdated in the folder be checked against current official sources outside it? → A: Yes. Verify and update them from current official sources (BdF, Légifrance, ANC, IFRS Foundation) and cite them on the slide (FR-014a).
- Q: How much should the decks cover the quests with no lecture block (BMC, regulatory watch, ESG)? → A: A short input block of 3–5 slides each: BMC with step 1 on Day 2; regulatory watch and ESG on Day 3 (FR-003a).
- Q: How do students get the missing data for the CONCOURSMANIA/LECTRA case? → A: Retrieve both companies' 2016 statements from their published annual accounts, present them as readable tables, and keep the existing answer key (FR-017a).
- Q: How long does each course day run? → A: 6 hours of teaching (9:00–12:00, 13:30–16:30), 18 hours in total; blocks beyond that are marked optional (FR-004, SC-001).
- Exercices and answer-key must be recomputed at 25 % tax rate.
