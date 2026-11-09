This session is a **computer lab** devoted to applying the advanced statistical tests from Sessions 11–13 in Excel.

## 1 Session goals

> **NOTE:**
>
> By the end of this practical session, you should be able to:
>
> - perform and interpret an **ANOVA test**,
> - perform and interpret a **Chi-square test of independence**,
> - perform and interpret a **test on the linear correlation coefficient**,
> - use Excel tools and functions to automate the decision process.

> **WARNING:**
>
> Review **Sessions 11–13** and the appendices below before completing the Excel workbooks.

## 2 Exercise 1 — ANOVA (based on Session 11)

### 2.1 Context

The following table shows measurements of the height (in mm) of a fern, taken in several different environments in France on randomly sampled specimens.

| Env 1 | Env 2 | Env 3 | Env 4 | Env 5 |
|------:|------:|------:|------:|------:|
|   112 |   141 |   156 |   187 |   241 |
|   115 |   146 |   167 |   105 |   264 |
|   112 |   135 |   143 |   179 |   225 |
|   118 |   147 |   178 |   123 |   257 |
|   124 |   154 |   145 |   114 |   248 |
|   132 |       |   169 |       |   258 |
|   131 |       |       |       |   136 |
|   115 |       |       |       |       |

A researcher wants to know whether the environment has an influence on plant size.

> **CAUTION:**
>
> **Mission 1.1** — After reading Session 11, Appendix 1, and using the Fisher table, complete Tables 1, 2, 3, and 4 of `PW - Session 14 - Exercise1.xlsx`.
>
> Goal: **perform and interpret an ANOVA test**.
>
> To go further:
>
> - use `VLOOKUP` to determine the critical value \\f\\,
> - use `IF` to automate the conclusion,
> - or use **Data** \\\rightarrow\\ **Data Analysis** \\\rightarrow\\ **Anova: Single Factor**.

> **CAUTION:**
>
> Use the following workflow:
>
> 1.  compute the group sizes \\n_j\\, group means \\\bar{x}\_j\\, and the overall mean \\\bar{x}\\,
> 2.  compute \\SSD\_{inter}\\ and \\SSD\_{intra}\\,
> 3.  compute
>
> \\ U\_{obs}=\frac{AS\_{inter}}{AS\_{intra}} \\
>
> 4.  read the Fisher critical value with the appropriate degrees of freedom,
> 5.  conclude with an Excel formula such as `IF(Uobs>f,"Reject H0","Do not reject H0")`.

## 3 Exercise 2 — Chi-square test (based on Session 12)

### 3.1 Context

In the early 1970s, the association *Prévention Routière* wanted to encourage the French population to wear seat belts. To study the link between injury severity and seat belt use, a random sample of 10,779 drivers involved in an accident yielded:

| Nature of injury    | Seat belt: YES | Seat belt: NO |
|---------------------|---------------:|--------------:|
| Severe or fatal     |              5 |           141 |
| Serious             |             25 |           330 |
| No or little injury |          1,229 |         9,049 |

> **CAUTION:**
>
> Can we say, with a \\5\\\\ risk, that there is a link between seat belt use and the nature of the injury? In other words, is the seat belt effective?
>
> **Mission 2.1** — From the `0 - Data` tab of `PW - Session 14 - Exercise2.xlsx`, create a pivot table to recreate the contingency table.
>
> **Mission 2.2** — Recreate the contingency table needed to perform the Chi-square test.
>
> **Mission 2.3** — Complete Tables 3, 4, 5, and 6 in the `2 - KHI-SQUARE Test` sheet.
>
> Goal: **perform and interpret a Chi-square test**.
>
> To go further:
>
> - use `VLOOKUP` to determine the critical value \\k\\,
> - use `IF` to automate the decision,
> - or use `CHISQ.TEST` and `CHISQ.INV` directly.

> **CAUTION:**
>
> Method to follow:
>
> 1.  compute the observed contingency table,
> 2.  compute row totals, column totals, and the grand total,
> 3.  compute the expected counts with
>
> \\ E\_{i,j}=\frac{n\_{i,.}\times n\_{.,j}}{n} \\
>
> 4.  verify that all expected counts are at least \\5\\,
> 5.  compute the Chi-square statistic,
> 6.  compare it with the critical value or use the p-value returned by `CHISQ.TEST`.

## 4 Exercise 3 — Linear correlation test (based on Session 13)

### 4.1 Context

Let \\X\\ be the net salary of women and \\Y\\ the net salary of men in the same household. It is assumed that \\(X,Y)\\ follows a bivariate Normal distribution. The two variables are studied on \\15\\ households.

> **CAUTION:**
>
> At the \\5\\\\ risk level, can we say that there is a link between salaries and gender?
>
> **Mission** — After reading Session 13 and Appendix 1, complete Tables 2, 3, and 4 of `PW - Session 14 - Exercise3.xlsx`.
>
> Goal: **perform and interpret a test on the linear correlation coefficient**.
>
> To go further:
>
> - use `IF` to automate the conclusion,
> - use `TINV(\alpha, n-2)` to determine \\t\\,
> - here \\\alpha=5\\\\ and \\n-2=13\\.

> **CAUTION:**
>
> Suggested method:
>
> 1.  compute \\\bar{x}\\, \\\bar{y}\\, \\s_x\\, \\s_y\\, and the covariance,
> 2.  compute the empirical correlation coefficient \\r\\,
> 3.  calculate
>
> \\ U\_{obs}=r\sqrt{\frac{n-2}{1-r^2}} \\
>
> 4.  compare \\\|U\_{obs}\|\\ with the Student critical value,
> 5.  conclude with a sentence about the existence, sign, and strength of the linear relationship.

## 5 Appendix 1 — Standard Excel functions

| Function                             | Description           |
|--------------------------------------|-----------------------|
| `SUM(range)`                         | Sum of values         |
| `AVERAGE(range)`                     | Arithmetic mean       |
| `COUNT(range)`                       | Count numeric entries |
| `IF(condition, val_true, val_false)` | Conditional logic     |

## 6 Appendix 2 — VLOOKUP function

> **NOTE:**
>
> `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`

Used to search for a value in the first column of a table and return a value from a specified column. A typical use here is to look up **critical values** in a statistical table.

> **TIP:**
>
> Set the fourth argument to `FALSE` to request an exact match.

## 7 Appendix 3 — Pivot tables

> **NOTE:**
>
> A **pivot table** is a tool for summarizing and analyzing data quickly.

Access it through:

**Insert** \\\rightarrow\\ **Tables** \\\rightarrow\\ **PivotTable**

> **IMPORTANT:**
>
> To create a contingency table from raw data, place one variable in the **rows**, the other in the **columns**, and the **count** in the values area.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Session 14 — {Practical} {Work:} {ANOVA,} {Chi-Square} \&
    {Correlation} in {Excel}},
  url = {https://ggilles.dev/teaching/decision-making-stat/session-14.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Session 14 — Practical Work: ANOVA, Chi-Square & Correlation in Excel.” <https://ggilles.dev/teaching/decision-making-stat/session-14.html>.
