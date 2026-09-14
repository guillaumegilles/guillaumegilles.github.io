# Data Model: Pedagogical Improvement — Mathematical Fundamentals

**Feature**: `006-improve-math-pedagogy` | **Date**: 2026-09-13

This is a content-only feature. "Entities" are the authoring objects that
make up the restructured course. There is no database or application model.

---

## Entity: Module

Eight instances (`module-1.qmd` … `module-8.qmd`). After restructuring, every
module conforms to the 12-section template.

### Attributes

| Attribute | Type | Constraint |
|---|---|---|
| `title` | string | Matches `index.qmd` roadmap entry; includes emoji number prefix |
| `abstract` | string (front matter) | One paragraph; appears in module list hover |
| `lang` | `"en"` | Required; set in YAML front matter |
| `sections` | list[Section] | Exactly 12 sections in canonical order (see below) |
| `simulation_type` | `"ojs"` \| `"static"` | Modules 1–7: `"ojs"`; Module 8: `"static"` |

### Validation rules

- Each module MUST contain all 12 section headings, in the canonical order.
- The `{ojs}` code block MUST appear inside Section 6 (Interactive
  Exploration), never in other sections.
- The hint callout MUST appear before the solution callout in Section 5
  (Guided Practice).
- The Continue link in Section 12 MUST resolve to the next module (or
  `module-8.qmd` for Module 7; `index.qmd` or `glossary.qmd` for Module 8).

---

## Entity: Section

12 canonical types. Each Section instance belongs to one Module.

| # | Name | Required callout / format | Min content |
|---|---|---|---|
| 1 | Diagnostic Activity | 2–4 questions (prose); `.callout-note collapse="true"` for answers | 2 questions + answers |
| 2 | Opening Problem | Blockquote `> Question?`; prompt to write prediction | 1 business/finance scenario |
| 3 | Core Concepts | ≥1 `.callout-note` (def) + ≥1 `.callout-tip` (formula) | All module concepts defined |
| 4 | Worked Example | Prose + displayed `$$...$$` steps; stated result | ≥1 fully worked example |
| 5 | Guided Practice | `.callout-tip collapse="true"` (hint) before `.callout-caution collapse="true"` (solution) | ≥1 multi-step exercise |
| 6 | Interactive Exploration | `{ojs}` block (Modules 1–7) or static `.callout-caution` blocks (Module 8) + 2–4 follow-up questions | 1 simulation or challenge |
| 7 | Applied Problem | Prose scenario with dataset or decision context | 1 business scenario + ≥2 questions |
| 8 | Common Errors | ≥1 `.callout-warning` with error + correction + explanation | 1 named error per module |
| 9 | Check Your Understanding | Numbered list of exactly 5 questions | 1 calculation, 1 conceptual, 1 applied, 1 error-diagnosis (+ 1 any type) |
| 10 | Summary | Numbered list of exactly 3 items | 3 key takeaways |
| 11 | Independent Work | Bulleted list | ≥3 study actions |
| 12 | Continue | `[Continue to Module N](module-N.qmd)` link | 1 navigation link |

---

## Entity: OJS Simulation

Seven instances, one per Module 1–7. Embedded in Section 6 of the parent
module.

### Attributes

| Attribute | Type | Value |
|---|---|---|
| `module` | int | 1–7 |
| `name` | string | See table below |
| `inputs` | list[OJSInput] | 2–4 `Inputs.*` widgets |
| `outputs` | list[OJSOutput] | 2–5 computed reactive values |
| `has_chart` | bool | `true` for Modules 5, 6, 7 (Observable Plot) |
| `follow_up_questions` | list[string] | 2–4 interpretation questions |

### Instance table

| Module | Simulation name | Key inputs | Key outputs | Chart? |
|---|---|---|---|---|
| 1 | Percentage-change simulator | Initial value, increase %, decrease % | After-increase value, final value, overall % change | No |
| 2 | Break-even simulator | Fixed cost, variable cost/unit, price/unit | Break-even Q*, revenue, cost, profit | No |
| 3 | Line-intersection explorer | a₁, b₁, a₂, b₂ | Intersection (x*, y*); graph of two lines | Yes (Plot) |
| 4 | Sequence explorer | u₀, d, r, n | Arithmetic and geometric sequence tables (side by side) | No |
| 5 | Compound-interest calculator | Principal, annual rate, periods, frequency | Simple value, compound value, cumulative interest | Yes (Plot) |
| 6 | Function-family explorer | Function type, 1–2 parameters | Graph updating in real time; domain + features text | Yes (Plot) |
| 7 | Profit-maximisation simulator | Quantity q (slider) | R(q), C(q), P(q); derivative-based q* | Yes (Plot) |

