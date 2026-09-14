# Research: Pedagogical Improvement — Mathematical Fundamentals

**Feature**: `006-improve-math-pedagogy` | **Date**: 2026-09-13

Sources: `specify-1.md` (financial-course pedagogy research),
`specify-2.md` (math-fundamentals-specific recommendations),
Quarto documentation, project constitution v1.5.0.

---

## Decision 1: OJS vs Shinylive — technology and privacy

**Decision**: Use Observable JS (OJS, `{ojs}` blocks) for all seven
interactive simulations (Modules 1–7). Shinylive Python is not used.

**Rationale**: OJS is compiled into self-contained JavaScript by the Quarto
renderer and embedded directly in `docs/`. At page load, the browser executes
only locally bundled code — no CDN requests, no WebAssembly bootstrap package
downloads, no external network calls. This satisfies the privacy-first
constitution (§IV) without compromise. Shinylive, by contrast, bootstraps a
Python runtime (Pyodide) from `jsdelivr.net` at page load, which constitutes
a third-party CDN call and would violate the constitution.

For the mathematics involved in all seven simulations (arithmetic, linear
equations, sequences, compound interest, function families, profit
maximisation), OJS reactive cells and `Inputs.*` components are fully
sufficient — no Python numerical libraries are needed.

**Alternatives considered**:
- *Shinylive only* — Rejected: CDN loading at page-load violates constitution
  §IV; adds a Python server dependency for a statically-hosted site.
- *OJS for most, Shinylive for one* — Rejected: the compound-interest chart
  (Module 5) and profit-maximisation curve (Module 7) are computable in pure
  OJS arithmetic; Shinylive would add complexity for no benefit.
- *Static exercises only (no interactivity)* — Rejected: the pedagogical
  research (`specify-1.md`, `specify-2.md`) identifies interactive exploration
  as a distinct learning phase that static exercises cannot replicate.

---

## Decision 2: OJS idiomatic patterns in Quarto

**Decision**: Each simulation uses the `viewof`/reactive-cell/`html`` pattern.

**Rationale**: This is the standard Quarto OJS pattern. `viewof` binds an
`Inputs.*` widget to a named variable; dependent cells re-evaluate reactively
whenever the input changes. `html`` template literals render dynamic output.
No `import` of external Observable notebooks is needed — all computations are
self-contained.

**Canonical patterns (used across all 7 simulations)**:

```
{ojs}
// Input slider
viewof paramA = Inputs.range([min, max], {
  value: defaultVal,
  step: stepSize,
  label: "Label"
})

// Reactive computation
result = paramA * someConstant

// Reactive display
html`<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-label">Result</span>
    <strong>${result.toFixed(2)}</strong>
  </div>
</div>`
```

For charts (Module 5 compound-interest growth, Module 7 profit curve):

```
{ojs}
// Build a data array reactively
data = Array.from({length: nPeriods + 1}, (_, t) => ({
  t,
  compound: principal * Math.pow(1 + rate / freq, t * freq)
}))

// Plot with Plot (bundled with Quarto)
Plot.plot({
  marks: [Plot.line(data, {x: "t", y: "compound"})],
  x: {label: "Period"},
  y: {label: "Value (€)"}
})
```

**CSS for metric display** (add to `assets/dark.scss` if not already present):

```scss
.metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}
.metric-card {
  padding: 0.75rem 1rem;
  border-radius: 6px;
  background: var(--bs-secondary-bg, #f8f9fa);
}
.metric-label {
  display: block;
  font-size: 0.8rem;
  opacity: 0.7;
  margin-bottom: 0.25rem;
}
```

**Alternatives considered**:
- *Import from Observable notebooks* — Rejected: creates an external CDN
  dependency (observablehq.com) at page load, violating §IV.
- *D3.js directly* — Rejected: Observable Plot (bundled) is a higher-level
  wrapper around D3 that requires less boilerplate and is already available.

---

## Decision 3: 12-section module template

**Decision**: Adopt the 12-section template from `specify-2.md` Section 4,
applied uniformly to all eight modules, adapted for Module 8.

**Rationale**: A consistent template reduces cognitive load for students
navigating multiple modules. Every section has a distinct pedagogical function:

