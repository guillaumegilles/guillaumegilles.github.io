# Contract: Giscus Custom Theme CSS

**Phase 1 output** — Public interface contract for the custom theme stylesheet.

> **Type**: Static asset / public URL contract
> **Interface owner**: guillaumegilles/guillaumegilles.github.io
> **Consumer**: giscus widget iframe (fetched server-side by `giscus.app`)

---

## Overview

`assets/giscus-retro-blackboard.css` is a publicly accessible static file served
at a stable HTTPS URL. It is consumed by giscus at iframe load time: giscus fetches
it, injects it as a `<link>` into the iframe `<head>`, and applies it as the widget
stylesheet. Because it is consumed by an external service via URL, it constitutes a
public interface contract.

Breaking this contract (wrong URL, wrong MIME type, invalid CSS, removed file) causes
the giscus widget to render in its default theme or fail to load styles.

---

## Stable URL

```
https://ggilles.dev/assets/giscus-retro-blackboard.css
```

**Served by**: GitHub Pages, `docs/assets/giscus-retro-blackboard.css`
**Content-Type**: `text/css; charset=utf-8`
**CORS**: Public (required — giscus fetches cross-origin)
**Cache-Control**: Managed by GitHub Pages default (immutable in practice via URL
stability; no cache-busting needed unless the file is replaced with a breaking change)

---

## Format Contract

| Requirement | Rule |
|---|---|
| File format | Plain CSS — no SCSS, no Less, no PostCSS-only syntax |
| `@import` | FORBIDDEN — giscus does not process imported URLs |
| `@use` / `@forward` | FORBIDDEN — SCSS-only directives |
| Selector scope | All declarations inside `main {}` or its sub-selectors |
| CSS custom property values | Hex literals, `rgb()`, or `rgba()` only — no `var()` references to host-page custom properties (cross-origin boundary) |
| File size | ≤ 15 KB (uncompressed) |
| Character encoding | UTF-8 |
| Browser support | CSS Level 4 custom properties (all modern evergreen browsers) |

---

## Required Sections

The CSS file MUST include all five sections below. Omitting any section leaves the
corresponding widget element unstyled (defaulting to GitHub blue or white).

### Section 1 — `main {}` CSS Custom Properties

All giscus CSS custom properties declared as a single rule on `main {}`.
Mandatory property groups:

| Group | Properties | Consequence if missing |
|---|---|---|
| Canvas/background | `--color-canvas-default`, `--color-canvas-overlay`, `--color-canvas-inset`, `--color-canvas-subtle` | Widget renders with off-palette background |
| Foreground text | `--color-fg-default`, `--color-fg-muted`, `--color-fg-subtle` | Comment text uses default (near-white or near-black) |
| Borders | `--color-border-default`, `--color-border-muted` | Dividers use GitHub-default grey |
| Primary button | `--color-btn-primary-bg`, `--color-btn-primary-text`, all `--color-btn-primary-*` | Submit / sign-in button shows GitHub green |
| Regular button | All `--color-btn-*` | Sort controls, pagination use default styling |
| Accent | `--color-accent-fg`, `--color-accent-emphasis`, `--color-accent-muted`, `--color-accent-subtle` | Links and focus rings use GitHub blue |
| Syntax highlight | All 30 `--color-prettylights-syntax-*` | Code in comments renders with light-theme syntax colours |
| Social reactions | `--color-social-reaction-bg-hover`, `--color-social-reaction-bg-reacted-hover` | Reaction hover states use GitHub defaults |
| Semantic | `--color-neutral-muted`, `--color-success-fg`, `--color-attention-*`, `--color-danger-*` | Warning and error states use GitHub palette |
| UI controls | `--color-segmented-control-bg`, `--color-segmented-control-button-bg`, `--color-segmented-control-button-selected-border`, `--color-action-list-item-default-hover-bg` | Sort-order BtnGroup unstyled |

### Section 2 — `color-scheme: dark`

```css
main {
  color-scheme: dark;
}
```

Required to signal dark mode to browser native form controls (textarea, scrollbars)
inside the iframe. Without this, the textarea and select elements render in light mode.

### Section 3 — Loading Spinner Images

```css
main .pagination-loader-container {
  background-image: url("https://github.com/images/modules/pulls/progressive-disclosure-line-dark.svg");
}

main .gsc-loading-image {
  background-image: url("https://github.githubassets.com/images/mona-loading-dark.gif");
}
```

These two selectors have no corresponding CSS custom properties. Without them,
loading states show bright (light) images against the dark background.

### Section 4 — Textarea Styling

```css
main .gsc-comment-box-textarea {
  background-color: #0D1610;      /* $board-darkest */
  color: #D2CCC0;                  /* $chalk */
  border-color: #2F4636;           /* $board-lighter */
}

main .gsc-comment-box-textarea::placeholder {
  color: #7E8F82;                  /* $chalk-dim */
}

main .gsc-comment-box-textarea:focus {
  border-color: #5BDB6D;           /* $phosphor-green */
  outline: none;
  box-shadow: 0 0 0 2px rgba(91, 219, 109, 0.2);
}
```

The textarea element is not addressable via CSS custom properties. Without this
section, the compose area renders with a white/light background (FR-003 / FR-004
violation for User Story 3).

### Section 5 — Markdown Toolbar

```css
main .gsc-comment-box-md-toolbar {
  background-color: #152119;      /* $board-dark */
  border-bottom-color: #2F4636;   /* $board-lighter */
}

main .gsc-toolbar-item {
  color: #7E8F82;                  /* $chalk-dim */
}

main .gsc-toolbar-item:hover {
  color: #D2CCC0;                  /* $chalk */
  background-color: rgba(47, 70, 54, 0.4);
}
```

---

## Stability Guarantees

| Stable (safe to target) | Unstable (avoid) |
|---|---|
| All `--color-*` CSS custom properties | `gsc-*` class names (explicitly warned in giscus CONTRIBUTING.md) |
| `main {}` selector scope | Internal HTML structure of giscus components |
| Loading image selectors (required non-variable rule) | Selector depths beyond `.gsc-comment-box-textarea` and `.gsc-toolbar-item` |

The four `gsc-*` selectors used in Sections 4–5 are the minimum required where no
CSS variable alternative exists. They should be reviewed whenever a giscus major
version is released.

---

## Breaking Changes

The following changes to this file or its URL constitute a breaking change that will
cause the widget to fall back to its default (off-palette) theme:

1. Renaming or moving the file (URL changes).
2. Making the file serve a non-`text/css` Content-Type.
3. Introducing a syntax error that prevents the file from parsing.
4. Removing the file without updating `posts/_metadata.yml` and `_quarto.yml`.
5. Adding `@import` rules (blocked by giscus CSP).

---

## Versioning

This CSS file has no formal version number. It is implicitly versioned by Git
commit. When giscus updates its internal HTML structure, the `gsc-*` class selectors
in Sections 4–5 may need to be revised. Check `giscus/giscus` release notes for
structural changes when updating the giscus configuration.
