# Quickstart & Validation Guide

**Feature**: `006-improve-math-pedagogy` | **Branch**: `007-improve-math-pedagogy`

This guide describes how to build the course and verify that all deliverables
satisfy the spec. Run validations after completing each implementation task
group.

---

## Prerequisites

- Quarto CLI installed (`quarto --version` ≥ 1.4).
- Working directory: `www/` (the repository root).
- Python virtual environment active if any `.qmd` files use Python code chunks
  (`.venv/` — `source .venv/bin/activate`).
- The feature branch `007-improve-math-pedagogy` is checked out.

---

## Build

### Render the full site

```sh
quarto render
```

Expected outcome: exit code 0, no errors or warnings about broken links or
missing files. Rendered HTML appears in `docs/`.

### Render the course only (faster iteration)

```sh
# Render a single module (fast, use during authoring)
quarto render teaching/mathematical-fundamentals/module-1.qmd --quiet

# Render all course files
quarto render teaching/mathematical-fundamentals/
```

Expected outcome: exit code 0 for every file. Math renders without markup
errors. OJS blocks produce sliders and output panels.

---

## Validation Scenarios

### V-01 — 12-section template present in all modules (SC-001)

**How to verify**: Open each rendered module in the browser and confirm that
all 12 section headings appear in the page Table of Contents:

```
Diagnostic Activity
Opening Problem
Core Concepts
Worked Example
Guided Practice
Interactive Exploration
Applied Problem
Common Errors
Check Your Understanding
Summary
Independent Work
Continue
```

**Pass criterion**: All 12 headings present, in the correct order, in all
8 module pages.

---

### V-02 — OJS simulations functional (SC-002)

**How to verify**: Open each of Modules 1–7 in a browser (Chrome or Firefox).
In Section 6 (Interactive Exploration):

1. Confirm sliders render (not blank, no JS error in DevTools console).
2. Move each slider; confirm outputs update without page reload.
3. For chart-based modules (3, 5, 6, 7): confirm the Observable Plot chart
   renders and updates.

**Module-by-module checks**:

| Module | Move this slider | Expect this change |
|---|---|---|
| 1 | `Decrease (%)` from 20 to 30 | Overall change becomes more negative |
| 2 | `Price/unit` below `Variable cost/unit` | Break-even Q* becomes negative (no viable break-even shown) |
| 3 | `a1` = `a2` (same slope) | "Parallel lines — no intersection" or Q* at infinity |
| 4 | `r` below 1 (geometric decay) | Geometric sequence decreases while arithmetic may increase |
| 5 | `freq` from 1 to 12 | Compound value increases; gap over simple interest widens |
| 6 | Switch to `exponential` | Graph shape changes; asymptote annotation updates |
| 7 | Move `q` to derivative-implied optimum | P(q) peaks; annotation confirms q* |

**Pass criterion**: All 7 OJS simulations respond correctly to slider changes;
no JavaScript errors in the browser console.

---

### V-03 — Module 8 static challenge (SC-002)

**How to verify**: Open Module 8, Section 6. Confirm:

1. 6–8 `.callout-caution` blocks are present, each labelled "Problem N —
   [neutral title]" (no method name in the title).
2. Expanding each block reveals: "Method: [Module N — method name]" followed
   by a full worked solution.
3. Problems cover at least Modules 1, 2, 3, 4 or 5, 6, and 7.

**Pass criterion**: All problems present, neutral titles, method label visible
only after expansion.

---

### V-04 — Guided Practice hint-before-solution order (SC-004)

**How to verify**: In each module, Section 5 (Guided Practice), inspect the
source `.qmd` file or the rendered page:

```sh
grep -n "callout-tip\|callout-caution" \
  teaching/mathematical-fundamentals/module-1.qmd
```

Confirm that a `.callout-tip collapse="true"` (hint) appears at a lower line
number than the `.callout-caution collapse="true"` (solution) within Section 5.

**Pass criterion**: For all 8 modules, hint callout line < solution callout
line within the Guided Practice section.

---

### V-05 — index.qmd five required additions (SC-005)

**How to verify**: Open `teaching/mathematical-fundamentals/index.qmd` and
confirm:

1. A `.callout-note` welcome block appears before the first `##` heading.
2. A `## Start Here` section is present with a numbered list of 5 steps,
   each linking to a real resource.
