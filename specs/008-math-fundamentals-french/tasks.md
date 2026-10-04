# Tasks: Mathematical Fundamentals — French Version

**Input**: Design documents from `specs/008-math-fundamentals-french/`

**Prerequisites**: plan.md ✅ · spec.md ✅ · research.md ✅ · data-model.md ✅ ·
contracts/url-structure.md ✅ · quickstart.md ✅

**Tests**: Not requested — validation is performed via `quarto render` and
the quickstart.md checklist.

**Organization**: Tasks grouped by user story to enable independent
implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no shared dependencies)
- **[Story]**: User story this task belongs to (US1, US2, US4)
- All file paths are relative to the repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the `fr/` directory structure and install the per-directory
metadata files that all subsequent tasks depend on.

**⚠️ CRITICAL**: Phase 2 and all user story phases depend on this being
complete first.

- [x] T001 Create `assets/lang-switch.html` — a self-contained HTML fragment
  containing a vanilla JavaScript language switcher. The script reads
  `window.location.pathname` on DOMContentLoaded; if the path starts with
  `/fr/` it strips the prefix and renders a link labelled
  "🇬🇧 English version" pointing to the EN counterpart; otherwise it prepends
  `/fr` and renders a link labelled "🇫🇷 Version française" pointing to the FR
  counterpart. The link MUST be wrapped in a `<p>` tag with class
  `lang-switch` (no inline styles; styling goes in `assets/dark.scss`).
  Add a `.lang-switch` rule to `assets/dark.scss` (small muted text, right-
  aligned, top margin).

- [x] T002 Create `fr/teaching/mathematical-fundamentals/_metadata.yml` with
  the following content — this file makes `lang: fr` the default for all FR
  pages and wires in the language switcher; it must replicate the inherited
  settings from `teaching/_metadata.yml` explicitly (since `fr/` does not
  inherit from `teaching/`):

  ```yaml
  lang: fr

  execute:
    echo: false

  comments:
    hypothesis: true

  format:
    html:
      toc: true
      toc-depth: 3
      include-before-body: ../../../assets/lang-switch.html
  ```

**Checkpoint**: `fr/teaching/mathematical-fundamentals/` directory and
`_metadata.yml` exist; `assets/lang-switch.html` and its `.lang-switch` SCSS
rule exist.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Update `_quarto.yml` so all 20 FR pages are reachable via the
sidebar and a language-switcher navbar tool is visible site-wide. Also wire
the language switcher into the English `mathematical-fundamentals` teaching
directory.

**⚠️ CRITICAL**: No user story work can be validated until this phase is
complete (sidebar entries must exist before `quarto render` accepts the FR
source files).

- [x] T003 Create `teaching/mathematical-fundamentals/_metadata.yml` — adds
  the language switcher include to the English mathematical-fundamentals
  directory (the `teaching/_metadata.yml` parent already sets `lang: en`,
  `execute.echo: false`, `comments.hypothesis: true`, and `format.html.toc`
  settings; this file only adds the include):

  ```yaml
  format:
    html:
      include-before-body: ../../assets/lang-switch.html
  ```

- [x] T004 Replace the existing partial `fr-mathematical-fundamentals` sidebar
  block in `_quarto.yml` (currently covers slides only) with the complete
  block below. The new block mirrors the English `mathematical-fundamentals`
  sidebar structure exactly — index first, 8 numbered module sections each
  with a Reference and a Slides link using French display text, then a
  Ressources section:

  ```yaml
  - id: fr-mathematical-fundamentals
    title: "Fondements Mathématiques"
    contents:
      - fr/teaching/mathematical-fundamentals/index.qmd
      - section: "**1. Calculs numériques**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-1.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-1-slides.qmd
      - section: "**2. Équations**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-2.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-2-slides.qmd
      - section: "**3. Courbes & Systèmes**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-3.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-3-slides.qmd
      - section: "**4. Suites**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-4.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-4-slides.qmd
      - section: "**5. Maths financières**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-5.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-5-slides.qmd
      - section: "**6. Fonctions**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-6.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-6-slides.qmd
      - section: "**7. Optimisation**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-7.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-7-slides.qmd
      - section: "**8. Révision**"
        contents:
          - text: "Référence"
            href: fr/teaching/mathematical-fundamentals/module-8.qmd
          - text: "Diapositives"
            href: fr/teaching/mathematical-fundamentals/module-8-slides.qmd
      - section: "**Ressources**"
        contents:
          - fr/teaching/mathematical-fundamentals/glossary.qmd
          - fr/teaching/mathematical-fundamentals/formula-sheet.qmd
          - fr/teaching/mathematical-fundamentals/learning-guide.qmd
  ```

