# Data Model: Mathematical Fundamentals — French Version

**Feature**: 008-math-fundamentals-french
**Date**: 2026-09-17

---

## Entities

### E-001: French Course Page (reference module)

**Files**: `fr/teaching/mathematical-fundamentals/module-1.qmd` … `module-8.qmd` (8 files)

**Required front matter fields**:

| Field | Type | Constraint |
|---|---|---|
| `title` | string | French translation of EN title |
| `abstract` | string | French translation of EN abstract |
| `lang` | string | Must equal `"fr"` (may be inherited from `_metadata.yml`) |
| `date-modified` | ISO date | Updated whenever content changes |

**Prohibited front matter**:
- `format: revealjs` — reference pages render as HTML; slides are a separate entity (E-002)

**Required sections (in order)**:

1. Learning Objectives callout (`.callout-note`)
2. Diagnostic Activity
3. Opening Problem
4. Core Concepts
5. Worked Example
6. Guided Practice — collapsible solution (`.callout-caution collapse="true"`)
7. Interactive Simulation (OJS or Shinylive)
8. Applied Problem
9. Common Errors (`.callout-warning`)

**Callout semantics**:

| Callout type | Usage |
|---|---|
| `.callout-note` | Definitions and learning objectives |
| `.callout-tip` | Key formulas |
| `.callout-warning` | Caveats and common errors |
| `.callout-caution collapse="true"` | Exercise solutions and proofs |

**Formula constraint**: LaTeX must be byte-identical to the English source. Use `$…$` for inline math and `$$…$$` for display math. No reformatting, no simplification.

**Required cross-link**: Each module page must include a visible link to its French slide deck counterpart (`module-N-slides.qmd` in the same directory).

**Relationship**: One-to-one with `teaching/mathematical-fundamentals/module-N.qmd`.

---

### E-002: French Slide Deck

**Files**: `fr/teaching/mathematical-fundamentals/module-1-slides.qmd` … `module-8-slides.qmd` (8 files)

**Required front matter fields**:

| Field | Value / Constraint |
|---|---|
| `title` | French translation of EN slide deck title |
| `subtitle` | `"Fondements Mathématiques · MS01-001-G"` (verbatim) |
| `lang` | `"fr"` |
| `format: revealjs` | Required block — see sub-fields below |
| `format.revealjs.theme` | `"../../../assets/dark-slides.scss"` (3 levels up, not 2) |
| `format.revealjs.slide-number` | `true` |
| `format.revealjs.progress` | `true` |
| `format.revealjs.controls` | `true` |
| `format.revealjs.transition` | `"slide"` |
| `format.revealjs.fig-align` | `"center"` |

**Required slide sequence**:

1. Title slide
2. Learning objectives
3. One slide per core concept (count matches EN source)
4. Worked example
5. Summary
6. Closing slide — links to French reference module (`module-N.qmd`, same directory)

**Formula constraint**: LaTeX byte-identical to EN source (same rule as E-001).

**Interactive block constraint**: No OJS or Shinylive blocks. Replace with a static equivalent or a "see reference page" note.

**Closing slide**: Must include an explicit link to `module-N.qmd` (French reference module in the same directory).

**Relationship**: One-to-one with `teaching/mathematical-fundamentals/module-N-slides.qmd`.

---

### E-003: French Resource Pages

**Files**: 3 files in `fr/teaching/mathematical-fundamentals/`

#### E-003a — `glossary.qmd`

| Field | Value |
|---|---|
| `title` | `"Glossaire"` |
| `lang` | `"fr"` |

- One entry per symbol/term; entry count must be ≥ English glossary entry count (VR-006).
- Each entry includes: notation, French definition, pronunciation guide for Greek letters.

#### E-003b — `formula-sheet.qmd`

| Field | Value |
|---|---|
| `title` | `"Aide-mémoire"` |
| `lang` | `"fr"` |
| `toc` | `true` |
| `toc-depth` | `2` |

- One section per module (8 sections total).
- All formulas verbatim from English source.
- Section headings and annotations translated into French.

