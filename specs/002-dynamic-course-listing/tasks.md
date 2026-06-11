# Tasks: Dynamic Course Listing

**Feature Branch**: `002-dynamic-course-listing`  
**Date Generated**: 2026-06-11  
**Feature Location**: `specs/002-dynamic-course-listing/`  
**Repository**: `guillaumegilles/guillaumegilles.github.io`

---

## Executive Summary

Transform `teaching.qmd` from a hardcoded course listing into a dynamic discovery system that automatically displays all courses from the `teaching/` directory, organized into three sections: Graduate, Undergraduate, and AI Guide.

**Total Tasks**: 15  
**Phases**: 5 (Setup → Foundational → 3 User Stories → Polish)  
**Estimated Effort**: ~4 hours  
**MVP Scope**: Phase 1 Setup + Phase 3 (User Story 1 core implementation)

---

## Implementation Strategy

### Phase-Based Execution
1. **Phase 1 (Setup)**: Project initialization and validation (~15 min)
2. **Phase 2 (Foundational)**: N/A — no blocking prerequisites
3. **Phase 3 (US1)**: Core listing implementation (~1.5 hours) — **MVP SCOPE**
4. **Phase 4 (US2)**: Metadata validation and automation (~1 hour)
5. **Phase 5 (US3)**: Scalability testing and performance (~1 hour)
6. **Phase 6 (Polish)**: Documentation and final validation (~30 min)

### Dependency Graph

```
Phase 1 (Setup)
    ↓
Phase 3 (US1) ← DEPENDS ON: Phase 1
    ↓
Phase 4 (US2) ← DEPENDS ON: Phase 3
    ↓
Phase 5 (US3) ← DEPENDS ON: Phase 4
    ↓
Phase 6 (Polish) ← DEPENDS ON: Phase 5
```

### Parallel Execution Opportunities
- **T005, T006, T007** (metadata audits) can run in parallel
- **T012, T013** (scalability testing) can run in parallel after T009

---

## Phase 1: Setup & Validation

**Goal**: Validate project structure, understand Quarto listings capabilities, and prepare for implementation.

**Independent Test Criteria**:
- ✅ All 6 existing courses verified in `teaching/` directory
- ✅ Each course has `index.qmd` with valid YAML front matter
- ✅ Quarto v1.4+ is installed and accessible
- ✅ Current `teaching.qmd` renders successfully
- ✅ Project structure aligns with plan.md requirements

**Tasks**:

- [ ] T001 Audit existing teaching directory structure and course index files in `teaching/`

  **Acceptance**: Verify all 6 courses (ai-dev, ai-papers, ece-proba, essca-stat, inseec-finance, mathematical-analysis) have `index.qmd` with valid YAML front matter containing at least `title` field.

  **Action**: List all subdirectories, check each has `index.qmd`, validate YAML structure, document findings.

- [ ] T002 Verify Quarto version and listings feature availability

  **Acceptance**: Confirm Quarto ≥ 1.4 is installed and `quarto --version` output shows version number.

  **Action**: Run `quarto --version`, verify ≥ 1.4, test Quarto preview with existing course page.

- [ ] T003 Create backup of current teaching.qmd before modifications

  **Acceptance**: Copy current `teaching.qmd` to `teaching.qmd.backup` at repository root.

  **Action**: `cp teaching.qmd teaching.qmd.backup`

- [ ] T004 Validate current teaching.qmd renders successfully in preview mode

  **Acceptance**: Run `quarto preview teaching.qmd`, verify page loads without errors in browser.

  **Action**: Run preview command, load page, verify all 6 courses visible in current hardcoded layout.

---

## Phase 2: Foundational (N/A)

No foundational/blocking prerequisites identified. Phase 3 tasks can proceed immediately after Phase 1.

---

## Phase 3: User Story 1 — Site Visitor Discovers Organized Course Catalog (P1)

**Goal**: Implement core dynamic course listing using Quarto listings feature. Site visitors see all courses automatically organized into three category sections.

