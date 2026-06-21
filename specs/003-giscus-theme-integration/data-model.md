# Data Model: Giscus Retro Blackboard Theme Integration

**Phase 1 output** — Entities, design-token mapping, and state transitions.

---

## Entities

### Entity 1 — DesignToken

A named colour or typography value from `assets/dark.scss` that both the host page
and the giscus theme file must share. Tokens are inlined as hex literals in the CSS
file because SCSS variables are not available in the giscus context.

| Token name (SCSS) | Hex value | Semantic role |
|---|---|---|
| `$board-darkest` | `#0D1610` | Deepest surface (navbar, code block bg, primary-btn text) |
| `$board-dark` | `#152119` | Secondary panel surface |
| `$board` | `#1C2E22` | Main canvas / default background |
| `$board-light` | `#253A2C` | Raised elements, inset surfaces, code blocks |
| `$board-lighter` | `#2F4636` | Borders, dividers, subtle separators |
| `$chalk` | `#D2CCC0` | Primary body text |
| `$chalk-bright` | `#EAE6DC` | Headings, emphasis, button text |
| `$chalk-dim` | `#7E8F82` | Muted / secondary text, placeholders |
| `$phosphor-green` | `#5BDB6D` | Links, primary accent, focus rings, primary-btn bg |
| `$phosphor-green-light` | `#84e391` | Hover state of phosphor-green (≈ lighten 15%) |
| `$phosphor-green-dark` | `#4fc460` | Active/selected state (≈ darken 12%) |
| `$pixel-amber` | `#F5A623` | Warnings, attention |
| `$pixel-cyan` | `#56CCF2` | Info, accent muted |
| `$pixel-red` | `#EB5757` | Danger, errors |
| `$code-color` | `#A8D8A0` | Code / monospace text colour |

> **Note**: `$phosphor-green-light` and `$phosphor-green-dark` are derived
> (lighten/darken) rather than explicit SCSS variables. The CSS literals are
> pre-computed and inlined directly.

---

### Entity 2 — GiscusCSSPropertyMapping

Maps each giscus CSS custom property (set on `main {}`) to a DesignToken value.
This is the core specification document the implementer follows when writing the
CSS file.

#### 2a — Syntax Highlighting (`--color-prettylights-syntax-*`)

These map to the Retro Blackboard terminal-green code palette. The same colour
family used in `dark.scss` for `code.sourceCode span` syntax highlighting.

| Giscus property | Value | Token |
|---|---|---|
| `--color-prettylights-syntax-comment` | `#7E8F82` | `$chalk-dim` |
| `--color-prettylights-syntax-constant` | `#A8D8A0` | `$code-color` |
| `--color-prettylights-syntax-entity` | `#5BDB6D` | `$phosphor-green` |
| `--color-prettylights-syntax-storage-modifier-import` | `#D2CCC0` | `$chalk` |
| `--color-prettylights-syntax-entity-tag` | `#56CCF2` | `$pixel-cyan` |
| `--color-prettylights-syntax-keyword` | `#5BDB6D` | `$phosphor-green` |
| `--color-prettylights-syntax-string` | `#A8D8A0` | `$code-color` |
| `--color-prettylights-syntax-variable` | `#EAE6DC` | `$chalk-bright` |
| `--color-prettylights-syntax-brackethighlighter-unmatched` | `#EB5757` | `$pixel-red` |
| `--color-prettylights-syntax-invalid-illegal-text` | `#0D1610` | `$board-darkest` |
| `--color-prettylights-syntax-invalid-illegal-bg` | `#EB5757` | `$pixel-red` |
| `--color-prettylights-syntax-carriage-return-text` | `#0D1610` | `$board-darkest` |
| `--color-prettylights-syntax-carriage-return-bg` | `#EB5757` | `$pixel-red` |
| `--color-prettylights-syntax-string-regexp` | `#A8D8A0` | `$code-color` |
| `--color-prettylights-syntax-markup-list` | `#D2CCC0` | `$chalk` |
| `--color-prettylights-syntax-markup-heading` | `#EAE6DC` | `$chalk-bright` |
| `--color-prettylights-syntax-markup-italic` | `#D2CCC0` | `$chalk` |
| `--color-prettylights-syntax-markup-bold` | `#EAE6DC` | `$chalk-bright` |
| `--color-prettylights-syntax-markup-deleted-text` | `#EAE6DC` | `$chalk-bright` |
| `--color-prettylights-syntax-markup-deleted-bg` | `#EB5757` | `$pixel-red` (low opacity) |
| `--color-prettylights-syntax-markup-inserted-text` | `#0D1610` | `$board-darkest` |
| `--color-prettylights-syntax-markup-inserted-bg` | `#5BDB6D` | `$phosphor-green` (low opacity) |
| `--color-prettylights-syntax-markup-changed-text` | `#EAE6DC` | `$chalk-bright` |
| `--color-prettylights-syntax-markup-changed-bg` | `#F5A623` | `$pixel-amber` (low opacity) |
| `--color-prettylights-syntax-markup-ignored-text` | `#7E8F82` | `$chalk-dim` |
| `--color-prettylights-syntax-markup-ignored-bg` | `#1C2E22` | `$board` |
| `--color-prettylights-syntax-meta-diff-range` | `#56CCF2` | `$pixel-cyan` |
| `--color-prettylights-syntax-brackethighlighter-angle` | `#7E8F82` | `$chalk-dim` |
| `--color-prettylights-syntax-sublimelinter-gutter-mark` | `#7E8F82` | `$chalk-dim` |
| `--color-prettylights-syntax-constant-other-reference-link` | `#A8D8A0` | `$code-color` |