- [x] T005 Add a language-switcher navbar tool to `_quarto.yml` under
  `website.navbar.tools`. This is a site-wide fallback (links to the course
  index pages, not the current page's counterpart — the per-page switching is
  handled by `assets/lang-switch.html`):

  ```yaml
  navbar:
    tools:
      - icon: translate
        text: "Langue / Language"
        menu:
          - text: "🇬🇧 English"
            href: /teaching/mathematical-fundamentals/index.html
          - text: "🇫🇷 Français"
            href: /fr/teaching/mathematical-fundamentals/index.html
  ```

  Merge this into the existing `navbar:` block without overwriting the
  existing `logo`, `title`, and `left:` keys.

**Checkpoint**: `quarto render` must exit 0 after Phase 2 even though FR
`.qmd` files do not yet exist — confirm by temporarily creating placeholder
stubs (one-line files) for all 20 FR paths listed in the sidebar, running
render, then deleting the stubs before starting Phase 3. Alternatively,
proceed directly to Phase 3 if creating placeholders is impractical; in that
case, the render gate is deferred to the Polish phase.

---

## Phase 3: User Story 1 — French Course Pages (Priority: P1) 🎯 MVP

**Goal**: A French-speaking student can navigate the full course — syllabus,
all 8 reference modules, glossary, formula sheet, and learning guide — entirely
in French.

**Independent Test**: Run `quarto render`, then open
`docs/fr/teaching/mathematical-fundamentals/index.html` and follow every
internal link. All destinations should render French prose with working
sidebar navigation. Count rendered HTML files:
`find docs/fr/teaching/mathematical-fundamentals -name "*.html" | grep -v slides | wc -l`
Expect ≥ 12 (index + 8 modules + glossary + formula-sheet + learning-guide).

### Implementation for User Story 1

- [x] T006 [US1] Create `fr/teaching/mathematical-fundamentals/index.qmd` —
  French course syllabus. Source: `teaching/mathematical-fundamentals/index.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "Fondements Mathématiques et Analyse de Données"
  subtitle: "MS01-001-G"
  description: |
    Cours de licence fournissant les outils mathématiques essentiels pour
    analyser et résoudre des problèmes quantitatifs en finance, économie et
    gestion.
  date-modified: 2026-07-23
  image: ../../teaching/mathematical-fundamentals/image.jpg
  lang: fr
  ---
  ```

  Translate ALL prose. Keep all LaTeX verbatim. Required sections (in order,
  all in French): welcome callout (`.callout-note`), Start Here numbered list,
  How to Study tip callout (`.callout-tip`), Course Information table, General
  Presentation, Targeted Competencies, Organisation & Schedule (linking to FR
  module `.qmd` files), Glossary link, Learning Progress checklist, Assessment
  table, Expected Personal Work, Recommended Literature (all 3 references with
  author/title/edition/publisher in French — T-VIII compliance).

  Organisation & Schedule section links must point to FR counterparts in the
  same `fr/teaching/mathematical-fundamentals/` directory (e.g.,
  `[Module 1](module-1.qmd)`, not to the English source).

- [x] T007 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-1.qmd` —
  French reference for Module 1. Source:
  `teaching/mathematical-fundamentals/module-1.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "1️⃣ Calculs mathématiques essentiels pour l'économie et la gestion"
  abstract: |
    Maîtrisez les opérations fondamentales et les propriétés des nombres réels,
    avec des applications en économie et gestion : priorités des opérations,
    valeur absolue, puissances, racines, fractions, pourcentages, indices et
    proportionnalité.
  lang: fr
  ---
  ```

  Translate ALL prose (section headings, callout titles and body text,
  exercise instructions, problem statements, application examples, worked
  example narrative, guided practice text, investigation questions, applied
  problem text, common-errors callout, summary bullets, independent-work
  instructions, "Continue" link label). Keep all LaTeX formulas byte-identical.
  Translate OJS widget labels: "Initial value (€)" → "Valeur initiale (€)";
  "Increase (%)" → "Hausse (%)"; "Decrease (%)" → "Baisse (%)"; "After the
  increase" → "Après la hausse"; "Final value" → "Valeur finale"; "Overall
  change" → "Variation globale". Translate all 4 Investigation questions.
  Slide-link line: `> 📊 **Diapositives** : [Voir les diapositives](module-1-slides.qmd)`.
  "Continue" link: `[Continuer vers le Module 2 →](module-2.qmd)`.

- [x] T008 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-2.qmd` —
  French reference for Module 2. Source:
  `teaching/mathematical-fundamentals/module-2.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "2️⃣ Maîtriser les équations pour mieux décider"
  abstract: |
    Factorisation, développement, identités remarquables et résolution
    d'équations du premier degré.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-2-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 3 →](module-3.qmd)`.

