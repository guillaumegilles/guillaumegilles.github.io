# Quickstart Validation Guide: Mathematical Finance Intuition-First Pedagogy

**Feature**: 011-math-finance-intuition
**Date**: 2026-10-11
**Status**: Complete

---

## Prerequisites

### Required Software
| Tool | Version | Install Command |
|------|---------|-----------------|
| Quarto | ≥ 1.4 | `brew install quarto` / `conda install -c conda-forge quarto` |
| Python | 3.11+ | `brew install python@3.11` / system package manager |
| Node.js | 18+ (for OJS via CDN) | `brew install node` / not strictly required |
| Git | any | `brew install git` |

### Python Dependencies (for Shinylive demos)
```bash
cd /home/guillaume/www
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# requirements.txt should include: numpy, pandas, scipy (for root-finding)
```

### Project Setup
```bash
cd /home/guillaume/www
git status  # verify on branch 011-math-finance-intuition or main
```

---

## Validation Steps

### 1. Render All Three Modules (Technical Validation)

```bash
cd /home/guillaume/www/fr/teaching/mathematical-finance

# Render each module individually (faster for iteration)
quarto render module-01.qmd --quiet
quarto render module-02.qmd --quiet
quarto render module-03.qmd --quiet

# Or render all at once
quarto render
```

**Expected**: All commands exit with code 0. No errors in output.

**If fails**: Check Quarto error output; common issues:
- LaTeX syntax errors in formulas
- Missing Python packages for Shinylive
- Malformed YAML front matter
- OJS/Shinylive code block syntax errors

---

### 2. Structural Grep Checks (Automated Requirement Validation)

Run from `/home/guillaume/www/fr/teaching/mathematical-finance/`:

#### 2.1 Concrete Case Openings (FR-001, SC-001)
```bash
# Should find 13+ matches (one per concept section: Séquences 2-5 × 3 modules)
grep -n "Situation concrète\|Cas réel" module-01.qmd module-02.qmd module-03.qmd
```
**Expected**: ≥ 13 matches. Each concept section (Séquences 2-5) has one.

#### 2.2 Formula Explanations (FR-003, SC-002)
```bash
# Should find matches for every formula box
grep -n "Explication en langage clair" module-01.qmd module-02.qmd module-03.qmd
```
**Expected**: Count matches formula boxes (~30). Each formula box has one immediately after.

#### 2.3 Erreur Fréquente Callouts (FR-006)
```bash
# Should find 13 matches (one per concept section, Séquences 2-5 only)
grep -n "Erreur fréquente" module-01.qmd module-02.qmd module-03.qmd
```
**Expected**: 13 matches. NOT in Séquence 6 (synthesis sections).

#### 2.4 Interactive Demos (FR-009, SC-003)
```bash
# Should find 4+ demo blocks
grep -n "shinylive-python\|ojs" module-01.qmd module-02.qmd module-03.qmd
```
**Expected**: ≥ 4 blocks:
- Module 1: 1 OJS (capitalisation vs actualisation)
- Module 2: 1 OJS (bond price-yield)
- Module 3: 1 Shinylive (VAN-TRI), 1 Shinylive (sensitivity)

#### 2.5 Règle d'Or Reinforcement (FR-005)
```bash
grep -n "Règle d'or\|ligne du temps avant toute formule" module-01.qmd module-02.qmd module-03.qmd
```
**Expected**: ≥ 4 matches (start of each module + before major calculation sections)

#### 2.6 Glossary Intuition Entries (FR-007)
```bash
# Check all 3 fields present for each symbol
grep -n "Ce que ça représente\|Pourquoi ça importe\|Intuition clé" glossaire.qmd
```
**Expected**: 3 × 47+ = 141+ matches (3 fields per symbol)

#### 2.7 Formulaire Intuition Reminders (FR-008)
```bash
grep -n "Cette formule répond à" formulaire.qmd
```
**Expected**: 10 matches (one per formula)

---

### 3. Browser Validation (Interactive Demos & Visuals)

Open rendered HTML files in browser:

```bash
# From project root
open docs/fr/teaching/mathematical-finance/module-01.html
open docs/fr/teaching/mathematical-finance/module-02.html
open docs/fr/teaching/mathematical-finance/module-03.html
```

#### 3.1 Interactive Demo Checks