#### 2b — Regular Button (`--color-btn-*`)

| Giscus property | Value | Token |
|---|---|---|
| `--color-btn-text` | `#D2CCC0` | `$chalk` |
| `--color-btn-bg` | `#1C2E22` | `$board` |
| `--color-btn-border` | `rgba(47,70,54,0.8)` | `$board-lighter` @80% |
| `--color-btn-shadow` | `0 0 transparent` | — (none) |
| `--color-btn-inset-shadow` | `0 0 transparent` | — (none) |
| `--color-btn-hover-bg` | `#253A2C` | `$board-light` |
| `--color-btn-hover-border` | `#2F4636` | `$board-lighter` |
| `--color-btn-active-bg` | `#2F4636` | `$board-lighter` |
| `--color-btn-active-border` | `#2F4636` | `$board-lighter` |
| `--color-btn-selected-bg` | `#253A2C` | `$board-light` |

#### 2c — Primary Button (`--color-btn-primary-*`)

The "Comment" submit button and sign-in CTA use phosphor-green.

| Giscus property | Value | Token |
|---|---|---|
| `--color-btn-primary-text` | `#0D1610` | `$board-darkest` |
| `--color-btn-primary-bg` | `#5BDB6D` | `$phosphor-green` |
| `--color-btn-primary-border` | `rgba(91,219,109,0.6)` | `$phosphor-green` @60% |
| `--color-btn-primary-shadow` | `0 0 transparent` | — |
| `--color-btn-primary-inset-shadow` | `0 0 transparent` | — |
| `--color-btn-primary-hover-bg` | `#84e391` | `$phosphor-green` lighten 15% |
| `--color-btn-primary-hover-border` | `rgba(91,219,109,0.8)` | `$phosphor-green` @80% |
| `--color-btn-primary-selected-bg` | `#4fc460` | `$phosphor-green` darken 12% |
| `--color-btn-primary-selected-shadow` | `0 0 transparent` | — |
| `--color-btn-primary-disabled-text` | `rgba(13,22,16,0.5)` | `$board-darkest` @50% |
| `--color-btn-primary-disabled-bg` | `rgba(91,219,109,0.4)` | `$phosphor-green` @40% |
| `--color-btn-primary-disabled-border` | `transparent` | — |

#### 2d — UI Controls

| Giscus property | Value | Token |
|---|---|---|
| `--color-action-list-item-default-hover-bg` | `rgba(47,70,54,0.5)` | `$board-lighter` @50% |
| `--color-segmented-control-bg` | `#152119` | `$board-dark` |
| `--color-segmented-control-button-bg` | `#1C2E22` | `$board` |
| `--color-segmented-control-button-selected-border` | `#2F4636` | `$board-lighter` |

#### 2e — Text / Foreground

| Giscus property | Value | Token |
|---|---|---|
| `--color-fg-default` | `#D2CCC0` | `$chalk` |
| `--color-fg-muted` | `#7E8F82` | `$chalk-dim` |
| `--color-fg-subtle` | `#7E8F82` | `$chalk-dim` |

#### 2f — Canvas / Background

| Giscus property | Value | Token |
|---|---|---|
| `--color-canvas-default` | `#1C2E22` | `$board` |
| `--color-canvas-overlay` | `#152119` | `$board-dark` |
| `--color-canvas-inset` | `#0D1610` | `$board-darkest` |
| `--color-canvas-subtle` | `#152119` | `$board-dark` |

#### 2g — Borders

| Giscus property | Value | Token |
|---|---|---|
| `--color-border-default` | `#2F4636` | `$board-lighter` |
| `--color-border-muted` | `rgba(47,70,54,0.6)` | `$board-lighter` @60% |

#### 2h — Semantic / Accent

