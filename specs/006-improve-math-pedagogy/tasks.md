# Tasks: Pedagogical Improvement — Mathematical Fundamentals Course

**Input**: Design documents from `specs/006-improve-math-pedagogy/`

**Prerequisites**: plan.md ✅ | spec.md ✅ | research.md ✅ | data-model.md ✅ |
contracts/ ✅ | quickstart.md ✅

**Tests**: No automated test tasks — this is a static content feature. Validation
uses `quarto render` exit codes and manual/scripted checks per `quickstart.md`.

**Organization**: Tasks grouped by phase and user story; each story is
independently renderable and verifiable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel with other [P] tasks in the same phase
- **[Story]**: User story this task belongs to (US1 / US2 / US3)
- Every task includes exact file paths

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Constitutional compliance, CSS foundation, and stub pages — blocks
all user story work.

**⚠️ CRITICAL**: All three tasks must be complete before any module content work
begins.

- [x] T001 Amend `.specify/memory/constitution.md`: replace T-IV wording
  "Shinylive interactive demo (`{shinylive-python}` block)" with "interactive
  demo — implemented as either a `{shinylive-python}` block (Shinylive Python)
  or a `{ojs}` block (Observable JS); use Shinylive when the simulation
  requires Python libraries; use OJS when the simulation is computable in pure
  JavaScript"; bump version field from 1.5.0 to 1.5.1; update
  `LAST_AMENDED_DATE` to 2026-09-13; update the T-IV gate row in
  `.specify/templates/plan-template.md` to read "Shinylive Python or OJS" (FR-031,
  `research.md` Decision 6)

- [x] T002 Add `.metric-grid`, `.metric-card`, and `.metric-label` CSS rules to
  `assets/dark.scss` — copy the exact SCSS block from `research.md` Decision 2
  ("CSS for metric display"); place after existing custom rules; required by all
  seven OJS simulations (Modules 1–7) before any module is rendered

- [x] T003 [P] Create stub `teaching/mathematical-fundamentals/formula-sheet.qmd`
  (front matter: `title: "Formula Sheet"`, `lang: en`; body: one sentence
  placeholder "Full formula reference coming soon.") and stub
  `teaching/mathematical-fundamentals/learning-guide.qmd` (same pattern with
  `title: "Learning Guide"`); add both files to the `mathematical-fundamentals`
  sidebar block in `_quarto.yml` under a new `- section: "Resources"` group
  after the module entries, alongside the existing `glossary.qmd` entry
  (FR-028) — prevents broken links when `index.qmd` Start Here section is added
  in Phase 4

**Checkpoint**: Run `quarto render teaching/mathematical-fundamentals/index.qmd
--quiet` → exit 0 (existing index renders cleanly with new sidebar entries).

---

## Phase 2: Foundational (Module 1 as Template Proof)

**Purpose**: Prove the 12-section template + OJS pattern on Module 1 before
scaling to Modules 2–8. All Phase 3 module tasks follow this validated blueprint.

**⚠️ CRITICAL**: T004 and T005 must be complete before T007–T013 begin. T006
must pass before any other module is restructured.

