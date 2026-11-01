# Data Model: Financial Analysis — 3-Day Course

The "data" is course content. Entities map to pages or table rows; there
is no database. Fields are what an author must supply.

## Course

| Field | Rule |
|---|---|
| title, description, objectives | On `index.qmd` |
| total teaching minutes | MUST equal 1 080 (FR-001, FR-003) |
| days | exactly 3 |
| literature | Author, title, edition, publisher (T-VIII) |
| competence mapping | Rewritten to match the final blocks (FR-013) |
| exams | Two entries, both flagged `outside_18h = true` (FR-012) |

## Day

| Field | Rule |
|---|---|
| number | 1, 2 or 3 |
| narrative goal | One sentence |
| prerequisites | Listed (edge case: late joiners) |
| preparation | Tasks + expected effort ≤ 45 min per evening |
| blocks | Ordered; durations sum to exactly 360 |
| boss deliverable | Slot, deliverable, grading criteria |
| breaks | Listed, not counted |

## Block

| Field | Rule |
|---|---|
| id | `D<day>-B<n>` |
| start offset (min) | Cumulative from day start |
| duration (min) | Integer; theory segment 20–30 inside quest blocks (FR-005) |
| learning goal | One sentence |
| sources | Existing page(s) or file(s) used (US1 scenario 3) |
| theory | Live segment (and pre-reading link) |
| worked example | Present (FR-006) |
| exercise | `exr-` block; answer folded (FR-006) |
| derivation | One `.callout-caution` per quest (T-VI) |
| demo | OJS block or `TODO:` callout (FR-017) |
| cut-first note | What to drop when late (edge case) |
| xp | Integer; sum over all blocks = 1 500 |

## Quest (existing, 9)

Maps 1:1 to a quest block (Q1…Q9 → D1-B2, D1-B3, D1-B4, D2-B1…D2-B3,
D3-B1…D3-B3). Fields: team size 3–5, deliverables, grading criteria, XP.

## Reference topic (existing, 6)

`banque-france`, `performances`, `structure-fi`, `liquidite`,
`banque-france-cotation`, `formules`. Fields: feeds-quests list (R4),
pre-reading minutes.

## Assessment item

| Field | Rule |
|---|---|
| kind | `xp-activity`, `boss`, `exam` |
| xp | 0 for exams |
| in_18h | true for xp/boss, false for exams |
| grade share | XP 40 %, exam 60 % (FR-011) |

Level: Junior < 400, Confirmed 400–800, Strategist 800–1 200, Expert
> 1 200 XP. (Thresholds are published as `>`; boundary values 400, 800 and
1 200 are assigned to the lower level and stated once in `evaluation.qmd`.)

## Source document

| Field | Rule |
|---|---|
| path | Under `fr/teaching/financial-analysis/` |
| status | `used`, `optional` or `archived` (FR-014) |
| used-in | Block id(s) when `used` |

## Change-log entry (FR-007)

block id · previous min · new min · what changed · destination
(`extension` / `homework` / `cut`) · reason.

## Relationships

Course 1—3 Day; Day 1—n Block; Block n—1 Quest (a quest is exactly one
block, a block is at most one quest); Block n—m Reference topic;
Block 1—n Assessment item; Source document n—m Block.

## Invariants

1. Σ block minutes per day = 360; Σ over days = 1 080.
2. Every quest and every reference topic appears in a block or the
   inventory.
3. Σ XP = 1 500 and is consistent with level thresholds.
4. Every page in FR has an EN counterpart at the mirrored path.
