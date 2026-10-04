# Feature Specification: Mathematical Fundamentals — French Version

**Feature Branch**: `008-math-fundamentals-french`

**Created**: 2026-09-17

**Status**: Draft

**Input**: Create a French version for the course mathematical foundation.
Recommendation requested on the best tooling approach (babelquarto or other).

---

## Technology Recommendation

### Why not babelquarto

babelquarto (r-multiverse/babelquarto) uses a **file-suffix pattern**: English
content lives in `chapter.qmd`, French in `chapter.fr.qmd`, all within the
same directory. This directly conflicts with the project constitution's
**Principle VI**, which states:

> "The folder-per-language pattern is the **only accepted implementation**."

Adopting babelquarto would require restructuring the entire site's
multilingual strategy, introduce an R-ecosystem dependency into a
Python/Quarto workflow, and violate a ratified governance principle.

### Recommended approach: folder-per-language (Quarto native)

Use the pattern already mandated and partially configured in the project:

- English: `teaching/mathematical-fundamentals/<file>.qmd`
- French: `fr/teaching/mathematical-fundamentals/<file>.qmd`

This approach:

- Requires **zero new dependencies** — Quarto renders `fr/**/*.qmd` natively
  (already listed in `_quarto.yml` render targets)
- Fully complies with Constitution Principle VI
- Enables per-page `lang: fr` front-matter for correct HTML attributes,
  hyphenation, and accessibility
- Is already partially scaffolded: the `_quarto.yml` has a
  `fr-mathematical-fundamentals` sidebar block for slide stubs
- Supports stub pages ("translation in progress") for pages not yet translated

The only manual work is: translating prose content in each `.qmd` file and
expanding the `_quarto.yml` sidebar block to include reference pages alongside
slides.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — French-Speaking Student Navigates the Full Course (Priority: P1)

A student whose preferred language is French visits the mathematical
fundamentals course. They find every page — the syllabus, all 8 reference
modules, the glossary, the formula sheet, and the learning guide — available
in French, with correct French navigation labels in the sidebar and coherent
prose throughout. They complete the course from start to finish without
needing to switch to English.

**Why this priority**: This is the core goal of the feature. Without full
French reference content, the course cannot be considered bilingual.

**Independent Test**: Can be tested by opening
`fr/teaching/mathematical-fundamentals/index.qmd` in a browser and following
every internal link; all destinations should render French prose without
missing pages or broken links.

**Acceptance Scenarios**:

1. **Given** a student lands on the French course index page, **When** they
   read the page, **Then** all prose — course description, learning
   objectives, module list, assessment table, recommended literature — is in
   French.
2. **Given** a student clicks any module link in the French sidebar,
   **When** the module page loads, **Then** all section headings, explanatory
   prose, callout labels, and exercise instructions are in French while LaTeX
   formulas remain unchanged.
3. **Given** a student opens the French glossary, **When** they look up a
   symbol, **Then** the definition, notation, and pronunciation guide (for
   Greek letters) are in French.

---

### User Story 2 — Instructor Switches Language Mid-Site (Priority: P2)

An instructor is preparing course materials on the English version of the site.
They click the language switcher in the navbar and arrive at the French
counterpart of the current page. They can verify that the French translation
matches the English source before pointing students to it.

**Why this priority**: The language switcher is mandated by Principle VI and
is the primary navigation mechanism between language versions. Without it,
French pages are discoverable only by typing URLs manually.

**Independent Test**: Can be tested from any English math fundamentals page by
clicking the language switcher and confirming the destination page is the
French counterpart with matching content structure.

**Acceptance Scenarios**:

1. **Given** an instructor is on `teaching/mathematical-fundamentals/module-3.qmd`,
   **When** they click the language switcher, **Then** they arrive at
   `fr/teaching/mathematical-fundamentals/module-3.qmd`.
2. **Given** an instructor is on a French module page, **When** they click the
   language switcher, **Then** they arrive at the corresponding English page.
3. **Given** the language switcher is visible, **When** a screen reader
   announces it, **Then** the link label clearly identifies both the target
   language and the current language.

---

### User Story 3 — Student Encounters a Not-Yet-Translated Page (Priority: P3)