### Validation rules

- Every OJS simulation MUST be self-contained in its `{ojs}` block(s): no
  `import` from external Observable notebooks.
- Every simulation MUST be followed immediately by 2–4 interpretation
  questions (markdown prose, not in the OJS block).
- `Inputs.range` MUST specify `min`, `max`, `step`, `value`, and `label`.
- All numerical outputs MUST use `.toFixed(2)` or equivalent for display.

---

## Entity: Static Mixed-Method Challenge (Module 8)

One instance, filling Section 6 of Module 8 in place of an OJS simulation.

### Attributes

| Attribute | Type | Constraint |
|---|---|---|
| `problem_count` | int | 6–8 |
| `source_modules` | list[int] | Covers at minimum Modules 1, 2, 3, 4/5, 6, 7 |
| `format` | string | Each problem: prose + `.callout-caution collapse="true"` |
| `callout_content` | string | Method label (e.g., "Compound interest — Module 5") + full worked solution |

### Validation rules

- Problem prompts MUST NOT name the method or the source module.
- Prompt MUST include: "Identify the appropriate mathematical method before
  expanding."
- Each `.callout-caution` title MUST reveal the method label on expansion.

---

## Entity: Formula Sheet

One instance (`formula-sheet.qmd`). Approximately 21 entries (see
`research.md` Decision 5 for full enumeration).

### Attributes

| Attribute | Type | Constraint |
|---|---|---|
| `lang` | `"en"` | Required front matter |
| `title` | string | "Formula Sheet" |
| `sections` | list[ModuleSection] | One section per module (Modules 1–7) |
| `entries_per_module` | int | 1–4 |
| `total_entries` | int | 20–25 |

### FormulaEntry attributes

| Attribute | Type | Constraint |
|---|---|---|
| `latex` | string | Valid LaTeX; renders via KaTeX |
| `label` | string | Plain-language name (≤ 10 words) |
| `description` | string | One sentence: what the formula computes |

### Validation rules

- Only applied formulas (directly used when solving exam problems) are listed.
- Intermediate algebraic properties and definitional rules are excluded.
- Every entry MUST have a label and a one-sentence description.

---

## Entity: Learning Guide

One instance (`learning-guide.qmd`). Four required subsections.

| Subsection | Content |
|---|---|
| How to prepare for each module | Prerequisites to review; 2–3 diagnostic questions to attempt before opening the page |
| Recommended study sequence | Step-by-step guide for a single ~90-minute module session |
| Error log | Template: error recorded, cause, corrected method, prevention rule; explanation of how to use it over the course |
| Revision schedule | 8-week plan (one module per week) + 2-week consolidation block before final exam |

### Validation rules

- No interactive components (purely static prose).
- Each subsection MUST be a Quarto `##` heading so it appears in the page ToC.

---

## Module Coverage Matrix

Confirms the 12-section template is applied to all eight modules, and which
sections require authoring effort vs. restructuring existing content.

| Section | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 |
|---|---|---|---|---|---|---|---|---|
| 1. Diagnostic Activity | NEW | NEW | NEW | NEW | NEW | NEW | NEW | NEW |
| 2. Opening Problem | NEW | NEW | NEW | NEW | NEW | NEW | NEW | NEW |
| 3. Core Concepts | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | N/A |
| 4. Worked Example | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | N/A |
| 5. Guided Practice | EXTEND | EXTEND | EXTEND | EXTEND | EXTEND | EXTEND | EXTEND | N/A |
| 6. Interactive Exploration | OJS NEW | OJS NEW | OJS NEW | OJS NEW | OJS NEW | OJS NEW | OJS NEW | STATIC NEW |
| 7. Applied Problem | NEW | NEW | NEW | NEW | NEW | NEW | NEW | N/A |
| 8. Common Errors | NEW | NEW | NEW | NEW | NEW | NEW | NEW | NEW |
| 9. Check Your Understanding | NEW | NEW | NEW | NEW | NEW | NEW | NEW | NEW |
| 10. Summary | NEW | NEW | NEW | NEW | NEW | NEW | NEW | NEW |
| 11. Independent Work | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | REUSE | NEW |
| 12. Continue | NEW | NEW | NEW | NEW | NEW | NEW | NEW | N/A* |

*Module 8 Continue links to the glossary or syllabus, not a ninth module.

**Legend**: REUSE = existing content restructured into this section without
major rewriting; EXTEND = existing collapsible solutions kept; hint callout
added before them; NEW = section authored from scratch; OJS NEW = OJS
simulation block authored from scratch.
