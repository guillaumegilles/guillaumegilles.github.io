# Data Model: Financial Analysis Slide Decks

This content model is a schema for the `.qmd` decks and the internal
coverage map. Nothing here is a database.

## Deck
| Field | Type | Rule |
|---|---|---|
| `path` | path | `fr/teaching/financial-analysis/slides/jour-{1,2,3}.qmd` |
| `title` | string | `"Jour N — <thème>"` |
| `subtitle` | string | `"Analyse financière et stratégique · INSEEC MSc"` |
| `footer` | link | `"[Retour au cours 📖](../index.qmd)"` |
| `blocks` | Block[] | ordered. Opens with an `Ouverture` block and closes with a `Récap` block |
| `minutes` | int | the sum of non-optional block minutes must be **360** |
| `warning_callouts` | int | ≤ 1 |
| `caution_callouts` | int | ≥ 1 (T-VI) |
| `todo_markers` | int | must be 0 before publishing |
| `en_stub` | path | `teaching/financial-analysis/slides/jour-N.qmd` must exist |

## Block
| Field | Type | Rule |
|---|---|---|
| `id` | slug | unique within the course (e.g. `b05-bilan-fonctionnel`) |
| `title` | string | section header slide (`#` level) |
| `minutes` | int | > 0. Appears on the agenda slide and in the notes |
| `optional` | bool | if true, the title ends with "(optionnel)" and it is excluded from the 360-min sum |
| `method_step` | 0–6 | 0 = fundamentals or context. Otherwise the BdF step taught |
| `quest` | Q1–Q9 or none | if set, the block's last slide links to `../modules/0N-*.qmd` |
| `reference_page` | path | a link to the course page (`../modules/…qmd`) that must resolve (FR-024) |
| `slides` | Slide[] | in role order: concept → formula → example → exercise (FR-005) |
| `sources` | Source[] | at least one source per block |

## Slide
| Field | Type | Rule |
|---|---|---|
| `role` | enum | `agenda`, `objectives`, `concept`, `definition`, `formula`, `derivation`, `example`, `exercise`, `focus`, `then-now`, `quest-input`, `recap`, `preview` |
| `heading` | string | `##` level |
| `figures` | Fact[] | any year-dependent number references a VerifiedFact and shows `::: aside` |
| `notes` | text | optional. Timing and answer-key filename. **Never** a solution |

Role-to-markup mapping: see [contracts/slide-deck-format.md](contracts/slide-deck-format.md).

## Exercise
| Field | Type | Rule |
|---|---|---|
| `id` | `exr-<slug>` | unique |
| `case` | string | e.g. `CONCOURSMANIA/LECTRA (2016)`, `CP3 — Fonds propres (ultra-frais)` |
| `task` | text | the instruction to students |
| `data` | table or path | readable data on the slide, or a link to the page holding it |
| `format` | string | team size or individual |
| `minutes` | int | counted in the block |
| `prerequisites` | Block.id[] | must come earlier in the same deck or a previous day |
| `answer_key` | path | an instructor document (e.g. `Cas pratiques d'analyse financière corrigé.docx`). Named in the notes and the coverage map |
| `key_tax_convention` | `25%` or `33⅓% (flagged)` | if flagged, the exercise slide says so |

## FocusBox
| Field | Rule |
|---|---|
| `company` | e.g. Orpéa, Casino, "Entreprises françaises" |
| `year` | the year of the event or data |
| `source` | Vernimmen letter number and date, or another source |
| `lesson` | 1–2 sentences on what the analyst should take away |

## VerifiedFact
| Field | Rule |
|---|---|
| `id` | F1…Fn (see research.md Part B) |
| `value` | as shown on the slide |
| `publisher`, `date`, `url` | required |
| `checked_on` | ISO date |
| `status` | `verified`, `fallback` (folder value with date) or `todo` (blocks publishing) |

## CoverageMap (`specs/014-financial-analysis-slides/coverage-map.md`, internal)
| Section | Rows | Satisfies |
|---|---|---|
| Original slides | 102 rows: slide no. → `deck/block/slide`, or `dropped: <reason>` | FR-009, SC-002 |
| Source files | one row per file in the folder → `used`, `partly used` or `not used` + reason | FR-020, SC-002 |
| Definitions | one row per ratio: chosen definition + rejected variants and sources | FR-012 |
| Verified facts | copied from research.md and kept up to date | FR-014a |
| Exercises | exercise → answer key → tax convention → gaps | FR-017a, FR-021 |
| Quest mapping | Q1–Q9 → block or input block or pointer | FR-003a |

## State: deck publication
`draft` → `content-complete` (all blocks present) → `verified` (0 `todo` facts, 0 `TODO: à vérifier`, coverage map complete) → `published` (in the sidebar, linked from `index.qmd`, renders clean).
