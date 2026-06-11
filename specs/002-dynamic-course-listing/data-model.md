# Phase 1: Data Model

**Date**: 2026-06-11 | **Status**: Complete | **Using Quarto Listings**

## Data Structures

### Course Entity (via Quarto Listings)

Quarto listings automatically extract metadata from YAML front matter in `index.qmd` files and render them as cards. Each course is defined by:

1. **Directory** (`teaching/{course-slug}/`)
2. **Landing Page** (`index.qmd` in the directory)
3. **YAML Metadata** (extracted automatically by Quarto)

```yaml
# Course Object (as discovered and rendered by Quarto listings)
Course:
  title: string                 # From YAML 'title' field (required)
  description: string           # From YAML 'description' or 'abstract' field
  image: string | null          # From YAML 'image' field (optional; card banner)
  date-modified: ISO8601 | null # From YAML 'date-modified' field (optional)
  link: string                  # Auto-generated: teaching/{slug}/index.qmd
```

---

## Metadata Schema

### Course Index Front Matter (index.qmd)

**Required Fields**:
```yaml
---
title: "Course Title"
---
```

**Recommended Fields** (for rich listings display):
```yaml
---
title: "Course Title"
abstract: "Brief description of the course"  # or 'description'
date-modified: 2026-05-19
---
```

**Optional Fields**:
```yaml
---
image: "course-banner.png"  # Card header image
lang: en
---
```

---

## Content Model for teaching.qmd

### Page Structure (Simplified with Quarto Listings)

After transformation:

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

[Introduction text + annotation info — unchanged from current]

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

## Validation Rules

### Discovery Rules
- ✅ Directory must exist at `teaching/{slug}/`
- ✅ File `teaching/{slug}/index.qmd` must exist (matching glob pattern)
- ✅ Must contain valid YAML front matter
- ✅ Must have `title` field (Quarto skips if missing)

### Rendering Rules
- ✅ Grid displays one listing section per category
- ✅ Empty listings are hidden by default
- ✅ Course cards are responsive
- ✅ Links are auto-generated

---

## Scalability

### Current Scale
- 6 courses across 3 categories
- Static configuration in `teaching.qmd`

### Future Enhancement
- Add new course glob patterns as needed
- Quarto listings scales to 50+ courses naturally
