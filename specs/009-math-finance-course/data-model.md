# Data Model: Cours de Mathématiques Financières (M1)

**Feature**: `009-math-finance-course`
**Phase**: 1 — Design
**Date**: 2026-10-04

This is a static Quarto website — there is no database or API. The "data model"
describes the **content entities** (pages and their required front-matter fields,
sections, and relationships) that must be present for the feature to be complete
and constitution-compliant.

---

## Entities

### 1. Syllabus Page (`index.qmd`)

**File**: `fr/teaching/mathematics-finance/index.qmd`
**Role**: Entry point for the course; satisfies T-VIII.

Required front-matter fields:

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `title` | string | yes | `"Mathématiques financières"` |
| `lang` | string | yes | `"fr"` |
| `date-modified` | ISO date | yes | `"2026-10-04"` |
| `abstract` | string | yes | brief course description |
| `image` | path | no | `"../../teaching/mathematical-finance/image.jpg"` |

Required sections (in order):

1. **Description du cours** — learning objectives (technical + managerial competencies)
2. **Architecture du cours** — table with 3 rows (Journée / Problématique / Thèmes / Production)
3. **Bibliographie recommandée** — 5 references with author, title, edition, publisher
4. Navigation links to each module

Relationships:
- Listed as first entry in `fr-mathematics-finance` sidebar block in `_quarto.yml`
- Linked from EN stub (`teaching/mathematical-finance/index.qmd`) via language switcher

---

### 2. Day-Module Page

**Files**: `fr/teaching/mathematics-finance/module-01.qmd`,
`module-02.qmd`, `module-03.qmd`
**Role**: Main teaching content pages; one per journée.

Required front-matter fields:

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `title` | string | yes | `"Journée 1 — Valeur temps de l'argent"` |
| `lang` | string | yes | `"fr"` |
| `date-modified` | ISO date | yes | `"2026-10-04"` |
| `abstract` | string | yes | journée problématique |

Required section structure (T-II order):

```
## Objectifs de la journée
## Séquence N — [Titre]
  ### Intuition économique
  ### Représentation (ligne du temps)
  ### Formalisation mathématique
    [formule LaTeX + explication en langage courant (T-III)]
    [preuve ou dérivation collapsible (T-VI)]
  ### Décision managériale
  ### Démonstration interactive [OJS block] (T-IV)
  ### Exercices
    #### Niveau 1 — Application directe
    #### Niveau 2 — Problème contextualisé
    #### Niveau 3 — Étude de cas
      [solutions in .callout-caution collapse="true" (T-II)]
## Synthèse et erreurs fréquentes
```

Module-specific content requirements:

| Module | Séquences | Interactive demo |
|--------|-----------|------------------|
| `module-01.qmd` | S1 Intro/diagnostic · S2 Intérêts simples & composés · S3 Actualisation · S4 Taux proportionnels & équivalents · S5 Annuités · S6 Cas pratique · S7 Synthèse | Demo 1: capitalisation vs actualisation (OJS) |
| `module-02.qmd` | S1 Réactivation · S2 Annuités constantes (emprunt) · S3 Autres modalités · S4 Coût actuariel · S5 Obligations · S6 Sensibilité (duration) · S7 Cas financement | Demo 2: prix obligataire vs taux de marché (OJS) |
| `module-03.qmd` | S1 Flux de trésorerie · S2 VAN · S3 TRI · S4 Délai de récupération · S5 Analyse du risque · S6 Cas intégrateur · S7 Évaluation finale | Demo 3: VAN/TRI (OJS) |

Relationships:
- Listed in `fr-mathematics-finance` sidebar block after `index.qmd`
- Each page links to `glossaire.qmd` for term definitions

---

### 3. Glossaire (`glossaire.qmd`)

**File**: `fr/teaching/mathematics-finance/glossaire.qmd`
**Role**: Central symbol and term registry; satisfies T-V.

Required front-matter: `title`, `lang: fr`, `date-modified`.

Required content: alphabetically ordered table (or definition list) with:

| Column | Description |
|--------|-------------|
| Notation | LaTeX symbol (e.g., `$C_0$`) |
| Nom | Term name in French |
| Définition | Plain-language French definition |
| Prononciation | For Greek letters (e.g., Δ → "delta") |
| Module(s) | Where introduced |

Minimum entries (derived from source plan):
`C0`, `Cn`, `i`, `n`, `V0`, `Vn`, `an`, `im`, `ia`, `ip`, `A`, `Am`, `I`, `CRD`,
`P0`, `C` (coupon), `N` (nominal), `r`, `DM`, `D*`, `Δr`, `I0`, `CFt`, `k`, `VAN`,
`TRI`, `IP`, `AE`, `E(VAN)`, `σ(VAN)`.

Relationships:
- Listed in `fr-mathematics-finance` sidebar block under `**Ressources**` section
- Referenced from each module page

