This session presents the **Chi-square test of independence**, used to study whether two characteristics are linked.

## 1 Introduction

### 1.1 Typical business and social science questions

The Chi-square test helps answer questions such as:

- Does the time spent on social networks depend on the user’s gender?
- Is the effect of a treatment independent of the dose administered?
- Is there a link between hair color and eye color?
- Is there a link between marital status and job type?

> **NOTE:**
>
> The **Chi-square test** is used to check whether a link exists between two characteristics:
>
> - when both characteristics are **qualitative**,
> - when one is qualitative and the other is quantitative but grouped into classes,
> - when both are quantitative but grouped into classes.

## 2 Chi-square test formulation

### 2.1 Setup

- Variable \\X\\ has \\p\\ modalities: \\A_1,A_2,\ldots,A_p\\
- Variable \\Y\\ has \\q\\ modalities: \\B_1,B_2,\ldots,B_q\\
- A sample of size \\n\\ is organized into a **contingency table** of dimension \\p \times q\\

### 2.2 Hypotheses

> **NOTE:**
>
> \\ H_0: X \text{ and } Y \text{ are independent} \qquad \text{vs.} \qquad H_1: X \text{ and } Y \text{ are dependent} \\

### 2.3 Notations for the contingency table

- \\n\_{i,j}\\: number of individuals simultaneously in category \\A_i\\ and category \\B_j\\,
- \\n\_{i,.}=\sum\_{j=1}^{q} n\_{i,j}\\: row total of row \\i\\,
- \\n\_{.,j}=\sum\_{i=1}^{p} n\_{i,j}\\: column total of column \\j\\,
- \\n=\sum\_{i=1}^{p}\sum\_{j=1}^{q} n\_{i,j}\\: grand total.

## 3 Expected counts and test statistic

### 3.1 Expected counts under independence

> **TIP:**
>
> If \\H_0\\ is true, the theoretical count in cell \\(i,j)\\ is:
>
> \\ E\_{i,j}=\frac{n\_{i,.}\times n\_{.,j}}{n} \\

> **WARNING:**
>
> The standard Chi-square test is considered valid when all expected counts satisfy:
>
> \\ E\_{i,j} \geq 5 \\
>
> If this condition is not met, some categories may need to be grouped.

### 3.2 Test statistic

> **TIP:**
>
> \\ U\_{obs}=\sum\_{i=1}^{p}\sum\_{j=1}^{q}\frac{(n\_{i,j}-E\_{i,j})^2}{E\_{i,j}} \\

Under \\H_0\\, the statistic follows approximately a Chi-square distribution with:

\\ \nu=(p-1)(q-1) \\

degrees of freedom.

### 3.3 Decision rule

> **TIP:**
>
> Reject \\H_0\\ at risk \\\alpha\\ if:
>
> \\ U\_{obs}\>k \\
>
> where \\k=\chi^2\_{\alpha}(\nu)\\ is the critical value read in the Chi-square table.

> **IMPORTANT:**
>
> In a Chi-square exercise, always proceed in this order:
>
> 1.  identify the two variables and their numbers of categories,
> 2.  compute row totals, column totals, and the grand total,
> 3.  compute the expected counts,
> 4.  check the validity condition,
> 5.  compute \\U\_{obs}\\ and compare it with the critical value.

## 4 Conclusion

- **\\H_0\\ rejected**: the data confirm a **link** between the two variables.
- **\\H_0\\ not rejected**: the data do not confirm a link at the chosen risk level.

## 5 Application exercise

### 5.1 Coffee consumption and marital status

> **CAUTION:**
>
> A marketing company selected a random sample of housewives (women under 50, assumed to be the main shopper in the household) to study the link between marital status and weekly coffee consumption.
>
> |  | Less than 1 cup/day | 1–2 cups/day | 2–3 cups/day | More than 3 cups/day |
> |----|---:|---:|---:|---:|
> | **Single** | 30 | 40 | 50 | 20 |
> | **Married** | 50 | 60 | 80 | 30 |
> | **Other** | 20 | 30 | 40 | 15 |
>
> Can we say, with a \\5\\\\ risk, that there is a link between coffee consumption level and marital status?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\X\\ = marital status, so \\p=3\\
> - \\Y\\ = coffee consumption level, so \\q=4\\
> - \\H_0\\: independence
> - \\H_1\\: dependence
>
> **Step 2 — Marginal totals**
>
> Row totals:
>
> \\ 140,\quad 220,\quad 105 \\
>
> Column totals:
>
> \\ 100,\quad 130,\quad 170,\quad 65 \\
>
> Grand total:
>
> \\ n=465 \\
>
> **Step 3 — Expected counts**
>
> Using
>
> \\ E\_{i,j}=\frac{n\_{i,.}n\_{.,j}}{n} \\
>
> we obtain approximately:
>
> |             | Less than 1 |    1–2 |    2–3 | More than 3 |
> |-------------|------------:|-------:|-------:|------------:|
> | **Single**  |      30.108 | 39.140 | 51.183 |      19.570 |
> | **Married** |      47.312 | 61.505 | 80.430 |      30.753 |
> | **Other**   |      22.581 | 29.355 | 38.387 |      14.677 |
>
> All expected counts are greater than \\5\\, so the test is valid.
>
> **Step 4 — Computed statistic**
>
> \\ U\_{obs}=\sum \frac{(n\_{i,j}-E\_{i,j})^2}{E\_{i,j}} \approx 0.650 \\
>
> **Step 5 — Critical value**
>
> The number of degrees of freedom is:
>
> \\ \nu=(3-1)(4-1)=6 \\
>
> At the \\5\\\\ level:
>
> \\ k=\chi^2\_{5\\}(6)=12.592 \\
>
> Since:
>
> \\ 0.650\<12.592 \\
>
> we do **not** reject \\H_0\\.
>
> **Conclusion:** with the counts given in the table above, the data do **not** confirm a link between coffee consumption level and marital status at the \\5\\\\ risk level.

