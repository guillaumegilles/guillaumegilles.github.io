# Contract: Syllabus Page (`index.qmd`)

Applies to `teaching/data-description/index.qmd`. Enforces FR-001,
FR-016, FR-017 and constitution T-VIII.

## Front matter (required)

```yaml
---
title: "Data Description"
subtitle: "MS03-001-G | Business School"
lang: en
draft: true   # removed together with all other 14 files once SC-001 is met
---
```

## Required content, in order

1. **Course description** — what the course covers and why (first
   stage of data analysis: numerical summaries + graphical
   representation), 2–4 sentences.
2. **Curriculum placement** — explicit note: successor to Mathematical
   Fundamentals (MS01, `teaching/mathematical-fundamentals/`) and
   Mathematical Analysis (MS02, `teaching/mathematical-analysis/`);
   prerequisite refresher for Inferential Statistics (MS04,
   `teaching/decision-making-stat/`) (FR-016).
3. **Learning objectives** — bulleted list.
4. **Session outline table** — grouped by the three parts, linking every
   session file:

   | Part | # | Session | Topic |
   |---|---|---|---|
   | I. Excel Fundamentals | 1–2 | [Session 1](session-01.qmd), [Session 2](session-02.qmd) | … |
   | II. Univariate Data Treatment | 3–9 | [Session 3](session-03.qmd) … [Session 9](session-09.qmd) | … |
   | III. Bivariate Data Treatment | 10–12 | [Session 10](session-10.qmd) … [Session 12](session-12.qmd) | … |

5. **Assessment** — Midterm Exam 35% (45 min) + Final Exam 65%
   (90 min), individual written exams with MCQ component; note that
   Session 12 includes original mock-exam practice (FR-018).
6. **Personal work** — 20h; brief description (exercises per part).
7. **Recommended Literature** — every entry from the source syllabi
   (French and English bibliographies), each with author(s), title,
   edition, and publisher (T-VIII; a course `index.qmd` without this
   section is incomplete/unpublishable).

## Validation checklist for this contract

- [ ] Front matter has `title`, `subtitle`, `lang: en`, `draft: true`
- [ ] Curriculum placement note present and links resolve
- [ ] Session outline table links to all 12 sessions, grouped correctly
      by part
- [ ] Assessment weighting/durations match the syllabus source exactly
      (35%/45min, 65%/90min)
- [ ] Recommended Literature section present with author/title/edition/
      publisher for every entry
