# Feature Specification: Complete English Course — Mathematical Fundamentals and Data Analysis

**Feature Branch**: `004-math-fundamentals-course`

**Created**: 2026-07-23

**Status**: Draft

**Input**: User description: "@teaching/mathematical-fundamentals/ based on every files inside both MS01-001-G_fondamentaux directories and quarto document already presents (module-1.qmd, module-2.qmd, etc.) prepare an complete course. Respect course materials but content MUST be in english"

## Overview

The `teaching/mathematical-fundamentals/` course ("Mathematical Fundamentals and Data Analysis", ESSCA MS01-001-G) currently exists as a partially-completed set of Quarto documents. The syllabus (`index.qmd`) is complete, Module 1 is well developed (mostly in French), Modules 2–3 are partially drafted (mixed language, some placeholder outline text), and Modules 4–7 contain only front-matter with empty bodies. The authoritative source content lives in two exported course archives (`MS01-001-G_Fondamentaux` and `MS01-001-G_Fondamentaux-26`) containing the instructor's slide decks (PPTX), student handouts (PDF), the final exam with corrections, and the syllabus.

This feature delivers a **complete, coherent, English-language course** across all eight modules, faithfully derived from the existing source materials (slides, handouts, exam) and the already-drafted Quarto documents, while translating all learner-facing content into English and preserving the pedagogical structure, examples, exercises, and mathematical rigor of the originals.

## Clarifications

### Session 2026-07-23

- Q: How comprehensive should each module's content be? → A: Comprehensive lessons matching the existing Module 1 depth — full lesson prose, multiple worked examples, and larger exercise banks covering every source concept.
- Q: Should exercises be interactive (shinylive) or static? → A: Static only — all exercises use revealable static solutions (collapsible callouts / details); Module 1's existing interactive quizzes are converted to static form.
- Q: What mathematical notation standard should the course use? → A: LaTeX everywhere — all math uses `$...$` / `$$...$$`, converting Module 1's inline Unicode/HTML notation to LaTeX.
- Q: How should Module 8 and site navigation be handled? → A: Create a dedicated `module-8.qmd` and register the index plus all modules 1–8 in the sidebar navigation (`_metadata.yml`).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner studies a complete, English module end-to-end (Priority: P1)

An undergraduate student opens any module page (Modules 1 through 8) on the course website and works through a self-contained lesson: an introduction explaining why the topic matters in economics/management, clearly stated learning objectives, definitions, worked examples drawn from real economic/business contexts, and progressive exercises with collapsible solutions — all written in English.

**Why this priority**: The core deliverable is complete learner-facing content. A single fully-realized module already delivers standalone educational value and proves the content pattern that all other modules follow.

**Independent Test**: Render the course site and open one module (e.g., Module 4). Confirm the page presents objectives, theory, worked examples, and exercises with solutions entirely in English, faithful to the corresponding source slide deck/handout, with correctly rendered mathematical notation.

**Acceptance Scenarios**:

1. **Given** a rendered module page, **When** the learner reads the introduction and objectives, **Then** they understand the topic's purpose and what they will be able to do after the module, stated in English.
2. **Given** a module containing worked examples, **When** the learner reads an example, **Then** the example matches a concept present in the source material and shows a step-by-step solution with a stated result.
3. **Given** an exercise with a hidden solution, **When** the learner expands the solution, **Then** a correct, verifiable answer is revealed.
4. **Given** any mathematical expression on the page, **When** the page renders, **Then** the notation displays correctly (no broken markup) and uses consistent, valid formatting.

---

### User Story 2 - Learner navigates the whole course from syllabus to exam prep (Priority: P2)

A student uses the syllabus/index page as the course home, follows links to each of the eight modules in sequence, and reaches a final revision/exam-preparation module, understanding the schedule, assessment method, and expected personal workload — all in English.

**Why this priority**: A connected, navigable course (not isolated pages) is what makes the deliverable usable as a course rather than a collection of notes. It depends on individual modules existing (P1) but adds the cross-cutting navigation and framing.

**Independent Test**: From the index page, follow every module link and the exam-prep link; confirm each destination exists, is in English, and the syllabus accurately reflects each module's topic and sequence.

**Acceptance Scenarios**:

