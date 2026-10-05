# Research: Cours de Mathématiques Financières (M1)

**Feature**: `009-math-finance-course`
**Phase**: 0 — Research
**Date**: 2026-10-04

---

## Decision Log

### 1. Technology for Interactive Demos

**Decision**: Use **OJS (Observable JS)** for all three interactive demos.

**Rationale**: All three demos (capitalisation vs actualisation, prix obligataire vs
taux de marché, VAN/TRI) involve pure arithmetic with no scientific Python dependencies.
OJS advantages over Shinylive for this use-case:
- Instant load (no ~5–10 s Pyodide bootstrap)
- Native reactivity — inputs auto-propagate without explicit reactive decorators
- Observable Plot handles bar/line charts in 5–10 lines
- Quarto ships OJS natively (no extension install)

**Alternatives considered**:
- _Shinylive Python_: Appropriate when NumPy/SciPy/Pandas/Matplotlib are needed.
  Rejected here — overkill for arithmetic.
- _Static charts_: Rejected — the spec (FR-005 / T-IV) requires interactive demos.

---

### 2. File Naming Convention

**Decision**: `module-01.qmd`, `module-02.qmd`, `module-03.qmd` for the three day-pages.

**Rationale**: Consistent with the established pattern in
`fr/teaching/mathematical-fundamentals/` (`module-1.qmd` … `module-8.qmd`). The
spec originally used `jour-1.qmd` in user stories; `module-NN.qmd` is preferred for
cross-course consistency. Zero-padded (`01`, `02`, `03`) for correct alphabetical sort.

**Alternatives considered**:
- `jour-1.qmd` etc.: Descriptive but inconsistent with existing FR course structure.
- `day-1.qmd` etc.: English naming for a French-language course — rejected.

---

### 3. English Parity Strategy

**Decision**: Refactor `teaching/mathematical-finance/index.qmd` into a **proper EN
syllabus** with `lang: en`, add a "full English course coming soon" notice, and add it
to a new `en-mathematics-finance` sidebar block. Do **not** create full EN course pages
(out of scope for this feature).

**Rationale**: The current `teaching/mathematical-finance/index.qmd` is a raw dump of
the French course plan (rendered as `teaching/mathematical-finance/index.html`). It has
no sidebar registration (constitution II violation) and no `lang:` front matter
(constitution VI violation). Refactoring the existing file into a stub EN syllabus
corrects both violations without expanding scope.

**Alternatives considered**:
- _Delete EN file entirely_: Rejected — the rendered HTML is already in `docs/`; removal
  would break the sitemap and existing URLs.
- _Create full EN course pages_: Out of scope; would double the workload. Noted as
  follow-up feature.

---

### 4. Recommended Bibliography

**Decision**: Five references selected for the course syllabus.

| # | Auteur(s) | Titre | Éd. | Éditeur | Langue |
|---|-----------|-------|-----|---------|--------|
| 1 | Devolder, Fox & Vaguener | *Mathématiques financières* | 3e, 2018 | Pearson France | 🇫🇷 Français |
| 2 | Quiry & Le Fur | *Finance d'entreprise* (Vernimmen) | Annuelle (2025) | Dalloz | 🇫🇷 Français |
| 3 | Berk & DeMarzo (adapt. Capelle-Blancard & Couderc) | *Finance d'entreprise* | 6e, 2024 | Pearson France | 🇫🇷 Traduit |
| 4 | Parienté | *Finance actuarielle — Méthodologie et applications* | 1re, 2016 | Pearson France | 🇫🇷 Français |
| 5 | Brealey, Myers & Allen | *Principles of Corporate Finance* | 14e, 2023 | McGraw-Hill Education | 🇬🇧 Anglais |

**Usage guidance**:
- **Devolder et al.**: Primary reference for mathematical rigor (intérêts, annuités,
  duration, obligations). Closest match to the Day 1 and Day 2 content.
- **Vernimmen**: Bible francophone pour la finance d'entreprise appliquée. Reference
  for NPV, IRR, cost of capital, risk analysis (Day 3).
- **Berk & DeMarzo** (FR adapt.): International pedagogy for students who need a
  structured, exercise-rich textbook. Covers all three days.
- **Parienté**: Bridge between actuarial mathematics and managerial decisions.
  Useful for Day 2 (amortization, actuarial rate) and Day 3 (investment selection).
- **Brealey, Myers & Allen**: English reference for students in international tracks
  or double-degree programs.

---

### 5. Interactive Demo Skeletons

#### Demo 1 — Capitalisation vs Actualisation (Module 01)

Recommended technology: **OJS**