| Giscus property | Value | Token |
|---|---|---|
| `--color-neutral-muted` | `rgba(37,58,44,0.8)` | `$board-light` @80% — inline code bg |
| `--color-accent-fg` | `#5BDB6D` | `$phosphor-green` — links, focus rings |
| `--color-accent-emphasis` | `#5BDB6D` | `$phosphor-green` — author border |
| `--color-accent-muted` | `rgba(86,204,242,0.3)` | `$pixel-cyan` @30% — info borders |
| `--color-accent-subtle` | `rgba(91,219,109,0.1)` | `$phosphor-green` @10% — info bg |
| `--color-success-fg` | `#5BDB6D` | `$phosphor-green` |
| `--color-attention-fg` | `#F5A623` | `$pixel-amber` |
| `--color-attention-muted` | `rgba(245,166,35,0.3)` | `$pixel-amber` @30% |
| `--color-attention-subtle` | `rgba(245,166,35,0.1)` | `$pixel-amber` @10% |
| `--color-danger-fg` | `#EB5757` | `$pixel-red` |
| `--color-danger-muted` | `rgba(235,87,87,0.3)` | `$pixel-red` @30% |
| `--color-danger-subtle` | `rgba(235,87,87,0.1)` | `$pixel-red` @10% |
| `--color-primer-shadow-inset` | `0 0 transparent` | — (no inset shadow) |

#### 2i — Social Reaction Hover States

| Giscus property | Value | Token |
|---|---|---|
| `--color-social-reaction-bg-hover` | `rgba(47,70,54,0.5)` | `$board-lighter` @50% |
| `--color-social-reaction-bg-reacted-hover` | `rgba(91,219,109,0.15)` | `$phosphor-green` @15% |

---

### Entity 3 — GiscusThemeFile

The deliverable CSS file.

| Field | Value |
|---|---|
| Source path | `assets/giscus-retro-blackboard.css` |
| Output path | `docs/assets/giscus-retro-blackboard.css` |
| Public URL | `https://ggilles.dev/assets/giscus-retro-blackboard.css` |
| Format | Plain CSS (no preprocessor, no @import) |
| Selector scope | All declarations on `main {}` — required by giscus |
| Non-variable rules | `main .pagination-loader-container` (dark SVG) and `main .gsc-loading-image` (dark GIF) |
| Typography override | `main { font-family: 'IBM Plex Mono', ui-monospace, monospace; }` for monospace preview; IBM Plex Sans already loaded by host page for body text |
| Target size | < 15 KB |

**File structure outline:**

```css
/* ─── Giscus Retro Blackboard Theme ─── */
/* Tokens inlined from assets/dark.scss  */

main {
  /* 1. Syntax highlighting (prettylights) */
  /* 2. Regular button (btn) */
  /* 3. Primary button (btn-primary) */
  /* 4. UI controls (segmented control, action list) */
  /* 5. Foreground text */
  /* 6. Canvas / background */
  /* 7. Borders */
  /* 8. Semantic / accent */
  /* 9. Social reactions hover */

  /* 10. Typography */
  color-scheme: dark;
}

/* 11. Loading images (require non-variable selectors) */
main .pagination-loader-container { … }
main .gsc-loading-image { … }

/* 12. Textarea & toolbar (no CSS variables for these) */
main .gsc-comment-box-textarea { … }
main .gsc-comment-box-md-toolbar { … }
```

---

### Entity 4 — GiscusConfiguration

The updated Quarto configuration referencing the custom theme.

**File**: `posts/_metadata.yml`

```yaml
comments:
  giscus:
    repo: guillaumegilles/guillaumegilles.github.io
    theme: https://ggilles.dev/assets/giscus-retro-blackboard.css  # ← NEW
format:
  html:
    toc: true
    toc-depth: 2
```

**File**: `_quarto.yml` — addition to `project.resources`:

```yaml
project:
  type: website
  output-dir: docs
  render:
    - "*.qmd"
    - "!*.md"
  post-render:
    - scripts/update-profile-readme.sh
  resources:
    - CNAME
    - assets/giscus-retro-blackboard.css  # ← NEW — copied verbatim to docs/assets/
```

---

## State Transitions

This feature is stateless (static files only). There is one observable state
transition in the user-facing widget:

```
[iframe creates] → opacity:0
  → [?theme= URL fetched by giscus SSR] → styles applied inside iframe head
  → [iframe load event fires] → opacity:1
  → [widget visible, fully themed]
```

If the CSS file is temporarily unavailable (deploy window):
```
[iframe creates] → opacity:0
  → [theme URL fetch fails] → giscus keeps prior stylesheet (double-buffer)
    or falls back to default theme
  → [iframe load event fires] → opacity:1
  → [widget visible — possibly default-styled, not broken]
```

---

## Validation Rules

1. The CSS file MUST be valid CSS 3/4 — parseable by browsers without errors.
2. Every `--color-*` value MUST be a hex, rgb(), or rgba() literal — no SCSS
   function calls, no `var()` references to host-page properties.
3. All declarations MUST be inside `main {}` or a sub-selector of it — no bare
   `:root {}` or `body {}` (they would apply to giscus.app's own page, not the
   widget).
4. No `@import` rules are permitted.
5. The file MUST be ≤ 15 KB when minified.
6. The `project.resources` entry in `_quarto.yml` MUST result in the file
   appearing at `docs/assets/giscus-retro-blackboard.css` after `quarto render`.