- [x] T009 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-3.qmd` —
  French reference for Module 3. Source:
  `teaching/mathematical-fundamentals/module-3.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "3️⃣ Analyse de courbes en économie et gestion"
  abstract: |
    Représentation graphique, droites, systèmes d'équations et inéquations
    du premier degré.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-3-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 4 →](module-4.qmd)`.

- [x] T010 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-4.qmd` —
  French reference for Module 4. Source:
  `teaching/mathematical-fundamentals/module-4.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "4️⃣ Introduction aux outils de mathématiques financières"
  abstract: |
    Étude des suites numériques : définition générale, suites arithmétiques
    et suites géométriques.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-4-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 5 →](module-5.qmd)`.

- [x] T011 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-5.qmd` —
  French reference for Module 5. Source:
  `teaching/mathematical-fundamentals/module-5.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "5️⃣ Application des mathématiques financières"
  abstract: |
    Intérêts simples et intérêts composés.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-5-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 6 →](module-6.qmd)`.

- [x] T012 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-6.qmd` —
  French reference for Module 6. Source:
  `teaching/mathematical-fundamentals/module-6.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "6️⃣ Fonctions utiles en économie et gestion"
  abstract: |
    Fonctions à une variable (sens, domaine de définition, valeurs interdites)
    et fonctions usuelles (affine, polynomiale, logarithme, exponentielle) ;
    équations du second degré simple et général.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-6-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 7 →](module-7.qmd)`.

- [x] T013 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-7.qmd` —
  French reference for Module 7. Source:
  `teaching/mathematical-fundamentals/module-7.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "7️⃣ Introduction à l'optimisation"
  abstract: |
    Taux de variation moyen et instantané, présentation intuitive de la
    dérivée, appliquée aux fonctions affines et polynomiales.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. Translate any OJS/Shinylive
  widget prose labels. Slide-link:
  `> 📊 **Diapositives** : [Voir les diapositives](module-7-slides.qmd)`.
  Navigation link: `[Continuer vers le Module 8 →](module-8.qmd)`.

- [x] T014 [P] [US1] Create `fr/teaching/mathematical-fundamentals/module-8.qmd` —
  French reference for Module 8. Source:
  `teaching/mathematical-fundamentals/module-8.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "8️⃣ Révision et préparation à l'examen final"
  abstract: |
    Révision générale et consolidation des acquis.
  lang: fr
  ---
  ```

  Translate ALL prose; keep all LaTeX verbatim. No slide-link (Module 8
  slides are a cross-module revision deck). Navigation: no "Continue" link;
  instead link back to `index.qmd`.

- [x] T015 [P] [US1] Create `fr/teaching/mathematical-fundamentals/glossary.qmd` —
  French glossary. Source: `teaching/mathematical-fundamentals/glossary.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "Glossaire"
  abstract: |
    Glossaire français-anglais des symboles et termes utilisés dans le cours
    de Fondements Mathématiques et Analyse de Données.
  date-modified: 2026-07-23
  lang: fr
  ---
  ```

  Translate ALL prose definitions into French. Keep mathematical notation
  (symbols, LaTeX) verbatim. Keep the structure: one `##` section per topic
  (matching the English section headers, translated), one definition list
  entry per term. Ensure entry count ≥ English glossary entry count (VR-006).
  Each entry must include: French term (with English equivalent in
  parentheses), notation if applicable, French plain-language definition,
  pronunciation guide for Greek letters.

- [x] T016 [P] [US1] Create `fr/teaching/mathematical-fundamentals/formula-sheet.qmd` —
  French formula sheet. Source:
  `teaching/mathematical-fundamentals/formula-sheet.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "Aide-mémoire"
  lang: fr
  toc: true
  toc-depth: 2
  ---
  ```

  Translate the intro paragraph and all section headings (one `##` per
  module) and all formula annotations/explanations into French. Keep all
  LaTeX display formulas (`$$…$$`) byte-identical. Keep section count = 8
  (one per module). The opening description paragraph must explain in French
  that this sheet lists the applied formulas invoked directly in exam
  problems.