---

### 4. Formulaire de Référence (`formulaire.qmd`)

**File**: `fr/teaching/mathematics-finance/formulaire.qmd`
**Role**: Quick-reference sheet with 10 essential formulas.

Required front-matter: `title`, `lang: fr`, `date-modified`.

Required formulas (in order):

| # | Nom | Formule |
|---|-----|---------|
| 1 | Capitalisation | $V_n = V_0(1+i)^n$ |
| 2 | Actualisation | $V_0 = V_n / (1+i)^n$ |
| 3 | Taux équivalent | $i_p = (1+i_a)^{1/m} - 1$ |
| 4 | Valeur acquise d'annuités | $V_n = A \cdot \frac{(1+i)^n - 1}{i}$ |
| 5 | Valeur actuelle d'annuités | $V_0 = A \cdot \frac{1-(1+i)^{-n}}{i}$ |
| 6 | Annuité d'un emprunt | $A = C_0 \cdot \frac{i}{1-(1+i)^{-n}}$ |
| 7 | Prix d'une obligation | $P_0 = \sum_{t=1}^n \frac{C_t}{(1+r)^t} + \frac{N}{(1+r)^n}$ |
| 8 | Valeur actuelle nette | $VAN = -I_0 + \sum_{t=1}^n \frac{CF_t}{(1+k)^t}$ |
| 9 | Taux de rentabilité interne | $0 = -I_0 + \sum_{t=1}^n \frac{CF_t}{(1+TRI)^t}$ |
| 10 | Annuité équivalente | $AE = VAN \cdot \frac{k}{1-(1+k)^{-n}}$ |

Relationships:
- Listed in `fr-mathematics-finance` sidebar under `**Ressources**` section

---

### 5. `_metadata.yml` (FR course directory)

**File**: `fr/teaching/mathematics-finance/_metadata.yml`
**Role**: Sets `lang: fr` for all pages in the directory without per-file repetition.

Content:

```yaml
lang: fr
```

---

### 6. English Stub / Syllabus (existing file update)

**File**: `teaching/mathematical-finance/index.qmd` (existing — refactored)
**Role**: English parity counterpart; satisfies Principle VI.

Front-matter required:

| Field | Type | Required | Value |
|-------|------|----------|-------|
| `title` | string | yes | `"Financial Mathematics"` |
| `lang` | string | yes | `"en"` |
| `date-modified` | ISO date | yes | `"2026-10-04"` |

Required content:
- Brief EN course description (1–2 paragraphs)
- A "Cours disponible en français" / link to FR counterpart
- Bilingual parity notice: "Full English version coming soon"

Note: the current content (the raw French course plan) is replaced by a proper EN
stub. The detailed course plan text is preserved verbatim in `research/source-notes.md`
(already exists at `specs/004-math-fundamentals-course/source-notes.md` pattern) or
can be moved to `specs/009-math-finance-course/source-notes.md` if needed.

---

### 7. `_quarto.yml` Sidebar Blocks

**File**: `_quarto.yml` (existing — edited)

New sidebar block 1 — English:

```yaml
#--- EN --- Mathematics Finance
- id: en-mathematics-finance
  title: "Financial Mathematics"
  contents:
    - teaching/mathematical-finance/index.qmd
```

New sidebar block 2 — French:

```yaml
#--- FR --- Mathematics Finance
- id: fr-mathematics-finance
  title: "Mathématiques financières"
  contents:
    - fr/teaching/mathematics-finance/index.qmd
    - fr/teaching/mathematics-finance/module-01.qmd
    - fr/teaching/mathematics-finance/module-02.qmd
    - fr/teaching/mathematics-finance/module-03.qmd
    - section: "**Ressources**"
      contents:
        - fr/teaching/mathematics-finance/glossaire.qmd
        - fr/teaching/mathematics-finance/formulaire.qmd
```

Insertion point: after the existing `fr-mathematical-fundamentals` block.

---

## State Transitions

Not applicable — static content pages have no runtime state. The "state" of the course
is its publication status (draft → published), tracked by the `draft:` front-matter
field (omit or set `false` to publish).

## Validation Rules

| Rule | Description |
|------|-------------|
| `lang: fr` | All FR pages must declare `lang: fr` (via `_metadata.yml` or per-file) |
| LaTeX syntax | All formulas use `$...$` (inline) or `$$...$$` (display) — no MathJax alternatives |
| Collapsible solutions | All exercise solutions use `.callout-caution` with `collapse="true"` |
| Collapsible proofs | All formal derivations use `.callout-caution` with `collapse="true"` |
| OJS blocks | Each module has exactly one primary OJS demo; additional demos are `TODO:` callouts |
| Bibliography | `index.qmd` lists all 5 references with author, title, edition, publisher |
| Sidebar registration | Every `.qmd` file in `fr/teaching/mathematics-finance/` is listed in `_quarto.yml` |