**Independent Test Criteria**:
- ✅ All 6 courses appear on teaching page without hardcoding
- ✅ Courses display in correct category sections (Graduate=1, Undergraduate=3, AI Guide=2)
- ✅ Each course card displays title, and clickable link
- ✅ Grid layout is responsive (tested on desktop, tablet, mobile)
- ✅ Page load time < 2 seconds
- ✅ Rendering produces no errors

**Dependencies**: ← Phase 1 (Setup complete)

**Tasks**:

- [ ] T005 [P] Audit metadata in all 6 course index.qmd files for Quarto listings compatibility

  **File Path**: All courses in `teaching/*/index.qmd`

  **Acceptance**: Document all `title`, `description`/`abstract`, and optional `date-modified` fields for each course. Identify any missing required fields.

  **Action**: Check YAML front matter in all 6 index.qmd files:
  - `teaching/ai-dev/index.qmd`
  - `teaching/ai-papers/index.qmd`
  - `teaching/ece-proba/index.qmd`
  - `teaching/essca-stat/index.qmd`
  - `teaching/inseec-finance/index.qmd`
  - `teaching/mathematical-analysis/index.qmd`

- [ ] T006 [P] Add missing metadata fields to course index.qmd files

  **File Paths**: `teaching/*/index.qmd` (update YAML front matter as needed)

  **Acceptance**: All 6 course index.qmd files have `title` and `abstract`/`description` fields. Empty descriptions are acceptable; system will gracefully render them.

  **Action**: For each course lacking `abstract` or `description`, add a brief description (1-2 sentences) to YAML front matter. Prioritize completeness; can improve descriptions in Polish phase.

- [ ] T007 [P] Document course categorization mapping

  **File Path**: Create inline documentation in `teaching.qmd` YAML comments

  **Acceptance**: Clear mapping of courses to categories documented:
  - Graduate: inseec-finance
  - Undergraduate: ece-proba, essca-stat, mathematical-analysis
  - AI Guide: ai-papers, ai-dev

  **Action**: Create reference table in spec notes; will guide listing configuration.

- [ ] T008 [US1] Update teaching.qmd front matter with listing configuration

  **File Path**: `teaching.qmd` (YAML front matter)

  **Acceptance**: Front matter contains three `listing` entries (graduate-courses, undergrad-courses, ai-guide-courses) with correct glob patterns or explicit file lists.

  **Action**: Add to YAML front matter:
  ```yaml
  listing:
    - id: graduate-courses
      contents: teaching/inseec-finance/index.qmd
      type: grid
      sort: title
    - id: undergrad-courses
      contents:
        - teaching/ece-proba/index.qmd
        - teaching/essca-stat/index.qmd
        - teaching/mathematical-analysis/index.qmd
      type: grid
      sort: title
    - id: ai-guide-courses
      contents:
        - teaching/ai-papers/index.qmd
        - teaching/ai-dev/index.qmd
      type: grid
      sort: title
  ```

- [ ] T009 [US1] Replace hardcoded grid sections with Quarto listing placeholders

  **File Path**: `teaching.qmd` (content sections)

  **Acceptance**: All hardcoded grid HTML (::::, ::: {.g-col-6}, etc.) replaced with simple div placeholders. Three section headers remain: "Graduate", "Undergraduate", "AI Guide".

  **Action**: Replace content sections with:
  ```markdown
  ## Graduate
  
  :::{#graduate-courses}
  :::
  
  ## Undergraduate
  
  :::{#undergrad-courses}
  :::
  
  ## AI Guide
  
  :::{#ai-guide-courses}
  :::
  ```

- [ ] T010 [US1] Test teaching.qmd rendering with Quarto preview

  **File Path**: `teaching.qmd`

  **Acceptance**: 
  - ✅ Page loads without errors
  - ✅ All 6 courses appear in grid layout
  - ✅ Courses organized into three sections
  - ✅ Each course displays as clickable card
  - ✅ Responsive layout verified on desktop

  **Action**: Run `quarto preview teaching.qmd`, load page in browser, verify all criteria.

- [ ] T011 [US1] Validate course links and navigation on rendered page

  **File Path**: `teaching.qmd` (rendered HTML output)

  **Acceptance**: Click each course link; verify browser navigates to correct course landing page (e.g., `teaching/inseec-finance/index.qmd`).

  **Action**: Test all 6 course links in rendered page; verify correct destination.

