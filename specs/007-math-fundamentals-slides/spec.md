# Feature Specification: Mathematical Fundamentals RevealJS Slide Decks

**Feature Branch**: `007-math-fundamentals-slides`

**Created**: 2026-09-15

**Status**: Draft

**Input**: User description: "create slide deck for mathematical-fundamentals
with revealjs to use during lecture. So the web pages are the reference and
the slides are used during lecture time"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Instructor Delivers a Module Lecture (Priority: P1)

The instructor opens the slide deck for a given module on a projected screen
at the start of lecture. They navigate slide by slide through the learning
objectives, core concepts with formulas, and a worked example, then close on
a summary. Students follow along on the projected view. No reference to the
full web page is needed during the lecture itself.

**Why this priority**: This is the primary purpose of the feature. Every
other story depends on having coherent, complete lecture slides per module.

**Independent Test**: Can be tested by loading any single module slide deck
in RevealJS full-screen mode and verifying all key concepts, at least one
formula, and one worked example appear in a logical teaching order, without
requiring the reference web page.

**Acceptance Scenarios**:

1. **Given** the instructor opens `module-1-slides.qmd` in presentation mode,
   **When** they advance through all slides, **Then** all seven core topics
   from Module 1 appear (order of operations, absolute value, powers, square
   roots, fractions, percentages, proportionality) with at least one formula
   each.
2. **Given** a module slide deck is open, **When** the instructor reaches the
   last slide, **Then** a summary of 2–3 key takeaways is visible.
3. **Given** a module slide deck is open, **When** the instructor navigates
   to the worked example slide, **Then** the example is presented in
   step-by-step form across one or more slides.

---

### User Story 2 — Student Reviews Slides After Lecture (Priority: P2)

After the lecture, a student visits the course site and finds the slide deck
for the module just covered. They click through the slides to recap the
session before attempting exercises.

**Why this priority**: High secondary value — slides published on the site
serve as a revision artifact. Students benefit from the same concise format
used in class.

**Independent Test**: Can be tested by navigating to the course sidebar,
finding the slide deck link, opening it in a browser, and confirming that the
full slide sequence is accessible without authentication or downloads.

**Acceptance Scenarios**:

1. **Given** a student is on the course index page, **When** they click the
   link to Module 1 slides in the sidebar, **Then** the RevealJS presentation
   opens in the browser.
2. **Given** a student is viewing a slide deck, **When** they want the full
   reference material, **Then** a visible link or slide directs them to the
   corresponding reference module page.

---

### User Story 3 — Consistent Coverage Across All 8 Modules (Priority: P3)

The instructor verifies that slide decks exist for all 8 modules before the
first lecture week. Each deck follows the same structure and visual style so
preparation time is predictable.

**Why this priority**: Consistency and completeness are important but do not
block the P1 use case; a single module's slides deliver value independently.

**Independent Test**: Can be tested by checking that 8 slide deck files exist,
each renders without errors, and each contains the same section types
(objectives, concepts, worked example, summary, link to reference).

**Acceptance Scenarios**:

1. **Given** all 8 module slide decks have been created, **When** the
   instructor renders the full site, **Then** all 8 decks appear in the
   course sidebar without errors.
2. **Given** any two module slide decks, **When** a reviewer compares their
   section structure, **Then** both contain: title, learning objectives, core
   concepts, worked example, summary, and reference link.

---

### Edge Cases

- What happens when a module has more core concepts than fit comfortably on
  a slide (e.g., Module 1 with 7 topics)? Each concept gets its own slide;
  overflow is split across slides rather than compressed.
- How does the site handle interactive OJS/Shinylive elements from the
  reference pages in the slide context? Interactive demos are omitted from
  slides; a static illustration or a "see reference page" note replaces them.
- What if a student views the slides on a small screen? RevealJS handles
  responsive scaling natively; no additional breakpoint work is required.
- Module 8 (Revision) has no new content — its slide deck is a curated
  cross-module review, not a repetition of the other seven decks.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The site MUST include one RevealJS slide deck per module (8
  total), each backed by a `.qmd` source file in the
  `teaching/mathematical-fundamentals/` directory.
- **FR-002**: Each slide deck MUST be registered in the course sidebar block
  in `_quarto.yml` so it appears in the site navigation.
- **FR-003**: Each slide deck MUST open in Quarto's RevealJS presentation
  format (not as a standard HTML page).
- **FR-004**: Each slide deck MUST contain, in order: module title slide,
  learning objectives slide(s), one slide per core concept (with key formula
  or rule), worked example slide(s), summary slide, and a closing "Reference"
  slide linking to the full module page.
- **FR-005**: Formulas MUST be rendered using standard LaTeX syntax
  (`$...$` / `$$...$$`) within slides.
- **FR-006**: Slides MUST NOT include OJS or Shinylive interactive blocks;
  where a demo exists in the reference page, the slides MUST show a static
  equivalent or a note directing students to the reference page.
- **FR-007**: The pedagogical order on each slide deck MUST mirror the
  reference page: theory first, then worked example, then summary.
- **FR-008**: Each slide deck MUST include a visible, clickable link back to
  the corresponding reference module page (either on the closing slide or in
  the slide footer).
- **FR-009**: Slide decks MUST render reproducibly from the committed
  `_freeze/` cache; no Python re-execution should be required.
- **FR-010**: A bilingual French stub slide deck MUST exist for each module
  under the `fr/teaching/mathematical-fundamentals/` path, containing at
  minimum the module title and a "translation in progress" notice with a link
  to the English slides, in accordance with the bilingual content strategy.

### Key Entities

- **Slide Deck**: A RevealJS `.qmd` file paired with a module, containing a
  structured sequence of slides for lecture use. Each deck maps 1-to-1 with
  a reference module page.
- **Reference Page**: The existing full-content module `.qmd` (e.g.,
  `module-1.qmd`), unchanged by this feature. The slide deck is a companion,
  not a replacement.
- **Module**: One of the 8 teaching units of the Mathematical Fundamentals
  course, each covering a defined mathematical topic with a business
  application angle.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 8 module slide decks exist, render without errors, and are
  reachable via the course sidebar — verifiable by running `quarto render`
  and confirming 0 errors and 8 slide deck URLs in the output.
- **SC-002**: An instructor can navigate from the first slide to the last of
  any module deck in under 10 minutes, covering all core concepts listed in
  the corresponding reference page's learning objectives.
- **SC-003**: Every core concept that appears in the reference page's
  "Core Concepts" section has a corresponding slide in the deck — no concept
  is silently omitted.
- **SC-004**: Each slide deck contains a working hyperlink to its reference
  module page, verifiable by following the link in a browser.
- **SC-005**: French stub decks exist for all 8 modules and render without
  errors.

## Assumptions

- The existing 8 module `.qmd` reference pages remain completely unchanged;
  slides are additive artifacts.
- Slide decks are published on the site and accessible to students after
  each lecture (they are not private or password-protected).
- No speaker-note section is required in v1; the slide format MUST accommodate
  future addition of speaker notes without structural rework.
- Interactive OJS/Shinylive simulations from the reference pages are out of
  scope for slides; static equivalents (formula + key result) are acceptable.
- The site's existing dark theme (`assets/dark.scss`) applies globally;
  RevealJS-specific styling adjustments (if any) MUST use the same file.
- French slide stubs are minimal (title + "translation in progress" + link to
  English counterpart) and are not considered full translations; full French
  slide content is out of scope for this feature.
- Slides are named using a consistent convention:
  `module-N-slides.qmd` (English) and the French mirror under `fr/`.
- Module 8 slides serve as a cross-module revision deck rather than
  introducing new material.