- [x] T017 [P] [US1] Create `fr/teaching/mathematical-fundamentals/learning-guide.qmd` —
  French learning guide. Source:
  `teaching/mathematical-fundamentals/learning-guide.qmd`.

  Required front matter:
  ```yaml
  ---
  title: "Guide d'apprentissage"
  lang: fr
  toc: true
  toc-depth: 2
  ---
  ```

  Translate ALL prose. Preserve structural headings (same hierarchy,
  translated). Translate all table content (the prerequisites-by-module
  table, any other tables). Keep module names/numbers consistent with the FR
  module titles used in index.qmd (T006).

**Checkpoint**: US1 is independently testable. Run `quarto render` and open
`docs/fr/teaching/mathematical-fundamentals/index.html`. Follow all sidebar
links. Confirm all 12 pages (index + 8 modules + 3 resources) render French
prose with no English body text and no broken links.

US3 NOTE: User Story 3 (stub pages for untranslated content) is automatically
satisfied by this phase — all 20 pages receive full translations; no
"translation in progress" stubs are needed. US3 acceptance scenarios are met
by any page in this phase rendering a complete French page at its expected URL.

---

## Phase 4: User Story 4 — French Slide Decks (Priority: P4)

**Goal**: An instructor teaching on a French-language campus can open any of
the 8 French slide decks and deliver the full lecture in French.

**Independent Test**: Open
`docs/fr/teaching/mathematical-fundamentals/module-1-slides.html` in a
browser. Navigate all slides; confirm all prose is in French; confirm all
LaTeX formulas are present; confirm the closing slide links to
`module-1.qmd` (French reference).

### Implementation for User Story 4

For all 8 slide decks, the required front matter block is:

```yaml
---
title: "[French module title]"
subtitle: "Fondements Mathématiques · MS01-001-G"
lang: fr
format:
  revealjs:
    theme: ../../../assets/dark-slides.scss
    slide-number: true
    progress: true
    controls: true
    transition: slide
    fig-align: center
---
```

Note the theme path is `../../../assets/dark-slides.scss` (3 levels up from
`fr/teaching/mathematical-fundamentals/`), vs. `../../assets/dark-slides.scss`
for the English slides (2 levels up from `teaching/mathematical-fundamentals/`).

The required slide sequence for each deck is:
1. Title slide (auto-generated from front matter)
2. "Objectifs d'apprentissage" — bullet list mirroring EN learning objectives
3. One slide per core concept (same count as EN source)
4. "Exemple résolu" — worked example
5. "Résumé" — 2–3 key takeaways
6. "Référence" — closing slide with link to French reference module

No OJS or Shinylive blocks in slides. Replace any interactive element from the
reference page with a static note: `> Voir la page de référence pour
l'exploration interactive.`

- [x] T018 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-1-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-1-slides.qmd`.
  Title: `"1️⃣ Calculs mathématiques essentiels pour l'économie et la gestion"`.
  Closing slide link: `[Retour au module de référence](module-1.qmd)`.
  Translate all slide prose; keep all LaTeX verbatim.

- [x] T019 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-2-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-2-slides.qmd`.
  Title: `"2️⃣ Maîtriser les équations pour mieux décider"`.
  Closing slide link: `[Retour au module de référence](module-2.qmd)`.

- [x] T020 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-3-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-3-slides.qmd`.
  Title: `"3️⃣ Analyse de courbes en économie et gestion"`.
  Closing slide link: `[Retour au module de référence](module-3.qmd)`.

- [x] T021 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-4-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-4-slides.qmd`.
  Title: `"4️⃣ Introduction aux outils de mathématiques financières"`.
  Closing slide link: `[Retour au module de référence](module-4.qmd)`.

- [x] T022 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-5-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-5-slides.qmd`.
  Title: `"5️⃣ Application des mathématiques financières"`.
  Closing slide link: `[Retour au module de référence](module-5.qmd)`.

- [x] T023 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-6-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-6-slides.qmd`.
  Title: `"6️⃣ Fonctions utiles en économie et gestion"`.
  Closing slide link: `[Retour au module de référence](module-6.qmd)`.

