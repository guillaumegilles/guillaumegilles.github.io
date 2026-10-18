# Module Template — Concrete-to-Abstract (contract v2.1)

Use this template to revise Modules 7–10 of the Data Description course.
It is distilled from the final **Module 6** page
(`teaching/data-description/modules/module-06.qmd`), which is the
reference implementation, and from
[contracts/module-page-contract-v2.md](./contracts/module-page-contract-v2.md),
which stays the normative source. When the two disagree, the contract
wins.

A page still written with v2 collapsible callouts can be converted
first (statements and solutions move verbatim):

```sh
.venv/bin/python specs/012-data-description-pedagogy/convert_callouts.py \
  teaching/data-description/modules/module-NN.qmd
```

Validate every revised page with:

```sh
.venv/bin/python specs/012-data-description-pedagogy/check_modules_v2.py \
  teaching/data-description/modules/module-NN.qmd
PROFILE_README_RUNNING=1 quarto render \
  teaching/data-description/modules/module-NN.qmd --quiet
```

---

## 1. Page skeleton (section order is fixed)

```markdown
---
title: "Module N — <Topic>"
subtitle: "Data Description | Part <…> — <…>"
date-modified: YYYY-MM-DD
---

**The business question.** <Wandering Fork question, 1 paragraph>.
<Last sentence leading into the hook, e.g. "We start with … small
enough to compute by hand, and only then write the formulas.">

## Learning objectives

By the end of this module, you will be able to:

- <≥ 3 measurable bullets on concepts and notation: explain in words,
  compute by hand, read a formula aloud, write a formula from words>

## Theory

### <Hook title>
### <Concept 1>
### <Concept 2>
…

## Worked example
## Proof / derivation
## Visual intuition
## Interactive demo
## Exercises
## Common mistakes
## Exit check
## Homework — Excel lab
### Using Excel
### Step 0 — check your class results
## Further reading
```

No heading containing `(Excel)` may appear above
`## Homework — Excel lab`.

---

## 2. The micro-cycle: Try it → See it → Say it → Write it → Decoder

Every **core concept** (introduced in this module) gets one
`### <Concept>` subsection inside `## Theory`, with the five steps in
this order. The *Use it* step is the `## Worked example` and the
by-hand exercises.

### 2.0 Hook (first Theory subsection)

A concrete contrast on a mini-dataset, a question for the class, **no
formula and no callout**.

```markdown
### Same mean, different days

Two Wandering Fork trucks recorded their revenue over the same five
days. The numbers are a simplified extract chosen so that you can
compute everything by hand.

| Day | Truck A "Steady" (€) | Truck B "Erratic" (€) |
|---|---:|---:|
| 1 | 590 | 370 |
| … | … | … |
| **Mean** | **620** | **620** |

Both trucks earn **€620 on an average day**. Which one would you rather
manage — and what would you tell the bank about each one's revenue?
```

### 2.1 Try it — prompt, table with `?` blanks, answer fold

```markdown
**Try it.** Complete the deviation table for Truck A
($n = 5$, $\bar{x} = 620$), working column by column.

| Day $i$ | $x_i$ (€) | $x_i-\bar{x}$ (€) | $(x_i-\bar{x})^2$ (€²) |
|---|---:|---:|---:|
| 1 | 590 | ? | ? |
| … | … | ? | ? |
| **Total** | **3,100** | **?** | **?** |

1. Fill the deviation column, then add it up. What do you notice?
2. Square each deviation and add up the squares.

Your turn: build the same table for Truck B.

<details class="answer">
<summary>Check your answer</summary>

<completed tables + one sentence of interpretation>

</details>
```

The summary must be exactly `Check your answer`, and the blank lines
around the answer are required (otherwise the Markdown inside is not
parsed). After the
answer, a short **"Why …?"** paragraph can turn the observation into the
motivation for the next step (Module 6: "deviations sum to 0 → square";
"only 4 of 5 deviations are free → divide by $n-1$").

### 2.2 See it — a picture of the same numbers

```markdown
**See it.** Step 2 of the figure draws each deviation as a bar from the
mean (sum = 0). Step 3 draws each squared deviation as a square.
```

See rule §5 for when to use an OJS figure.

### 2.3 Say it — one plain sentence

```markdown
In plain words: measure how far each observation is from the mean,
square those distances, average them (with $n-1$), and take the square
root to get back to the original unit.
```

The line starts with `In plain words:`. If the v1 page already had an
"In plain words" paragraph, merge it here — don't duplicate it.

### 2.4 Write it — the existing callout, verbatim

```markdown
::: {.callout-tip}
#### Formula — sample variance and standard deviation
<existing v1 text and formula, unchanged>
:::
```

