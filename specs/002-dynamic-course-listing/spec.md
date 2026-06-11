# Feature Specification: Dynamic Course Listing

**Feature Branch**: `002-dynamic-course-listing`

**Created**: 2026-06-11

**Status**: Draft

**Input**: Transform `teaching.qmd` into a dynamic listing page that automatically displays all courses from the `teaching/` directory.

## User Scenarios & Testing

### User Story 1 - Site Visitor Discovers Organized Course Catalog (Priority: P1)

A site visitor navigates to the teaching page and immediately sees all available courses organized into three logical categories: Graduate, Undergraduate, and AI Guide. The courses are displayed as attractive grid cards showing the course title, institution/school, description, and a clickable link to access the course materials. The page requires no manual updates when new courses are added to the teaching directory.

**Why this priority**: This is the core value proposition of the feature. Site visitors need to quickly discover and access all available courses without navigating through multiple pages or encountering missing/outdated listings. This is the main user journey that drives engagement with course materials.

**Independent Test**: Can be fully tested by loading the teaching page and verifying that (1) all 6 existing courses appear in their correct categories, (2) each course displays title, institution, description, and link, and (3) the layout is properly organized into three distinct sections with grid formatting.

**Acceptance Scenarios**:

1. **Given** the teaching page is loaded, **When** the page renders, **Then** six courses are visible (inseec-finance, ece-proba, essca-stat, mathematical-analysis, ai-papers, ai-dev) organized into three labeled sections
2. **Given** courses are displayed, **When** viewing the Graduate section, **Then** only inseec-finance is shown; Undergraduate section shows ece-proba, essca-stat, mathematical-analysis; AI Guide shows ai-papers, ai-dev
3. **Given** a course card is displayed, **When** viewing the card, **Then** it shows course title, institution/school, description excerpt, and a clickable link button
4. **Given** a course link is clicked, **When** the link is activated, **Then** the browser navigates to the course landing page (e.g., `teaching/inseec-finance/index.qmd`)
5. **Given** the page layout is rendered, **When** viewing on different screen sizes, **Then** the grid layout adapts appropriately (maintains visual hierarchy on mobile/tablet/desktop)

---

### User Story 2 - Site Maintainer Adds New Course Automatically (Priority: P2)

A site maintainer creates a new course directory under `teaching/` with an `index.qmd` file containing proper metadata (title, institution, abstract). When the teaching page is rebuilt, the new course automatically appears in the appropriate section without requiring any manual updates to `teaching.qmd` or course registration.

**Why this priority**: Eliminates manual maintenance overhead and ensures consistency. As courses are added/removed, the page stays current without developer intervention. Enables scalability and reduces risk of outdated course listings.

**Independent Test**: Can be fully tested by (1) creating a new test course directory with index.qmd and metadata, (2) rebuilding the site, and (3) verifying the course appears in the correct section without any manual configuration in teaching.qmd.

**Acceptance Scenarios**:

1. **Given** a new course directory is created at `teaching/new-course/` with a properly formatted `index.qmd`, **When** the site is rebuilt, **Then** the course automatically appears on the teaching page
2. **Given** a course is added, **When** the course has metadata indicating its category (Graduate/Undergraduate/AI), **Then** it appears in the correct section
3. **Given** course metadata is incomplete, **When** the course lacks a title or abstract, **Then** the page still renders without errors and displays available metadata

---

### User Story 3 - Course Discovery and Filtering at Scale (Priority: P3)

As the course catalog grows beyond the current 6 courses, the page remains performant and organized. The three-section layout scales gracefully to accommodate many courses, and future enhancements (like search or filtering) are feasible due to the automated discovery mechanism.

**Why this priority**: Prepares the system for future growth and maintains performance as new courses are added. While not critical for the initial 6 courses, this ensures the solution is sustainable long-term.

**Independent Test**: Can be tested by adding multiple courses to each section and verifying the page still loads quickly and maintains proper organization without performance degradation.

**Acceptance Scenarios**:

1. **Given** 15+ courses exist across three sections, **When** the page loads, **Then** all courses are displayed and the page load time remains under 3 seconds
2. **Given** many courses in one section, **When** viewing the grid, **Then** layout adapts naturally (wrapping to multiple rows as needed)

---

### Edge Cases

- What happens when a course directory exists but lacks an `index.qmd` file? (Course should be skipped/excluded from listing)
- How does the system handle malformed metadata in `index.qmd` files? (Page renders without errors; missing metadata fields display as empty/default values)
- What if a course has no `abstract` metadata? (First paragraph or a sensible default is used for description)
- How are courses categorized if metadata doesn't specify a category? (Category is inferred from directory name or predefined mapping, e.g., `ai-*` → AI Guide)
- What happens if `teaching/` directory is empty? (Page renders gracefully, displaying all three sections as empty with appropriate messaging)

