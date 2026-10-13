# Quickstart: Validating the concrete-to-abstract revision

**Feature**: `012-data-description-pedagogy`

Run from the repository root (`/home/guillaume/www`).

## Prerequisites

- Quarto 1.10.x (`quarto --version`)
- Project venv with NumPy (`.venv/`, already present) for the checks
- Branch `012-data-description-pedagogy` checked out

## 1. Structure check (revised modules)

```sh
.venv/bin/python specs/012-data-description-pedagogy/check_modules_v2.py \
  teaching/data-description/modules/module-06.qmd
```

**Expected**: `OK` for every rule in
[module-page-contract-v2.md](./contracts/module-page-contract-v2.md)
(section order, time plan = 180 without Excel lab, Try it before the
first formula, a decoder per formula callout, exit check, homework
fields, no `(Excel)` exercise before the homework). Exit code 0.

Unrevised modules still pass the v1 checker:

```sh
.venv/bin/python specs/010-data-description-10-modules/check_modules.py \
  teaching/data-description/modules/module-0{7,8,9}.qmd \
  teaching/data-description/modules/module-10.qmd
```

## 2. Numbers check

```sh
.venv/bin/python -c "import numpy as np
for x in ([590,610,630,630,640],[370,470,670,720,870]):
    x=np.array(x,float); print(x.mean(), x.max()-x.min(), x.var(ddof=1), x.std(ddof=1), round(x.std(ddof=1)/x.mean()*100,2))"
```

**Expected**: `620 50 400 20 3.23` and `620 500 40000 200 32.26` — the
values printed on the page ([research.md](./research.md) R2). The
Harbour worked-example values (478.97, 18,793.33, 137.09, 21.82%) are
unchanged:

```sh
git --no-pager diff main -- teaching/data-description/modules/module-06.qmd \
  | grep -E '^-.*(478\.97|18\{,\}793\.33|137\.09|21\.82)'
```

**Expected**: no output (no line holding these values was deleted
without being re-added).

## 3. Fidelity check

Open `specs/012-data-description-pedagogy/fidelity-record.md` and
confirm every row of [data-model.md](./data-model.md) §4 has a matching
block on the revised page — in particular Homework 1–3 contain the
former Excel Exercises 4–6 and their solutions.

## 4. Render

```sh
PROFILE_README_RUNNING=1 quarto render \
  teaching/data-description/modules/module-06.qmd --quiet
```

**Expected**: exit 0; no new `_freeze/` entry (the figure is OJS,
rendered in the browser). `PROFILE_README_RUNNING=1` prevents the
post-render hook from pushing to the GitHub profile repo.

Privacy check (Principle IV) — the page must not load OJS or Plot from
a third-party CDN:

```sh
grep -oE 'https?://[a-z0-9.-]*(jsdelivr|unpkg|esm\.sh|observablehq)[^"]*' \
  docs/teaching/data-description/modules/module-06.html | sort -u
```

**Expected**: no output; or the same URLs as the already-published
`docs/teaching/mathematical-fundamentals/module-4.html` (existing
precedent, to be flagged to the owner rather than silently accepted).

## 5. Browser walkthrough (manual, ~10 min)

`quarto preview teaching/data-description/modules/module-06.qmd`, then:

1. Read top to bottom: no formula appears before the first *Try it*.
2. Every formula callout is followed by a *Notation decoder*.
3. The OJS two-truck figure: step 1 shows two rows of dots and a mean
   line at 620; step 2 adds deviation segments and "sum = 0"; step 3
   shows squares and the totals 1,600 vs 160,000.
4. *Try it*, exercise, exit-check and homework answers are collapsed by
   default and expand correctly.
5. The Shinylive demo still loads.
6. The time plan has no Excel lab row and totals 180.
7. Pretend to be a student who missed class: can Homework be done from
   the page alone (estimated time, Step 0, instructions, solutions)?

## 6. French stubs (Constitution VI, FR-021)

```sh
for f in teaching/data-description/modules/*.qmd; do
  test -f "fr/$f" || echo "missing: fr/$f"; done
grep -c 'fr/teaching/data-description/modules/' _quarto.yml
```

**Expected**: no `missing:` line, and a count of 13 (sidebar entries).
On the rendered Module 6 page, the language switcher opens the French
stub, which links back to the English page.

## 7. Full site gate (before commit)

```sh
quarto render
```

**Expected**: exit 0 (constitution render gate). Commit `docs/` and
`_freeze/` with the source changes. Note: a full render runs the
post-render hook, which pushes `about.qmd` to the profile repo.

## 8. In-class outcome (after teaching Module 6)

Record exit-check results against SC-004 (≥ 80% explain $s$ in a
sentence; ≥ 70% compute $s^2$ of 5 values by hand) in the fidelity
record's notes, to inform the Module 7 revision.