- [x] T024 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-7-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-7-slides.qmd`.
  Title: `"7️⃣ Introduction à l'optimisation"`.
  Closing slide link: `[Retour au module de référence](module-7.qmd)`.

- [x] T025 [P] [US4] Create `fr/teaching/mathematical-fundamentals/module-8-slides.qmd`.
  Source: `teaching/mathematical-fundamentals/module-8-slides.qmd`.
  Title: `"8️⃣ Révision et préparation à l'examen final"`.
  This is a cross-module revision deck; it has no single reference module.
  Closing slide: `[Retour au programme](index.qmd)`.

**Checkpoint**: US4 testable. Open any FR slide deck in browser; confirm
RevealJS presentation mode; confirm French prose; confirm closing slide links
to the correct French reference page; confirm LaTeX renders.

---

## Phase 5: User Story 2 — Language Switcher End-to-End (Priority: P2)

**Goal**: A user on any English or French math fundamentals page can switch
to its counterpart in one click. The switcher implementation was built in
Phase 1–2; this phase verifies the end-to-end behaviour now that all FR pages
exist.

**Independent Test**: From the English `module-3.qmd` page in the rendered
site, click the "🇫🇷 Version française" link; confirm it lands on
`fr/teaching/mathematical-fundamentals/module-3.html`. Then click "🇬🇧 English
version" and confirm the return to
`teaching/mathematical-fundamentals/module-3.html`. Both transitions should
complete in one click.

### Implementation for User Story 2

- [x] T026 [US2] Run `quarto preview` and verify `assets/lang-switch.html`
  is injected on both English and French mathematical-fundamentals pages:
  open `http://localhost:4848/teaching/mathematical-fundamentals/module-2.html`
  and confirm the "🇫🇷 Version française" link is visible and points to
  `/fr/teaching/mathematical-fundamentals/module-2.html`.
  Open `http://localhost:4848/fr/teaching/mathematical-fundamentals/module-2.html`
  and confirm the "🇬🇧 English version" link points to
  `/teaching/mathematical-fundamentals/module-2.html`.
  If the switcher is not injected, debug `teaching/mathematical-fundamentals/
  _metadata.yml` (T003) and `fr/teaching/mathematical-fundamentals/_metadata.yml`
  (T002) `include-before-body` paths.

- [x] T027 [US2] Verify the navbar `translate` tool (T005) is visible on
  every page of the site (not just math fundamentals) and that clicking
  "🇫🇷 Français" navigates to
  `/fr/teaching/mathematical-fundamentals/index.html`. Confirm no existing
  navbar keys (`logo`, `title`, `left:`) were overwritten during the merge
  in T005.

**Checkpoint**: US2 acceptance scenarios pass. All four user stories are now
independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Render gate, glossary parity check, and freeze/docs commit.

- [x] T028 Run `quarto render` from the repository root and confirm exit code
  0. Check that `docs/fr/teaching/mathematical-fundamentals/` exists and
  contains at least 20 HTML files:
  `find docs/fr/teaching/mathematical-fundamentals -name "*.html" | wc -l`.
  Fix any render errors before proceeding.

- [x] T029 [P] Glossary parity audit: count `##` section headers in both
  `teaching/mathematical-fundamentals/glossary.qmd` and
  `fr/teaching/mathematical-fundamentals/glossary.qmd`; counts must be equal
  (VR-006 from data-model.md). If counts differ, add missing entries to the
  French glossary.

- [x] T030 [P] Recommended Literature check: open
  `fr/teaching/mathematical-fundamentals/index.qmd` and confirm the
  Bibliographie recommandée section lists all 3 references present in the
  English `index.qmd`, each with author, title, edition, and publisher in
  French (T-VIII compliance, VR from spec FR-007).

- [x] T031 Run the full quickstart.md validation checklist (Steps 1–10 in
  `specs/008-math-fundamentals-french/quickstart.md`). Document any
  failures and fix them. Once all steps pass, commit `_freeze/`, `docs/`,
  and all source changes together in a single commit (Development Workflow:
  "Both EN and FR render targets MUST pass").

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
  └─► Phase 2 (Foundational) — depends on _metadata.yml and lang-switch.html
        ├─► Phase 3 (US1) — depends on sidebar block existing in _quarto.yml
        └─► Phase 4 (US4) — depends on sidebar block existing in _quarto.yml
              └─► Phase 5 (US2) — depends on FR pages from US1+US4 existing
                    └─► Phase 6 (Polish) — depends on all pages existing
