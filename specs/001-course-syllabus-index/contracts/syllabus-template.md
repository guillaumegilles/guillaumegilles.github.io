# Contract: Canonical Course Syllabus `index.qmd`

This is the structural contract every `teaching/<course>/index.qmd` MUST
conform to. It is the "interface" the rest of the site (sidebar, search,
students) relies on. Deviations fail the Constitution Check (T-VIII, FR-001..009).

## 1. Front matter (required)

```yaml
---
title: "<Course Title>"
lang: en            # or fr — matches authored language
date-modified: 2026-06-05
# NO per-file `format:`/`theme:` override — global assets/dark.scss applies
---
```

## 2. Body skeleton (required order)

```markdown
## Présentation / Overview

<One or more paragraphs describing the course.>

## Objectifs / Learning Objectives

- Objective 1
- Objective 2
- ...

## Plan des séances / Session Outline

| # | Session | Topics Covered |
|---|---------|----------------|
| 1 | [Session title](session-file.qmd) | Topic A, Topic B |
| 2 | [Session title](other-file.qmd)   | Topic C, Topic D |

## Bibliographie recommandée / Recommended Literature

<!-- Book profile -->
| Author(s) | Title | Edition | Publisher/Source |
|-----------|-------|---------|------------------|
| Lastname, F. | *Full Title* | 3rd | Publisher |
| Org. | *Title* | N/A | https://example.org |
```

### Paper-profile literature (FR-009 — e.g. ai-papers)

```markdown
## Recommended Literature

| Author(s) | Title | Year | Publication Venue |
|-----------|-------|------|-------------------|
| Vaswani et al. | *Attention Is All You Need* | 2017 | NeurIPS |
```

## 3. Sidebar registration (required, in `_quarto.yml`)

The syllabus MUST be the FIRST item in the course's sidebar block:

```yaml
- id: <course-id>
  contents:
    - teaching/<course>/index.qmd   # FIRST, always
    - ...                           # sessions follow
```

## 4. Bilingual counterpart stub contract

For an **EN-authored** syllabus, a French counterpart stub MUST exist at the
mirrored path `fr/teaching/<course>/index.qmd`. (FR-authored courses are
deferred to the language-normalization feature; do **not** create an `en/`
tree.)

```markdown
---
title: "<Source Course Title>"
lang: fr
---

::: {.callout-note}
## Traduction en cours / Translation in progress

Cette page n'est pas encore traduite.
[Voir la version originale »](../../../teaching/<course>/index.qmd)
:::
```

The stub MUST be registered in `_quarto.yml` and verified to render with a
working backlink so it never 404s.

## 5. Acceptance assertions (machine-checkable)

For each `teaching/<course>/index.qmd`:

1. `quarto render teaching/<course>/index.qmd --quiet` exits 0.
2. Front matter contains `title`, `lang`, `date-modified`.
3. No `theme:`/`format:` override present in the file.
4. A line matching `## .*Literature|## .*Bibliographie` exists, followed within
   the section by a Markdown table header row (`| ... |`) with ≥1 data row.
5. A session-outline table with header `| # |` exists; every link in it resolves
   to an existing file (locality-independent).
6. The course's sidebar block in `_quarto.yml` lists this file first.
7. For EN-authored courses: a French stub exists at `fr/teaching/<course>/index.qmd`,
   renders, and its backlink resolves. (FR-authored courses: deferred.)