---

## Phase 4: User Story 2 — Site Maintainer Adds New Course Automatically (P2)

**Goal**: Validate that new courses automatically appear on the teaching page without manual configuration. Ensure metadata extraction and categorization work correctly.

**Independent Test Criteria**:
- ✅ New course added to `teaching/test-course/` with `index.qmd`
- ✅ Site rebuilds without manual `teaching.qmd` updates
- ✅ New course appears in correct category section
- ✅ Course metadata displays correctly (title, description, link)
- ✅ No errors or broken layouts

**Dependencies**: ← Phase 3 (US1 complete) — T009, T010

**Tasks**:

- [ ] T012 [US2] Create test course directory with index.qmd and metadata

  **File Path**: `teaching/test-course/index.qmd`

  **Acceptance**: New test course directory exists with valid `index.qmd` containing YAML front matter with `title` and `abstract` fields.

  **Action**: Create directory and file:
  ```bash
  mkdir -p teaching/test-course
  ```
  Create `teaching/test-course/index.qmd` with:
  ```yaml
  ---
  title: "Test Course"
  abstract: "A test course for validating dynamic listing behavior."
  date-modified: 2026-06-11
  ---

  ## Overview
  This is a test course for validating the dynamic course listing system.
  ```

- [ ] T013 [US2] Add test course to appropriate category in teaching.qmd listing

  **File Path**: `teaching.qmd` (YAML front matter)

  **Acceptance**: Test course added to one of the three listing sections (e.g., added to undergrad-courses for testing).

  **Action**: Update `undergrad-courses` listing to include `teaching/test-course/index.qmd`:
  ```yaml
  - id: undergrad-courses
    contents:
      - teaching/ece-proba/index.qmd
      - teaching/essca-stat/index.qmd
      - teaching/mathematical-analysis/index.qmd
      - teaching/test-course/index.qmd  # NEW
    type: grid
    sort: title
  ```

- [ ] T014 [US2] Rebuild site and verify test course appears

  **File Path**: `teaching.qmd` (rendered output)

  **Acceptance**: 
  - ✅ Site rebuilds successfully (`quarto render`)
  - ✅ Test course appears in "Undergraduate" section
  - ✅ Course card displays title "Test Course" and description
  - ✅ Course link works correctly

  **Action**: Run `quarto render`, verify test course appears on teaching page with correct metadata.

- [ ] T015 [US2] Remove test course and verify section updates dynamically

  **File Path**: `teaching/test-course/` directory and `teaching.qmd`

  **Acceptance**: 
  - ✅ Test course directory removed
  - ✅ Test course listing removed from `teaching.qmd`
  - ✅ Site rebuilds successfully
  - ✅ Test course no longer appears on page

  **Action**: Delete test course directory and remove from listing, run `quarto render`, verify removal.

---

## Phase 5: User Story 3 — Course Discovery and Filtering at Scale (P3)

**Goal**: Validate performance and layout behavior as course catalog grows. Ensure system scales gracefully to 50+ courses.

**Independent Test Criteria**:
- ✅ Multiple courses (15+) render without performance degradation
- ✅ Page load time remains < 3 seconds
- ✅ Grid layout wraps correctly across multiple rows
- ✅ Responsive layout maintained on all screen sizes
- ✅ No memory or rendering errors

**Dependencies**: ← Phase 4 (US2 complete)

**Tasks**:

- [ ] T016 [P] [US3] Create 5 additional test courses in each category

  **File Paths**: 
  - `teaching/test-grad-1/index.qmd` through `teaching/test-grad-3/index.qmd`
  - `teaching/test-undergrad-1/index.qmd` through `teaching/test-undergrad-3/index.qmd`
  - `teaching/test-ai-1/index.qmd` through `teaching/test-ai-3/index.qmd`

  **Acceptance**: 9 test course directories created, each with valid `index.qmd` and YAML metadata.

  **Action**: Create test courses using script or manual creation. Each should have unique title and description for identification.