`.callout-note` for definitions, `.callout-tip` for formulas. **Keep
v1 text byte-for-byte** (T-I); only its position changes.

### 2.5 Notation decoder — directly after every `.callout-tip`

A plain section, **not a callout** (Constitution V, v2.0.0): a heading,
the table and the sentence.

```markdown
#### Notation decoder: sample variance and standard deviation

| Symbol | Read aloud | In our example (Truck A) |
|---|---|---|
| $n$ | "n" | 5 days |
| $x_i$ | "x sub i" | the value on day $i$, e.g. $x_1 = 590$ |
| $\bar{x}$ | "x-bar" | the mean, 620 |
| $\sum_{i=1}^{n}$ | "add up, for i from 1 to n" | the Total row: 1,600 |
| $s^2$ | "s squared" | 400 €² |

**Whole formula as a sentence:** "the sample variance is the sum, over
all $n$ days, of each day's squared distance from the mean, divided by
$n-1$; the standard deviation is its square root."
```

Rules: every symbol of the formula callout appears in the table; the
"In our example" column uses the numbers from the Try it; the checker
requires the decoder before the next `###` heading. Remarks that
followed the formula in v1 (e.g. a "Why $n-1$" warning) become plain
prose after the decoder, or a link to a dedicated post; they are not
callouts.

### Callouts allowed on a module page

| Type | Use for |
|---|---|
| `.callout-note` | Definitions |
| `.callout-tip` | Formulas |
| `.callout-caution` | The proof in `## Proof / derivation` |
| `.callout-warning` | `## Common mistakes` (one block) |
| `.callout-important` | `TODO:` markers |

Everything else (decoders, remarks, exercises, answers) is plain
markup.

---

## 3. Recall cycle (concepts from earlier modules)

A concept defined in an earlier module needs only **Try it + Say it +
link**, no new formula callout and no decoder:

```markdown
**Recall.** You computed $Q_1$ and $Q_3$ in
[Module 5](module-05.qmd); the IQR is simply the gap between them, read
off the boxplot as the length of the box.
```

If a v1 page restates an earlier formula in a `.callout-tip`, keep the
callout (T-I) and give it a decoder anyway — the checker requires one
after every tip in `## Theory`.

---

## 4. Mini-dataset rules

- ≤ 6 values per dataset (or ≤ 6 pairs, or a 2×2 / 2×3 table).
- Whole-number means and deviations; perfect squares where a square
  root is taken.
- Hand arithmetic for one Try it ≤ 5 minutes.
- Set in the Wandering Fork world and labelled as a simplified extract.
- Verify every number with `.venv/bin/python` (NumPy, `ddof=1`; SciPy
  where needed) and record the values, the check and the alternatives
  considered in `research.md` as `## R<k>. Module N mini-datasets`.
- The real-data worked example stays unchanged; the mini-data never
  replace it.

---

## 5. "See it" rule

- Use an `{ojs}` figure when a picture adds meaning (positions,
  distances, areas, shapes, quadrants). Use `//| echo: false`.
- **Only the built-in `html` template + inline SVG** — no Observable
  Plot, `Inputs` or d3, because Quarto's runtime fetches them from
  `cdn.jsdelivr.net` (Principle IV). Module 6's two-truck figure and the
  Module 3/5/9 demos are the reference.
- Compute every displayed total in JavaScript from the data arrays (no
  hard-coded results); colours as SVG attributes, never `style=`.
- A step picker is a plain `<form>` of radio buttons exposed with
  `viewof` (see Module 6, `viewof step`).
- When no picture fits, use a table or a number line written in
  Markdown. **"See it" is never skipped.**

---

## 6. Exercises and answer folds

Exercises use Quarto's built-in exercise block: the statement stays
visible, the solution is folded, and Quarto numbers them in page order
("Exercise 1 (Shortcut formula)"). Link to one with `@exr-<slug>`.

```markdown
## Exercises

All exercises below are done by hand; the Excel ones are in the
[homework](#homework-excel-lab).

::: {#exr-shortcut-formula name="Shortcut formula"}
A sample of $n=5$ values has $\sum x_i = 100$ and $\sum x_i^2 = 2140$.
Find the sample variance.

<details class="answer">
<summary>Solution</summary>

$\bar{x}=100/5=20$, so $s^2 = \frac{1}{4}(2140-2000) = 35$.

</details>
:::
```

- `name` is a short title, no `(by hand)` tag and no "click for
  solution".
- Slugs are lowercase words joined by `-`, unique on the page.
- Summary labels: `Check your answer` (Try it), `Solution` (exercises,
  homework), `Answers` (exit check), `Expected results` (Step 0).
- The proof in `## Proof / derivation` is a `.callout-caution`;
  `collapse="true"` is optional, and the title says "(click to
  expand)" only when it is collapsed.

