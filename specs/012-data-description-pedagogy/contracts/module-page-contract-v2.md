# Contract: Module page — v2.1 (concrete-to-abstract)

Supersedes `specs/010-data-description-10-modules/contracts/module-page-contract.md`
for every **revised** module. Unrevised modules keep the v1 contract
until revised (research R7). Checked by
`specs/012-data-description-pedagogy/check_modules_v2.py`.

**v2.1 (2026-10-18)** changes from v2:

- The `## Time plan` section is removed from module pages (owner
  decision). Timing guidance lives in `module-template.md` only.
- Exercises use Quarto's built-in exercise block (`::: {#exr-…}`),
  auto-numbered, with the statement visible.
- Try-it answers, exercise solutions, exit-check answers, Step 0
  results and homework solutions are folded in
  `<details class="answer">` instead of `.callout-caution
  collapse="true"`.
- Notation decoders are plain `#### Notation decoder: <name>` sections
  (heading + table + sentence), not callouts.
- Callouts are limited to the Constitution V roles (v2.0.0): note =
  definition, tip = formula, caution = proof, warning = common
  mistakes, important = `TODO:`. The proof's collapse is optional.
- `lang:` is no longer set per page (inherited from
  `teaching/_metadata.yml`).
- `convert_callouts.py` converts a v2 page to v2.1 (answers and
  exercises; decoders are unboxed by hand).

## Front matter

`title`, `subtitle`, `date-modified`; no `date`, no `lang:` (inherited
from `teaching/_metadata.yml`, Constitution VI). Bump `date-modified` on
revision.

## Section order (fixed)

| # | Heading | Required content |
|---|---|---|
| 1 | *(intro paragraph)* | Business question in the Wandering Fork setting |
| 2 | `## Learning objectives` | ≥ 3 measurable bullets on concepts and notation |
| 3 | `## Theory` | Hook, then one concept cycle per core concept (below) |
| 4 | `## Worked example` | Full Wandering Fork data; numbers unchanged vs v1 |
| 5 | `## Proof / derivation` | ≥ 1 `.callout-caution`; `collapse="true"` optional, and the title says "click to expand" only when collapsed |
| 6 | `## Visual intuition` | Geometric/visual reading (T-VII) |
| 7 | `## Interactive demo` | `{ojs}` or Shinylive block, or `.callout-important` `TODO:` (T-IV: prefer OJS when the computation is plain arithmetic; OJS demos use only the built-in `html` template, not Plot, Inputs or d3, which the runtime fetches from a CDN) |
| 8 | `## Exercises` | By hand only: ≥ 3 exercise blocks incl. one named `Formula to words` and one named `Words to formula`; see "Answer folds and exercises" |
| 9 | `## Common mistakes` | `.callout-warning`, ≥ 1 item |
| 10 | `## Exit check` | 3–5 numbered questions, then one answer fold; no Excel question |
| 11 | `## Homework — Excel lab` | See below |
| 12 | `## Further reading` | ≥ 1 OpenStax + ≥ 1 Khan Academy |

No `(Excel)` exercise may appear before `## Homework — Excel lab`.

## Answer folds and exercises

**Answer fold** — used for every answer or solution:

```markdown
<details class="answer">
<summary>Check your answer</summary>

…answer, verbatim (Markdown, math and tables allowed)…

</details>
```

Blank lines after `<summary>` and before `</details>` are required so
the content is parsed as Markdown. Summary labels: `Check your answer`
(Try it), `Solution` (exercises, homework), `Answers` (exit check),
`Expected results` (Step 0).

**Exercise block** — in `## Exercises`:

```markdown
::: {#exr-<slug> name="<Short title>"}
<statement, visible>

<details class="answer">
<summary>Solution</summary>

<solution>

</details>
:::
```

Quarto renders the title as "Exercise k (<Short title>)", numbered
automatically in page order; `@exr-<slug>` links to it. The `(by hand)`
tag is dropped: every exercise in the section is by hand, and a one-line
intro under `## Exercises` says so.

## Theory: hook and concept cycles

1. `### <Hook title>` — a concrete contrast (e.g., two trucks, same
   mean) with a question for the class; no formula.
2. For each core concept, a `### <Concept>` subsection containing, in
   this order:

   | Step | Markup |
   |---|---|
   | Try it | `**Try it.**` prompt + table (blanks as `?`), then an answer fold with summary `Check your answer` |
   | See it | Figure, number line or table on the same numbers |
   | Say it | One plain sentence, starting `In plain words:` |
   | Write it | Existing `.callout-note` (definition) or `.callout-tip` (formula) |
   | Decoder | Plain section (no callout): `#### Notation decoder: <name>`, a table `Symbol | Read aloud | In our example` and a `Whole formula as a sentence:` line |

   Every symbol in a formula callout appears in its decoder table.
   The first formula callout of the module MUST come after the first
   Try it answer fold. Recall concepts (defined in an earlier module)
   need Try it + Say it + link only.

## Synthesis module exception (Module 10)

A module whose purpose is review and a mock exam (Module 10) introduces
no new concept, so it is checked with `check_modules_v2.py --synthesis`:

- **Waived**: the hook and concept-cycle rules (first formula after a
  Try it; a decoder after every formula callout) and the formula ↔ words
  exercise rule in `## Exercises` (≥ 1 exercise block is still needed).
- **Still required**: section order, exit check, homework section, and
  every other rule.
- Formula callouts that remain on the page (e.g., in the walkthrough)
  SHOULD still link to the decoder in the module where they were
  introduced.

## Homework — Excel lab

In this order:

1. Intro paragraph containing `Estimated time:` (≤ 60 min), where to do
   it, and `Follow-up:` (debrief at the start of Module N+1).
2. `### Using Excel` — concept → English-locale function table; link to
   `excel-functions.qmd` (former `## Using Excel`, unchanged).
3. `### Step 0 — check your class results` — re-enter the in-class
   mini-dataset and confirm the hand results; expected values in an
   answer fold (`Expected results`).
4. `### Homework k (Excel) — …` headings, statement and optional
   `**How to.**` line visible, solution in an answer fold (`Solution`);
   all former Excel exercises present. Homework items are not exercise
   blocks, so they don't continue the in-class exercise numbering.

## Callout semantics (Constitution V, v2.0.0)

| Type | Use for |
|---|---|
| `.callout-note` | Definitions |
| `.callout-tip` | Formulas |
| `.callout-caution` | Proofs and derivations (only in `## Proof / derivation`) |
| `.callout-warning` | Common mistakes (one block) |
| `.callout-important` | `TODO:` markers |

Not callouts: exercises (exercise blocks), answers (folds), decoders,
remarks and background (plain prose, headings, tables). Styling of
`.theorem.exercise` and `details.answer` lives in `assets/dark.scss`.
No new callout classes, no `style=`, no `<style>`.

## Style rules

Unchanged from v1: prose ≤ 80 characters; `$…$` / `$$…$$`; new symbols in
`glossary.qmd`; course conventions (`.S` by default, `QUARTILE.EXC`).

## Review checklist (copy into commit / PR)

- [ ] Business question present; hook is the first Theory subsection
- [ ] No `## Time plan` section
- [ ] Module 10 only: checked with `--synthesis` (waived rules above)
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