- [x] T004 Restructure `teaching/mathematical-fundamentals/module-1.qmd` to the
  12-section template (`contracts/module-page.md`):
  (a) Insert **§1 Diagnostic Activity**: three prerequisite questions — (1) evaluate
  `4 + 3 × 5`, (2) calculate 25% of 240, (3) a price rises from €80 to €92,
  find the % increase — followed by `.callout-note collapse="true" title="Check
  your answers"` with answers 19, 60, 15%;
  (b) Insert **§2 Opening Problem** immediately after: "A company increases its
  price by 20%, then reduces the new price by 20%. Does the product return to
  its original price?" as a blockquote; add "Write down your prediction before
  continuing.";
  (c) Reorganize existing theory into **§3 Core Concepts** — wrap each
  definition in `.callout-note` and each key rule/formula in `.callout-tip`;
  (d) Confirm existing worked examples are in **§4 Worked Example** (no
  rewrite needed, only label the sub-section);
  (e) Extend **§5 Guided Practice** — insert `.callout-tip collapse="true"
  title="Hint"` with one guiding step BEFORE the existing `.callout-caution
  collapse="true"` solution callout; the hint must appear at a lower line number
  than the solution;
  (f) Insert **§7 Applied Problem** — a business scenario (e.g., a retailer's
  revenue changes: compute absolute change, relative change, and interpret in
  one sentence) with at least 2 numbered questions and no solution given;
  (g) Insert **§8 Common Errors** `.callout-warning title="Common error —
  dividing by the wrong reference value"` showing the incorrect calculation
  (using final value as denominator) vs. the correct one (using initial value),
  with a one-sentence explanation;
  (h) Insert **§9 Check Your Understanding** — numbered list of exactly 5
  questions: (1) a calculation, (2) a conceptual definition, (3) an applied
  context question, (4) an error-diagnosis question, (5) a "find the value"
  question;
  (i) Insert **§10 Summary** — exactly 3 numbered takeaway sentences;
  (j) Insert **§11 Independent Work** — bulleted list of at least 3 study
  actions (complete exercises, record errors in error log, review glossary);
  (k) Insert **§12 Continue** — `[Continue to Module 2 →](module-2.qmd)`;
  (l) **Remove** the existing `.callout-important` TODO callout in the Order
  of Operations section (it is superseded by the OJS simulator in §6);
  (FR-001–FR-012)

- [x] T005 Add **§6 Interactive Exploration** OJS percentage-change simulator to
  `teaching/mathematical-fundamentals/module-1.qmd` between §5 Guided Practice
  and §7 Applied Problem — follow `contracts/ojs-simulation.md` exactly:
  three `{ojs}` code blocks:
  Block 1 — inputs: `viewof initialValue = Inputs.range([10, 1000], {value:
  100, step: 10, label: "Initial value"})`, `viewof increaseRate =
  Inputs.range([0, 100], {value: 20, step: 1, label: "Increase (%)"})`,
  `viewof decreaseRate = Inputs.range([0, 100], {value: 20, step: 1, label:
  "Decrease (%)"})`;
  Block 2 — reactive cells: `valueAfterIncrease = initialValue * (1 +
  increaseRate / 100)`, `finalValue = valueAfterIncrease * (1 - decreaseRate /
  100)`, `overallChange = 100 * (finalValue - initialValue) / initialValue`;
  Block 3 — html metric-grid display of all four values (initial, after
  increase, final, overall change) using `.toFixed(2)`;
  After the OJS blocks, add `### Investigation` with exactly 4 questions:
  (1) "Set both rates to 20%. What is the overall % change?",
  (2) "Repeat with 10%, 30%, and 50%. Does the pattern hold?",
  (3) "Does the initial value affect the overall % change? Explain.",
  (4) "Find a decrease rate that exactly reverses an increase of 25%. Why is
  this rate not 25%?"
  (FR-013)

- [x] T006 Render and validate Module 1: run `quarto render
  teaching/mathematical-fundamentals/module-1.qmd --quiet` and verify exit 0;
  open in browser and confirm: (a) all 12 section headings appear in the ToC
  sidebar, (b) three OJS sliders render (not blank), (c) output metric cards
  update when a slider is moved (no JS errors in DevTools console), (d) the
  hint `.callout-tip` appears above the solution `.callout-caution` in §5
  (quickstart.md V-01, V-02, V-04 — Module 1 only)

**Checkpoint**: Module 1 is a fully functional, renderable 12-section module
with a working OJS simulation. The template is proven. Modules 2–8 follow this
exact blueprint.

---

## Phase 3: User Story 1 — Full Module Learning Loop (Priority: P1) 🎯 MVP

**Goal**: All eight modules follow the 12-section template (`contracts/module-
page.md`) with one interactive exploration component per module (OJS for
Modules 1–7, static challenge for Module 8).

**Independent Test**: Run `quarto render teaching/mathematical-fundamentals/
--quiet` → exit 0; verify quickstart.md checks V-01 (12 sections in all
modules), V-02 (OJS widgets in Modules 1–7), V-03 (Module 8 static challenge),
V-04 (hint before solution in all modules), V-09 (Continue links complete
chain).

### Implementation for User Story 1

