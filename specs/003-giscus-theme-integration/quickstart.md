# Quickstart: Giscus Retro Blackboard Theme Integration

**Phase 1 output** — How to implement, test, and verify the feature end-to-end.

---

## Prerequisites

- Git repository cloned locally at the repo root
- `quarto` CLI installed and working (`quarto --version`)
- A modern browser (Chrome, Firefox, or Safari)
- A GitHub account for testing the sign-in and comment form (User Story 3)
- Production site already deployed at `https://ggilles.dev` with giscus configured

---

## Step 1 — Create the theme CSS file

Create `assets/giscus-retro-blackboard.css` as a new file in the repository.
Use the token mapping from `specs/003-giscus-theme-integration/data-model.md` and
the format rules from `specs/003-giscus-theme-integration/contracts/giscus-theme-css.md`.

The file MUST:
- Declare all CSS custom properties on `main {}`
- Include `color-scheme: dark` on `main {}`
- Include the two loading-image background-image overrides
- Include the textarea and toolbar selectors
- Be valid plain CSS (no SCSS syntax, no `@import`)

> **Local verification**: Open `assets/giscus-retro-blackboard.css` in a browser
> directly (`file://…`) — it should load without errors in the browser console.
> Run it through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to
> confirm there are no parse errors.

---

## Step 2 — Register the file in `_quarto.yml`

Add one line to the `project.resources` list so Quarto copies it to `docs/assets/`:

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
    - assets/giscus-retro-blackboard.css    # ← add this line
```

> **Local verification**: Run `quarto render`. Confirm `docs/assets/giscus-retro-
> blackboard.css` exists after the build.

---

## Step 3 — Update giscus configuration in `posts/_metadata.yml`

Add the `theme` key with the production URL:

```yaml
comments:
  giscus:
    repo: guillaumegilles/guillaumegilles.github.io
    theme: https://ggilles.dev/assets/giscus-retro-blackboard.css
format:
  html:
    toc: true
    toc-depth: 2
```

> **Note**: The URL must be the production domain. During local development,
> giscus will still fetch the theme from the production URL (not localhost),
> so the theme needs to be deployed to production before local testing shows
> the custom appearance.

---

## Step 4 — Local development verification (pre-deploy)

While the custom theme will only apply fully after the file is deployed to
production, you can validate the CSS file itself locally:

1. Run `quarto render` — verify it exits 0.
2. Confirm `docs/assets/giscus-retro-blackboard.css` exists and matches the source.
3. Open `quarto preview` and navigate to any post page.
4. Open browser DevTools → Network tab. Look for requests to `giscus.app`.
5. In the iframe Network requests, confirm `?theme=https://ggilles.dev/assets/
   giscus-retro-blackboard.css` appears in the giscus widget URL.
6. The theme will still show the default style (production file not yet deployed),
   but the URL parameter confirms the configuration is wired correctly.

---

## Step 5 — Deploy and verify in production

1. Commit all changes:
   - `assets/giscus-retro-blackboard.css` (new)
   - `_quarto.yml` (resources entry)
   - `posts/_metadata.yml` (theme URL)
   - `docs/assets/giscus-retro-blackboard.css` (rendered output)
   - `docs/` (full render output)
   - `_freeze/` (if any computational outputs changed)

2. Push to `main`. GitHub Pages deploys `docs/` within ~60 seconds.

3. Verify the CSS file is reachable:
   ```sh
   curl -I https://ggilles.dev/assets/giscus-retro-blackboard.css
   # Expected: HTTP/2 200 and Content-Type: text/css
   ```

4. Navigate to any published post (e.g., `https://ggilles.dev/posts/<slug>/`).
   Scroll to the giscus widget at the bottom.

---

## Acceptance Verification Checklist

Work through each Success Criterion from the spec:

### SC-001 — Visual integration (no off-palette colours)
- [ ] Widget background matches `#1C2E22` (`$board`) or another board surface tone
- [ ] Comment text colour is `#D2CCC0` (`$chalk`) — matches page body text
- [ ] Section dividers use `#2F4636` (`$board-lighter`) — same as page rule colour

### SC-002 — Zero GitHub-default blue, white, or off-palette colours
- [ ] Open DevTools → Elements → inspect the giscus `<iframe>` content
- [ ] Search for `#0969da`, `#ffffff`, `#fff` in the applied styles — should not appear
- [ ] No white backgrounds visible anywhere in the widget

### SC-003 — Phosphor-green accents on all interactive elements
- [ ] Hover over a reaction emoji button — highlight is green (`#5BDB6D`), not blue
- [ ] View the "Sign in with GitHub" CTA — green primary colour
- [ ] Submit button (if signed in) — green background, dark text

### SC-004 — No horizontal scroll at any width
- [ ] Resize browser to 320 px width
- [ ] Confirm the widget content stays within the column; no horizontal scrollbar

### SC-005 — No FOUC on standard connection
- [ ] Hard-reload a post page (Ctrl+Shift+R / Cmd+Shift+R)
- [ ] Observe giscus widget loading: it should be invisible until fully themed
      (opacity:0 → opacity:1), never showing a white or default-themed flash

### SC-006 — No manual deployment steps
- [ ] Confirm `docs/assets/giscus-retro-blackboard.css` is present in the commit
- [ ] Confirm no additional `wrangler deploy` or manual upload was needed

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Widget still shows default theme after deploy | CSS file not accessible at the URL | `curl -I https://ggilles.dev/assets/giscus-retro-blackboard.css` — check 200 + text/css |
| 404 on the CSS file | Missing from `project.resources` or `quarto render` not run | Add to `_quarto.yml` resources, re-render, commit `docs/assets/giscus-retro-blackboard.css` |
| CSS file served but theme not applied | CORS error or parse error | Check browser console for the giscus iframe; validate CSS at jigsaw.w3.org |
| Bright textarea on comment form | Section 4 missing from CSS file | Add `main .gsc-comment-box-textarea { … }` rule |
| Bright loading spinner | Section 3 missing from CSS file | Add `.pagination-loader-container` and `.gsc-loading-image` rules |
| Theme applied locally but not on reload | Browser cache | Hard-reload; or check GitHub Pages propagation (~60 s) |

---

## Maintenance Notes

- **giscus updates**: When giscus releases a new version, check its release notes for
  structural changes. The `gsc-*` class selectors in the CSS file (Sections 4–5 of
  the contract) may need updating. CSS custom properties are the stable API and should
  not require changes for minor updates.
- **Design token changes**: If `assets/dark.scss` palette values change, the
  corresponding hex literals in `assets/giscus-retro-blackboard.css` must be
  updated manually (they are intentionally inlined, not shared via SCSS variables).
- **URL stability**: Do not rename or move the CSS file. The URL
  `https://ggilles.dev/assets/giscus-retro-blackboard.css` is the public contract
  consumed by giscus at every page load. A rename requires updating `_metadata.yml`
  and deploying before the old URL goes stale.
