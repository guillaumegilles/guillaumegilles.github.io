# Research: Giscus Retro Blackboard Theme Integration

**Phase 0 output** — All NEEDS CLARIFICATION items resolved before Phase 1 design.

---

## Decision 1 — How to host the custom theme CSS

**Decision**: Deliver the theme as `assets/giscus-retro-blackboard.css` (plain CSS,
committed to the repo), list it under `project.resources` in `_quarto.yml` so Quarto
copies it verbatim to `docs/assets/giscus-retro-blackboard.css`, and reference it in
`posts/_metadata.yml` as the full production URL
`https://ggilles.dev/assets/giscus-retro-blackboard.css`.

**Rationale**: giscus resolves any `https://` URL as a "custom" theme and injects it
as a `<link>` inside its iframe before the page paints (server-side SSR). The file
must be served from a stable public HTTPS URL. Quarto's `project.resources` list is
the documented mechanism for copying static assets that are not processed by the
build pipeline (no compilation, no hash suffix). Files listed there land at
`docs/<path>` verbatim, giving a deterministic URL on GitHub Pages.

**Alternatives considered**:
- `raw.githubusercontent.com` URL — rejected: browsers block stylesheets served
  without `Content-Type: text/css`; raw GitHub doesn't set the correct MIME type.
- jsDelivr CDN (`cdn.jsdelivr.net/gh/…`) — rejected: introduces an external CDN
  as a single point of failure; CSS is only available after CDN picks up the commit
  (propagation delay); adds an unnecessary third-party dependency.
- Inline into `assets/dark.scss` — rejected: Quarto compiles SCSS into `docs/
  site_libs/` at a non-deterministic path; even if the source were accessible,
  SCSS is not valid CSS and giscus does not pre-process it.

---

## Decision 2 — Theming mechanism: CSS custom properties vs gsc-* classes

**Decision**: Use CSS custom properties on the `main {}` selector as the primary
and exclusive theming mechanism. Target `gsc-*` class selectors only for the three
elements that have no corresponding CSS variable: the comment textarea, the Markdown
toolbar, and the loading spinner images.

**Rationale**: giscus's `CONTRIBUTING.md` explicitly states that CSS custom
properties are the stable theming API, and warns that `gsc-*` class names and HTML
structure "are subject to change." Minimising reliance on class names reduces
maintenance burden when giscus updates its internals. All colour, background, border,
and accent properties are fully expressible via the documented variable set.

**Alternatives considered**:
- Target only `gsc-*` class names — rejected: brittle; CONTRIBUTING.md warns these
  may change without notice.
- Mix both equally — rejected: creates unnecessary duplication; wherever a CSS
  variable covers the need, it is always preferred.

---

## Decision 3 — File format: plain CSS, no SCSS, no @import

**Decision**: The theme file is a plain `.css` file. SCSS syntax is not used. No
`@import` rules appear in the file.

**Rationale**: giscus fetches the theme URL and injects the response directly into
its iframe `<head>` as a stylesheet. It does not pre-process the file in any way. The
giscus `CONTRIBUTING.md` explicitly forbids `@import` in custom theme files: *"you
cannot @import a syntax theme and must inline it in your CSS."* SCSS would not be
compiled by giscus, so SCSS tokens are not available. All design token values are
therefore inlined as literal hex colours (the same values used in `dark.scss`).

**Alternatives considered**:
- SCSS with `@use "dark"` — rejected: SCSS compilation only happens in the Quarto
  pipeline for the host page; giscus receives raw file bytes.
- CSS custom properties defined in a `:root {}` block on the host page, referenced
  in the theme file — rejected: the giscus iframe is cross-origin; CSS custom
  properties on the host page's `:root` are not inherited by the iframe.

---

## Decision 4 — Dark-variant loading spinners