| # | Section | Callout / Format | Pedagogical function |
|---|---|---|---|
| 1 | Diagnostic Activity | `.callout-note collapse="true"` (answers) | Surface prior knowledge; identify gaps |
| 2 | Opening Problem | Blockquote question + prompt | Motivate the method before teaching it |
| 3 | Core Concepts | `.callout-note` (defs) + `.callout-tip` (formulas) | Definitions, rules, prose explanations |
| 4 | Worked Example | Numbered steps + displayed math | Model the full solution process |
| 5 | Guided Practice | `.callout-tip collapse="true"` (hint) + `.callout-caution collapse="true"` (solution) | Progressive disclosure: hint before solution |
| 6 | Interactive Exploration | `{ojs}` block + interpretation questions | Experiment: observe parameter effects |
| 7 | Applied Problem | Prose scenario + questions | Transfer: real economics/management context |
| 8 | Common Errors | `.callout-warning` | Diagnose mistakes proactively |
| 9 | Check Your Understanding | Numbered list (5 questions) | Self-assess across question types |
| 10 | Summary | Numbered list (3 items) | Consolidate: three key takeaways |
| 11 | Independent Work | Bulleted checklist | Set expectations for out-of-class work |
| 12 | Continue | Markdown link | Navigate to next module |

**Module 8 adaptation**: Section 6 (Interactive Exploration) uses a static
mixed-method challenge (six to eight unlabelled problems, each in a
`.callout-caution collapse="true"` block) instead of an OJS simulation.

**Alternatives considered**:
- *Each module has a different structure* — Rejected: inconsistency increases
  cognitive load and undermines the "Understand → Calculate → Visualise →
  Interpret → Apply" mental model the research advocates.
- *Fewer sections (6)* — Rejected: the diagnostic, common-errors, and
  self-assessment sections are the primary additions that close the
  pedagogical gap; removing them defeats the purpose of this feature.

---

## Decision 4: Per-module simulator designs

**Module 1 — Percentage-change simulator**

Inputs: initial value (10–1000), increase rate (0–100 %), decrease rate
(0–100 %).
Outputs: value after increase, final value, overall % change.
Key question: "Why does a +20% followed by a −20% not return to the original
value?"
Module 1 `TODO:` callout (for an order-of-operations quiz) is removed; the
existing static exercises in Section 1 provide adequate practice, and the OJS
simulator fills the Interactive Exploration slot.

**Module 2 — Break-even simulator**

Inputs: fixed cost F (€), variable cost v (€/unit), selling price p (€/unit).
Outputs: Q* = F / (p − v), revenue R(Q*), total cost C(Q*), profit display.
Key question: "At what quantity does revenue equal total cost?"

**Module 3 — Line-intersection explorer**

Inputs: slope a₁, intercept b₁, slope a₂, intercept b₂ (all via sliders).
Outputs: graph of y₁ = a₁x + b₁ and y₂ = a₂x + b₂; computed intersection
(x*, y*) displayed algebraically.
Key question: "At what activity level do two pricing models give the same
result?"

**Module 4 — Sequence explorer**

Inputs: initial term u₀, common difference d (arithmetic), common ratio r
(geometric), number of terms n.
Outputs: side-by-side table of arithmetic and geometric sequence values.
Key question: "Under what conditions does a geometric sequence eventually
exceed an arithmetic sequence started with the same first term?"

**Module 5 — Compound-interest calculator with chart**

Inputs: principal P (€), annual rate i (%), number of periods n (years),
capitalisation frequency k (1 = annual, 2 = semi-annual, 4 = quarterly,
12 = monthly).
Outputs: simple-interest value, compound-interest value, cumulative interest
earned; Observable Plot line chart of compound value over time.
Key question: "Which has more impact on the final value: the interest rate,
the number of periods, or the capitalisation frequency?"

**Module 6 — Function-family explorer**

Inputs: function type (affine / quadratic / exponential / logarithmic) via
`Inputs.select`; up to two shape parameters (e.g., slope + intercept for
affine; a, b, c for quadratic) via sliders.
Outputs: Observable Plot graph updating in real time; displayed domain
statement and key features (intercepts, vertex or asymptote, sense of
variation) as text.
Key question: "Which function type best represents the economic phenomenon
you are modelling?"

**Module 7 — Profit-maximisation simulator**

Inputs: quantity q (0–200 units) via slider; fixed parameters for revenue
R(q) = pq − aq² and cost C(q) = F + vq shown as constants.
Outputs: R(q), C(q), P(q) = R(q) − C(q) for the chosen q; Observable Plot
showing all three curves; derivative-based optimal q* displayed alongside.
Key question: "Does the slider-discovered maximum agree with the derivative
solution? Why?"

**Module 8 — Static mixed-method challenge**