- [x] T007 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-2.qmd`
  to 12-section template + OJS break-even simulator:
  §1 Diagnostic: 3 questions — factor `x² + 4x`, expand `2(3x − 5)`, solve
  `5x − 8 = 12` — with `.callout-note collapse answers`;
  §2 Opening Problem: "A café has fixed costs of €2,000/month and variable
  costs of €3/unit, selling at €8/unit. How many units must it sell to cover
  its costs?" + prediction prompt;
  §3 Core Concepts: preserve existing algebraic definitions in `.callout-note`
  blocks; add break-even formula Q* = F/(p−v) in `.callout-tip`;
  §4 Worked Example: preserve existing worked examples;
  §5 Guided Practice: insert hint callout BEFORE existing solution callout;
  §6 Interactive Exploration — OJS break-even simulator: `viewof fixedCost =
  Inputs.range([0, 5000], {value: 2000, step: 100, label: "Fixed cost (€)"})`,
  `viewof variableCost = Inputs.range([0, 100], {value: 3, step: 0.5, label:
  "Variable cost per unit (€)"})`, `viewof price = Inputs.range([0, 200],
  {value: 8, step: 0.5, label: "Selling price per unit (€)"})`; reactive
  cells: `bep = fixedCost / (price - variableCost)`, revenue, cost, profit at
  bep; metric-grid html display; `### Investigation` with 3 questions including
  "What happens when the selling price equals the variable cost?";
  §7–§11 Applied Problem, Common Errors (distributing 3(x+4) as 3x+4),
  Check Your Understanding (5 questions), Summary (3 takeaways), Independent
  Work; §12 Continue link to `module-3.qmd` (FR-001–FR-012, FR-014)

- [x] T008 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-3.qmd`
  to 12-section template + OJS line-intersection explorer:
  §1 Diagnostic: 3 questions — read the y-intercept of y = 2x + 3, compute
  slope between (0,1) and (2,5), say whether y = −x + 4 is increasing or
  decreasing — with `.callout-note collapse answers`;
  §2 Opening Problem: "Two mobile phone plans: Plan A costs €10/month + €0.05
  per minute; Plan B costs €25/month + €0.01 per minute. At what usage do they
  cost the same?" + prediction prompt;
  §3 Core Concepts: preserve existing line/graph definitions; add intersection
  formula in `.callout-tip`;
  §4 Worked Example: preserve existing;
  §5 Guided Practice: insert hint before solution;
  §6 OJS line-intersection explorer: `viewof a1 = Inputs.range([-5, 5],
  {value: 2, step: 0.5, label: "Slope line 1"})`, `viewof b1`, `viewof a2`,
  `viewof b2` (intercepts range −10 to 10); reactive `xStar = (b2-b1)/(a1-a2)`,
  `yStar = a1*xStar + b1`; Observable Plot with two lines + intersection point;
  display x* and y* as metric cards; `### Investigation` with 3 questions
  including "What happens when both slopes are equal?";
  §7–§11 Applied Problem, Common Errors (confusing slope and intercept),
  Check Your Understanding, Summary, Independent Work; §12 Continue to
  `module-4.qmd` (FR-001–FR-012, FR-015)

- [x] T009 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-4.qmd`
  to 12-section template + OJS sequence explorer:
  §1 Diagnostic: 3 questions — next term of 3, 7, 11, 15…; next term of 2, 6,
  18, 54…; is the sequence 100, 50, 25 arithmetic or geometric? — with answers;
  §2 Opening Problem: "You receive a salary raise of €1,000/year (arithmetic)
  vs. 3%/year (geometric). After 10 years, which gives you a higher salary?" +
  prediction prompt;
  §3 Core Concepts: preserve sequence definitions; add uₙ = u₀ + nd and
  uₙ = u₀·rⁿ in `.callout-tip` blocks, each with a plain-language description;
  §4 Worked Example: preserve;
  §5 Guided Practice: insert hint before solution;
  §6 OJS sequence explorer: `viewof u0 = Inputs.range([0, 100], {value: 10,
  step: 1, label: "Initial term u₀"})`, `viewof d = Inputs.range([-10, 10],
  {value: 5, step: 1, label: "Common difference d (arithmetic)"})`,
  `viewof r = Inputs.range([0.5, 2.0], {value: 1.05, step: 0.05, label:
  "Common ratio r (geometric)"})`, `viewof n = Inputs.range([1, 20], {value:
  10, step: 1, label: "Number of terms"})`;
  display side-by-side Markdown-style table (using `html\``) of both sequences
  for terms 0 through n; `### Investigation` with 3 questions including "Under
  what conditions does the geometric sequence eventually exceed the arithmetic
  one?";
  §7–§11 Applied Problem, Common Errors (mixing up d and r), Check Your
  Understanding, Summary, Independent Work; §12 Continue to `module-5.qmd`
  (FR-001–FR-012, FR-016)