```

Phase 3 and Phase 4 can start in parallel once Phase 2 is complete.

### User Story Dependencies

- **US1 (P1)**: Depends on Phase 1 + Phase 2 only. No dependency on US4.
- **US4 (P4)**: Depends on Phase 1 + Phase 2 only. No dependency on US1.
- **US2 (P2)**: Implementation in Phase 2; full test requires US1 pages to
  exist. Can be partially tested after Phase 2 (switcher code is present)
  but end-to-end verification (Phase 5) requires US1 to be complete.
- **US3 (P3)**: Satisfied by US1 full translations. No dedicated phase.

### Parallel Opportunities

All tasks marked `[P]` within a phase can run concurrently:

**Phase 3 parallel group** (12 tasks, T007–T017 all touch different files):
```
T006 (index.qmd — no [P] because it links to all modules, write last)
T007 ─┐
T008  │
T009  │
T010  ├─ Run in parallel (8 independent module files)
T011  │
T012  │
T013  │
T014 ─┘
T015 ─┐
T016  ├─ Run in parallel (3 independent resource files)
T017 ─┘
```

**Phase 4 parallel group** (8 tasks, T018–T025 all touch different files):
```
T018 ─┐
T019  │
T020  │
T021  ├─ Run in parallel (8 independent slide deck files)
T022  │
T023  │
T024  │
T025 ─┘
```

---

## Parallel Example: Phase 3 (US1)

```text
# Run the 8 module reference translations in parallel:
Task T007: fr/teaching/mathematical-fundamentals/module-1.qmd
Task T008: fr/teaching/mathematical-fundamentals/module-2.qmd
Task T009: fr/teaching/mathematical-fundamentals/module-3.qmd
Task T010: fr/teaching/mathematical-fundamentals/module-4.qmd
Task T011: fr/teaching/mathematical-fundamentals/module-5.qmd
Task T012: fr/teaching/mathematical-fundamentals/module-6.qmd
Task T013: fr/teaching/mathematical-fundamentals/module-7.qmd
Task T014: fr/teaching/mathematical-fundamentals/module-8.qmd

# Run the 3 resource translations in parallel (after or during modules):
Task T015: fr/teaching/mathematical-fundamentals/glossary.qmd
Task T016: fr/teaching/mathematical-fundamentals/formula-sheet.qmd
Task T017: fr/teaching/mathematical-fundamentals/learning-guide.qmd

# Run last (depends on module titles being finalised):
Task T006: fr/teaching/mathematical-fundamentals/index.qmd
```

---

## Implementation Strategy

### MVP (User Story 1 only)

1. Complete Phase 1: Setup (T001–T002)
2. Complete Phase 2: Foundational (T003–T005) — sidebar + switcher infrastructure
3. Complete Phase 3: US1 (T006–T017) — 12 French content pages
4. **STOP AND VALIDATE**: Run `quarto render`; follow all FR sidebar links
5. A French-speaking student can now read the full course — **MVP delivered**

### Incremental Delivery

1. Setup + Foundational → infrastructure ready
2. US1 (Phase 3) → French course readable, US3 satisfied → render and review
3. US4 (Phase 4) → French slide decks available → render and review
4. US2 (Phase 5) → language switcher end-to-end verified → render and review
5. Polish (Phase 6) → render gate + glossary parity + commit

### Parallel Agent Strategy

With multiple LLM agents (or developers), once Phase 2 is complete:

- **Agent A**: US1 modules — T007 through T014 (8 reference modules)
- **Agent B**: US1 resources + index — T015, T016, T017, then T006
- **Agent C**: US4 slides — T018 through T025 (8 slide decks)
- **Coordinator**: Phase 1, Phase 2, Phase 5, Phase 6

---

## Notes

- `[P]` tasks touch different files and have no shared write dependencies;
  they are safe to run in parallel
- `[Story]` labels map to user stories from `specs/008-math-fundamentals-french/spec.md`
- All LaTeX must be byte-identical to the English source — do not simplify,
  reformat, or reorder terms
- OJS widget prose labels must be translated; OJS computation code must be
  copied verbatim
- The theme path in FR slide decks (`../../../assets/dark-slides.scss`) is
  the only structural difference from EN slide front matter
- Stop at each checkpoint to validate independently before proceeding
- Commit `_freeze/`, `docs/`, and source together (Development Workflow)