- [ ] T017 [P] [US3] Add test courses to listing configuration temporarily

  **File Path**: `teaching.qmd` (YAML front matter)

  **Acceptance**: All test courses added to appropriate listing sections.

  **Action**: Update all three listing entries to include test courses (total 15 courses: 4 graduate, 6 undergraduate, 5 ai-guide).

- [ ] T018 [US3] Measure page load time and performance with 15 courses

  **File Path**: `teaching.qmd` (rendered output)

  **Acceptance**: 
  - ✅ Page load time < 3 seconds (measured via browser DevTools)
  - ✅ No errors in browser console
  - ✅ Grid layout adapts naturally to 15 courses

  **Action**: Rebuild site, measure load time, verify performance goals met.

- [ ] T019 [P] [US3] Test responsive layout on mobile, tablet, and desktop

  **File Path**: `teaching.qmd` (rendered output)

  **Acceptance**: 
  - ✅ Desktop (1920×1080): Grid displays multiple columns
  - ✅ Tablet (768×1024): Grid adapts to 2 columns
  - ✅ Mobile (375×667): Grid adapts to single column
  - ✅ All courses visible and navigable on all screen sizes

  **Action**: Test using browser DevTools device emulation on all three breakpoints.

- [ ] T020 [US3] Clean up test courses and restore original state

  **File Paths**: 
  - `teaching/test-*/` directories
  - `teaching.qmd` listing configuration

  **Acceptance**: All test courses removed, `teaching.qmd` restored to show only original 6 courses.

  **Action**: Remove all test course directories and revert listing configuration to original 6 courses only.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Documentation, final validation, and production readiness.

**Independent Test Criteria**:
- ✅ All documentation complete and accurate
- ✅ Code follows project conventions
- ✅ All 6 original courses verified present and correct
- ✅ No hardcoded course references remain in `teaching.qmd`
- ✅ Backward compatibility maintained with existing course pages
- ✅ Site renders successfully from clean clone

**Dependencies**: ← Phase 5 (US3 complete)

**Tasks**:

- [ ] T021 Verify all course metadata has complete and consistent fields

  **File Paths**: All courses in `teaching/*/index.qmd`

  **Acceptance**: All courses have `title` and `abstract` fields; descriptions are clear and consistent.

  **Action**: Review all 6 course index.qmd files, ensure metadata is complete.

- [ ] T022 Add inline documentation to teaching.qmd explaining Quarto listings usage

  **File Path**: `teaching.qmd` (comments in YAML front matter)

  **Acceptance**: Comments explain listing configuration, course discovery mechanism, and how to add new courses.

  **Action**: Add YAML comments documenting:
  ```yaml
  # Dynamic course discovery via Quarto listings
  # Each listing section discovers courses from specified files/directories
  # To add a new course:
  # 1. Create directory: teaching/course-slug/
  # 2. Add index.qmd with title and abstract fields
  # 3. Add course path to appropriate listing section below
  ```

- [ ] T023 Final verification: render full site and check teaching page

  **File Path**: `teaching.qmd` (rendered output)

  **Acceptance**: 
  - ✅ Full site renders without errors (`quarto render`)
  - ✅ Teaching page displays all 6 original courses
  - ✅ All courses in correct categories
  - ✅ All links work correctly
  - ✅ Layout responsive and professional

  **Action**: Run full `quarto render`, open teaching page in browser, verify all criteria.

- [ ] T024 Commit changes to feature branch

  **File Paths**: `teaching.qmd`, `specs/002-dynamic-course-listing/`, updated course `index.qmd` files

  **Acceptance**: Changes committed to `002-dynamic-course-listing` branch with clear commit messages.

  **Action**: 
  ```bash
  git add teaching.qmd teaching/*/index.qmd specs/002-dynamic-course-listing/
  git commit -m "feat: implement dynamic course listing with Quarto listings"
  ```

- [ ] T025 Create summary documentation for future maintainers

  **File Path**: `specs/002-dynamic-course-listing/IMPLEMENTATION_NOTES.md`

  **Acceptance**: Document created explaining how to add/remove/modify courses in the future.

  **Action**: Create guide covering:
  - How the dynamic listing works (Quarto listings feature)
  - How to add a new course
  - How to modify course metadata
  - Troubleshooting common issues
  - Performance notes

