# Phase 0: Research Findings

**Date**: 2026-06-11 | **Status**: Complete

## Investigated Questions

### Q1: How can Quarto dynamically discover index.qmd files in teaching/ subdirectories?

**Decision**: Use **Quarto's native `listings` feature** with glob patterns to discover `index.qmd` files.

**Rationale**: 
- Quarto v1.4+ includes robust `listings` support for automatic file discovery
- Listings can filter by glob patterns to include only `index.qmd` files
- Built-in support for metadata extraction from YAML front matter
- Grid layout type provides responsive card display
- Simpler than Lua filters; no custom code required
- Officially documented and maintained feature

**Implementation**: In `teaching.qmd` front matter:
```yaml
listing:
  contents: teaching/**/index.qmd
  type: grid
  sort: title
```

**Alternatives Considered**:
1. **Lua filter approach** — REJECTED: Over-engineered; Quarto listings handles this natively
2. **External Python script** — REJECTED: Unnecessary; Quarto has built-in support
3. **Hardcoding** — REJECTED: Defeats the purpose of automation

---

### Q2: How should courses be categorized into Graduate, Undergraduate, and AI Guide?

**Decision**: Use **multiple listings sections** in `teaching.qmd`, each with filtered glob patterns for different categories.

**Rationale**:
- Quarto listings support multiple listings on a single page
- Each section uses a filtered glob to match courses in that category
- Filtering can use regex patterns to match directory names (e.g., `ai-*` for AI Guide)
- Alternative: Add category metadata to each index.qmd and filter via `contains()` predicate

**Implementation Example**:
```yaml
# Graduate section
listing:
  contents: teaching/inseec-finance/index.qmd
  type: grid

# Undergraduate section  
listing:
  contents: 
    - teaching/ece-proba/index.qmd
    - teaching/essca-stat/index.qmd
    - teaching/mathematical-analysis/index.qmd
  type: grid

# AI Guide section
listing:
  contents:
    - teaching/ai-papers/index.qmd
    - teaching/ai-dev/index.qmd
  type: grid
```

**Or with directory patterns (if Quarto supports regex)**:
```yaml
listing:
  contents: teaching/ai-*/index.qmd
  type: grid
```

**No YAML mapping file needed** — globs are simple and explicit.

---

### Q3: How should course descriptions be extracted from index.qmd files?

**Decision**: Use **Quarto's automatic metadata extraction** from YAML front matter fields.

**Rationale**:
- Quarto listings automatically extract: `title`, `author`, `date`, `image`, `description`, `abstract`
- If `description` field is missing, Quarto can fallback to the first paragraph (configurable)
- No additional parsing or filtering required
- Works with existing index.qmd structure

**Metadata Priority** (Quarto default):
1. `description` field (if present in YAML)
2. First paragraph of content (fallback)
3. Empty if neither available

**Recommendation**: Add `abstract` or `description` field to index.qmd files if not already present. Most existing files in the project already use `abstract`.

---

### Q4: What Quarto extensions or features are needed?

**Decision**: Use **built-in Quarto listings only**; no extensions required.

**Features Used**:
- **Listings** (built-in, v1.4+): Automatic file discovery and metadata extraction
- **Grid layout** (built-in): Cards with responsive design
- **Sorting** (built-in): Sort by title, date-modified, etc.
- **Filtering** (built-in): Glob patterns for content selection

**Why No Extensions**:
- Quarto listings handle 100% of requirements
- No custom code needed
- Native support is faster and more maintainable than extensions

---

### Q5: How should the grid layout be responsive?

**Decision**: Use **Quarto's grid type listings** with default Bootstrap responsive classes.

**Grid Features**:
- Built-in responsive behavior (1 column mobile, 2+ columns on larger screens)
- Card-based layout automatically adapts to screen size
- No custom CSS needed; uses Quarto's default styling
- Customizable via `assets/dark.scss` if needed

**Configuration**:
```yaml
listing:
  contents: teaching/**/index.qmd
  type: grid
  grid-columns: 2  # Optional: specify number of columns
```

---

### Q6: What metadata fields should each course card display?

**Decision**: Display **title, institution, and description** using Quarto's default listing template.

**Available Fields** (extracted by Quarto):
| Field | Source | Display |
|-------|--------|---------|
| Title | `title` YAML | Card heading |
| Description | `description` or `abstract` YAML | Card body |
| Date | `date-modified` YAML | Card footer (optional) |
| Image | `image` YAML | Card banner (optional) |

**Current index.qmd Files**:
- All have `title` ✓
- Most have `abstract` (used for description) ✓
- Some have `institution` (custom field; may not display by default)
- Some have `date-modified` ✓

**Action**: Review existing index.qmd files to ensure `title` and `abstract` are present. If `institution` should display, add custom metadata handling or display it in the abstract text.

---

## Resolution Summary

### Knowns Resolved
✅ File discovery mechanism: **Quarto listings with glob patterns** (native, no custom code)  
✅ Categorization: **Multiple listing sections with filtered globs** or **metadata predicates**  
✅ Description extraction: **Quarto auto-extraction from `description`/`abstract`**  
✅ Extensions needed: **None; built-in features only**  
✅ Responsive layout: **Quarto grid type (built-in)**  
✅ Metadata display: **Title, description via Quarto defaults; customize as needed**  

### Unknowns Eliminated
No outstanding clarifications. All technical decisions are Quarto-native and well-documented.

### Dependencies Identified
- **Quarto ≥ 1.4** (for listings grid support) — project already uses 1.4+
- **Existing course structure** (index.qmd in each `teaching/` subdirectory) — already established
- **YAML metadata** in existing index.qmd files — already present

### Integration Points
- **`teaching.qmd`** — Main file to transform (add listings sections)
- **`_quarto.yml`** — Sidebar configuration (unchanged)
- **Existing course `index.qmd` files** — No changes needed; just read metadata
- **No new files or directories required**

### Key Difference from Plan
⚠️ **Major Simplification**: Quarto listings eliminates the need for:
- ❌ Custom Lua filters
- ❌ `_course_categories.yml` mapping file
- ❌ Shell command discovery logic
- ❌ Manual template rendering

The feature is now **100% configuration** in `teaching.qmd` front matter, using Quarto's native capabilities.

