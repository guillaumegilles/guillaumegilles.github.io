# Contract: Course Pages and Timetable Format

The course exposes no API. Its interfaces are the pages students and
instructors read and the timetable table that validation reads. This
contract fixes both.

## 1. Page set (FR = `fr/teaching/financial-analysis/`, EN = `teaching/financial-analysis/`)

| Page | FR | EN | Audience |
|---|---|---|---|
| `index.qmd` (home, syllabus, per-day summary) | full | **full** | students |
| `planning.qmd` (full timetable, printable) | full | **full** | both |
| `evaluation.qmd` | full | stub | students |
| `glossaire.qmd` | full | stub | students |
| `modules/01…09-*.qmd` (quests) | full | stub | students |
| `modules/{banque-france,banque-france-cotation,performances,structure-fi,liquidite,formules}.qmd` | full | stub | students |
| `exercices/examen-1h.qmd`, `examen-final.qmd` | full | stub | both |
| `enseignant/jour-{1,2,3}.qmd` | full | stub | instructor |
| `annexes/inventaire-sources.qmd` | full | stub | instructor |

Stub body (EN): title, one line "Translation in progress", link to the
French page. Language comes from the directory `_metadata.yml`; pages do
not set `lang:`.

## 2. Timetable table format (`planning.qmd`, both languages)

One table per day, with exactly these columns, so a script can sum them:

```markdown
| Block | Start (min) | Duration (min) | Goal | Sources | Cut first |
|-------|------------:|---------------:|------|---------|-----------|
| D1-B1 | 0 | 15 | … | … | … |
```

Rules:

- `Block` matches `D[1-3]-B[1-9]`.
- `Start` is the previous start plus the previous duration (starts at 0).
- `Duration` is an integer; the column sums to 360 per table.
- Breaks appear in a separate "Breaks" list under the table, never as rows.
- The EN and FR tables have identical Block, Start and Duration values.

## 3. Quest page minimum content

Each quest page, in order: objectives; prerequisites and pre-reading (plain
list); live theory outline (with minutes); worked example; derivation in a
`.callout-caution`; exercise(s) as `::: {#exr-<slug> name="…"}` with
folded `<details class="answer">`; deliverables and grading criteria; XP;
cut-first note; demo or `TODO:` `.callout-important`.

## 4. Navigation

`_quarto.yml` contains one EN and one FR sidebar for the course. Order:
index, planning, evaluation, Day 1/2/3 groups (their quests), reference
group (reference topics, formules), glossaire, exams, instructor group.
`index.qmd` is the first entry (T-VIII). No page exists outside a sidebar.

## 5. Stability

Existing paths under `modules/` and `exercices/` keep their names (FR-019).
New paths listed in section 1 are the only additions.
