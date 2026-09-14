# Contract: Improved Course Entry Page (index.qmd)

**Feature**: `006-improve-math-pedagogy`
**Applies to**: `teaching/mathematical-fundamentals/index.qmd`

This contract defines the five required additions to `index.qmd`. All
existing content (Course Information, General Presentation, Targeted
Competencies, Assessment, Expected Personal Work, Recommended Literature) is
preserved unchanged. The additions are inserted at the positions described
below.

---

## Front Matter (no change required)

The existing front matter is preserved. `lang: en` MUST be present (add if
missing).

---

## Required Addition 1 — Welcome callout

**Position**: Immediately after the front matter YAML block, before any `##`
heading.

**Callout type**: `.callout-note` (constitution: definitions and background
information).

**Content**: A welcome callout summarising in 5 bullet points what the course
enables students to do. Each bullet is an action verb + outcome.

```markdown
::: {.callout-note title="Welcome to the course"}
This course will help you develop the mathematical reasoning and calculation
skills needed to solve quantitative problems in finance, economics, and
management.

Throughout the course, you will learn to:

- perform calculations accurately;
- translate practical problems into mathematical expressions;
- choose an appropriate calculation method;
- interpret equations, functions, graphs, and numerical results;
- use mathematical tools to support managerial decisions.
:::
```

---

## Required Addition 2 — Start Here section

**Position**: First `##` section of the page (before "Course Information").

**Content**: A numbered list of 5 preparation steps, each linking to a
resource. Steps are numbered 1–5 and use inline markdown links.

```markdown
## Start Here

Before beginning the first module:

1. Read the [syllabus](#course-information) for a complete course overview.
2. Consult the [Learning Guide](learning-guide.qmd) to understand how to
   study each module effectively.
3. Complete the diagnostic activity at the start of Module 1.
4. Bookmark the [Glossary](glossary.qmd) for symbol and term lookups.
5. Download or bookmark the [Formula Sheet](formula-sheet.qmd).
```

**Constraints**:
- All 5 steps MUST link to a real resource (anchor, `.qmd` file, or section).
- `learning-guide.qmd` and `formula-sheet.qmd` MUST exist when this link
  is published.

---

## Required Addition 3 — How to study each module (tip callout)

**Position**: Immediately after the Start Here section, before "Course
Information".

**Callout type**: `.callout-tip`.

**Content**: The 6-step module learning sequence, presented as a numbered
list.

```markdown
::: {.callout-tip title="How to study each module"}
Each module follows the same learning sequence:

1. **Diagnose** — attempt the diagnostic activity to identify gaps.
2. **Understand** — read the core concepts and definitions.
3. **Observe** — study the worked example step by step.
4. **Practise** — attempt the guided exercise (use the hint before the
   solution).
5. **Experiment** — interact with the simulation and answer the
   investigation questions.
6. **Apply** — work through the applied problem and common errors.
:::
```

---

## Required Addition 4 — Application questions in Course Roadmap

**Position**: Inside each existing module entry within `## Course Roadmap`
(or `## Organisation & Schedule` if that heading is used).

**Content**: A bolded application question added **after** the existing topic
list for each module. The question contextualises the module's relevance to
economics, finance, or management.

Application questions by module (MUST match these exactly):

| Module | Application question |
|---|---|
| 1 | **Application question**: How can we calculate and interpret a change in price, revenue, cost, or market share? |
| 2 | **Application question**: At what sales volume does a company reach its break-even point? |
| 3 | **Application question**: At what level of activity do two pricing or cost models produce the same result? |
| 4 | **Application question**: How can we model a quantity that grows by a fixed amount or by a fixed percentage? |
| 5 | **Application question**: How does capitalisation frequency affect the future value of an investment? |
| 6 | **Application question**: Which type of function best represents a given economic or managerial phenomenon? |
| 7 | **Application question**: Which price, quantity, or production level maximises profit or minimises cost? |
| 8 | **Application question**: Can you identify the appropriate mathematical method without being told which module the problem comes from? |

**Constraint**: The topic-list descriptions MUST remain in place. Application
questions supplement; they do not replace existing content.

---

## Required Addition 5 — Learning Progress checklist

**Position**: New `## Learning Progress` section, after the Course Roadmap
and before Assessment.

**Content**: A markdown task list with one checkbox per module.

```markdown
## Learning Progress

Use this checklist to track your progress through the course.

- [ ] Module 1: Numerical calculations
- [ ] Module 2: Algebra and equations
- [ ] Module 3: Graphs, systems, and inequalities
- [ ] Module 4: Numerical sequences
- [ ] Module 5: Financial mathematics
- [ ] Module 6: Common functions
- [ ] Module 7: Derivatives and optimisation
- [ ] Module 8: Revision and exam preparation
```

---

## Global Constraints

- All existing `index.qmd` content is preserved exactly.
- No existing `##` heading is renamed or removed.
- Prose wraps at 80 characters.
- `lang: en` set in front matter.
- Both `formula-sheet.qmd` and `learning-guide.qmd` MUST be registered in
  `_quarto.yml` sidebar before this page is published (FR-028).