1. **Given** the index/syllabus page, **When** the learner reads it, **Then** all course information (schedule, competencies, assessment, workload, recommended reading) is presented in English.
2. **Given** the module list on the index page, **When** the learner clicks each module link, **Then** they arrive at the corresponding module whose title and content match the syllabus description.
3. **Given** the final module, **When** the learner opens it, **Then** it provides revision material and exam preparation aligned with the earlier modules.

---

### User Story 3 - Instructor verifies fidelity to source materials (Priority: P3)

The course owner compares each finished module against the original slide deck, handout, and exam to confirm that concepts, examples, exercises, and results were preserved (not invented or omitted) and only translated/re-presented in English.

**Why this priority**: Fidelity is a correctness/quality guarantee. It is essential to trust the deliverable but is a verification activity layered on top of the content produced in P1/P2.

**Independent Test**: Pick any module and cross-check its concept list and worked examples against the source PPTX/PDF; confirm every source concept appears and no numerical results contradict the source.

**Acceptance Scenarios**:

1. **Given** a module's source slide deck, **When** the instructor lists its concepts, **Then** each concept appears in the corresponding Quarto module.
2. **Given** a worked example or exercise result in the source, **When** compared to the module, **Then** numerical results and formulas agree.
3. **Given** the completed course, **When** the instructor scans all learner-facing text, **Then** no untranslated French learner-facing prose remains.

---

### Edge Cases