### 5.2 Exercise 2 — Purchase frequency by age group

> **CAUTION:**
>
> A retail chain surveys a random sample of \\300\\ loyalty-card holders to study the link between age group and purchase frequency:
>
> |                 | Never | Occasionally | Regularly |
> |-----------------|------:|-------------:|----------:|
> | **Under 35**    |    30 |           50 |        70 |
> | **35 and over** |    45 |           60 |        45 |
>
> Can we say, with a \\5\\\\ risk, that there is a link between age group and purchase frequency? And at a \\1\\\\ risk?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\X\\ = age group, so \\p=2\\
> - \\Y\\ = purchase frequency, so \\q=3\\
> - \\H_0\\: independence
> - \\H_1\\: dependence
> - \\\nu=(2-1)(3-1)=2\\
>
> **Step 2 — Marginal totals**
>
> Row totals: \\150\\, \\150\\. Column totals: \\75\\, \\110\\, \\115\\. Grand total: \\n=300\\.
>
> **Step 3 — Expected counts**
>
> Since both row totals equal \\150\\, each expected count equals \\n\_{i,.}\times n\_{.,j}/300 = 150\times n\_{.,j}/300 = n\_{.,j}/2\\:
>
> |                 | Never | Occasionally | Regularly |
> |-----------------|------:|-------------:|----------:|
> | **Under 35**    |  37.5 |         55.0 |      57.5 |
> | **35 and over** |  37.5 |         55.0 |      57.5 |
>
> All expected counts are \\\geq 5\\ ✓.
>
> **Step 4 — Computed statistic**
>
> \\ U\_{obs}=\frac{(30-37.5)^2}{37.5}+\frac{(50-55)^2}{55}+\frac{(70-57.5)^2}{57.5}+\frac{(45-37.5)^2}{37.5}+\frac{(60-55)^2}{55}+\frac{(45-57.5)^2}{57.5} \\
>
> \\ =1.500+0.455+2.717+1.500+0.455+2.717\approx 9.344 \\
>
> **Step 5 — Critical values**
>
> \\ \chi^2\_{5\\}(2)=5.991 \qquad \text{and} \qquad \chi^2\_{1\\}(2)=9.210 \\
>
> Since \\9.344\>5.991\\ and \\9.344\>9.210\\, we **reject** \\H_0\\ at both risk levels.
>
> **Conclusion:** with both \\5\\\\ and \\1\\\\ risk, the data confirm a **link between age group and purchase frequency**. Customers under 35 tend to purchase more regularly, whereas older customers purchase less frequently.

### 5.3 Exercise 3 — Education level and job satisfaction

> **CAUTION:**
>
> An HR consultancy surveys \\245\\ randomly selected employees to study the link between education level and job satisfaction:
>
> |                     | Low satisfaction | Medium satisfaction | High satisfaction |
> |---------------------|-----------------:|--------------------:|------------------:|
> | **No degree**       |               25 |                  30 |                10 |
> | **Bachelor**        |               15 |                  45 |                40 |
> | **Master or above** |                5 |                  20 |                55 |
>
> Can we say, with a \\5\\\\ risk, that education level and job satisfaction are linked?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\X\\ = education level (\\p=3\\), \\Y\\ = satisfaction level (\\q=3\\)
> - \\H_0\\: independence, \\H_1\\: dependence
> - \\\nu=(3-1)(3-1)=4\\
>
> **Step 2 — Marginal totals**
>
> Row totals: \\65\\, \\100\\, \\80\\. Column totals: \\45\\, \\95\\, \\105\\. Grand total: \\n=245\\.
>
> **Step 3 — Expected counts**
>
> \\ E\_{i,j}=\frac{n\_{i,.}\times n\_{.,j}}{245} \\
>
> |               |   Low | Medium |  High |
> |---------------|------:|-------:|------:|
> | **No degree** | 11.94 |  25.20 | 27.86 |
> | **Bachelor**  | 18.37 |  38.78 | 42.86 |
> | **Master+**   | 14.69 |  31.02 | 34.29 |
>
> All expected counts are \\\geq 5\\ ✓.
>
> **Step 4 — Computed statistic**
>
> \\ U\_{obs}=\frac{(25-11.94)^2}{11.94}+\frac{(30-25.20)^2}{25.20}+\frac{(10-27.86)^2}{27.86} +\frac{(15-18.37)^2}{18.37}+\frac{(45-38.78)^2}{38.78}+\frac{(40-42.86)^2}{42.86} \\
>
> \\ +\frac{(5-14.69)^2}{14.69}+\frac{(20-31.02)^2}{31.02}+\frac{(55-34.29)^2}{34.29} \\
>
> \\ \approx 14.29+0.91+11.45+0.62+1.00+0.19+6.40+3.91+12.51\approx 51.28 \\
>
> **Step 5 — Critical value**
>
> \\ \chi^2\_{5\\}(4)=9.488 \\
>
> Since \\51.28\>9.488\\, we **reject** \\H_0\\.
>
> **Conclusion:** with a \\5\\\\ risk, the data confirm a **strong link between education level and job satisfaction**. Higher-educated employees report noticeably higher satisfaction levels.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Session 12 — {Chi-Square} {Test}},
  url = {https://ggilles.dev/teaching/decision-making-stat/session-12.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Session 12 — Chi-Square Test.” <https://ggilles.dev/teaching/decision-making-stat/session-12.html>.