#### E-003c — `learning-guide.qmd`

| Field | Value |
|---|---|
| `title` | `"Guide d'apprentissage"` |
| `lang` | `"fr"` |
| `toc` | `true` |
| `toc-depth` | `2` |

- All prose translated into French.
- Structural headings identical to English source (same hierarchy, translated text).

---

### E-004: French Course Syllabus

**File**: `fr/teaching/mathematical-fundamentals/index.qmd`

**Required front matter fields**:

| Field | Value / Constraint |
|---|---|
| `title` | `"Fondements Mathématiques et Analyse de Données"` (verbatim) |
| `subtitle` | `"MS01-001-G"` |
| `description` | French prose description |
| `date-modified` | ISO date |
| `image` | `"../../teaching/mathematical-fundamentals/image.jpg"` (reuses EN asset) |
| `lang` | `"fr"` |

**Required sections (in order)**:

1. Welcome callout (French text, `.callout-note`)
2. Start Here — numbered list
3. How to Study Each Module — tip callout (`.callout-tip`)
4. Course Information
5. General Presentation
6. Targeted Competencies
7. Organisation & Schedule — links to each FR module page
8. Glossary link
9. Learning Progress checklist
10. Assessment table
11. Expected Personal Work
12. Recommended Literature — must list all 3 references with author, title, edition, and publisher (T-VIII compliance)

**Relationship**: One-to-one with `teaching/mathematical-fundamentals/index.qmd`.

---

### E-005: Language Switcher Include

**File**: `fr/teaching/mathematical-fundamentals/_lang-switch.qmd`
(shared via `include-before-body` in `_metadata.yml` for both EN and FR teaching directories)

**Content**: A single OJS block implementing the following logic:

```
read window.location.pathname
if pathname starts with "/fr/"
  → strip "/fr" prefix → link to English counterpart
else
  → prepend "/fr" → link to French counterpart
render as a styled pill/badge link
```

**Displayed text**:
- On FR pages: `"🇬🇧 English version"` (links to EN counterpart)
- On EN pages: `"🇫🇷 Version française"` (links to FR counterpart)

**Styling constraint**: Uses only existing CSS classes from `assets/dark.scss`. No inline styles permitted.

**Inclusion mechanism**: Referenced in `include-before-body` inside `_metadata.yml` for both `teaching/mathematical-fundamentals/` and `fr/teaching/mathematical-fundamentals/`.

**Relationship**: Shared include; not derived from any single EN source file.

---

### E-006: French Sidebar Block (`_quarto.yml` entry)

**Location**: `website.sidebar` array in `_quarto.yml`

**id**: `fr-mathematical-fundamentals`
**title**: `"Fondements Mathématiques"`

**Structure** (mirrors the English `mathematical-fundamentals` block exactly):

```
id: fr-mathematical-fundamentals
title: "Fondements Mathématiques"
contents:
  - fr/teaching/mathematical-fundamentals/index.qmd
  - section: "Module 1 — …"
    contents:
      - fr/teaching/mathematical-fundamentals/module-1.qmd       # Reference
      - fr/teaching/mathematical-fundamentals/module-1-slides.qmd # Slides
  … (sections 2–8, same pattern)
  - section: "Ressources"
    contents:
      - fr/teaching/mathematical-fundamentals/glossary.qmd
      - fr/teaching/mathematical-fundamentals/formula-sheet.qmd
      - fr/teaching/mathematical-fundamentals/learning-guide.qmd
```

**Constraint**: Must list all 20 FR `.qmd` files. No orphaned pages, no missing entries (VR-008).

**Relationship**: Parallel to the existing `mathematical-fundamentals` sidebar block.

---

## Validation Rules

