# Data Model: Mathematical Fundamentals RevealJS Slide Decks

**Branch**: `007-math-fundamentals-slides` | **Date**: 2026-09-15
**Spec**: [spec.md](spec.md) | **Research**: [research.md](research.md)

This document describes the content model for each artifact created by this
feature. "Data model" here means the schema for slide deck files and their
sidebar registrations, not a database schema.

---

## Entity 1: English Slide Deck File

**File path**: `teaching/mathematical-fundamentals/module-N-slides.qmd`
**Count**: 8 files (one per module)

### Front Matter Schema

```yaml
---
title: "[EMOJI] [Module Title] — Slides"
subtitle: "Mathematical Fundamentals · MS01-001-G"
lang: en
format:
  revealjs:
    theme: assets/dark-slides.scss
    slide-number: true
    progress: true
    controls: true
    transition: slide
    fig-align: center
---
```

**Field rules**:
- `title`: Must match the reference page title (e.g., `"1️⃣ Essential Mathematical
  Calculations for Economics and Management — Slides"`).
- `subtitle`: Constant across all decks; anchors the presentation in the course context.
- `lang: en`: Required by Constitution VI.
- `format: revealjs`: Overrides the global `format: html` for this file only.
- `theme: assets/dark-slides.scss`: Points to the RevealJS-specific SCSS file.
- `slide-number: true`, `progress: true`, `controls: true`: Standard presenter
  controls; aids navigation during lecture.
- `transition: slide`: Clean directional transition between slides.

### Required Slide Sections (in order)

| Section | Slide Type | Content |
|---|---|---|
| Title slide | Auto-generated from `title` + `subtitle` | — |
| Learning Objectives | Bullet list | Verbatim from reference page `callout-note` |
| Concept slide(s) | `## Concept Name` level-2 heading | Key rule/formula + 1-sentence explanation |
| Worked Example | `## Worked Example` | Step-by-step, may span 2–3 slides |
| Summary | `## Summary` | 2–3 key takeaways (numbered list) |
| Reference | `## 📖 Full Reference` | Link to `module-N.qmd` with call-to-action |

**Slide heading convention**:
- Level-2 headings (`##`) create new slides.
- Level-3 headings (`###`) create sub-slides (vertical navigation) — use
  sparingly; prefer flat horizontal structure for lecture use.

**Formula blocks**: Use `$$...$$` for displayed equations on their own slide
or `$...$` for inline math within a bullet point. Do not use HTML entities.

**Key Concept callout pattern** (replaces `.callout-tip` from reference page):
```markdown
::: {.callout-tip}
#### Key Rule
$$\text{formula here}$$
Plain-language explanation of what this computes.
:::
```

**Common Error pattern** (where reference page highlights one):
```markdown
::: {.callout-warning}
**Common mistake**: [brief description]
:::
```

### Module-Specific Concept Counts

| Module | Title | Core Concept Slides |
|---|---|---|
| 1 | Essential Mathematical Calculations | 7 (one per concept: order of ops, absolute value, powers, square root, fractions, percentages, proportionality) |
| 2 | Mastering Equations | 4 (expanding, factoring, notable identities, first-degree equations) |
| 3 | Curve Analysis | 4 (graph reading, equation of a line, systems, inequalities) |
| 4 | Financial-Mathematics Tools | 3 (sequences, arithmetic sequences, geometric sequences) |
| 5 | Application of Financial Mathematics | 2 (simple interest, compound interest) |
| 6 | Functions in Economics | 3 (function concept/domain, usual functions, second-degree equations) |
| 7 | Introduction to Optimization | 3 (average rate of change, instantaneous rate/derivative, applications) |
| 8 | Revision and Exam Preparation | 7 recap slides (one per prior module) + method-identification slide + exam strategy slide |

**Minimum total slides per deck** (title + objectives + concepts + example +
summary + reference): typically 10–15 slides per module.

---

## Entity 2: RevealJS Theme File

**File path**: `assets/dark-slides.scss`
**Count**: 1 file (shared by all 8 slide decks)

### SCSS Schema