```{ojs}
viewof C0 = Inputs.range([100, 10000], {value: 1000, step: 100, label: "C₀ (€)"})
viewof i  = Inputs.range([0.01, 0.20], {value: 0.05, step: 0.001, label: "Taux i"})
viewof n  = Inputs.range([1, 30],      {value: 10,   step: 1,     label: "Périodes n"})

data = Array.from({length: n + 1}, (_, t) => [
  {t, valeur: C0 * (1 + i) ** t,                            serie: "Capitalisation"},
  {t, valeur: C0 * (1 + i) ** n / (1 + i) ** (n - t),      serie: "Actualisation"}
]).flat()

Plot.plot({
  marks: [
    Plot.barY(data, {x: "t", y: "valeur", fill: "serie", fx: "t"}),
    Plot.ruleY([0])
  ],
  color: {legend: true},
  x: {label: "Période"},
  y: {label: "Valeur (€)"}
})
```

#### Demo 2 — Prix obligataire vs taux de marché (Module 02)

Recommended technology: **OJS**

```{ojs}
viewof C  = Inputs.range([0, 200],    {value: 50,   step: 1,     label: "Coupon C (€)"})
viewof N  = Inputs.range([100, 2000], {value: 1000, step: 100,   label: "Nominal N (€)"})
viewof n2 = Inputs.range([1, 30],     {value: 10,   step: 1,     label: "Maturité n"})
viewof r0 = Inputs.range([0.01, 0.15],{value: 0.05, step: 0.001, label: "Taux de référence r"})

bondPrice = (r) => C * (1 - (1 + r) ** -n2) / r + N * (1 + r) ** -n2

curve = Array.from({length: 141}, (_, k) => ({r: 0.01 + k * 0.001, prix: bondPrice(0.01 + k * 0.001)}))
P0     = bondPrice(r0)
status = P0 > N ? "Prime (surcote)" : P0 < N ? "Escompte (décote)" : "Au pair"

md`**Prix P₀ au taux ${(r0*100).toFixed(1)} % :** ${P0.toFixed(2)} € — *${status}*`

Plot.plot({
  marks: [
    Plot.lineY(curve, {x: "r", y: "prix"}),
    Plot.dot([{r: r0, prix: P0}], {x: "r", y: "prix", fill: "red", r: 5}),
    Plot.ruleY([N], {stroke: "gray", strokeDasharray: "4"})
  ],
  x: {label: "Taux de marché r", tickFormat: "%"},
  y: {label: "Prix P₀ (€)"}
})
```

#### Demo 3 — VAN et TRI (Module 03)

Recommended technology: **OJS**

```{ojs}
I0        = 10000
cashflows = [3000, 3500, 4000, 4000, 3000]   // CF₁ … CF₅ (à contextualiser)

viewof k = Inputs.range([0.00, 0.50], {value: 0.10, step: 0.005, label: "Taux d'actualisation k"})

npv = (rate) => -I0 + cashflows.reduce((sum, cf, t) => sum + cf / (1 + rate) ** (t + 1), 0)

vanCurve = Array.from({length: 101}, (_, j) => ({k: j * 0.005, van: npv(j * 0.005)}))

currentVAN = npv(k)

tri = (() => {
  let lo = 0.0001, hi = 0.9999
  for (let i = 0; i < 50; i++) { const mid = (lo + hi) / 2; npv(mid) > 0 ? (lo = mid) : (hi = mid) }
  return (lo + hi) / 2
})()

md`**VAN au taux ${(k*100).toFixed(1)} % :** ${currentVAN.toFixed(2)} € | **TRI ≈** ${(tri*100).toFixed(2)} %`

Plot.plot({
  marks: [
    Plot.lineY(vanCurve, {x: "k", y: "van"}),
    Plot.ruleY([0], {stroke: "gray"}),
    Plot.dot([{k: tri, van: 0}],     {x: "k", y: "van", fill: "red",  r: 6}),
    Plot.dot([{k, van: currentVAN}], {x: "k", y: "van", fill: "blue", r: 5})
  ],
  x: {label: "Taux k", tickFormat: "%"},
  y: {label: "VAN (€)"}
})
```

---

### 6. Directory Path — `mathematics-finance` vs `mathematical-finance`

**Decision**: Use **`mathematics-finance`** for the French course path
(`fr/teaching/mathematics-finance/`), keeping `mathematical-finance` for the existing
English path.

**Rationale**: The existing English path `teaching/mathematical-finance/` is already
rendered in `docs/` and indexed in `docs/sitemap.xml`; changing it would break existing
URLs. The French path is new and can use a cleaner slug. The slight asymmetry
(`mathematical-finance` EN vs `mathematics-finance` FR) is acceptable; the sidebar IDs
and navbar links establish the canonical relationship.

**Alternatives considered**:
- _Use `mathematical-finance` for both_: Would put FR files in
  `fr/teaching/mathematical-finance/`, directly mirroring the EN path. Acceptable and
  arguably more symmetric. Chosen against because the spec explicitly targets
  `fr/teaching/mathematics-finance/`. Either choice is valid; this decision is final
  for this feature.

---

## All NEEDS CLARIFICATION Items Resolved

No `[NEEDS CLARIFICATION]` markers were present in the spec. All design decisions
above stem from research and constitution analysis.
