# Contract: Restructured Module Page

**Feature**: `006-improve-math-pedagogy`
**Applies to**: `teaching/mathematical-fundamentals/module-1.qmd` through
`module-8.qmd`

This contract defines the required structure and content rules for every
module page after restructuring. A page that does not satisfy all constraints
MUST NOT be considered done.

---

## Front Matter (required)

```yaml
---
title: "N️⃣ [Module title]"
abstract: |
  [One paragraph, ≤ 60 words, describing what the student will learn and why
  it matters in an economics/management context.]
lang: en
---
```

- `title` MUST match the module entry in `index.qmd` (Course Roadmap).
- `lang: en` MUST be present.
- `abstract` MUST be present and non-empty.

---

## Section Order (mandatory)

Sections MUST appear in the following order. Heading text MUST match exactly
(case and punctuation). No sections may be omitted; no additional top-level
`##` sections may be inserted between them.

```
## Diagnostic Activity
## Opening Problem
## Core Concepts
## Worked Example
## Guided Practice
## Interactive Exploration
## Applied Problem
## Common Errors
## Check Your Understanding
## Summary
## Independent Work
## Continue
```

Sub-sections (`###`, `####`) may be added inside any section as needed.

---

## Section Contracts

### 1 — Diagnostic Activity

**Purpose**: Surface what students already know; help them identify gaps
before reading theory.

**Required elements**:
- 2–4 numbered prerequisite questions, presented as prose (no callout wrapper
  around the questions themselves).
- A `.callout-note` with `collapse="true"` and title "Check your answers"
  containing the correct answers.
- A closing sentence directing the student to note which topics need
  attention.

**Callout**: `.callout-note collapse="true"` for the answers only.

**Example structure**:
```markdown
## Diagnostic Activity

Attempt these questions without consulting the lesson.

1. [Question 1]
2. [Question 2]
3. [Question 3]

::: {.callout-note collapse="true" title="Check your answers"}
1. [Answer 1]
2. [Answer 2]
3. [Answer 3]
:::

Use your results to identify topics that need particular attention.
```

---

### 2 — Opening Problem

**Purpose**: Motivate the module's central concept with a provocative
business, economics, or finance scenario.

**Required elements**:
- 1–2 sentences setting a concrete, real-world scenario.
- A blockquote (`> `) containing the question that the module's method
  resolves.
- A prompt: "Write down your prediction before continuing."

**No callout wrapping** — plain prose + blockquote only.

```markdown
## Opening Problem

[1–2 sentence scenario.]

> [Provocative question?]

Write down your prediction before continuing.
```

---

### 3 — Core Concepts

**Purpose**: Define concepts formally, state rules, and explain the
plain-language meaning of every formula.

**Required elements**:
- At least one `.callout-note` with a `#### [Concept name]` title containing
  a formal definition or statement of a rule.
- At least one `.callout-tip` with a `#### [Formula / Key rule]` title
  containing the LaTeX formula and its plain-language description.
- Every formula MUST be accompanied by a sentence explaining what it computes
  and why it is useful in context.

**Callouts**: `.callout-note` for definitions; `.callout-tip` for key
formulas and shortcuts.

---

### 4 — Worked Example

**Purpose**: Model the full solution process for one representative problem.

