# Contract: Slide Deck File Format

**Feature**: 007-math-fundamentals-slides
**Date**: 2026-09-15

This contract specifies the required structure and front matter for every
RevealJS slide deck file created by this feature. Any file that does not
conform to this contract is considered malformed.

---

## English Slide Deck Contract

### File Location

```
teaching/mathematical-fundamentals/module-{N}-slides.qmd
```

where `{N}` is the module number (1–8).

### Front Matter

```yaml
---
title: "{EMOJI} {Module Title} — Slides"
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

**Required fields**: `title`, `lang`, `format.revealjs.theme`.
**Prohibited**: `format: html` (the global default is overridden by
`format: revealjs`). No inline `style=` attributes. No `<style>` blocks.

### Required Slide Structure

Slides MUST appear in this order. Each `##` heading creates a new slide.

```markdown
## Learning Objectives
[bullet list, verbatim from reference page]

## {Concept 1 Name}
[Key rule/formula in a .callout-tip block + 1-sentence explanation]

## {Concept 2 Name}
...repeat for each concept...

## Worked Example
[Worked example from reference page, condensed to key steps]

## Summary
[Numbered list, 2–3 key takeaways]

## 📖 Full Reference
[Link to module-N.qmd with text "See the complete module for theory,
exercises, and interactive simulations."]
```

### Formula Rule

- Displayed equations: `$$...$$`
- Inline equations: `$...$`
- No HTML math entities (e.g., no `&times;`)

### Prohibited Content

- `{ojs}` code blocks
- `{shinylive-python}` code blocks
- `{python}` / `{r}` code blocks
- Inline `style=` attributes
- `<style>` blocks

### Callout Convention (inherited from Constitution V)

| Callout type | Slide use |
|---|---|
| `.callout-tip` | Key formula or rule |
| `.callout-warning` | Common mistake or caveat |
| `.callout-note` | Definition or contextual note |

---

## French Stub Slide Deck Contract

### File Location

```
fr/teaching/mathematical-fundamentals/module-{N}-slides.qmd
```

### Front Matter

```yaml
---
title: "{EMOJI} {French Module Title} — Diapositives"
lang: fr
format:
  revealjs:
    theme: assets/dark-slides.scss
    slide-number: true
---
```

**Required fields**: `title`, `lang: fr`, `format.revealjs.theme`.

### Required Content

```markdown
## 🚧 Traduction en cours

::: {.callout-note}
Ce support de cours est en cours de traduction.

Consultez la [version anglaise](../../teaching/mathematical-fundamentals/module-{N}-slides.qmd)
en attendant.
:::
```

The relative link path from `fr/teaching/mathematical-fundamentals/` back to
`teaching/mathematical-fundamentals/` is `../../teaching/mathematical-fundamentals/`.

---

## RevealJS Theme File Contract

### File Location

```
assets/dark-slides.scss
```

### Required Structure

```scss
/*-- scss:defaults --*/
// RevealJS SCSS variables only — NO Bootstrap variables or @import of dark.scss

/*-- scss:rules --*/
// Optional custom CSS rules for .reveal elements
```

**Prohibited**: `@import "dark.scss"` or any Bootstrap variable reference.
**Required**: File must exist before any slide deck can render with
`theme: assets/dark-slides.scss`.

---

## Validation

A slide deck file passes contract validation when:

1. `quarto render teaching/mathematical-fundamentals/module-{N}-slides.qmd`
   exits with code 0.
2. The output HTML at
   `docs/teaching/mathematical-fundamentals/module-{N}-slides.html` exists.
3. Opening the HTML in a browser shows a RevealJS presentation (not a
   standard HTML page with navbar/sidebar).
4. All required slide sections are present in the rendered output.
5. At least one `$$...$$` formula is visible in the concept slides.
6. The "📖 Full Reference" slide contains a working link to `module-{N}.html`.