| Demo | Module | File | Test |
|------|--------|------|------|
| Capitalisation vs Actualisation | 1 | module-01.html | Slider for rate/periods updates future/present value instantly |
| Bond Price-Yield | 2 | module-02.html | Slider for yield updates price curve in real-time |
| VAN-TRI Profile | 3 | module-03.html | Slider for discount rate shows VAN curve crossing zero at TRI |
| Sensitivity Analysis | 3 | module-03.html | Dropdown/sliders for scenarios update tornado chart/table |

**Expected**: All demos load (OJS: instant; Shinylive: ~2-3s cold start), respond to input, no console errors.

#### 3.2 Visual Diagram Checks

| Concept | Module | Verify |
|---------|--------|--------|
| Duration Timeline | 2 | Weighted cash flow blocks; center of gravity marked |
| VAN Profile | 3 | VAN vs. k curve; TRI marked at x-intercept |
| Convexity | 2 | Price-yield curve with tangent + curvature annotation |
| Annuity Timeline | 1 | Period-by-period cash flows with PV arrows |

---

### 4. Content Quality Spot-Checks

#### 4.1 Concrete Case Quality (Sample 3 sections)
Open each module, navigate to Séquence 2, 3, 4 — verify:
- [ ] Narrative is a relatable financial decision (not pure math)
- [ ] Specific numbers used (EUR amounts, realistic rates)
- [ ] Ends with a decision question (?)
- [ ] Appears BEFORE any formula box

#### 4.2 Formula Explanation Quality (Sample 5 formulas)
For each sampled formula box, verify the following `.callout-note` block has:
- [ ] **Ce que calcule cette formule**: 1 sentence, business meaning
- [ ] **Rôle de chaque paramètre**: All symbols covered, economic roles
- [ ] **Ce que signifie le résultat**: Business interpretation (VAN > 0 = value creation, etc.)
- [ ] **Intuition directionnelle**: "Si X change, Y change comment"

#### 4.3 Erreur Fréquente Quality (Sample 3)
For each sampled `.callout-warning`, verify:
- [ ] **L'intuition piège**: Plausible wrong reasoning
- [ ] **Pourquoi c'est faux**: Technical reason
- [ ] **Le bon raisonnement**: Correct approach
- [ ] **Astuce mémo**: Actionable memory aid

#### 4.4 Glossary Entry Quality (Sample 10 symbols)
Open `glossaire.qmd`, verify 10 random symbols have:
- [ ] **Ce que ça représente**: 1 sentence, plain language
- [ ] **Pourquoi ça importe**: 1 sentence, business relevance
- [ ] **Intuition clé**: 1 sentence, directional/analogy

---

### 5. Freeze Cache & Output Commit

```bash
cd /home/guillaume/www

# Verify _freeze/ updated
git status _freeze/

# Commit source + freeze + rendered output
git add fr/teaching/mathematical-finance/*.qmd
git add _freeze/fr/teaching/mathematical-finance/
git add docs/fr/teaching/mathematical-finance/
git commit -m "feat: intuition-first pedagogy for mathematical finance course

- Restructure 13 concept sections with 7-step abstraction ladder
- Add concrete case openings, formula explanations, erreur fréquente
- Add 4 interactive demos (2 OJS, 2 Shinylive)
- Update glossaire (47+ symbols) with 3-field intuition template
- Update formulaire (10 formulas) with intuition reminders
- Reinforce Règle d'or timeline principle throughout"
```

---

## Success Criteria Summary

Targets updated with the actual numbers measured on 2026-10-11 (T064).