**Decision**: Override the two required loading-image rules to use GitHub's dark
variants:
- `pagination-loader-container` → `progressive-disclosure-line-dark.svg`
- `gsc-loading-image` → `mona-loading-dark.gif`

**Rationale**: The site is dark-only (no light/dark toggle). Using the dark spinner
variant prevents a brief bright spinner during loading, which would clash with the
dark board surface. These images are served from `github.githubassets.com` — the
same CDN giscus already uses for other assets — so no new third-party dependency is
introduced.

**Alternatives considered**:
- Default (light) spinners — rejected: bright spinner visible against dark background
  for ~200–800 ms on slow connections; conflicts with FR-002 (board surface colours).
- Custom hosted spinner — rejected: unnecessary asset management overhead for a
  detail that GitHub's CDN handles reliably.

---

## Decision 5 — FOUC (Flash of Unstyled Content) prevention

**Decision**: No additional FOUC prevention is needed from the Quarto/host-page
side. giscus's three-layer built-in mechanism is sufficient.

**Rationale**: giscus prevents FOUC through three independent layers:
1. **Server-side SSR**: When the iframe loads, Next.js resolves the `?theme=` URL
   and injects `<link id="giscus-theme" rel="stylesheet" href="..." />` into the
   iframe `<head>` before any React hydration or content renders. The theme CSS is
   applied before the first paint inside the iframe.
2. **iframe opacity:0**: `client.ts` sets `iframe.style.opacity = '0'` immediately
   on creation and only removes it after the `load` event fires, hiding any
   intermediate render state.
3. **Double-buffered theme swap**: Dynamic theme changes (e.g., from a
   `setConfig` postMessage) use a `<link id="giscus-theme-temp">` that only
   replaces the active stylesheet after it successfully loads, preventing any
   unstyled frame.

FR-008 ("theme MUST be applied before the widget becomes visible") is satisfied by
mechanism 1 + 2 without any extra work on the implementer's side.

**Alternatives considered**:
- Injecting a `<style>` block on the host page targeting the iframe — rejected:
  cross-origin iframes block external CSS injection.
- Using `data-loading` attribute CSS hack to delay iframe visibility — rejected:
  redundant; giscus's opacity trick already achieves this.

---

## Decision 6 — Configuration location

**Decision**: Set `comments.giscus.theme` in `posts/_metadata.yml` only. No
`_quarto.yml` or per-post front matter changes to the giscus options.

**Rationale**: `posts/_metadata.yml` is the established configuration location for
giscus on this site (per constitution tech stack table and current config). It
applies to every post in `posts/` without per-post changes, satisfying FR-009. The
Quarto giscus integration reads the `theme` key from `comments.giscus` and passes it
as the `data-theme` attribute to the `client.js` `<script>` tag, which becomes the
`?theme=` URL parameter in the iframe src — exactly the mechanism giscus expects.

**Alternatives considered**:
- Top-level `_quarto.yml` format.html.comments block — not used: the existing
  working configuration is in `_metadata.yml`; changing it without cause risks
  breaking the existing repo/category binding.
- Per-post front matter — rejected explicitly by FR-009.

---

## Resolved NEEDS CLARIFICATION Items

| Item | Resolution |
|------|-----------|
| How is the CSS file made publicly accessible? | `project.resources` in `_quarto.yml` → copied to `docs/assets/` verbatim |
| Is `raw.githubusercontent.com` acceptable as the theme URL? | No — incorrect MIME type; use `https://ggilles.dev/assets/giscus-retro-blackboard.css` |
| Can `dark.scss` variables be shared with the giscus theme? | No — SCSS not processed by giscus; values must be inlined as literals |
| Does giscus handle FOUC automatically? | Yes — three-layer mechanism; no extra work needed |
| Is `@import` allowed in the theme file? | No — explicitly forbidden by giscus CONTRIBUTING.md |
| Where exactly does the `theme` key go? | `posts/_metadata.yml` under `comments.giscus.theme` |
