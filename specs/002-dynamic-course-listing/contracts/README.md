# Interface Contracts

## Overview

This feature is a **purely internal transformation** of the teaching page — it has no external interfaces or contracts. The feature:

- ✅ Consumes internal data (course metadata from `teaching/` subdirectories)
- ✅ Produces static HTML output (rendered by Quarto, no APIs)
- ✅ Has no external integrations (no database, API calls, or services)
- ✅ Is transparent to users (same page URL, same navigation)

## Data Flow (Internal Only)

```
teaching/ directory (source)
  ↓
Lua filter (discovery + metadata extraction)
  ↓
teaching.qmd (template rendering)
  ↓
Quarto render → docs/teaching.html (output)
```

All interfaces are **file-based** and **internal to the build process**.

---

## Category Mapping Contract (Internal)

**File**: `teaching/_course_categories.yml`

**Format**: YAML key-value mapping

**Consumer**: Lua filter (`_extensions/teaching-listing/listing.lua`)

**Contract**:
```yaml
graduate: [string]        # Array of course slugs
undergraduate: [string]   # Array of course slugs
ai_guide: [string]        # Array of course slugs
heuristics: [object]      # Optional: pattern-based fallback rules
```

This is **not a public contract** — it's an internal data structure consumed by the render process.

---

## Course Metadata Contract (Internal)

**Source**: `teaching/{slug}/index.qmd` YAML front matter

**Consumer**: Lua filter

**Contract**:
```yaml
title: string             # Required: Course name
institution?: string      # Optional: School/organization
abstract?: string         # Optional: Course description
date-modified?: ISO8601   # Optional: Last update date
lang?: string             # Optional: Language code (e.g., "en")
```

This is **not a public contract** — it's the existing metadata structure of course pages, already defined by `_quarto.yml` sidebar configuration.

---

## Conclusion

No public-facing contracts are introduced by this feature. All interfaces remain internal to the build and rendering process. The output is static HTML identical in structure to the current teaching page.
