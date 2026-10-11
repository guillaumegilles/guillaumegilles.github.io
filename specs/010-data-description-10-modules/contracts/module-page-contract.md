# Contract: Module page

Every `teaching/data-description/modules/module-NN.qmd` MUST satisfy this
contract. It is the checklist reviewers use for FR-005 to FR-013 and
SC-002.

## Front matter

```yaml
---
title: "Module N — <title from catalogue>"
subtitle: "Data Description | <Part name>"
date-modified: 2026-MM-DD
lang: en
---
```

- No `date`; use `date-modified` (site convention).
- `draft: true` and `filters: [shinylive]` are inherited from
  `modules/_metadata.yml`; do not set them per file.
- Render a draft module for review with
  `PROFILE_README_RUNNING=1 quarto render <file> -M draft:false`
  (`PROFILE_README_RUNNING=1` stops the post-render hook from pushing to
  the GitHub profile repo).

## Section order (fixed)

| # | Heading | Required content |
|---|---|---|
| 1 | *(intro paragraph)* | The **business question**, in the Wandering Fork setting |
| 2 | `## Learning objectives` | ≥ 3 measurable bullets |
| 3 | `## Time plan` | Theory / Excel / exercises minutes, summing to 180 |
| 4 | `## Theory` | `.callout-note` definitions, `.callout-tip` formulas; each formula followed by a plain-language "what and why" sentence |
| 5 | `## Worked example` | Computed on the Wandering Fork data, numbers matching the dataset |
| 6 | `## Using Excel` | Table of concept → English-locale function/steps; link to `excel-functions.qmd` |
| 7 | `## Proof / derivation` | ≥ 1 `.callout-caution collapse="true"` |
| 8 | `## Visual intuition` | Geometric or visual reading (T-VII) |
| 9 | `## Interactive demo` | Shinylive block (required M3, M5, M9) **or** `.callout-important` `TODO:` |
| 10 | `## Exercises` | ≥ 1 by-hand and ≥ 1 Excel exercise; each a `.callout-caution collapse="true"` with solution; the callout title carries the track tag, e.g. `#### Exercise 1 (by hand) — title` or `#### Exercise 3 (Excel) — title` |

`## Time plan` is a table with one row per block whose first cell starts
with `Theory`, `Excel` or `Exercises` and whose second cell is the
minutes (an integer), for example `| Theory | 70 |`.
| 11 | `## Common mistakes` | `.callout-warning`, ≥ 1 item |
| 12 | `## Further reading` | ≥ 1 OpenStax and ≥ 1 Khan Academy entry |

Theory → worked example → exercises MUST stay in that relative order
(Constitution T-II). Sections 7–9 sit between the example and the
exercises.

## Callout semantics (Constitution V)

`.callout-note` definitions · `.callout-tip` formulas ·
`.callout-warning` caveats · `.callout-important` exam tips and TODOs ·
`.callout-caution` exercises and collapsible proofs.

## Further-reading entry format

```markdown
| Source | Where | What it adds | Time |
|---|---|---|---|
| OpenStax IBS 2e | §2.3 *Measures of the Center of the Data* | Mean, median, mode, grouped mean | ~12 pp |
| Khan Academy | *Summarizing quantitative data* ([unit](https://www.khanacademy.org/math/statistics-probability)) — lesson "Mean, median and mode" | Short videos and practice | ~30 min |
```

Khan Academy links are unit-level only unless the owner has verified a
deeper link (research §2). Do not embed videos.

## Style rules

- Prose wrapped at 80 characters; code blocks and URLs exempt.
- No inline `style=` and no `<style>` blocks in the page.
- Math via `$…$` and `$$…$$`.
- Every new symbol appears in `glossary.qmd`.
- Conventions as in research §3 (`QUARTILE.EXC`, `.S` by default).

## Review checklist (copy into PR)

- [ ] Business question present
- [ ] ≥ 3 measurable objectives
- [ ] Time plan sums to 180
- [ ] Every formula has a prose explanation
- [ ] Worked-example numbers recompute from the dataset
- [ ] Excel table uses English-locale names and links the function page
- [ ] Collapsible derivation present
- [ ] Visual intuition present
- [ ] Demo present (M3/M5/M9) or `TODO` callout
- [ ] By-hand and Excel exercises with solutions
- [ ] Further reading has OpenStax + Khan Academy
- [ ] Glossary updated
- [ ] `quarto render` of this file exits 0