A student navigating the French site reaches a page whose full translation has
not yet been completed. Instead of a 404 or a page of English content, they
see a brief French-language stub that acknowledges the translation is in
progress and provides a direct link to the English version.

**Why this priority**: Principle VI prohibits silently absent pages. Stubs
prevent broken navigation and communicate clearly, but they deliver less
student value than fully translated pages.

**Independent Test**: Can be tested by navigating to any declared stub URL and
confirming the page renders in French with a "translation in progress" notice
and a working link to the English counterpart.

**Acceptance Scenarios**:

1. **Given** a student navigates to a French stub page, **When** the page
   loads, **Then** the stub contains: a French title, a short notice in French
   explaining the translation is in progress, and a hyperlink to the English
   counterpart.
2. **Given** a French stub page is rendered, **When** the site is built,
   **Then** it exits without errors (stubs are valid Quarto sources).

---

### User Story 4 — Instructor Delivers Lecture in French with Slide Decks (Priority: P4)

An instructor teaching on a French-language campus opens the French slide deck
for a module. The slides display French prose headings and key explanations
while retaining all LaTeX formulas unchanged. The instructor can deliver the
full lecture in French without switching to the English deck.

**Why this priority**: French slides are the companion to French reference
pages. Spec 007 created English slides and scoped French slides as stubs only;
this feature completes them with full French content.

**Independent Test**: Can be tested by opening any French module slide deck and
verifying that all non-formula text (title, section headers, worked example
labels, summary points) is in French.

**Acceptance Scenarios**:

1. **Given** an instructor opens the French slide deck for Module 1, **When**
   they advance through all slides, **Then** all prose text is in French while
   all LaTeX formulas are identical to the English deck.
2. **Given** a French slide deck is open, **When** the instructor reaches the
   closing slide, **Then** it links to the French reference module page (not
   the English one).

---

### Edge Cases

- What happens when a module has a Shinylive or OJS interactive widget? Widget
  prose labels should be translated in the French `.qmd`; the computation
  code itself is unchanged.
- What if a French translation introduces a different term for a mathematical
  concept? The French glossary is authoritative; the term used in module prose
  must match the glossary entry.
- What if the English source module is updated after the French translation
  exists? The French page must be updated manually; no automated sync is in
  scope for this feature.
- What happens with the `image.jpg` referenced in the English index? Images
  without text are language-neutral and may be referenced by relative path
  from the `fr/` page.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The site MUST provide a French-language version of every page
  in `teaching/mathematical-fundamentals/` at the mirrored path
  `fr/teaching/mathematical-fundamentals/`.
- **FR-002**: Every French page MUST declare `lang: fr` in its Quarto front
  matter.
- **FR-003**: The `_quarto.yml` MUST include a complete French sidebar block
  for the mathematical fundamentals course that mirrors the English sidebar
  structure, covering: course index, all 8 reference modules, all 8 slide
  decks, glossary, formula sheet, and learning guide.
- **FR-004**: A language switcher MUST appear in the site navbar, linking
  between the current page's English and French counterparts. Each direction
  must be labelled clearly (e.g., "FR" / "EN").
- **FR-005**: Every French `.qmd` file MUST be a complete, standalone file
  with fully translated prose. Partial translations using CSS/JS div toggles
  within a single file are forbidden (Principle VI).
- **FR-006**: Pages not yet fully translated MUST render a stub page in
  French containing: a French-language title, a notice in French that the
  translation is in progress, and a hyperlink to the corresponding English
  page.
- **FR-007**: The French course index (`fr/teaching/mathematical-fundamentals/
  index.qmd`) MUST serve as the French syllabus and MUST include: course
  description in French, French learning objectives, session outline linking
  to each French module, course information, and a Recommended Literature
  section (Principle T-VIII).
- **FR-008**: All 8 French reference module pages MUST follow the same
  pedagogical structure as their English counterparts: theory → worked
  examples → exercises with collapsible solutions (Principle T-II).
- **FR-009**: All LaTeX formulas (`$...$` / `$$...$$`) MUST be reproduced
  verbatim in French pages; only surrounding prose is translated.