3. A `.callout-tip` "How to study each module" block with a 6-step list
   appears after "Start Here".
4. Each module entry in the Course Roadmap ends with a bolded **Application
   question**: line.
5. A `## Learning Progress` section with 8 checkbox list items is present.

**Pass criterion**: All five elements present; all links in Start Here resolve
to existing pages.

---

### V-06 — Formula sheet completeness (SC-006)

**How to verify**: Open `formula-sheet.qmd` and count entries per module:

```sh
grep -c "^\|" teaching/mathematical-fundamentals/formula-sheet.qmd
```

Confirm:
- Seven module sections (## Module 1 through ## Module 7).
- Total entries: 20–25 (the table in `research.md` lists 21 canonical
  entries).
- Every entry has a LaTeX formula and a one-sentence description.

**Pass criterion**: 7 sections, 20–25 entries, all entries have descriptions.

---

### V-07 — Learning guide subsections (SC-007)

**How to verify**: Open `learning-guide.qmd` and confirm the presence of
four `##` sections:

```sh
grep "^## " teaching/mathematical-fundamentals/learning-guide.qmd
```

Expected headings (in any order):
- `## How to Prepare for Each Module` (or similar)
- `## Recommended Study Sequence` (or similar)
- `## Error Log` (or similar)
- `## Revision Schedule` (or similar)

**Pass criterion**: All four subsections present.

---

### V-08 — Sidebar navigation (SC-008)

**How to verify**: Inspect `_quarto.yml` for the
`mathematical-fundamentals` sidebar block:

```sh
grep -A 30 "mathematical-fundamentals" _quarto.yml | grep -E "formula-sheet|learning-guide"
```

**Pass criterion**: `formula-sheet.qmd` and `learning-guide.qmd` appear in
the sidebar block.

---

### V-09 — Continue link chain (SC-010)

**How to verify**: From the rendered site, open Module 1 and click the
"Continue" link at the bottom. Repeat for Modules 2–7, confirming each
Continue link resolves to the next module.

Alternatively, check source files:

```sh
grep -h "Continue" teaching/mathematical-fundamentals/module-*.qmd
```

Confirm:
- `module-1.qmd` → `module-2.qmd`
- `module-2.qmd` → `module-3.qmd`
- ...
- `module-7.qmd` → `module-8.qmd`
- `module-8.qmd` → `index.qmd` (or `glossary.qmd`)

**Pass criterion**: All 8 Continue links resolve correctly.

---

### V-10 — Zero build errors (SC-009)

```sh
quarto render 2>&1 | grep -i "error\|warning"
```

**Pass criterion**: No errors. Acceptable: Quarto deprecation warnings that
are pre-existing and unrelated to this feature.

---

### V-11 — Constitution T-IV amendment applied (SC-011)

```sh
grep "Observable JS\|OJS\|1.5.1" .specify/memory/constitution.md
```

**Pass criterion**: The string "Observable JS" (or "OJS") appears in T-IV;
version is "1.5.1"; `LAST_AMENDED_DATE` is updated to 2026-09-13.

---

## Implementation Order (recommended)

The following order minimises rework risk:

1. **Amendment** (`constitution.md` T-IV) — unblocks all interactive work.
2. **Scaffolding** (`formula-sheet.qmd`, `learning-guide.qmd`, sidebar in
   `_quarto.yml`) — unblocks link validation.
3. **Module 1** (full 12-section restructure + OJS simulator) — validates the
   template; all subsequent modules follow the same pattern.
4. **index.qmd** additions — short, independent.
5. **Modules 2–7** (restructure + OJS simulators) — order is flexible;
   Module 5 first recommended (chart-based simulator is most complex).
6. **Module 8** (restructure + static challenge) — last, after all other
   modules are stable so the challenge can reference them accurately.
7. **Final render + full validation run** (V-01 through V-11).

---

## References

- `contracts/module-page.md` — full 12-section template contract
- `contracts/ojs-simulation.md` — OJS code patterns and per-module specs
- `contracts/index-page.md` — index.qmd additions contract
- `data-model.md` — module coverage matrix (REUSE vs NEW vs EXTEND per cell)
- `research.md` — OJS code patterns, formula list (21 entries), T-IV
  amendment wording
