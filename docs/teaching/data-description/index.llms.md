## 1 Syllabus

This course is the natural sequel to [Mathematical Fundamentals (MS01)](../../teaching/mathematical-fundamentals/index.llms.md) and [Mathematical Analysis (MS02)](../../teaching/mathematical-analysis/index.llms.md), and it is itself the prerequisite refresher for [Inferential Statistics (MS04)](../../teaching/decision-making-stat/index.llms.md), whose own Session 6 explicitly revisits the numerical summaries introduced here before moving on to confidence intervals and hypothesis testing.

- **Department**: Operations Management and Decision Science
- **Code**: MS03-001-G
- **Semester**: 03
- **Teaching campuses**: Aix-en-Provence, Angers, Bordeaux, Boulogne-Billancourt, Lyon, Strasbourg
- **Total hours**: 30.00
- **ECTS credits**: 4.00
- **Open to exchange students**: No

## 2 Learning objectives

By the end of this course, you will be able to:

1.  Identify the type and level of measurement of a variable and say which summaries it allows (Module 1).
2.  Build the right frequency table and chart for a qualitative or a quantitative variable, by hand in class and in Excel with `COUNTIFS`, PivotTables and charts (Modules 2–3).
3.  Compute and interpret central tendency, position, dispersion and shape, by hand in class and in Excel at home with `AVERAGE`, `MEDIAN`, `QUARTILE.EXC`, `STDEV.S` and `SKEW` (Modules 4–7).
4.  Build and read a contingency table and a scatter plot for two variables observed together (Module 8).
5.  Compute and interpret covariance, correlation and a simple linear regression line, by hand in class and in Excel at home with `CORREL`, `SLOPE`, `INTERCEPT` and `RSQ` (Module 9).
6.  Run a complete descriptive analysis of a new dataset and explain it to a business audience (Module 10).

## 3 Module outline

The course has **10 modules of 3 hours**. Each module follows the same pattern: a business question; concrete activities on a few numbers you compute by hand, *before* any formula; a notation decoder that reads every formula aloud and links each symbol to those numbers; a worked example on the shared dataset; a short derivation; exercises by hand with collapsible solutions; common mistakes; a short exit check; and an **Excel lab done as homework** at the end of the module page, so class time goes to concepts, notation and practice.

| Part | Module | Hours |
|----|----|---:|
| I. Organising data | 1️⃣ [What is statistics? Data types and measurement](../../teaching/data-description/statistics.llms.md) | 3 |
| I. Organising data | 2️⃣ [Organising qualitative data: frequency tables and charts](../../teaching/data-description/qualitative-data.llms.md) | 3 |
| I. Organising data | 3️⃣ [Organising quantitative data: histograms and cumulative curves](../../teaching/data-description/quantitative-data.llms.md) | 3 |
| II\. Summarising one variable | 4️⃣ [Measures of central tendency](../../teaching/data-description/central-tendancy.llms.md) | 3 |
| II\. Summarising one variable | 5️⃣ [Measures of position: quartiles, percentiles, boxplot](../../teaching/data-description/position.llms.md) | 3 |
| II\. Summarising one variable | 6️⃣ [Measures of dispersion: variance, standard deviation, CV](../../teaching/data-description/dispersion.llms.md) | 3 |
| II\. Summarising one variable | 7️⃣ [Shape of distributions and univariate review](../../teaching/data-description/shape.llms.md) | 3 |
| III\. Two variables and synthesis | 8️⃣ [Bivariate analysis I: contingency tables and scatter plots](../../teaching/data-description/contingency-table.llms.md) | 3 |
| III\. Two variables and synthesis | 9️⃣ [Bivariate analysis II: covariance, correlation, regression](covariance.qmd) | 3 |
| III\. Two variables and synthesis | 1️⃣0️⃣ [Synthesis, review and mock exam](../../teaching/data-description/synthesis.llms.md) | 3 |

## 4 Assessment

| Examination | % of overall grade | Assessment mode | Duration | Covers |
|----|----|----|----|----|
| Midterm Exam (ME) | 35% | Individual written, MCQ component | 45 min | Modules 1–5 |
| Final Exam (FE) | 65% | Individual written, MCQ component | 90 min | Modules 1–10 |

## 5 Personal work

**Volume**: 20 hours. Complete the exercises associated with each part of the course (Organising Data, Summarising One Variable, Two Variables and Synthesis) between modules — every module page’s collapsible exercises are designed for exactly this.

Each module ends with an **Excel homework** (about 50–60 minutes), debriefed during the first 10 minutes of the next module (Module 10’s homework is a self-check against the solutions on the page). That is about 10 of the 20 hours; the rest is by-hand revision with the exercises and exit checks.

## 6 Conventions

Several textbook formulas differ slightly; this course always uses the following (see also the [glossary](../../teaching/data-description/glossary.llms.md)).

| Question | Convention | Excel |
|----|----|----|
| Quartiles and percentiles | Position \\(n+1)\times p\\ with interpolation | `QUARTILE.EXC`, `PERCENTILE.EXC` |
| Variance and standard deviation | Sample formulas (\\n-1\\) by default | `VAR.S`, `STDEV.S` |
| Skewness | Adjusted Fisher–Pearson coefficient | `SKEW` |
| Kurtosis | Conceptual only: no formula | — |
| Excel function names | English locale; French names on the [functions page](modules/excel-functions.qmd) | — |

## 7 Recommended Literature

| Author(s) | Title | Edition | Publisher/Source |
|----|----|----|----|
| Pupion, P.-C. | *Statistiques pour la gestion* | 2004 | Dunod |
| Avenel, M.; Riffault, J.-F. | *Mathématiques appliquées à la gestion* | 2005 | Sup’Foucher |
| Posière, J.-P. | *Mathématiques appliquées à la gestion* | 2005 | Gualino |
| Roger, P. | *Mathématiques pour l’économie et la gestion* | 2006 | Pearson Education |
| Saporta, G. | *Probabilités, Analyse des données et Statistique* | 2006 | Technip |
| Py, B. | *Statistique descriptive* | 2007 | Economica |
| Sydsaeter, K.; Hammond, P. | *Essential Mathematics for Economic Analysis* | 2012 | Pearson |
| Holmes, A.; Illowsky, B.; Dean, S. | *Introductory Business Statistics* | 2nd ed. | OpenStax, Rice University (free online, [openstax.org](https://openstax.org/details/books/introductory-business-statistics-2e)) |
| Khan Academy | *Statistics and Probability* (online course) | Current online version | Khan Academy ([khanacademy.org](https://www.khanacademy.org/math/statistics-probability)) |

*Introductory Business Statistics 2e* is © Rice University and licensed under CC BY-NC-SA 4.0. Each module’s further-reading table names the exact OpenStax sections and Khan Academy units to read.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Data {Description}},
  url = {https://ggilles.dev/teaching/data-description/},
  langid = {en},
  abstract = {**Welcome to MS03-001-G: Data Description.** This course
    introduces the basic statistical tools corresponding to the first
    stage of data analysis: numerical summaries and graphical
    representation of data, computed hands-on in Excel. By the end of
    the course, you will be able to take a raw column of business data
    like sales, weather, customer counts and turn it into frequency
    tables, charts, and summary indicators that support a real business
    decision. A single running case study, **“The Wandering Fork”** (a
    fictional food-truck business), carries every worked example so
    results build on each other across the whole course.}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Data Description.” <https://ggilles.dev/teaching/data-description/>.