---

## Validation Checklist

### Pre-Implementation
- [ ] All design documents reviewed (spec.md, plan.md, data-model.md, research.md, quickstart.md)
- [ ] Project structure validated (Phase 1, T001-T004)
- [ ] Quarto version confirmed ≥ 1.4 (Phase 1, T002)
- [ ] Backup created (Phase 1, T003)

### Core Implementation (MVP — Phase 3, US1)
- [ ] Metadata audited and enhanced (Phase 3, T005, T006)
- [ ] Front matter updated with listing config (Phase 3, T008)
- [ ] Hardcoded grids replaced with placeholders (Phase 3, T009)
- [ ] Preview tested and validated (Phase 3, T010, T011)

### Automated Discovery (Phase 4, US2)
- [ ] Test course creation and validation (Phase 4, T012, T013)
- [ ] Automatic appearance verified (Phase 4, T014)
- [ ] Cleanup and restoration verified (Phase 4, T015)

### Scalability (Phase 5, US3)
- [ ] Scale testing with 15+ courses (Phase 5, T016-T020)
- [ ] Performance validated < 3 seconds (Phase 5, T018)
- [ ] Responsive layout tested on 3 breakpoints (Phase 5, T019)

### Production (Phase 6)
- [ ] All documentation complete (Phase 6, T022, T025)
- [ ] Full site render successful (Phase 6, T023)
- [ ] Changes committed (Phase 6, T024)

---

## Success Metrics

| Metric | Target | Phase | Validation |
|--------|--------|-------|-----------|
| All 6 courses appear | 100% | 3 (US1) | T010 ✅ |
| Correct categorization | 100% | 3 (US1) | T010 ✅ |
| Page load time | < 2 sec | 3 (US1) | T010 ✅ |
| New course auto-discovery | Working | 4 (US2) | T014 ✅ |
| Scalability to 15 courses | < 3 sec | 5 (US3) | T018 ✅ |
| Responsive layout | 3 breakpoints | 5 (US3) | T019 ✅ |
| Documentation complete | 100% | 6 (Polish) | T025 ✅ |
| Zero hardcoding | 100% | 6 (Polish) | T023 ✅ |

---

## Notes for Developers

### Getting Started
1. Start with Phase 1 (Setup) — validates environment and dependencies
2. Phase 3 (US1) is the MVP — focus here first for core functionality
3. Phases 4-5 validate automated discovery and scalability
4. Phase 6 finalizes and documents

### Key Files to Edit
- **Primary**: `teaching.qmd` — transform from hardcoded to dynamic listing
- **Secondary**: `teaching/*/index.qmd` — enhance metadata fields
- **Documentation**: `specs/002-dynamic-course-listing/tasks.md`, `IMPLEMENTATION_NOTES.md`

### Quarto Listings Reference
```yaml
listing:
  - id: section-id              # Unique identifier (use in placeholder div)
    contents: path/to/files     # Glob pattern or list of files
    type: grid                  # Card layout (also: default, table)
    sort: title                 # Sort field (default: date-modified)
```

### Troubleshooting
- **Courses not appearing**: Check glob paths, verify `id` matches placeholder `#id`
- **Layout broken**: Hard refresh browser (Ctrl+Shift+R), check Quarto cache
- **Missing descriptions**: Add `abstract` or `description` to YAML front matter
- **Performance issues**: Monitor with 15+ courses (Phase 5, T018)

---

## References

- **Spec**: `specs/002-dynamic-course-listing/spec.md`
- **Plan**: `specs/002-dynamic-course-listing/plan.md`
- **Research**: `specs/002-dynamic-course-listing/research.md`
- **Data Model**: `specs/002-dynamic-course-listing/data-model.md`
- **Quickstart**: `specs/002-dynamic-course-listing/quickstart.md`
- **Quarto Docs**: https://quarto.org/docs/reference/cells/cell-options.html#listing
- **Quarto Listings**: https://quarto.org/docs/websites/listings.html

---

**Last Updated**: 2026-06-11  
**Generated By**: Task Generation Workflow  
**Feature Branch**: `002-dynamic-course-listing`