| Check | Target | Actual | Command |
|-------|--------|--------|---------|
| Renders (3 modules + glossaire + formulaire) | 5/5 exit 0 | 5/5, no warning | `quarto render <file>.qmd` |
| Concrete cases | 13 (+1 for M2 S6b) | 14 (4 / 6 / 4) | `grep "Situation concrète\|Cas réel" module-0*.qmd \| wc -l` |
| Formula explanations | = formula-box audit (drafts.md T038) | 21 (8 / 6 / 7), 21 boxes | `grep "Explication en langage clair" module-0*.qmd \| wc -l` |
| Erreur fréquente | 13, none in synthesis | 13 (4 / 5 / 4) | `grep "^## Erreur fréquente" module-0*.qmd \| wc -l` |
| Interactive demos | 4 (2 OJS + 2 Shinylive) | 4: OJS M1 S3, OJS M2 S5, Shinylive M3 S3 + S5 | `grep '^```{ojs}\|^```{shinylive-python}' module-0*.qmd` |
| Règle d'or | ≥ 4 | 25 (12 / 7 / 6) | `grep "Règle d'or\|ligne du temps avant toute formule" module-0*.qmd` |
| Glossary intuition fields | ≥ 198 (66 entries × 3) | 198 (33 symbols + 33 terms) | `grep "Ce que ça représente\|Pourquoi ça importe\|Intuition clé" glossaire.qmd \| wc -l` |
| Formulaire reminders | 10 | 10 | `grep "Cette formule répond à" formulaire.qmd \| wc -l` |
| Browser demos work | 4/4 functional | 4/4 mounted (headless Chromium: 3 OJS sliders M1, 4 M2, 2 Shinylive viewers M3); interactive use still to try by hand | Manual |
| Visual diagrams render | 4/4 present | 4/4: annuity flowchart (M1), duration bars + convexity lines (M2, `xychart`), VAN profile in the Shinylive VAN–TRI app (M3) | Manual |

The plan's earlier estimates ("~30" explanations, "47+" glossary entries)
are superseded: the course has 21 formula-bearing boxes and 66 glossary
entries.

**Sandbox render note**: without write access to `~/.cache` and
`~/.local/share`, render with `XDG_CACHE_HOME`, `XDG_DATA_HOME` and
`JUPYTER_RUNTIME_DIR` pointing to `/tmp`, after copying `~/.cache/quarto`
into the new cache (it holds Deno's `std/io` module needed by the Shinylive
filter offline) and linking `~/.cache/shinylive`.

---

## Troubleshooting

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| `quarto render` fails on Shinylive | Missing Python packages | `pip install numpy pandas scipy` in `.venv` |
| OJS demo not showing | JavaScript error | Check browser console; verify `{ojs}` syntax |
| Shinylive cold start timeout | Pyodide load slow | First load takes 2-3s; subsequent loads cached |
| Grep count too low | Missing sections | Check Séquence headings match; verify callout syntax |
| `_freeze/` not updating | Quarto didn't re-execute | Delete specific `_freeze/` entry to force re-run |

---

## Next Steps After Validation

1. If all checks pass → Feature complete, ready for merge
2. If checks fail → Fix issues, re-run validation
3. Run `/speckit-analyze` to verify spec/plan/tasks alignment
4. Create English stubs per Constitution VI (deferred, separate task)

---

## Baseline

Recorded 2026-10-11 (T001–T003), before any content change.

### Renders (T001)

Quarto 1.10.19. Single-file renders with `--quiet` of `module-01.qmd`,
`module-02.qmd`, `module-03.qmd`, `glossaire.qmd`, `formulaire.qmd`: no
output printed. (Exit codes were masked by a pipe in the baseline run; the
first reliably checked renders, after US1, all exit 0.)

**Note**: renders need write access to `~/.cache/quarto` (sass cache). In a
sandbox without it, every render fails with `ERROR: unable to open database
file` — this is environmental, not a content error.

### Structural counts (T002)

| Check | Baseline | Target |
|-------|----------|--------|
| `Situation concrète\|Cas réel` (modules) | 0 | 13 |
| `Explication en langage clair` (modules) | 0 | 1 per formula box |
| `Erreur fréquente` (modules) | 0 | 13 |
| `shinylive-python\|{ojs}` (modules) | 3 (OJS: M1 S3, M2 S5, M3 S3) | ≥ 4 |
| `Règle d'or\|ligne du temps avant toute formule` (modules) | 1 (M1 S5) | ≥ 4 |
| Glossary 3-field lines | 0 | ≥ 198 |
| `Cette formule répond à` (formulaire) | 0 | 10 |

### Shinylive (T003)

- Extension present: `_extensions/quarto-ext/shinylive/_extension.yml`
  (v0.2.0, contributes filter `shinylive.lua`).
- Python package `shinylive` 0.8.6 installed in `.venv/`.
- No page or `_metadata.yml` currently enables the filter: existing
  `{shinylive-python}` blocks (e.g. `teaching/data-description/modules/module-03.qmd`)
  render as plain `<pre class="{shinylive-python}">` code, not as apps.
- Snippet to add to the front matter of `module-03.qmd` (T049):

  ```yaml
  filters:
    - shinylive
  ```