| ID | Rule | How to test |
|---|---|---|
| VR-001 | Every file in `teaching/mathematical-fundamentals/*.qmd` has a counterpart in `fr/teaching/mathematical-fundamentals/` — file counts must match (20 = 20) | `diff <(ls teaching/mathematical-fundamentals/*.qmd \| xargs -n1 basename) <(ls fr/teaching/mathematical-fundamentals/*.qmd \| xargs -n1 basename)` |
| VR-002 | Every FR `.qmd` declares `lang: fr` (directly or via `_metadata.yml`) | Grep front matter; inspect `_metadata.yml` |
| VR-003 | Slide decks declare `format: revealjs` with `theme: ../../../assets/dark-slides.scss` | Grep `module-*-slides.qmd` front matter |
| VR-004 | Reference modules do NOT declare `format: revealjs` | Grep `module-[1-8].qmd` front matter |
| VR-005 | LaTeX formulas in FR files are byte-identical to their EN source counterparts | Diff extracted math blocks between EN and FR pairs |
| VR-006 | French glossary entry count ≥ English glossary entry count | Count heading-level entries in both files |
| VR-007 | `quarto render` exits 0 with both EN and FR in render target | `quarto render && echo OK` |
| VR-008 | The `fr-mathematical-fundamentals` sidebar block in `_quarto.yml` lists all 20 FR pages | Count `fr/teaching/mathematical-fundamentals/` entries under the sidebar id |

---

## File Inventory

### 20 FR `.qmd` files (source → counterpart mapping)

| EN source | FR counterpart |
|---|---|
| `teaching/mathematical-fundamentals/index.qmd` | `fr/teaching/mathematical-fundamentals/index.qmd` |
| `teaching/mathematical-fundamentals/module-1.qmd` | `fr/teaching/mathematical-fundamentals/module-1.qmd` |
| `teaching/mathematical-fundamentals/module-2.qmd` | `fr/teaching/mathematical-fundamentals/module-2.qmd` |
| `teaching/mathematical-fundamentals/module-3.qmd` | `fr/teaching/mathematical-fundamentals/module-3.qmd` |
| `teaching/mathematical-fundamentals/module-4.qmd` | `fr/teaching/mathematical-fundamentals/module-4.qmd` |
| `teaching/mathematical-fundamentals/module-5.qmd` | `fr/teaching/mathematical-fundamentals/module-5.qmd` |
| `teaching/mathematical-fundamentals/module-6.qmd` | `fr/teaching/mathematical-fundamentals/module-6.qmd` |
| `teaching/mathematical-fundamentals/module-7.qmd` | `fr/teaching/mathematical-fundamentals/module-7.qmd` |
| `teaching/mathematical-fundamentals/module-8.qmd` | `fr/teaching/mathematical-fundamentals/module-8.qmd` |
| `teaching/mathematical-fundamentals/module-1-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-1-slides.qmd` |
| `teaching/mathematical-fundamentals/module-2-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-2-slides.qmd` |
| `teaching/mathematical-fundamentals/module-3-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-3-slides.qmd` |
| `teaching/mathematical-fundamentals/module-4-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-4-slides.qmd` |
| `teaching/mathematical-fundamentals/module-5-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-5-slides.qmd` |
| `teaching/mathematical-fundamentals/module-6-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-6-slides.qmd` |
| `teaching/mathematical-fundamentals/module-7-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-7-slides.qmd` |
| `teaching/mathematical-fundamentals/module-8-slides.qmd` | `fr/teaching/mathematical-fundamentals/module-8-slides.qmd` |
| `teaching/mathematical-fundamentals/glossary.qmd` | `fr/teaching/mathematical-fundamentals/glossary.qmd` |
| `teaching/mathematical-fundamentals/formula-sheet.qmd` | `fr/teaching/mathematical-fundamentals/formula-sheet.qmd` |
| `teaching/mathematical-fundamentals/learning-guide.qmd` | `fr/teaching/mathematical-fundamentals/learning-guide.qmd` |

### 2 FR-specific support files (no EN counterpart)

| File | Purpose |
|---|---|
| `fr/teaching/mathematical-fundamentals/_metadata.yml` | Inherits `lang: fr`; sets `include-before-body` for language switcher |
| `fr/teaching/mathematical-fundamentals/_lang-switch.qmd` | OJS language switcher include (E-005) |