---

## 7. Homework rules

```markdown
## Homework — Excel lab

Reproduce, in Excel, every indicator you computed by hand in class,
with `<FUNC1>`, `<FUNC2>` …, then apply them to the full dataset.

**Estimated time:** about 50–60 minutes. Any spreadsheet application
works, at home or in a campus computer room.

**Follow-up:** a 10-minute debrief at the start of
[Module N+1](module-0N+1.qmd). Bring your Step 0 results and any
question on Homework 1–k.

### Using Excel

<former `## Using Excel` section, content unchanged, H2 → H3>

### Step 0 — check your class results

1. Type <mini-dataset> in `A2:A6` …
2. Compute `=…` …
3. Compare every result with your hand computation.

<details class="answer">
<summary>Expected results</summary>

| Indicator | <Set 1> | <Set 2> |
|---|---:|---:|
| … | … | … |

</details>

### Homework 1 (Excel) — <former Exercise k title>

<statement, verbatim>

**How to.** <at most one line of exact steps>

<details class="answer">
<summary>Solution</summary>

<solution, verbatim>

</details>
```

- Estimated time ≤ 60 minutes (SC-005; ≤ 10 h over the course).
- **All** former `(Excel)` exercises move here, statements and
  solutions verbatim, renumbered `Homework 1 … k (Excel)`; add at most
  one `**How to.**` line before each solution.
- Homework items are `###` headings (they appear in the page's table
  of contents), not exercise blocks, so their numbering stays separate
  from the in-class exercises.
- In-class exercises are numbered automatically by Quarto.
- Log every move and renumbering in `fidelity-record.md`.

---

## 8. Per-module revision checklist (from contract v2.1)

- [ ] Business question present; hook is the first Theory subsection
- [ ] No `## Time plan` section
- [ ] Module 10 only: checked with `--synthesis` (see §9)
- [ ] Every concept: Try it → See it → Say it → Write it → Decoder
- [ ] Every formula callout has a decoder covering all its symbols
- [ ] Worked-example numbers identical to v1
- [ ] Derivation, visual intuition, demo kept
- [ ] By-hand exercise blocks incl. formula ↔ words; no Excel before
      homework
- [ ] Every answer and solution in a `<details class="answer">` fold
- [ ] Callouts only for definitions, formulas, the proof, common
      mistakes and TODOs; decoders are plain sections
- [ ] No `lang:` in front matter
- [ ] Exit check: 3–5 questions, folded answers
- [ ] Homework: estimated time, follow-up, Using Excel, Step 0, all
      former Excel exercises
- [ ] Fidelity map row for every moved/renumbered block
- [ ] Glossary updated
- [ ] `check_modules_v2.py` passes; `quarto render` of the file exits 0

Exercise markup for the two notation exercises (the names must contain
`Formula to words` and `Words to formula`):

```markdown
::: {#exr-formula-words name="Formula to words"}
(a) Read $<formula>$ aloud as one sentence. Which indicator is it?

<details class="answer">
<summary>Solution</summary>

(a) "…"

</details>
:::

::: {#exr-words-formula name="Words to formula"}
Write in symbols: (a) "…"; (b) "…".

<details class="answer">
<summary>Solution</summary>

(a) $…$. (b) $…$.

</details>
:::
```

Exit-check markup:

```markdown
## Exit check

Five minutes, no calculator needed except for question 4.

1. In one sentence, what does … measure?
2. Why …?
3. Read $<formula>$ aloud as a sentence.
4. Compute … for the values ….
5. Which indicator …, and why?

<details class="answer">
<summary>Answers</summary>

1. …

</details>
```

No Excel question in the exit check.

---

## 9. Module 10 exception (copied from contract v2.1)

> **Synthesis module exception (Module 10)**
>
> A module whose purpose is review and a mock exam (Module 10)
> introduces no new concept, so it is checked with
> `check_modules_v2.py --synthesis`:
>
> - **Waived**: the hook and concept-cycle rules (first formula after a
>   Try it; a decoder after every formula callout) and the formula ↔
>   words exercise rule in `## Exercises` (≥ 1 exercise block is still
>   needed).
> - **Still required**: section order, exit check, homework section,
>   and every other rule.
> - Formula callouts that remain on the page (e.g., in the walkthrough)
>   SHOULD still link to the decoder in the module where they were
>   introduced.

Checker command for Module 10:

```sh
.venv/bin/python specs/012-data-description-pedagogy/check_modules_v2.py \
  --synthesis teaching/data-description/modules/module-10.qmd
```

Module 10 still needs ≥ 1 `::: {#exr-…}` exercise block. Its
homework follow-up is a self-check with the solutions, since there is
no next module.