**Required elements**:
- A `### [Descriptive title]` sub-heading naming the context (e.g., "Worked
  example — successive discounts").
- Step-by-step calculation using displayed math (`$$...$$`).
- A stated final result in bold or a display equation.

**No callout wrapping** — prose + math only (the student should see the
full solution without needing to expand anything).

---

### 5 — Guided Practice

**Purpose**: Let the student attempt an exercise with progressive support —
hint first, solution second.

**Required elements**:
- 1 multi-step exercise prompt (prose + numbered sub-questions).
- A `.callout-tip collapse="true"` with a descriptive title (e.g., "Hint")
  containing one or two guiding steps — MUST appear before the solution.
- A `.callout-caution collapse="true"` with title "Show the solution"
  containing the complete worked solution.

**Constraint**: The hint callout MUST appear before the solution callout in
the source file. A solution without a preceding hint is a contract violation.

---

### 6 — Interactive Exploration

**Purpose**: Let students experiment with parameters and observe effects
before formulating an explanation.

**Modules 1–7** (OJS simulation):

```markdown
## Interactive Exploration

[1–2 sentences introducing what the simulation demonstrates.]

```{ojs}
// OJS code: viewof inputs, reactive computations, html`` display
```

### Investigation

1. [Interpretation question — observe]
2. [Interpretation question — explain]
3. [Interpretation question — generalise]
4. [Optional: find a specific input that produces a target output]
```

**Constraints (OJS)**:
- MUST use only bundled OJS APIs (`Inputs`, `html`, `Plot`) — no `import`.
- MUST include 2–4 `### Investigation` questions immediately after the code
  block.
- All inputs MUST specify `min`, `max`, `step`, `value`, `label`.
- Numerical outputs MUST be formatted (`.toFixed(2)` or equivalent).

**Module 8** (static mixed-method challenge):

```markdown
## Interactive Exploration

The following problems are drawn from across Modules 1–7.
Identify the appropriate mathematical method before expanding.

::: {.callout-caution collapse="true" title="Problem 1 — [neutral title]"}
**Method**: [Module N — method name]

[Full worked solution]
:::

::: {.callout-caution collapse="true" title="Problem 2 — [neutral title]"}
...
:::
```

**Constraints (Module 8)**:
- 6–8 problems; at minimum one from each of Modules 1, 2, 3, 4 or 5, 6, 7.
- Callout titles MUST NOT name the method or module (e.g., "Problem 3 — A
  savings scenario", not "Problem 3 — Compound interest").
- The method label inside the callout MUST name the source module.

---

### 7 — Applied Problem

**Purpose**: Transfer the module's method to a realistic business/finance/
economics scenario with genuine decision relevance.

**Required elements**:
- A concrete scenario with numbers (not generic "company X").
- At least 2 numbered questions asking the student to calculate and interpret.
- No collapsible solution (this section is for independent attempt; answers
  may be given in Section 11 Independent Work or the exercise bank).

---

### 8 — Common Errors

**Purpose**: Proactively address the most frequent mistakes for this module's
topic.

**Required elements**:
- At least one `.callout-warning` block with a descriptive title (e.g.,
  "Common error — dividing by the wrong value").
- Content: the incorrect working (shown), the correct working (shown), and a
  one-sentence explanation of why the error occurs.

**Callout**: `.callout-warning` (constitution §V).

```markdown
::: {.callout-warning title="Common error — [description]"}
A student writes:
$$[incorrect]$$

The correct calculation is:
$$[correct]$$

[Explanation of why the error occurs.]
:::
```

---

### 9 — Check Your Understanding

**Purpose**: Self-assessment covering multiple question types.

**Required elements**:
- A numbered list of exactly **5** questions.
- Coverage: at minimum one calculation question, one conceptual question, one
  applied question, and one error-diagnosis question. The fifth question may
  be any type.
- No solutions revealed in this section (students self-check via the formula
  sheet, glossary, or by re-reading the module).

---

### 10 — Summary

**Purpose**: Consolidate the three most important takeaways.

**Required elements**:
- A numbered list of exactly **3** items.
- Each item is a complete sentence capturing a key insight (not just a term).

---

### 11 — Independent Work

**Purpose**: Set clear expectations for out-of-class practice.

**Required elements**:
- A bulleted list of at least 3 study actions (e.g., "Complete exercises 1–5",
  "Record any errors in your error log", "Review the glossary entries for this
  module").

---

### 12 — Continue

**Purpose**: Guide the student to the next module without leaving them to
navigate alone.

**Required elements**:
- A single link: `[Continue to Module N →](module-N.qmd)` for Modules 1–7.
- Module 8: `[Return to the course syllabus →](index.qmd)` or a link to the
  glossary.

---

## Global Constraints

- All prose wraps at 80 characters.
- All mathematics uses LaTeX: `$...$` inline, `$$...$$` display.
- No inline `style=` attributes; no `<style>` blocks.
- No Unicode math characters in place of LaTeX.
- `lang: en` in front matter.
- No untranslated French learner-facing prose.