Six to eight unlabelled problems drawn from Modules 1–7 (one or two per
module). Each problem:
- Presented as plain text with no method hint.
- Prompt: "Identify the appropriate mathematical method before expanding."
- `.callout-caution collapse="true"` block reveals: method label (e.g.,
  "Compound interest — Module 5") + full worked solution.

---

## Decision 5: Formula sheet scope (applied formulas only)

**Decision**: ~20–25 applied formulas, one to four per module, Modules 1–7.

**Enumerated entries**:

| Module | Formula | Plain-language label |
|---|---|---|
| 1 | $\Delta\% = \dfrac{V_f - V_i}{V_i} \times 100$ | Percentage change |
| 1 | $I = \dfrac{V}{V_0} \times 100$ | Index number |
| 1 | $\dfrac{a}{b} = \dfrac{c}{x} \Rightarrow x = \dfrac{bc}{a}$ | Rule of proportionality ("rule of three") |
| 1 | $(1-t_1)(1-t_2)$ | Combined factor for two successive discounts |
| 2 | $a(b+c) = ab + ac$ | Distributive law (expanding) |
| 2 | $Q^* = \dfrac{F}{p - v}$ | Break-even quantity |
| 3 | $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ | Slope of a line |
| 3 | $y = mx + b$ | Affine function (slope-intercept form) |
| 3 | $x^* = \dfrac{b_2 - b_1}{a_1 - a_2}$ | Intersection of two affine functions |
| 4 | $u_n = u_0 + nd$ | Arithmetic sequence — general term |
| 4 | $S_n = \dfrac{n+1}{2}(u_0 + u_n)$ | Arithmetic sequence — sum of first $n+1$ terms |
| 4 | $u_n = u_0 \cdot r^n$ | Geometric sequence — general term |
| 4 | $S_n = u_0 \cdot \dfrac{1-r^{n+1}}{1-r}$ | Geometric sequence — sum of first $n+1$ terms ($r\neq 1$) |
| 5 | $V_s = P(1 + ni)$ | Simple interest — future value |
| 5 | $V_c = P\!\left(1 + \dfrac{i}{k}\right)^{nk}$ | Compound interest — future value |
| 5 | $P = \dfrac{V_c}{\left(1+i\right)^n}$ | Present value (annual compounding) |
| 6 | $\Delta = b^2 - 4ac$ | Discriminant of a quadratic |
| 6 | $x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$ | Quadratic formula |
| 6 | $\ln(e^x) = x,\quad e^{\ln x} = x$ | Inverse relationship: ln and exp |
| 7 | $(x^n)' = nx^{n-1}$ | Derivative of a power function |
| 7 | $(af + bg)' = af' + bg'$ | Linearity of the derivative |
| 7 | $f'(x^*) = 0$ | Necessary condition for a local extremum |

Total: 21 entries. Intermediate properties (fraction rules, power laws,
notable identities as stand-alone definitions) are excluded per the
clarification (Session 2026-09-13).

---

## Decision 6: Constitution T-IV amendment (FR-031)

**Decision**: PATCH amendment to T-IV, version 1.5.0 → 1.5.1.

**Current wording** (T-IV):
> Priority concepts in each course MUST have a Shinylive interactive demo
> (`{shinylive-python}` block). Where a demo has not yet been built, a
> `.callout-important` block with a `TODO:` label MUST mark the gap so
> missing demos are trackable.

**Proposed replacement**:
> Priority concepts in each course MUST have an interactive demo —
> implemented as either a `{shinylive-python}` block (Shinylive Python) or a
> `{ojs}` block (Observable JS). The choice of technology MUST be justified
> by the nature of the computation: use Shinylive when the simulation requires
> Python libraries; use OJS when the simulation is computable in pure
> JavaScript (arithmetic, algebra, elementary statistics). Where a demo has
> not yet been built, a `.callout-important` block with a `TODO:` label MUST
> mark the gap so missing demos are trackable.

**Governance compliance**:
- PATCH bump (wording clarification + new option; no existing principle
  removed or redefined).
- Version: 1.5.0 → 1.5.1.
- `LAST_AMENDED_DATE` updated to 2026-09-13.
- Sync pass: `plan-template.md` Constitution Check row T-IV updated to
  reflect "Shinylive Python or OJS"; `spec-template.md` and
  `tasks-template.md` require no changes.

**Rationale**: OJS satisfies the pedagogical intent of T-IV (interactive,
explorable, reactive) while being strictly more privacy-preserving than
Shinylive for computations that do not need Python. The amendment does not
weaken the requirement — it expands the approved implementation options.
