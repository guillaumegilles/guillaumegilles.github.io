# Feature Specification: Course Syllabus Index Pages

**Feature Branch**: `001-course-syllabus-index`

**Created**: 2026-05-31

**Status**: Draft

**Input**: Every teaching course root MUST have an `index.qmd` that serves as
the course syllabus. It MUST be the first sidebar entry and MUST include a
Recommended Literature section listing primary textbooks and supplementary
references with author(s), title, edition, and publisher.

---

## Clarifications

### Session 2026-06-01

- Q: What format should the Recommended Literature section use? → A: Markdown table with fixed columns (Author | Title | Edition | Publisher), one row per reference.
- Q: What format should the session outline use? → A: Markdown table with columns `| # | Session Title | Topics Covered |`, session title linking to the session file.
- Q: What should a FR bilingual stub contain? → A: EN course title as the page title, a "translation in progress" callout block in French, and a direct link to the EN syllabus.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Student finds the course reading list (Priority: P1)

A student arrives at a course page for the first time and needs to know what
to buy or borrow before the first session.

**Why this priority**: The recommended literature is the primary actionable
information a new student needs. Everything else is secondary.

**Independent Test**: Navigate to any `teaching/<course>/` URL; a syllabus
page is present with a populated "Recommended Literature" section containing
at least one entry. Delivers standalone value as a course entry point.

**Acceptance Scenarios**:

1. **Given** a visitor navigates to `teaching/essca-stat/`, **When** the page
   loads, **Then** they see a course description, a session outline, and a
   "Recommended Literature" section listing textbooks with author, title,
   edition, and publisher.
2. **Given** the sidebar for any course, **When** a visitor looks at the
   navigation links, **Then** the course `index.qmd` appears as the first
   entry before any session pages.
3. **Given** a literature entry, **When** a visitor reads it, **Then** it
   contains at minimum: author(s), full title, edition, and publisher.

---

### User Story 2 — Instructor updates the reading list (Priority: P2)

An instructor wants to swap a textbook edition or add a supplementary
reference to a course without touching the session content files.

**Why this priority**: Literature changes are routine maintenance; having a
single authoritative location makes updates fast and prevents stale references
scattered across session files.

**Independent Test**: Edit the `index.qmd` literature table for one course,
run `quarto render`, verify the updated entry appears on the rendered page and
no session file needed changing.

**Acceptance Scenarios**:

1. **Given** the course `index.qmd`, **When** an instructor edits the
   Recommended Literature section, **Then** the change is reflected on the
   published page after a render without editing any other file.
2. **Given** a course with supplementary references, **When** the instructor
   adds a new row to the literature table, **Then** the render succeeds and
   the new entry appears in the correct section.

---

### User Story 3 — French-language visitor reads the syllabus (Priority: P3)

A French-speaking student navigates to the FR counterpart of a course syllabus
and finds a translated stub or full translation of the syllabus including the
literature section.

**Why this priority**: Principle VI requires EN/FR parity. A syllabus only in
English fails this requirement.

**Independent Test**: Navigate to `fr/teaching/<course>/`; either a full
French syllabus or a "translation in progress" stub with a link to the English
version is rendered.

**Acceptance Scenarios**:

1. **Given** a course with an English `index.qmd`, **When** a visitor
   navigates to `fr/teaching/<course>/`, **Then** they see either a complete
   French syllabus or a bilingual stub — never a 404.
2. **Given** a stub page, **When** a visitor views it, **Then** it shows the
   EN course title, a French "traduction en cours" callout, and a direct link
   to the English syllabus.

---

### Edge Cases

- What if a (future) course has session pages but no `index.qmd`? → An
  `index.qmd` MUST be created; the course is considered incomplete without one.
  (All six current courses already have one — see Assumptions.)
- What if a course has no fixed textbook (e.g., paper-reading seminars)?
  → The literature section MUST still exist; it may list primary papers or
  online resources in lieu of books, but the section heading MUST be present.
- What if a literature entry has no edition (e.g., online resource or working
  paper)? → Edition is listed as "N/A" or omitted with a note; author, title,
  and publisher/source remain mandatory.
- What if the FR counterpart `index.qmd` does not yet exist? → A stub file
  MUST be created per Principle VI; the stub is not considered a full syllabus
  but it prevents a broken navigation entry.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Every course under `teaching/` MUST have an `index.qmd` at its
  root directory.
- **FR-002**: Each `index.qmd` MUST include a course description paragraph and
  a set of learning objectives.
- **FR-003**: Each `index.qmd` MUST include a session outline as a Markdown
  table with columns `| # | Session Title | Topics Covered |`. The Session
  Title cell MUST be a Markdown link pointing to the corresponding session
  file.