- [x] T010 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-5.qmd`
  to 12-section template + OJS compound-interest calculator with chart:
  §1 Diagnostic: 3 questions — compute simple interest on €1,000 at 5% for 2
  years; identify the capitalisation period in "compounded quarterly"; convert
  5% annual rate to quarterly rate — with answers;
  §2 Opening Problem: "€5,000 invested at 4% for 10 years — how much more does
  monthly compounding give compared to annual compounding?" + prediction;
  §3 Core Concepts: add simple-interest formula Vs = P(1+ni) and compound-
  interest formula Vc = P(1 + i/k)^(nk) in `.callout-tip` with descriptions;
  §4 Worked Example: preserve;
  §5 Guided Practice: insert hint before solution;
  §6 OJS compound-interest calculator: `viewof principal = Inputs.range([100,
  10000], {value: 5000, step: 100, label: "Principal P (€)"})`, `viewof rate =
  Inputs.range([0, 20], {value: 4, step: 0.1, label: "Annual rate i (%)"})`,
  `viewof periods = Inputs.range([1, 30], {value: 10, step: 1, label:
  "Number of years n"})`, `viewof freq = Inputs.select([1, 2, 4, 12], {value:
  1, label: "Capitalisation frequency k"})`;
  reactive: `simpleVal = principal*(1 + (rate/100)*periods)`, `compoundVal =
  principal * Math.pow(1 + (rate/100)/freq, periods*freq)`, `cumInterest =
  compoundVal - principal`; metric-grid display; Observable Plot line chart of
  compound value over time (array of {t, v} for t = 0..periods); `###
  Investigation` with 4 questions including "Which has more impact: the rate,
  the number of periods, or the frequency?";
  §7–§11 Applied Problem, Common Errors (using n instead of nk in the
  exponent), Check Your Understanding, Summary, Independent Work; §12 Continue
  to `module-6.qmd` (FR-001–FR-012, FR-017)

- [x] T011 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-6.qmd`
  to 12-section template + OJS function-family explorer:
  §1 Diagnostic: 3 questions — identify f(x) = 3x + 2 as affine/quadratic/
  other; compute the discriminant of x² − 5x + 6; is log(x) defined for
  x = −1? — with answers;
  §2 Opening Problem: "A firm's revenue grows very rapidly at first, then
  levels off. Which of these four function families — affine, quadratic,
  exponential, logarithmic — best models this pattern?" + prediction;
  §3 Core Concepts: preserve function definitions; add quadratic formula and
  discriminant in `.callout-tip`; add ln/exp inverse relationship;
  §4 Worked Example: preserve;
  §5 Guided Practice: insert hint before solution;
  §6 OJS function-family explorer: `viewof funcType = Inputs.select(["affine",
  "quadratic", "exponential", "logarithmic"], {value: "affine", label:
  "Function type"})`, `viewof param1 = Inputs.range([-5, 5], {value: 1,
  step: 0.5, label: "Parameter a"})`, `viewof param2 = Inputs.range([-10, 10],
  {value: 0, step: 0.5, label: "Parameter b"})`;
  reactive `data` array (x from −5 to 5) computed based on `funcType`: affine
  → a*x+b, quadratic → a*x²+b, exponential → Math.exp(a*x)+b (cap at
  reasonable y-range), logarithmic → a*Math.log(Math.max(x, 0.01))+b;
  Observable Plot line chart; add text output showing domain statement and
  notable features; `### Investigation` with 3 questions including "Which
  function type grows fastest for large x?";
  §7–§11 Applied Problem, Common Errors (domain error for logarithm), Check
  Your Understanding, Summary, Independent Work; §12 Continue to `module-7.qmd`
  (FR-001–FR-012, FR-018)

