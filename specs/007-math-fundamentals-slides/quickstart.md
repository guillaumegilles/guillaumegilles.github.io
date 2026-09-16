# Quickstart Validation Guide: RevealJS Slide Decks

**Branch**: `007-math-fundamentals-slides` | **Date**: 2026-09-15
**Contract**: [contracts/slide-deck-format.md](contracts/slide-deck-format.md)

This guide describes how to validate that the slide deck feature is working
correctly. Run these checks after implementation, in the order shown.

---

## Prerequisites

```sh
# Activate Python environment (required for quarto render)
source .venv/bin/activate

# Confirm Quarto is available
quarto --version
```

---

## Step 1 — Create the Theme File

Before rendering any slide deck, `assets/dark-slides.scss` must exist.

**Expected state**: `assets/dark-slides.scss` is present in the repo root.

```sh
ls assets/dark-slides.scss   # must not error
```

---

## Step 2 — Render a Single Slide Deck (Smoke Test)

Start with Module 1 as the canary.

```sh
quarto render teaching/mathematical-fundamentals/module-1-slides.qmd --quiet
```

**Expected outcome**:
- Exit code 0, no errors in stderr.
- File `docs/teaching/mathematical-fundamentals/module-1-slides.html` created.

**Failure modes**:
- `Error: theme file not found` → `assets/dark-slides.scss` is missing or
  path is wrong in front matter.
- `Error: format not supported in website context` → verify `format: revealjs`
  is in the file's front matter (not only in `_quarto.yml`).

---

## Step 3 — Visual Inspection of Module 1 Slides

Open the rendered file in a browser:

```sh
open docs/teaching/mathematical-fundamentals/module-1-slides.html
# or on Linux:
xdg-open docs/teaching/mathematical-fundamentals/module-1-slides.html
```

**Checklist**:
- [ ] Presentation opens in full-screen RevealJS (not a standard website page
      with navbar/sidebar/footer).
- [ ] Title slide shows the module title and `"Mathematical Fundamentals ·
      MS01-001-G"` subtitle.
- [ ] Navigation arrows and slide-number indicator are visible.
- [ ] "Learning Objectives" slide appears as the second slide.
- [ ] At least one concept slide with a `.callout-tip` block and a formula
      (rendered LaTeX, not raw `$$...$$`) is present.
- [ ] "Worked Example" slide(s) walk through a step-by-step calculation.
- [ ] "Summary" slide has 2–3 numbered takeaways.
- [ ] "📖 Full Reference" slide has a visible, clickable link.

---

## Step 4 — Verify Reference Link

On the "📖 Full Reference" slide, click the link to the full module page.

**Expected outcome**: The browser navigates to
`module-1.html` (the reference page), which opens as a standard website page
with navbar and sidebar.

---

## Step 5 — Render All 8 English Slide Decks

```sh
for n in 1 2 3 4 5 6 7 8; do
  quarto render teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet
  echo "Module ${n}: OK"
done
```

**Expected outcome**: All 8 `echo "Module N: OK"` lines printed; no errors.

---

## Step 6 — Verify Sidebar Registration

Render the full site and check that the slides appear in the sidebar.

```sh
quarto render --quiet
```

Then open `docs/teaching/mathematical-fundamentals/index.html` in a browser.

**Checklist**:
- [ ] A "**Slides**" section appears in the left sidebar.
- [ ] All 8 "Module N — Slides" links are listed.
- [ ] Clicking a slide link opens the RevealJS presentation (not a 404).

---

## Step 7 — Verify Module-Page Links

Open `docs/teaching/mathematical-fundamentals/module-1.html`.

**Checklist**:
- [ ] A "📊 Lecture slides: View the slides for this module" link is visible
      near the top of the page (before the Diagnostic Activity section).
- [ ] Clicking the link opens `module-1-slides.html`.

---

## Step 8 — Render French Stubs

```sh
for n in 1 2 3 4 5 6 7 8; do
  quarto render fr/teaching/mathematical-fundamentals/module-${n}-slides.qmd --quiet
  echo "FR stub Module ${n}: OK"
done
```

**Expected outcome**: All 8 stubs render without errors.

Then open `docs/fr/teaching/mathematical-fundamentals/module-1-slides.html`.

**Checklist**:
- [ ] Stub opens as a RevealJS presentation.
- [ ] "🚧 Traduction en cours" slide is visible.
- [ ] Link to the English slides is present and working.

---

## Step 9 — Full Site Render (Final Gate)

```sh
quarto render
echo "Exit code: $?"
```

**Expected outcome**: Exit code 0. All 16 slide decks (8 EN + 8 FR stubs)
rendered. No errors or warnings related to this feature.

---

## Common Issues & Fixes

| Symptom | Likely Cause | Fix |
|---|---|---|
| RevealJS not found / wrong output format | `format: revealjs` missing from file front matter | Add to each slide file's YAML |
| `theme file not found` | `assets/dark-slides.scss` missing or wrong path | Create the file; verify relative path |
| Slides appear as normal HTML page (with navbar) | `format: html` taking precedence | Ensure `format: revealjs` is in the individual file, not in `_quarto.yml` globals |
| LaTeX renders as raw text | Missing MathJax in RevealJS config | Add `html-math-method: mathjax` to `format.revealjs` in front matter |
| Link to reference page broken | Wrong relative path in "📖 Full Reference" slide | Use `module-N.qmd` (Quarto resolves to `.html`) |
| FR stub renders 404 | Not registered in sidebar or `fr/` directory missing | Create `fr/teaching/mathematical-fundamentals/` and register in `_quarto.yml` |