- **FR-004**: Each `index.qmd` MUST include a "Recommended Literature" section
  with at least one entry.
- **FR-005**: Every Recommended Literature entry MUST be formatted as a row in
  a Markdown table with fixed columns: `| Author(s) | Title | Edition | Publisher/Source |`.
  For entries with no edition (e.g., online resources), the Edition cell MUST
  contain "N/A". For papers (FR-009), the columns map as:
  Author(s) | Title | Year | Publication Venue.
- **FR-006**: The course `index.qmd` MUST be registered as the first entry of
  its course sidebar block in `_quarto.yml`.
- **FR-007**: The `index.qmd` front matter MUST declare `lang: en` (or `lang:
  fr` for French variants) and include a `title` and `date-modified` field.
- **FR-008**: A FR counterpart (`fr/teaching/<course>/index.qmd`) MUST exist
  for every EN syllabus. If a full translation is not yet available, the stub
  MUST contain: (1) the EN course title as the Quarto `title` front-matter
  field, (2) `lang: fr` in front matter, (3) a `.callout-note` block in French
  with a "traduction en cours" notice, and (4) a Markdown link to the EN
  syllabus (`../../../teaching/<course>/index.qmd`).
- **FR-009**: Courses that use papers rather than books (e.g., `ai-papers`)
  MUST list their primary readings in the literature section, using the paper's
  authors, title, year, and publication venue in place of edition/publisher.

### Key Entities

- **Course Syllabus** (`index.qmd`): The entry-point document for a course.
  Attributes: title, lang, date-modified, description, learning objectives,
  session outline, recommended literature.
- **Literature Entry**: A single reading recommendation formatted as a table row.
  Mandatory columns: Author(s), Title, Edition (or "N/A"), Publisher/Source.
  For papers: Author(s), Title, Year, Publication Venue. Optional extra column: URL.
- **Bilingual Stub**: A minimal FR `index.qmd` for a course not yet fully
  translated. Required: `title` = EN course title, `lang: fr`, a
  `.callout-note` block in French with "traduction en cours" notice, and a
  link to the EN syllabus. Treated as a placeholder; not a complete syllabus.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 6 courses under `teaching/` have an `index.qmd` that renders
  without errors (`quarto render` exits 0).
- **SC-002**: 100% of course `index.qmd` files contain a non-empty Recommended
  Literature section before the feature branch is merged.
- **SC-003**: Every course `index.qmd` is the first item in its sidebar block
  in `_quarto.yml`; no course page is reachable from the sidebar before the
  syllabus.
- **SC-004**: Every EN syllabus has a corresponding FR file (full translation
  or stub) so that navigating to `fr/teaching/<course>/` never returns a 404.
- **SC-005**: A reviewer can find the textbook author, title, edition, and
  publisher for every course's primary resource within 10 seconds of landing
  on the syllabus page.

---

## Assumptions

- The six courses currently present (`ai-dev`, `ai-papers`, `ece-proba`,
  `essca-stat`, `inseec-finance`, `mathematical-analysis`) are the full scope;
  new courses added later will follow T-VIII by constitution.
- `essca-stat` and `inseec-finance` already have `index.qmd` files — these
  need amendment to add literature sections, not full rewrites.
- **Correction (confirmed during planning)**: all six courses already have an
  `index.qmd` (`ai-papers`, `ece-proba`, and `mathematical-analysis` included).
  This feature therefore *amends* existing files; it does not create new ones.
- FR counterpart stubs (not full translations) are acceptable for the initial
  merge; full translations are a follow-on task.
- Literature lists for paper-reading courses (`ai-papers`) may reference
  foundational papers (e.g., "Attention Is All You Need") rather than books.
- The `_quarto.yml` sidebar entries (including the broken `ece-proba`
  reference) will need updating — this is in scope for this feature.

---

## Out of Scope / Deferred

These items are intentionally **not** delivered by this feature and are tracked
for a separate **language-normalization** feature. Principle VI (full EN+FR
parity) is therefore only **partially** satisfied here; this is a consciously
recorded deviation, not a reinterpretation of the principle.

- **Full bilingual parity for FR-authored courses**: `inseec-finance`,
  `ece-proba`, and `mathematical-analysis` are authored in French at the site
  root. Relocating them under `fr/` with English root counterparts is a
  site-wide migration and is deferred. No `en/` tree is created by this feature.
- **Navbar language switcher** (Principle VI): not added here. Adding a working
  EN⇄FR switcher belongs to the language-normalization feature once both
  language trees exist.
- **Full translations**: only French *stubs* are produced for the three
  EN-authored courses; complete translations are follow-on work.
