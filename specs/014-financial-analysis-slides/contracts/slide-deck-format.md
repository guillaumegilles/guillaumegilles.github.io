# Contract: Slide Deck Format

This applies to the three decks in `fr/teaching/financial-analysis/slides/`
and to the EN stubs in `teaching/financial-analysis/slides/`.

## 1. Directory metadata

`fr/teaching/financial-analysis/slides/_metadata.yml`, which copies the
`fr/teaching/mathematical-fundamentals/slides/` pattern:

```yaml
format:
  revealjs:
    theme: ../../../../assets/dark-slides.scss
    slide-number: true
    progress: true
    controls: true
    transition: slide
    fig-align: center
```

`teaching/financial-analysis/slides/_metadata.yml` is the same, except for the
theme path `../../../assets/dark-slides.scss`. It sets no `lang:`, which is
inherited from the parent directories.

## 2. Deck front matter

```yaml
---
title: "Jour 1 — Les fondamentaux de l'analyse financière"
subtitle: "Analyse financière et stratégique · INSEEC MSc"
footer: "[Retour au cours 📖](../index.qmd)"
date-modified: 2026-10-18
---
```

There is no `format:` key, since it comes from `_metadata.yml`. There is no
`lang:` key. Do not use `date: today`.

## 3. Deck skeleton (every day)

```markdown
## Programme de la journée            ← role: agenda (table: horaire | bloc | durée | activité/quête)
## Objectifs                           ← role: objectives (3–6 verbs: calculer, interpréter, retraiter…)

# Bloc N — <titre>                     ← section slide per block (no attributes)
## <concept> …
## <formula> …
## Exemple — <cas> …
## Exercice — <cas> …
## Pour aller plus loin                ← links: reference page + quest

# Récapitulatif
## Ce qu'il faut retenir               ← 4–6 bullets
## Demain                              ← preview (Day 1, 2) / Examen & suite (Day 3)
```

Section-level `#` headings start each block. The agenda table must list every
block with its minutes, and the non-optional minutes must add up to 360.

## 4. Role → markup

| Role | Markup |
|---|---|
| definition | `::: {.callout-note}` + `## <term>` inside |
| formula | `::: {.callout-tip}` with `$$…$$`, **followed** by one plain sentence "Ce que mesure…" |
| derivation | `::: {.callout-caution}` with numbered steps (≥ 1 per deck) |
| common mistake | `::: {.callout-warning}` (≤ 1 per deck) |
| unverified fact | `::: {.callout-important}` "TODO: à vérifier — …" (must be **0** at publish) |
| example | plain slide `## Exemple — …`, with a table and `. . .` pauses for step-by-step reveals |
| exercise | `::: {#exr-<slug> name="<Cas>"}` containing the task, data (or link), format and duration. **No solution** |
| focus | blockquote starting `> **Focus — <Entreprise> (<année>)**`, 1–3 lines + lesson |
| then-now | 2-column `:::: {.columns}` "Avant" / "Aujourd'hui" |
| source | `::: aside` → `Source : <éditeur>, <titre>, <date>.` on every slide with year-dependent figures or rebuilt third-party content |
| speaker notes | `::: notes` → `Durée : N min · Corrigé : <fichier> · Optionnel : …` |
| dense table | add `{.smaller}` or `{.scrollable}` to the `##` heading |
| diagram | ```` ```{mermaid} ```` (`flowchart`, `xychart-beta` or `quadrantChart`), with no `%%{init}%%` |

Forbidden: inline `style=`, `<style>`, `<img>` of third-party material,
`<iframe>`/video embeds, `<details>` solutions, and executable code chunks.

## 5. Links

- Course pages: relative paths such as `../modules/structure-fi.qmd` and `../modules/02-archives-consolidees.qmd`. Each one must exist at render time.
- Videos and external documents: absolute `https://` links with the publisher in the link text.
- Answer keys: named in `::: notes` only, never linked from public slides.

## 6. EN stub (each of `jour-1..3`)

```markdown
---
title: "Day N — <English title>"
subtitle: "Financial Analysis · INSEEC MSc"
footer: "[Back to the course 📖](../index.qmd)"
date-modified: 2026-10-18
---

## Translation in progress

These lecture slides are currently available in French only.

[Open the French slides →](/fr/teaching/financial-analysis/slides/jour-N.html)
```

## 7. Sidebar registration (`_quarto.yml`)

```yaml
    #--- FR --- Financial Analysis
    - id: fr-financial-analysis
      title: "Analyse financière"
      contents:
        - fr/teaching/financial-analysis/index.qmd
        - section: "**Diapositives**"
          contents:
            - fr/teaching/financial-analysis/slides/jour-1.qmd
            - fr/teaching/financial-analysis/slides/jour-2.qmd
            - fr/teaching/financial-analysis/slides/jour-3.qmd
```

The existing EN block `inseec-finane` is repaired to:
`teaching/financial-analysis/index.qmd`, followed by a `**Slides**` section
listing the 3 EN stubs. Other course pages stay out of this feature's scope
(spec 013).

## 8. Syllabus link (`fr/teaching/financial-analysis/index.qmd`)

Add a `## Diapositives` subsection under `# Séances`. It holds a 3-row table
(Jour | Thème | Lien), placed after "Plan des séances". No other change.

## 9. Acceptance checks per deck

1. `quarto render <deck> --quiet` exits 0.
2. The agenda minutes of non-optional blocks add up to 360.
3. The deck has ≥ 1 `callout-caution`, ≤ 1 `callout-warning` and 0 `TODO: à vérifier`.
4. Every `{#exr-…}` block has a `::: notes` naming its answer key.
5. Every slide with a year-dependent figure has an `::: aside` source.
6. The deck contains no `<iframe>`, no `<details>` and no `style=`.
7. Every relative link resolves in `docs/`.
