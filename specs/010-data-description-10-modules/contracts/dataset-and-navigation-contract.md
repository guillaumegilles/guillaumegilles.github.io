# Contract: Dataset files and course navigation

## 1. Dataset files (`teaching/data-description/data/`)

### `wandering-fork.csv`

- UTF-8, comma-separated, header row, `.` as decimal separator, ISO
  dates, LF line endings.
- 240 data rows; column order and names exactly as in
  `data-model.md` §2.
- Original-column values for Harbour days 1–30 identical to
  `specs/005-data-description-course/wandering-fork-dataset.csv`.

### `wandering-fork.xlsx`

| Sheet | Content |
|---|---|
| `data` | The full table as an Excel Table named `tblFork` |
| `harbour_30d` | The 30-day hand-computation subset, Harbour |
| `campus_30d` | The 30-day subset, Campus |
| `dictionary` | One row per column: name, type, unit, meaning |

### Other files

`payroll-skew.csv` (10–20 rows) and `lakeside-bakery.csv` (120 rows),
same CSV rules, each with its own dictionary on `dataset.qmd`.

### Guarantees

1. All invariants in `data-model.md` §2 hold.
2. Every number quoted in a module can be recomputed from these files
   using the Excel steps on that page.
3. The files contain only invented data (FR-027).
4. Column names are English and locale-independent; formulas use
   English-locale function names, with the EN/FR list linked.

### Change rule

Changing any value in `wandering-fork.csv` invalidates quoted figures.
Any change MUST be followed by re-running the generator's recompute step
and updating every affected module in the same commit.

## 2. Sidebar (`_quarto.yml`, id `data-description`)

Exactly these entries, in this order (Constitution II, FR-036):

```yaml
- id: data-description
  title: "Data Description"
  contents:
    - teaching/data-description/index.qmd
    - section: "**Part I — Organising data**"
      contents:
        - teaching/data-description/modules/module-01.qmd
        - teaching/data-description/modules/module-02.qmd
        - teaching/data-description/modules/module-03.qmd
    - section: "**Part II — Summarising one variable**"
      contents:
        - teaching/data-description/modules/module-04.qmd
        - teaching/data-description/modules/module-05.qmd
        - teaching/data-description/modules/module-06.qmd
        - teaching/data-description/modules/module-07.qmd
    - section: "**Part III — Two variables and synthesis**"
      contents:
        - teaching/data-description/modules/module-08.qmd
        - teaching/data-description/modules/module-09.qmd
        - teaching/data-description/modules/module-10.qmd
    - section: "**Reference**"
      contents:
        - teaching/data-description/modules/dataset.qmd
        - teaching/data-description/modules/glossary.qmd
        - teaching/data-description/modules/excel-functions.qmd
```

Reachability rule (SC-010): any module, the dataset page, the glossary
and the function page are reachable from the syllabus in ≤ 2 clicks.

## 3. Draft and publish

- `modules/_metadata.yml` contains `draft: true` while the course is
  unfinished (drafts render blank and leave navigation, search and the
  sitemap).
- Publishing = remove that line **and** rewrite `index.qmd` in the same
  change.
- `index.qmd` MUST NOT be marked draft at any point.

## 4. Syllabus (`index.qmd`) required parts

Course description · curriculum placement (follows MS01, MS02; precedes
MS04) · learning objectives · module outline table linking M1–M10 with
hours · assessment table (midterm 35%/45 min covers M1–M5; final
65%/90 min covers M1–M10) · personal work (20 h) · conventions table
(quartiles `EXC`, sample `.S`) · **Recommended Literature** including
OpenStax IBS 2e and Khan Academy Statistics and Probability, each with
author/provider, title, edition and publisher/source (Constitution
T-VIII, FR-034).
