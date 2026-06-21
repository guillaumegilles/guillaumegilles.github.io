# Tasks: Giscus Retro Blackboard Theme Integration

**Branch**: `003-giscus-theme-integration` | **Date**: 2026-06-20 | **Plan**: [plan.md](plan.md)

---

## Phase 0 — Setup

| ID | Task | Status | Notes |
|----|------|--------|-------|
| T-01 | Verify repo is on feature branch `003-giscus-theme-integration` | [X] | Pre-condition check |
| T-02 | Read all spec artifacts (spec.md, plan.md, data-model.md, contracts/, quickstart.md) | [X] | Context loaded |

---

## Phase 1 — Core Implementation

| ID | Task | File(s) | Status | Notes |
|----|------|---------|--------|-------|
| T-03 | Create `assets/giscus-retro-blackboard.css` with all 60+ CSS custom properties | `assets/giscus-retro-blackboard.css` | [X] | Sections 1–13 per contract |
| T-04 | Add `assets/giscus-retro-blackboard.css` to `project.resources` in `_quarto.yml` | `_quarto.yml` | [X] | Ensures Quarto copies file to `docs/assets/` |
| T-05 | Add `theme: https://ggilles.dev/assets/giscus-retro-blackboard.css` to `posts/_metadata.yml` | `posts/_metadata.yml` | [X] | Wires theme URL into giscus configuration |

---

## Phase 2 — Validation

| ID | Task | Status | Notes |
|----|------|--------|-------|
| T-06 | Verify `assets/giscus-retro-blackboard.css` exists and is valid CSS | [X] | File created, 11 KB < 15 KB limit |
| T-07 | Verify `_quarto.yml` `project.resources` contains the CSS file entry | [X] | Entry confirmed |
| T-08 | Verify `posts/_metadata.yml` `comments.giscus.theme` URL is set | [X] | URL confirmed |
| T-09 | Run `quarto render` to confirm build succeeds and `docs/assets/giscus-retro-blackboard.css` is produced | [ ] | Requires local quarto CLI |
| T-10 | Deploy to production and verify `curl -I https://ggilles.dev/assets/giscus-retro-blackboard.css` returns 200 + text/css | [ ] | Post-deploy check |

---

## Completion Criteria

All of T-03 through T-08 completed. T-09 and T-10 require `quarto` CLI and production
deploy respectively — these are post-commit verification steps described in
`quickstart.md` Step 4 and Step 5.

See `quickstart.md` for the full acceptance verification checklist (SC-001 through SC-006).
