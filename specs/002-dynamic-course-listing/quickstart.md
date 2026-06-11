# Phase 1: Quickstart Guide

**Date**: 2026-06-11 | **Status**: Complete | **Using Quarto Listings**

## Implementation Overview

This implementation uses Quarto's native **listings** feature — no custom Lua filters, no external mapping files. Just YAML configuration in `teaching.qmd`.

---

## Step 1: Update teaching.qmd Front Matter

Add `listing` configuration to the YAML front matter:

```yaml
---
title: "Teaching"
description: |
  Course materials for statistics, financial analysis, and more.
listing:
  - id: graduate-courses
    contents: teaching/inseec-finance/index.qmd
    type: grid
    sort: title
  - id: undergrad-courses
    contents:
      - teaching/ece-proba/index.qmd
      - teaching/essca-stat/index.qmd
      - teaching/mathematical-analysis/index.qmd
    type: grid
    sort: title
  - id: ai-guide-courses
    contents:
      - teaching/ai-papers/index.qmd
      - teaching/ai-dev/index.qmd
    type: grid
    sort: title
---
```

### Field Definitions
- `id`: Unique identifier for listing (used in placeholder div)
- `contents`: Files to include (glob patterns or list of files)
- `type`: Layout (`grid` for cards, `default` for blog-style, `table` for tabular)
- `sort`: Sort field (default: `title`)

---

## Step 2: Replace Hardcoded Grids with Listing Placeholders

Replace all manual grid HTML with simple placeholder divs:

**Old (hardcoded)**:
```markdown
## Graduate

:::::: {.grid}
::: {.g-col-6}
### Financial Analysis
**INSEEC · MSc**
[Open course →](teaching/inseec-finance/index.qmd){.btn .btn-outline-primary .btn-sm}
:::
::::::
```

**New (dynamic)**:
```markdown
## Graduate

:::{#graduate-courses}
:::

## Undergraduate

:::{#undergrad-courses}
:::

## AI Guide

:::{#ai-guide-courses}
:::
```

---

## Step 3: Test

```bash
quarto preview teaching.qmd
```

Verify:
- ✅ All 6 courses appear in correct sections
- ✅ Grid layout is responsive
- ✅ Course links work
- ✅ Page loads fast

---

## Implementation Checklist

- [ ] Update `teaching.qmd` front matter with listing configuration
- [ ] Replace hardcoded grid sections with placeholders
- [ ] Run `quarto preview teaching.qmd` and verify all courses appear
- [ ] Test responsive layout on mobile/tablet/desktop
- [ ] Full render: `quarto render`
- [ ] Commit changes

---

## Complete Updated teaching.qmd

```markdown
---
title: "Teaching"
description: |
  Course materials for statistics, financial analysis, and more.
listing:
  - id: graduate-courses
    contents: teaching/inseec-finance/index.qmd
    type: grid
    sort: title
  - id: undergrad-courses
    contents:
      - teaching/ece-proba/index.qmd
      - teaching/essca-stat/index.qmd
      - teaching/mathematical-analysis/index.qmd
    type: grid
    sort: title
  - id: ai-guide-courses
    contents:
      - teaching/ai-papers/index.qmd
      - teaching/ai-dev/index.qmd
    type: grid
    sort: title
---

I teach at **ESSCA** (statistics & information systems) and **INSEEC** (financial
analysis, graduate level). Course materials live here and are updated each semester.

### Annotating Course Pages

All course pages support **collaborative annotation** via [Hypothesis](https://web.hypothes.is/).

[Rest of content unchanged...]

## Graduate

:::{#graduate-courses}
:::

## Undergraduate

:::{#undergrad-courses}
:::

## AI Guide

:::{#ai-guide-courses}
:::
```

---

## Key Advantages

✅ **Zero custom code** — Just YAML configuration  
✅ **Native Quarto** — v1.4+ built-in feature  
✅ **Automatic metadata extraction** — No manual mapping  
✅ **Responsive grid** — Built-in responsive design  
✅ **Maintainable** — Easy to add/remove courses  

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Courses not appearing | File path incorrect or listing `id` ≠ placeholder `id` | Check glob paths exist, verify `id` matches |
| Grid layout broken | CSS cache issue | Hard refresh browser (Ctrl+Shift+R) |
| Empty descriptions | `abstract` field missing from index.qmd | Add `abstract: "..."` to YAML front matter |