- **Mixed-language legacy content**: Existing drafts (Modules 1–3) contain French prose and some French-only exercise prompts; these must be translated to English while preserving the mathematics and correct answers.
- **Placeholder/outline dumps**: Module 3 currently contains large repeated outline fragments extracted from slides; these must be consolidated into coherent lesson prose, not left as raw bullet repetition.
- **Empty modules**: Modules 4–7 have only front-matter; their bodies must be authored from the source decks/handouts.
- **Source-only concepts not yet drafted**: Where a source deck covers a concept absent from the current Quarto draft (e.g., EXCEL applications, sum-of-terms formulas), the module must incorporate it.
- **Interactive quiz components**: Module 1 embeds Shiny/`shinylive` quiz blocks; these are converted to static exercises with revealable solutions (in English), and no new interactive components are introduced.
- **Notation consistency**: Some existing content mixes LaTeX math and inline Unicode/HTML notation; the finished course should use consistent, correctly-rendering mathematical notation.
- **Non-lesson archive items**: The source archives contain forum pages, URLs, and duplicate exports; these are references only and must not be treated as required lesson content.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The course MUST provide complete learner-facing lesson content for all eight modules: (1) Essential mathematical calculations for economics and management, (2) Mastering equations for better decision-making, (3) Curve analysis in economics and management, (4) Introduction to financial mathematics tools, (5) Application of financial mathematics, (6) Presentation of functions useful in economics and management, (7) Introduction to optimization, and (8) Final-exam revision/preparation.
- **FR-002**: All learner-facing content (prose, headings, objectives, examples, exercise prompts, solutions, tables, captions) MUST be written in English.
- **FR-003**: Each module's content MUST be faithfully derived from the corresponding source materials in `MS01-001-G_Fondamentaux` and/or `MS01-001-G_Fondamentaux-26` (slide decks, student handouts, exam), preserving concepts, worked examples, exercises, and numerical results.
- **FR-004**: Each module MUST include, at minimum: an introduction motivating the topic in an economics/management context, explicit learning objectives, core definitions and rules, at least one fully worked example, and a set of practice exercises with revealable solutions.
- **FR-004a**: Each module MUST be developed to a depth comparable to the existing Module 1 — full explanatory lesson prose, multiple worked examples, and an exercise bank sized to cover every concept in the corresponding source deck (not concise summary notes).
- **FR-005**: The topic coverage of each module MUST match the syllabus (`index.qmd`) descriptions and the plan of the corresponding source deck (e.g., Module 4 MUST cover numerical sequences including arithmetic and geometric sequences, their definitions, sums of terms, and sense of variation).
- **FR-006**: Existing partially-drafted modules (1–3) MUST be completed and translated to English, with the correct mathematics and answers from the drafts preserved and any placeholder/outline-dump text rewritten into coherent lesson prose.
- **FR-007**: Empty modules (4–7) MUST be authored in full from the source materials.
- **FR-008**: The final module (8) MUST be delivered as a dedicated `module-8.qmd` document providing revision material and final-exam preparation aligned with the content of Modules 1–7 and the final-exam source material.
- **FR-008a**: The site navigation (sidebar in `_metadata.yml`) MUST register the index page and all eight modules (1–8) so learners can reach every module from the course navigation.
- **FR-009**: Mathematical notation MUST render correctly and use consistent formatting throughout the course, with no broken markup. All mathematics MUST be expressed in LaTeX (`$...$` for inline and `$$...$$` for display); existing inline Unicode/HTML notation (e.g., Module 1's superscripts and `<sub>`/`<sup>` markup) MUST be converted to LaTeX.
- **FR-010**: The index/syllabus page MUST be presented in English and MUST link to every module; module titles and descriptions MUST remain consistent between the index and the module pages.
- **FR-011**: Cross-module navigation links present in module front-matter MUST resolve to the correct module pages.
- **FR-012**: Exercises MUST use static, revealable solutions (e.g., collapsible callouts or details blocks); the course MUST NOT rely on interactive runtime quiz components. Module 1's existing interactive (`shinylive`) quizzes MUST be converted to equivalent static exercises with revealable solutions, presented in English.
- **FR-013**: Worked examples and exercises SHOULD use real economic, financial, or management contexts (e.g., wages, discounts, savings, interest, cost functions, break-even) consistent with the source materials.
- **FR-014**: Non-lesson archive artifacts (forums, external URLs, duplicate exports) MUST NOT be presented as required course lessons; they may inform content but are not learner-facing deliverables.
- **FR-015**: The completed course MUST render successfully as part of the existing site build without introducing render errors.

### Key Entities *(include if feature involves data)*

- **Course**: The overall "Mathematical Fundamentals and Data Analysis" offering; attributes include title, general presentation, targeted competencies, schedule, assessment scheme, expected personal workload, and recommended reading. Represented by the index/syllabus page.
- **Module**: A self-contained lesson (eight in total); attributes include title, learning objectives, introductory motivation, definitions/rules, worked examples, exercises with solutions, and scheduled date. Each maps to one source slide deck (and, where available, a student handout).
- **Source Material**: An authoritative input artifact (slide deck PPTX, student handout PDF, final exam PDF, syllabus) from which module content is derived; used to guarantee fidelity, not published directly.
- **Exercise**: A practice item within a module; attributes include the prompt, an optional real-world context, and a revealable correct solution/result.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All eight modules present complete lesson content (introduction, objectives, theory, at least one worked example, and exercises with solutions) — 8 of 8 modules complete.
- **SC-002**: 100% of learner-facing text across the course is in English (zero untranslated French learner-facing prose remains).
- **SC-003**: Every concept listed in each source module's plan appears in the corresponding module (100% concept coverage per module).
- **SC-004**: 100% of worked-example and exercise results that also appear in the source materials agree with the source (no contradicting numerical answers).
- **SC-005**: The course renders with zero broken mathematical expressions and zero build/render errors on the site.
- **SC-006**: Every module link on the index page and every cross-module navigation link resolves to an existing, correct module page (0 broken links).
- **SC-007**: A learner can navigate from the syllabus through all eight modules to exam preparation without encountering an empty or placeholder page.

## Assumptions

- The eight-module structure defined in the existing `index.qmd` syllabus is authoritative and will be preserved; Module 8 (final-exam preparation) is included even though it currently has no `module-8.qmd` file.
- "Both MS01-001-G_fondamentaux directories" refers to `MS01-001-G_Fondamentaux` (the full 2024/25 export with all eight decks, handouts, and exam) and `MS01-001-G_Fondamentaux-26` (the 2026 partial export covering Modules 2–4); where they overlap, the more complete/newer version is preferred, and no source concept is dropped.
- The deliverable is the set of Quarto module documents (and the syllabus) under `teaching/mathematical-fundamentals/`; the raw archive folders remain reference inputs and are not modified or published as lessons.
- "Respect course materials" means preserving the pedagogical intent, examples, exercises, and results of the source — translation and re-presentation in English are expected, but inventing unrelated content or omitting covered concepts is not.
- Existing interactive/`shinylive` quiz functionality and the site's math rendering toolchain remain available and are reused rather than replaced.
- Learner-facing content is translated to English; proper nouns, author names, and institutional references may remain as-is.
- The recommended-reading list and any references may remain bibliographic (titles unchanged) even if originally French-language works.
