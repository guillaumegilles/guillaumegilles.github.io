# Contract: Session Page (`session-NN.qmd`)

Applies to all 12 files under `teaching/data-description/`. Enforces
FR-002, FR-006, FR-007, FR-008, FR-009, FR-011, FR-012, FR-017, and
FR-018 (Session 12 only), plus constitution T-II/T-III/T-IV/T-VI/T-VII.

## Front matter (required)

```yaml
---
title: "Session NN — <Topic>"
subtitle: "Data Description | Part <I/II/III>"
lang: en
draft: true   # removed from all 15 files together only once SC-001 is met
---
```

## Required body structure, in order (T-II, NON-NEGOTIABLE)

1. **Introduction** — one short paragraph on why the topic matters for
   data-driven decisions (plain English, T-III).
2. **Learning objectives** — a bulleted list of concrete, checkable
   outcomes.
3. **Theory** — definitions and formulas in LaTeX (`$...$`/`$$...$$`),
   each formula followed by a plain-language explanation of what it
   computes and why (T-III). At least one `.callout-note` (definition)
   and one `.callout-tip` (formula) per major concept, per constitution
   §V.
4. **Worked example** — uses "The Wandering Fork" dataset (Sessions
   3–12) or the warm-up dataset (Sessions 1–2), pulling numbers only
   from `data-model.md`/`wandering-fork-dataset.csv` (FR-006). Shows a
   full step-by-step solution with a stated result.
5. **Using Excel** — a table or `.callout-tip` naming the exact
   English-locale Excel function(s)/steps for every statistical concept
   introduced in this session (FR-007).
6. **Proof / derivation** — at least one collapsible
   (`.callout-caution collapse="true"`) formal derivation of the
   session's central formula or result (FR-011, T-VI).
7. **Visual/geometric intuition** — surfaced wherever the concept has
   one (FR-012, T-VII), e.g., embedded chart or geometric description.
8. **Interactive demo** *(only for the 4 sessions covering a FR-008
   priority concept)* — a `{shinylive-python}` block seeded with "The
   Wandering Fork" data. Any other priority concept without a demo gets
   a `.callout-important` `TODO:` block instead (constitution T-IV
   escape hatch).
9. **Exercises** — practice items with `.callout-caution
   collapse="true"` revealable solutions (FR-009). MCQ-style self-check
   items (ported from the source's "adaptive learning path") are static
   question/options/feedback blocks, not live quizzes.
10. **(Session 12 only) Mock exam** — an originally-authored section
    mixing MCQ and short-answer items on "The Wandering Fork" data,
    mirroring the Midterm/Final Exam format and difficulty described in
    the syllabus, with revealable solutions (FR-018). MUST NOT reproduce
    verbatim source exam questions or answer keys.

## Validation checklist for this contract

- [ ] Front matter has `title`, `subtitle`, `lang: en`, `draft: true`
- [ ] Sections appear in the order above; none skipped except item 8/10
      where explicitly scoped
- [ ] All math is LaTeX; no raw Unicode superscripts/HTML sub-sup tags
- [ ] Every formula has a plain-language explanation nearby
- [ ] Worked-example numbers trace back to `data-model.md`/the CSV
- [ ] At least one collapsible proof and one revealable exercise solution
- [ ] No proprietary source figures, verbatim exam text, or answer keys
      appear anywhere on the page (FR-003/FR-018)