- [x] T012 [P] [US1] Restructure `teaching/mathematical-fundamentals/module-7.qmd`
  to 12-section template + OJS profit-maximisation simulator:
  §1 Diagnostic: 3 questions — compute f'(x) for f(x) = 3x² − 4x; find x
  where f'(x) = 0 for f(x) = −x² + 6x; is x = 3 a max or min for the
  previous function? — with answers;
  §2 Opening Problem: "A manufacturer's profit is P(q) = 40q − 0.1q² − 500.
  Which quantity maximises profit?" + prediction;
  §3 Core Concepts: preserve derivative definitions and rules (existing content
  in module-7.qmd is already strong); add f'(x*) = 0 condition in `.callout-
  tip`;
  §4 Worked Example: preserve;
  §5 Guided Practice: insert hint before solution;
  §6 OJS profit-maximisation simulator: fixed parameters R(q) = 60q − 0.2q²,
  C(q) = 500 + 20q displayed as constants; `viewof quantity = Inputs.range([0,
  200], {value: 50, step: 1, label: "Quantity q (units)"})`;
  reactive: `revenue = 60*quantity - 0.2*quantity**2`, `cost = 500 +
  20*quantity`, `profit = revenue - cost`; `qStar = (60-20)/(2*0.2)` (=100,
  derivative solution); Observable Plot showing R(q), C(q), P(q) curves with
  vertical marker at qStar; metric-grid display of R(q), C(q), P(q) at the
  slider position; `### Investigation` with 4 questions including "Move the
  slider to q = 100. Does the displayed P(q) match the derivative-based q*?
  Explain why.";
  §7–§11 Applied Problem, Common Errors (not verifying max vs. min, accepting
  f'=0 without checking second derivative), Check Your Understanding, Summary,
  Independent Work; §12 Continue to `module-8.qmd` (FR-001–FR-012, FR-019)

- [x] T013 [US1] Restructure `teaching/mathematical-fundamentals/module-8.qmd`
  to 12-section template + static 8-problem mixed-method challenge — complete
  AFTER T007–T012 are stable so challenge problems accurately reference them:
  §1 Diagnostic Activity: 4 mixed-method identification questions (unlabelled —
  student must identify method) with answers;
  §2 Opening Problem: "In the following problems, no chapter title is provided.
  Can you identify the right mathematical method before you begin?" + "Write
  down which method you would use for each of the following scenarios before
  continuing.";
  §3 Core Concepts: a reference summary table with 7 rows (one per method/
  module): Method name | When to use | Key formula or concept;
  §4 Worked Example: one cross-module integration problem (e.g., find the
  break-even quantity given a compound-interest-financed fixed cost);
  §5 Guided Practice: one cross-module exercise with hint and solution;
  §6 Interactive Exploration — 8 static `.callout-caution collapse="true"`
  problems; titles use neutral descriptors ("Problem 1 — A pricing scenario",
  etc., no method name); problems drawn one per module (Modules 1–7) plus one
  integration problem; each callout body starts with "**Method**: [Module N —
  method name]" then presents the full worked solution; prompt above: "Identify
  the appropriate mathematical method before expanding each problem.";
  §7 Applied Problem: an unlabelled multi-step problem requiring 2+ different
  methods;
  §8 Common Errors: method-identification errors (e.g., applying % change
  formula to a sequence problem);
  §9 Check Your Understanding: 5 unlabelled questions from Modules 1–7;
  §10 Summary: 3 exam-strategy takeaways;
  §11 Independent Work: review glossary, formula sheet, and one past exam;
  §12 Continue: `[Return to the course syllabus →](index.qmd)`
  (FR-001–FR-012, FR-020)

