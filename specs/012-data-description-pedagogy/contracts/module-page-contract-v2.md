# Contract: Module page — v2 (concrete-to-abstract)

Supersedes `specs/010-data-description-10-modules/contracts/module-page-contract.md`
for every **revised** module. Unrevised modules keep the v1 contract
until revised (research R7). Checked by
`specs/012-data-description-pedagogy/check_modules_v2.py`.

## Front matter

Unchanged from v1 (`title`, `subtitle`, `date-modified`, `lang: en`; no
`date`). Bump `date-modified` on revision.

## Section order (fixed)

| # | Heading | Required content |
|---|---|---|
| 1 | *(intro paragraph)* | Business question in the Wandering Fork setting |
| 2 | `## Learning objectives` | ≥ 3 measurable bullets on concepts and notation |
| 3 | `## Time plan` | Table; total 180; no `Excel lab` row (see below) |
| 4 | `## Theory` | Hook, then one concept cycle per core concept (below) |
| 5 | `## Worked example` | Full Wandering Fork data; numbers unchanged vs v1 |
| 6 | `## Proof / derivation` | ≥ 1 `.callout-caution collapse="true"` |
| 7 | `## Visual intuition` | Geometric/visual reading (T-VII) |
| 8 | `## Interactive demo` | `{ojs}` or Shinylive block, or `.callout-important` `TODO:` (T-IV: prefer OJS when the computation is plain arithmetic; OJS demos use only the built-in `html` template, not Plot, Inputs or d3, which the runtime fetches from a CDN) |
| 9 | `## Exercises` | By hand only: ≥ 3 exercises incl. ≥ 1 formula → words and ≥ 1 words → formula; titles `#### Exercise k (by hand) — …`; each `.callout-caution collapse="true"` |
| 10 | `## Common mistakes` | `.callout-warning`, ≥ 1 item |
| 11 | `## Exit check` | 3–5 numbered questions + one `.callout-caution collapse="true"` with answers; no Excel question |
| 12 | `## Homework — Excel lab` | See below |
| 13 | `## Further reading` | ≥ 1 OpenStax + ≥ 1 Khan Academy |

No `(Excel)` exercise may appear before `## Homework — Excel lab`.

## Time plan

Table rows `| <Block> | <minutes> | <what you do> |`, any block labels,
plus a `**Total**` row of 180. Rules:

- Sum of block minutes = 180.
- No block label starting with `Excel lab`.
- At most one `Excel preview` block, ≤ 5 minutes (instructor demo on
  screen, not a lab; spec Assumptions).
- A `Homework debrief` block (≤ 10) is required when the previous
  module is revised (it has homework).

## Theory: hook and concept cycles

1. `### <Hook title>` — a concrete contrast (e.g., two trucks, same
   mean) with a question for the class; no formula.
2. For each core concept, a `### <Concept>` subsection containing, in
   this order:

   | Step | Markup |
   |---|---|
   | Try it | Prompt + table (blanks as `?`), then `.callout-caution collapse="true"` titled `#### Try it — check your answer` |
   | See it | Figure, number line or table on the same numbers |
   | Say it | One plain sentence, starting `In plain words:` |
   | Write it | Existing `.callout-note` (definition) or `.callout-tip` (formula) |
   | Decoder | `.callout-note` titled `#### Notation decoder — <name>` with table `Symbol | Read aloud | In our example` and a `Whole formula as a sentence:` line |

   Every symbol in a formula callout appears in its decoder table.
   The first formula callout of the module MUST come after the first
   `Try it` callout. Recall concepts (defined in an earlier module) need
   Try it + Say it + link only.

## Synthesis module exception (Module 10)

A module whose purpose is review and a mock exam (Module 10) introduces
no new concept, so it is checked with `check_modules_v2.py --synthesis`:

- **Waived**: the hook and concept-cycle rules (first formula after a
  Try it; a decoder after every formula callout) and the formula ↔ words
  exercise rule in `## Exercises`.
- **Still required**: section order, time plan (180, no Excel lab,
  debrief row), exit check, homework section, and every other rule.
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
   mini-dataset and confirm the hand results.
4. `#### Homework k (Excel) — …` items, each `.callout-caution
   collapse="true"` with solution; all former Excel exercises present.

## Callout semantics (Constitution V)

Unchanged: note = definitions/decoders · tip = formulas · warning =
caveats/mistakes · important = exam tips/TODOs · caution = exercises,
Try-it answers, exit-check answers, homework, proofs. No new classes, no
`style=`, no `<style>`.

## Style rules

Unchanged from v1: prose ≤ 80 characters; `$…$` / `$$…$$`; new symbols in
`glossary.qmd`; course conventions (`.S` by default, `QUARTILE.EXC`).

## Review checklist (copy into commit / PR)

- [ ] Business question present; hook is the first Theory subsection
- [ ] Time plan = 180, no Excel lab, Excel preview ≤ 5 min, debrief row
      if required
- [ ] Module 10 only: checked with `--synthesis` (waived rules above)
- [ ] Every concept: Try it → See it → Say it → Write it → Decoder
- [ ] Every formula callout has a decoder covering all its symbols
- [ ] Worked-example numbers identical to v1
- [ ] Derivation, visual intuition, demo kept
- [ ] By-hand exercises incl. formula ↔ words; no Excel before homework
- [ ] Exit check: 3–5 questions, collapsible answers
- [ ] Homework: estimated time, follow-up, Using Excel, Step 0, all
      former Excel exercises
- [ ] Fidelity map row for every moved/renumbered block
- [ ] Glossary updated
- [ ] `check_modules_v2.py` passes; `quarto render` of the file exits 0
