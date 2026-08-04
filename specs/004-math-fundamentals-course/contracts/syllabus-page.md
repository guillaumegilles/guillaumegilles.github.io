# Contract: Syllabus Page Structure (`index.qmd`)

The course syllabus is the student's entry point (T-VIII) and the first sidebar
entry.

## Front matter

```yaml
---
title: "Mathematical Fundamentals and Data Analysis"
description: "<short English description>"
date: <course start>
lang: en
image: image.png
categories: [Mathematics, Undergraduate-level]
---
```

## Required sections (all English — FR-010)

1. **Course information** — affiliation, semester, campuses, total hours, ECTS,
   language of instruction, exchange-student availability.
2. **General presentation** — objectives of the course.
3. **Targeted competencies** — competencies 2.3 and 5.2.
4. **Organisation & planning** — a list linking to each module
   (`module-1.qmd` … `module-8.qmd`), each with its one-line topic and date.
   Module titles/descriptions MUST match the module pages (FR-010).
5. **Assessment** — continuous control 50% + final exam 50% table (preserved).
6. **Expected personal work** — workload (≈50 h).
7. **Recommended Literature** — REQUIRED (T-VIII). Each entry MUST include
   author(s), title, edition, and publisher. Titles may remain in their original
   language, but surrounding prose is English.

## Rules

- MUST be the first entry in the `mathematical-fundamentals` sidebar block in
  `_quarto.yml` (§II, T-VIII).
- Every module link MUST resolve (SC-006, SC-007).
- Absence of a Recommended Literature section = incomplete/unpublished (T-VIII).

## Acceptance

- [ ] All eight modules linked and reachable (SC-007).
- [ ] Recommended Literature present with full bibliographic detail (T-VIII).
- [ ] Entirely in English (SC-002).