- [x] T014 [US1] Validate all 8 modules: run `quarto render
  teaching/mathematical-fundamentals/ --quiet` and verify exit 0; check V-01
  (all 12 section headings in each module's ToC), V-02 (OJS sliders render in
  Modules 1–7), V-03 (Module 8: 6-8 collapsibles, neutral titles, method label
  inside), V-04 (hint callout line number < solution callout line number in
  every module's §5), V-09 (Continue links: M1→M2→…→M7→M8, M8→index) per
  `quickstart.md`

**Checkpoint**: All 8 modules independently renderable with complete 12-section
template. User Story 1 is fully functional. Any module can be opened and studied
from start to finish without encountering a missing section or placeholder.

---

## Phase 4: User Story 2 — Course Entry Page as Learning Hub (Priority: P2)

**Goal**: `index.qmd` delivers all five required additions (welcome callout,
Start Here, learning-sequence tip, application questions, progress checklist),
transforming it from an institutional syllabus into a learner-oriented hub.

**Independent Test**: Render `teaching/mathematical-fundamentals/index.qmd` and
verify quickstart.md V-05 (all 5 elements present, all Start Here links
resolve).

### Implementation for User Story 2

- [x] T015 [US2] Add three elements to the top of
  `teaching/mathematical-fundamentals/index.qmd`:
  (a) A `.callout-note title="Welcome to the course"` block — 5 bullet-point
  outcomes: "perform calculations accurately", "translate practical problems
  into mathematical expressions", "choose an appropriate calculation method",
  "interpret equations, functions, graphs, and numerical results", "use
  mathematical tools to support managerial decisions" — placed before the first
  `##` heading;
  (b) A new `## Start Here` section — 5 numbered steps: (1) read the syllabus
  (anchor link to `#course-information`), (2) read the Learning Guide
  `learning-guide.qmd`, (3) complete the Module 1 Diagnostic Activity, (4)
  bookmark the Glossary `glossary.qmd`, (5) bookmark the Formula Sheet
  `formula-sheet.qmd`;
  (c) A `.callout-tip title="How to study each module"` immediately after Start
  Here — 6 numbered steps: Diagnose, Understand, Observe, Practise (hint
  before solution), Experiment (simulation + investigation questions), Apply
  (`contracts/index-page.md` Required Additions 1–3)
  (FR-021, FR-022, FR-023)

- [x] T016 [US2] Add a bolded application question after each module's topic
  list in the Course Roadmap section of
  `teaching/mathematical-fundamentals/index.qmd` — use the exact 8 questions
  from `contracts/index-page.md` Required Addition 4 (Module 1 through
  Module 8); place each question on a new line after the topic list, formatted
  as `**Application question**: [question text]`; do NOT remove or replace the
  existing topic-list descriptions (FR-024)

- [x] T017 [US2] Add `## Learning Progress` section to
  `teaching/mathematical-fundamentals/index.qmd`, positioned after the Course
  Roadmap section and before the Assessment section — 8 Markdown task-list
  items: `- [ ] Module 1: Numerical calculations` through `- [ ] Module 8:
  Revision and exam preparation` (FR-025)

- [x] T018 [US2] Validate index.qmd: run `quarto render
  teaching/mathematical-fundamentals/index.qmd --quiet` → exit 0; verify V-05:
  (a) welcome callout present before first `##` heading, (b) `## Start Here`
  section with 5 numbered steps and all links resolving, (c) `.callout-tip`
  How-to-study block with 6 steps, (d) application question after each of the
  8 module entries in the Roadmap, (e) `## Learning Progress` with 8 checkbox
  items per `quickstart.md`

**Checkpoint**: `index.qmd` is a complete learner-oriented course home. A
student can orient themselves, prepare, and navigate to any module from this
single page.

---

## Phase 5: User Story 3 — Supporting Reference Pages (Priority: P3)

**Goal**: `formula-sheet.qmd` (21 applied formulas) and `learning-guide.qmd`
(4 subsections) replace their stub content and serve as independent revision
resources.

**Independent Test**: Render the course and verify quickstart.md V-06 (formula
sheet: 7 sections, ~21 entries), V-07 (learning guide: 4 `##` sections), V-08
(both files in `_quarto.yml` sidebar).

### Implementation for User Story 3

- [x] T019 [P] [US3] Replace stub content in
  `teaching/mathematical-fundamentals/formula-sheet.qmd` with full content:
  front matter: `title: "Formula Sheet"`, `lang: en`, `toc: true`,
  `toc-depth: 2`; opening note: "Applied formulas only — approximately one to
  four per module. Intermediate rules are covered in each module's Core
  Concepts section."; seven `## Module N` sections; within each section, a
  definition-list or table presenting the 21 formula entries from `research.md`
  Decision 5 enumerated table: LaTeX formula (`$$...$$`) + plain-language label
  + one-sentence description — Module 1: 4 entries (% change, index number,
  proportionality, combined discount factor); Module 2: 2 entries (distributive
  law, break-even Q*); Module 3: 3 entries (slope, affine form, intersection);
  Module 4: 4 entries (arithmetic term, arithmetic sum, geometric term,
  geometric sum); Module 5: 3 entries (simple interest, compound interest,
  present value); Module 6: 3 entries (discriminant, quadratic formula,
  ln/exp inverse); Module 7: 3 entries (power derivative, linearity of
  derivative, optimality condition) (FR-026)

- [x] T020 [P] [US3] Replace stub content in
  `teaching/mathematical-fundamentals/learning-guide.qmd` with full content:
  front matter: `title: "Learning Guide"`, `lang: en`, `toc: true`;
  `## How to Prepare for Each Module` — per-module checklist of
  prerequisites to review and 2 self-test diagnostic questions to attempt
  before opening the module page (draw from the Diagnostic Activities written
  in T004–T013);
  `## Recommended Study Sequence` — step-by-step guide for a 90-minute
  session: (1) attempt Diagnostic Activity (15 min), (2) read Core Concepts
  (20 min), (3) study Worked Example (10 min), (4) attempt Guided Practice
  using hint then solution (20 min), (5) interact with simulation and answer
  Investigation questions (10 min), (6) attempt Applied Problem (15 min);
  `## Error Log` — Markdown table template with 4 columns (Error made / Root
  cause / Correct method / Prevention rule); instructions: record errors
  immediately after correcting exercises; review the log before each
  assessment; look for patterns;
  `## Revision Schedule` — 8-week plan (Module 1 week 1 through Module 7 week
  7, Module 8 revision week 8); 2-week consolidation block: week 9 (formula
  sheet + error log review), week 10 (timed practice exam under exam conditions)
  (FR-027)

- [x] T021 [US3] Validate formula sheet and learning guide: run `quarto render
  teaching/mathematical-fundamentals/ --quiet` → exit 0; verify V-06 (7
  `## Module N` sections in formula-sheet.qmd, 20–25 entries total, every
  entry has LaTeX + description), V-07 (4 `##` headings in learning-guide.qmd),
  V-08 (`formula-sheet.qmd` and `learning-guide.qmd` appear in
  `_quarto.yml` mathematical-fundamentals sidebar) per `quickstart.md`

**Checkpoint**: Both reference pages are complete. Students have a formula
sheet for exam revision and a learning guide for effective study — both linked
from the sidebar.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Full-site verification, global quality checks, and repository
housekeeping.

- [x] T022 Run full site render from repository root: `quarto render` and verify
  exit code 0 with no render errors; check that `docs/` is updated (quickstart
  V-10, SC-009)

- [x] T023 Run all quickstart.md validation checks V-01 through V-11 in sequence;
  document any failures with the exact failing check ID and the first
  non-passing symptom; fix any issues introduced by this feature (not
  pre-existing)

- [x] T024 [P] Verify `lang: en` front matter is present in all 11 modified
  `.qmd` files: run `grep -L "lang: en"
  teaching/mathematical-fundamentals/module-{1..8}.qmd
  teaching/mathematical-fundamentals/index.qmd
  teaching/mathematical-fundamentals/formula-sheet.qmd
  teaching/mathematical-fundamentals/learning-guide.qmd`; add `lang: en` to
  any file not returned as empty (constitution §VI)

- [x] T025 [P] Commit `docs/` (rendered HTML) and any `_freeze/` entries
  alongside the `.qmd` source changes in the same git commit (constitution §III)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 complete (T001–T003) — BLOCKS
  Phases 3, 4, 5
- **Phase 3 (US1)**: Depends on Phase 2 complete (T004–T006) — T007–T012 can
  run in parallel with each other; T013 depends on T007–T012; T014 depends on
  T013
- **Phase 4 (US2)**: Depends on Phase 1 complete (T003 — stubs must exist for
  links); can start after Phase 1 independently of Phase 3
- **Phase 5 (US3)**: Depends on Phase 1 complete (stubs must exist); can run
  after Phase 1 independently; T019 and T020 are parallel
- **Phase 6 (Polish)**: Depends on Phases 3, 4, and 5 all complete

### User Story Dependencies

- **US1 (Phase 3)**: T006 must pass; then T007–T012 parallel; T013 last; T014
  validates
- **US2 (Phase 4)**: Depends on T003 (stubs + sidebar) only; independent of US1
- **US3 (Phase 5)**: Depends on T003 (stubs created); T019 and T020 parallel;
  T021 validates; independent of US1 and US2

### Within US1

```
T004 → T005 → T006 (module 1 proof, sequential — same file)
                ↓
T007 ─┐
T008 ─┤
T009 ─┤ all parallel (different files)
T010 ─┤
T011 ─┤
T012 ─┘
  ↓
T013 (module 8 — depends on T007–T012 being stable)
  ↓
T014 (validate all 8 modules)
```

### Parallel Opportunities

**Phase 1**: T002 ∥ T003 (different files)

**Phase 3 (US1)**: T007 ∥ T008 ∥ T009 ∥ T010 ∥ T011 ∥ T012 (six different
module files, once T006 passes)

**Phase 4 (US2)**: T015, T016, T017 are sequential (same file); can run in
parallel with Phase 3 or 5

**Phase 5 (US3)**: T019 ∥ T020 (different files)

**Phase 6**: T024 ∥ T025

---

## Parallel Example: User Story 1 (after T006 passes)

```text
Parallel batch — all six can be worked simultaneously by different agents:

Task T007: Restructure module-2.qmd (12 sections + break-even OJS)
Task T008: Restructure module-3.qmd (12 sections + line-intersection OJS)
Task T009: Restructure module-4.qmd (12 sections + sequence OJS)
Task T010: Restructure module-5.qmd (12 sections + compound-interest OJS)
Task T011: Restructure module-6.qmd (12 sections + function-family OJS)
Task T012: Restructure module-7.qmd (12 sections + profit-max OJS)

Then sequential:
Task T013: Restructure module-8.qmd (depends on T007–T012 stable)
Task T014: Full validation of all 8 modules
```

---

## Implementation Strategy

### MVP First (Module 1 as Template Proof)

1. Complete **Phase 1** (T001–T003): Setup — ~30 min
2. Complete **Phase 2** (T004–T006): Module 1 restructured + OJS sim validated
3. **STOP and VALIDATE**: Open rendered Module 1 in browser; confirm all 12
   sections, OJS slider works, hint before solution
4. Deploy/demo Module 1 if ready — already delivers standalone educational value

### Incremental Delivery

1. Phase 1 + Phase 2 → Module 1 complete (MVP: proven template)
2. Phase 3 T007–T012 (parallel) + T013 + T014 → All 8 modules complete (US1)
3. Phase 4 (T015–T018) → Course home improved (US2)
4. Phase 5 (T019–T021) → Reference pages complete (US3)
5. Phase 6 (T022–T025) → Full-site validation and housekeeping

### Parallel Team Strategy

With multiple agents (after Phase 1 and Phase 2 complete):

- **Agent A**: T007, T008, T009 (Modules 2, 3, 4)
- **Agent B**: T010, T011, T012 (Modules 5, 6, 7)
- **Agent C**: T015, T016, T017 (index.qmd improvements — US2)
- **Agent D**: T019, T020 (formula sheet + learning guide — US3)
- After all: T013 (Module 8), T014, T018, T021, T022–T025

---

## Notes

- `[P]` tasks involve different files and have no blocking inter-task
  dependencies within the same phase
- `[US1/US2/US3]` labels map tasks to user story phases for traceability
- Each user story phase is independently renderable and verifiable
- The 12-section template is fully specified in `contracts/module-page.md`
- OJS code patterns and per-module simulator specs are in `contracts/ojs-simulation.md`
- All 21 formula entries are enumerated in `research.md` Decision 5
- Module 1 (T004–T005) should be fully confirmed (T006 passes) before beginning
  T007–T012 in parallel, even though they involve different files
- Module 8 (T013) should be last among the modules — its challenge problems
  reference solved examples from Modules 1–7
