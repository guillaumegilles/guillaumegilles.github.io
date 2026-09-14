# Contract: OJS Simulation Block

**Feature**: `006-improve-math-pedagogy`
**Applies to**: Section 6 (Interactive Exploration) of Modules 1–7

---

## Required Structure

An OJS simulation block consists of **three mandatory parts** in this order:

1. An introductory sentence (markdown prose, outside the code block).
2. One or more `{ojs}` code blocks containing all reactive code.
3. A `### Investigation` sub-section with 2–4 follow-up questions (markdown
   prose, outside the code block).

```markdown
[1–2 sentence intro explaining what the simulation demonstrates.]

```{ojs}
// All reactive code here
```

### Investigation

1. [Question requiring the student to observe a specific behaviour]
2. [Question requiring the student to explain why it occurs]
3. [Question requiring the student to generalise across parameters]
4. [Optional: find a specific input that produces a target output]
```

---

## OJS Code Requirements

### Inputs

Every input MUST use an `Inputs.*` factory function and MUST be declared with
`viewof`:

```
{ojs}
viewof paramName = Inputs.range([min, max], {
  value: defaultValue,
  step: stepSize,
  label: "Human-readable label"
})
```

For categorical choices:

```
{ojs}
viewof funcType = Inputs.select(
  ["affine", "quadratic", "exponential", "logarithmic"],
  {value: "affine", label: "Function type"}
)
```

**Constraints**:
- `min`, `max`, `step`, `value`, and `label` MUST all be specified for
  `Inputs.range`.
- `value` and `label` MUST be specified for `Inputs.select`.
- Labels MUST be plain English, ≤ 6 words.

### Reactive Computations

Dependent values are declared as bare reactive cells (no `viewof`):

```
{ojs}
result = paramA * (1 + paramB / 100)
```

Computations MUST be self-contained: no `import` from external URLs or
Observable notebooks.

### Display Output

Metric cards (numerical outputs without a chart):

```
{ojs}
html`
<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-label">Label</span>
    <strong>${value.toFixed(2)}</strong>
  </div>
  <!-- additional cards -->
</div>
`
```

Charts (Observable Plot, bundled with Quarto):

```
{ojs}
Plot.plot({
  marks: [
    Plot.line(data, {x: "xField", y: "yField", stroke: "series"})
  ],
  x: {label: "X-axis label"},
  y: {label: "Y-axis label"},
  color: {legend: true}
})
```

**Constraints**:
- All floating-point outputs MUST use `.toFixed(2)` (or `.toFixed(N)` where
  N is appropriate for the domain) to avoid excessive decimal display.
- `Plot` is available globally (bundled by Quarto OJS runtime); no import
  needed.
- `html` template literal is available globally; no import needed.

---

## Privacy Constraint

MUST NOT use any of the following:
- `import ... from "https://..."` (external CDN)
- `import ... from "@observablehq/..."` (Observable notebook CDN)
- `require(...)` calls to external URLs

All APIs used (`Inputs`, `Plot`, `html`, `d3` if needed) are bundled
by Quarto's OJS runtime and are available without import.

---

## CSS Classes

The `.metric-grid` and `.metric-card` classes MUST be available. Add to
`assets/dark.scss` if not already present (see `research.md` Decision 2 for
the SCSS snippet). Inline `style=` attributes MUST NOT be used.

---

## Per-Module Simulation Specifications

| Module | Inputs | Outputs | Chart? |
|---|---|---|---|
| 1 | `initialValue` (10–1000), `increaseRate` (0–100), `decreaseRate` (0–100) | After-increase value, final value, overall % change | No |
| 2 | `fixedCost` (0–5000), `variableCost` (0–100), `price` (0–200) | Break-even Q*, revenue, cost, profit at Q* | No |
| 3 | `a1`, `b1`, `a2`, `b2` (slopes −5 to 5, intercepts −10 to 10) | x*, y*; Plot of two lines | Yes |
| 4 | `u0` (0–100), `d` (−10 to 10), `r` (0.5–2.0), `n` (1–20 terms) | Table of arithmetic sequence, table of geometric sequence | No |
| 5 | `principal` (100–10000), `rate` (0–20 %), `periods` (1–30), `freq` (1/2/4/12) | Simple value, compound value, cumulative interest; line chart over time | Yes |
| 6 | `funcType` (select), `param1`, `param2` (domain-specific sliders) | Plot of function; domain + key features text | Yes |
| 7 | `quantity` (0–200) | R(q), C(q), P(q); optimal q* via f'(q)=0; Plot of all three curves | Yes |

---

## Investigation Questions — Minimum Standards

Each simulation MUST be followed by at least 2 and at most 4 numbered
questions under `### Investigation`. At minimum:

1. One **observation** question: "What happens to [output] when you
   increase [input]?"
2. One **explanation** question: "Can you explain why [observed behaviour]
   occurs without referring to the graph?"

Additional questions may ask the student to find a specific parameter value
that produces a target output (e.g., "Find a decrease rate that exactly
reverses an increase of 25%.").