- **FR-010**: All callout blocks MUST use Quarto's native `.callout-*` divs
  with the same semantic mapping defined in Principle V (`.callout-note` for
  definitions, `.callout-tip` for key formulas, etc.).
- **FR-011**: The French glossary MUST list every mathematical symbol and term
  introduced across the 8 modules with: notation, French plain-language
  definition, and pronunciation guide for Greek letters.
- **FR-012**: The French formula sheet MUST reproduce all formulas from the
  English formula sheet, with section headings and annotations in French.
- **FR-013**: The French learning guide MUST translate all instructional prose
  (study method, error-log instructions) while preserving the same structural
  headings.
- **FR-014**: All 8 French slide decks MUST contain fully translated prose
  (titles, section headers, worked example labels, summary points) with
  LaTeX formulas unchanged, and each closing slide MUST link to the
  corresponding French reference module page.
- **FR-015**: The site MUST render (`quarto render`) with exit code 0 after
  all French pages are added, with both `_freeze/` and `docs/` committed
  alongside source changes (Principle III and Development Workflow).

### Key Entities

- **French course page**: A `.qmd` file at
  `fr/teaching/mathematical-fundamentals/<file>.qmd` with `lang: fr` front
  matter and fully translated prose, mirroring an English source page.
- **French stub page**: A minimal `.qmd` file at the French path that renders
  a "translation in progress" notice in French with a link to the English
  counterpart. Stubs are valid Quarto sources and MUST render without errors.
- **Language switcher**: A navbar element linking between the EN and FR
  counterparts of the current page, present on every page of the site.
- **French sidebar block**: A `_quarto.yml` sidebar entry covering all
  French mathematical fundamentals pages, enabling sidebar navigation on
  French pages.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Every English page in `teaching/mathematical-fundamentals/`
  (index + 8 modules + 8 slide decks + glossary + formula sheet + learning
  guide = 19 pages) has a French counterpart (full translation or stub) at
  `fr/teaching/mathematical-fundamentals/` — verifiable by comparing file
  counts.
- **SC-002**: A French-speaking student can navigate from the course index
  through any module and back to the index using only the French sidebar,
  without encountering a dead link or an English-only page.
- **SC-003**: Switching language from any English math fundamentals page
  reaches the correct French counterpart in exactly 1 click, and vice versa.
- **SC-004**: `quarto render` exits with 0 errors after all French pages are
  created, and the output `docs/` directory contains the rendered French
  HTML files.
- **SC-005**: All 8 French reference module pages pass a structural audit:
  each contains at least one callout of type `.callout-note`, one LaTeX
  formula, one worked example, and one collapsible exercise.
- **SC-006**: The French glossary contains an entry for every symbol that
  appears in the English glossary (entry count parity between EN and FR
  glossary).

---

## Assumptions

- The English mathematical fundamentals course is the **source of truth**;
  the French version is derived from it and must not introduce content that
  does not exist in English.
- **babelquarto is not used**: the folder-per-language pattern mandated by
  Principle VI is the sole multilingual implementation strategy. No new
  Quarto extensions or npm/R packages are introduced for this feature.
- Mathematical notation (LaTeX) requires no translation; only prose is
  translated.
- Images without text labels (e.g., `image.jpg`) are shared between language
  versions by relative path reference and do not require duplication.
- Shinylive and OJS interactive widget computation code is unchanged; only
  prose labels embedded in widget UI (if any) are translated.
- Translation is performed manually or with AI assistance on a per-file basis;
  no automated translation pipeline is in scope.
- The `fr/` directory does not yet exist; this feature creates it from
  scratch.
- The existing `fr-mathematical-fundamentals` sidebar block in `_quarto.yml`
  currently covers only slides (stubs); this feature expands it to cover all
  pages including the index, reference modules, and resource pages.
- A language switcher in the navbar is required by Principle VI but has not
  yet been implemented; its implementation is in scope for this feature.
- French module slide decks replace the stubs mandated by Spec 007 (FR-010)
  with fully translated content; the stub placeholder files created by
  Spec 007 are superseded by this feature.
- `quarto render` must pass for both EN and FR targets before any commit that
  touches `.qmd` sources (Principle VI and Development Workflow).