```scss
/*-- scss:defaults --*/
// Colour palette aligned with the site's dark/blackboard theme
$backgroundColor: #1a1a2e;   // Deep dark background
$mainColor: #d4cfc6;          // Warm off-white body text
$headingColor: #eae6dc;       // Bright chalk-white headings
$linkColor: #5bdb6d;          // Accent green (matches site)
$selectionBackgroundColor: #3d7a4a;
$mainFontSize: 1.8rem;
$mainFont: "Source Sans Pro", sans-serif;
$headingFont: "Source Sans Pro", sans-serif;
$headingTextTransform: none;

/*-- scss:rules --*/
.reveal pre code {
  background: #0d1610;
  color: #a8d8a0;
}
.reveal .callout-tip {
  border-left-color: $linkColor;
}
.reveal .callout-warning {
  border-left-color: #f0a500;
}
```

**Rule**: This file MUST NOT import or extend `assets/dark.scss` (Bootstrap
variables are incompatible with RevealJS SCSS context).

---

## Entity 3: French Stub Slide Deck File

**File path**: `fr/teaching/mathematical-fundamentals/module-N-slides.qmd`
**Count**: 8 files (one per module)

### Front Matter Schema

```yaml
---
title: "[EMOJI] [French Module Title] — Diapositives"
lang: fr
format:
  revealjs:
    theme: assets/dark-slides.scss
    slide-number: true
---
```

### Required Content (minimal stub)

```markdown
## 🚧 Traduction en cours

::: {.callout-note}
Ce support de cours est en cours de traduction.

Consultez la [version anglaise](../../teaching/mathematical-fundamentals/module-N-slides.qmd)
en attendant.
:::
```

**Field rules**:
- `lang: fr`: Required by Constitution VI.
- `title`: French translation of the module title with `— Diapositives` suffix.
- Link in stub body must point to the English counterpart via a relative path.
- Stub renders as a valid RevealJS deck with two slides (title + stub slide).

### French Module Title Mapping

| Module | French Title |
|---|---|
| 1 | Calculs Mathématiques Essentiels |
| 2 | Maîtriser les Équations |
| 3 | Analyse des Courbes |
| 4 | Outils de Mathématiques Financières |
| 5 | Application des Mathématiques Financières |
| 6 | Fonctions Utiles en Économie et Gestion |
| 7 | Introduction à l'Optimisation |
| 8 | Révision et Préparation à l'Examen |

---

## Entity 4: Sidebar Registration in `_quarto.yml`

**File path**: `_quarto.yml`
**Change**: Add a `"**Slides**"` section to the `mathematical-fundamentals`
sidebar, after the existing module list and before the `**Resources**` section.

### Schema (YAML fragment)

```yaml
- section: "**Slides**"
  contents:
    - text: "Module 1 — Slides"
      href: teaching/mathematical-fundamentals/module-1-slides.qmd
    - text: "Module 2 — Slides"
      href: teaching/mathematical-fundamentals/module-2-slides.qmd
    - text: "Module 3 — Slides"
      href: teaching/mathematical-fundamentals/module-3-slides.qmd
    - text: "Module 4 — Slides"
      href: teaching/mathematical-fundamentals/module-4-slides.qmd
    - text: "Module 5 — Slides"
      href: teaching/mathematical-fundamentals/module-5-slides.qmd
    - text: "Module 6 — Slides"
      href: teaching/mathematical-fundamentals/module-6-slides.qmd
    - text: "Module 7 — Slides"
      href: teaching/mathematical-fundamentals/module-7-slides.qmd
    - text: "Module 8 — Slides"
      href: teaching/mathematical-fundamentals/module-8-slides.qmd
```

**Rule**: Each `href` uses the `.qmd` source path (not `.html`). Quarto
resolves the output path automatically.

---

## Entity 5: "Slides" Link on Each Reference Module Page

**File paths**: `teaching/mathematical-fundamentals/module-N.qmd` (8 files,
minor additive edit to each)

**Change**: Add a single link at the top of each reference module page (after
the opening callout, before the Diagnostic Activity section) pointing to the
slide deck:

```markdown
> 📊 **Lecture slides**: [View the slides for this module](module-N-slides.qmd)
```

This link is a navigational convenience only; it does not change the
reference page's content or structure.

---

## Relationships

```
module-N.qmd (reference page)
    │
    ├──links to──► module-N-slides.qmd (EN slides)
    │                   │
    │                   └──links back to──► module-N.qmd
    │
    └── sidebar entry in _quarto.yml
            │
            └── also links to──► module-N-slides.qmd

fr/…/module-N-slides.qmd (FR stub)
    └──links to──► module-N-slides.qmd (EN slides)
```