## Requirements

### Functional Requirements

- **FR-001**: System MUST automatically discover all `index.qmd` files in subdirectories of `teaching/` without manual configuration or hardcoding
- **FR-002**: System MUST exclude all non-`index.qmd` files from the course listing (e.g., lecture notes, assets, other `.qmd` files)
- **FR-003**: System MUST categorize discovered courses into three sections: Graduate, Undergraduate, and AI Guide
- **FR-004**: System MUST extract and display course title from the `title` metadata field in each `index.qmd` YAML front matter
- **FR-005**: System MUST extract and display course institution/school from metadata if available (e.g., `institution` or `school` field)
- **FR-006**: System MUST extract and display course description from the `abstract` metadata field, or fall back to the first paragraph of content if abstract is absent
- **FR-007**: System MUST display courses using Quarto's grid system (`.grid` and `.g-col` classes) to create a responsive card layout
- **FR-008**: System MUST provide clickable links for each course that point to the course landing page (e.g., `teaching/course-name/index.qmd`)
- **FR-009**: System MUST maintain backward compatibility with existing course pages (no breaking changes to course structure or metadata expectations)
- **FR-010**: System MUST render the teaching page without errors when courses are added, removed, or modified, without requiring changes to the `teaching.qmd` file itself

### Key Entities

- **Course**: A course landing page represented by a directory under `teaching/` containing an `index.qmd` file. Attributes include:
  - `directory_name`: Slug identifying the course (e.g., `inseec-finance`)
  - `title`: Human-readable course name (from metadata)
  - `institution`: School/university offering the course (from metadata, optional)
  - `abstract`: Short course description (from metadata or first paragraph)
  - `link`: URL path to course landing page
  - `category`: One of "Graduate", "Undergraduate", or "AI Guide"

- **Course Section**: A grouping of courses by category (Graduate, Undergraduate, AI Guide). Contains:
  - `section_name`: Display name of the section
  - `courses`: List of Course entities in this section
  - `grid_layout`: Quarto grid formatting (e.g., `.g-col-6` for two-column layout)

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 6 existing courses (inseec-finance, ece-proba, essca-stat, mathematical-analysis, ai-papers, ai-dev) automatically display on teaching page in correct categories without any hardcoded course references in `teaching.qmd`
- **SC-002**: Teaching page loads and fully renders all courses within 2 seconds on standard broadband connection (no performance degradation compared to current manual layout)
- **SC-003**: Adding a new course directory to `teaching/` with proper `index.qmd` and metadata results in automatic display on page within one site rebuild cycle
- **SC-004**: Course grid layout displays consistently across desktop (1920×1080), tablet (768×1024), and mobile (375×667) viewports with proper responsive behavior
- **SC-005**: 100% of courses display all four required elements: title, institution, description, and clickable link
- **SC-006**: Page rendering handles missing or malformed metadata gracefully without breaking the layout or throwing display errors
- **SC-007**: Site maintainer can add a new course to `teaching/` directory and verify its appearance on the teaching page without needing to edit `teaching.qmd` or any template files

## Assumptions

- **Quarto Processing**: The site uses Quarto for rendering all `.qmd` files. Dynamic course discovery will rely on Quarto's templating and/or JavaScript functionality to scan the teaching directory at build time or runtime.
- **Metadata Standards**: All course `index.qmd` files follow YAML front matter conventions with `title` and `abstract` metadata fields. Not all fields are mandatory; the system gracefully handles missing optional fields.
- **Course Categorization**: Courses are categorized based on a predefined mapping that can be embedded in metadata or inferred from directory naming conventions (e.g., `ai-*` directories → AI Guide section). The current 6 courses fit into the three specified categories.
- **Directory Structure**: The `teaching/` directory contains only course subdirectories (no files at root level). Each course directory contains an `index.qmd` file.
- **Build Process**: Site is rebuilt using standard Quarto CLI commands when courses are added, removed, or modified. Changes take effect after rebuild.
- **Backward Compatibility**: Existing course `index.qmd` files are not modified; the feature only changes how `teaching.qmd` renders and displays course information.
- **No Database Required**: Course discovery relies on the file system; no external database or API is required. This keeps the solution simple and self-contained.
- **Link Format**: Course landing pages are accessible via relative URLs from `teaching.qmd` (e.g., `teaching/course-name/index.qmd` or equivalently, the rendered HTML path).
- **UI Framework**: Grid layout uses Quarto's built-in `.grid` system (Bootstrap), no additional CSS frameworks required.
