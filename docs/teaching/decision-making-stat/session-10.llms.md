This session is a **computer lab** devoted to applying the inferential tools studied in Sessions 06–09 directly in Excel.

## 1 Session goals

> **NOTE:**
>
> After this practical session, you should be able to:
>
> 1.  carry out calculations with the centred reduced normal distribution,
> 2.  calculate and interpret a confidence interval for an unknown mean or proportion,
> 3.  formulate, process, and interpret a conformity test of an unknown mean or proportion against a reference value,
> 4.  formulate, process, and interpret a comparison test between two means or two proportions.

> **WARNING:**
>
> After carefully reading **Sessions 06–09** and **Appendixes 1–4** below, complete the exercises in the following Excel files:
>
> - `PW 10 - CI.xlsx` — Confidence intervals
> - `PW 10 - Conformity.xlsx` — Conformity tests
> - `PW 10 - Comparison.xlsx` — Comparison tests

## 2 Mission roadmap

### 2.1 Workbook 1 — Confidence intervals

> **CAUTION:**
>
> Open `PW 10 - CI.xlsx` and, for each question:
>
> 1.  identify the parameter to estimate (\\\mu\\ or \\p\\),
> 2.  compute the sample quantities needed,
> 3.  determine the critical quantile,
> 4.  calculate the confidence interval,
> 5.  interpret the interval in context.

### 2.2 Workbook 2 — Conformity tests

> **CAUTION:**
>
> Open `PW 10 - Conformity.xlsx` and, for each test:
>
> 1.  write the null and alternative hypotheses,
> 2.  identify whether the test is left-tailed, right-tailed, or two-tailed,
> 3.  compute the observed statistic \\U\_{obs}\\,
> 4.  compare it with the critical value,
> 5.  conclude in words at the chosen significance level.

### 2.3 Workbook 3 — Comparison tests

> **CAUTION:**
>
> Open `PW 10 - Comparison.xlsx` and, for each comparison:
>
> 1.  identify the two populations or subpopulations,
> 2.  determine whether you are comparing **means** or **proportions**,
> 3.  compute the appropriate test statistic,
> 4.  state the rejection rule,
> 5.  conclude on the existence and direction of the difference.

## 3 Quick methodological reminders

### 3.1 Confidence intervals

> **TIP:**
>
> For a large sample and an unknown mean:
>
> \\ IC\_{1-\alpha}(m)=\left\[\bar{x}-z\_{\alpha/2}\frac{s}{\sqrt{n}},\\\bar{x}+z\_{\alpha/2}\frac{s}{\sqrt{n}}\right\] \\
>
> For an unknown proportion:
>
> \\ IC\_{1-\alpha}(p)=\left\[\hat{p}-z\_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}},\\\hat{p}+z\_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\right\] \\

### 3.2 Hypothesis tests

> **TIP:**
>
> Conformity test for a mean:
>
> \\ U\_{obs}=\frac{\bar{x}-\mu_0}{s/\sqrt{n}} \\
>
> Conformity test for a proportion:
>
> \\ U\_{obs}=\frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} \\
>
> Comparison test between two means:
>
> \\ U\_{obs}=\frac{\bar{x}\_1-\bar{x}\_2}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}} \\
>
> Comparison test between two proportions:
>
> \\ U\_{obs}=\frac{\hat{p}\_1-\hat{p}\_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}} \\

> **IMPORTANT:**
>
> In every Excel exercise, keep the same structure:
>
> 1.  **identify** the parameter,
> 2.  **write** \\H_0\\ and \\H_1\\ when there is a test,
> 3.  **compute** the statistic or the interval,
> 4.  **interpret** the result in a full sentence.

## 4 Appendix 1 — The centred reduced normal distribution in Excel

### 4.1 Reminder

> **NOTE:**
>
> Let \\X \sim \mathcal{N}(\mu, \sigma^2)\\ and let \\a\\ be a fixed real number. Computing \\P(X \leq a)\\ is equivalent to determining the area under the density curve to the left of \\a\\.

We saw in class that a table of the distribution function of \\\mathcal{N}(0,1)\\ allows these computations.

### 4.2 Inverse problem

Suppose the probability \\p\\ is known but the quantile \\z\\ is unknown. We seek \\z\\ such that:

\\ P(Z \leq z)=p \\

> **TIP:**
>
> - To obtain a cumulative probability from a standardized value, use `NORM.S.DIST(z, TRUE)`.
> - To obtain the quantile associated with a probability \\p\\, use `NORM.S.INV(p)`.

For example, if \\p=0.975\\, then `NORM.S.INV(0.975)` returns approximately \\z=1.96\\.

## 5 Appendix 2 — Standard functions in Excel

| Function | Description | Example |
|----|----|----|
| `SUM(range)` | Sum of values | `SUM(A1:A5)` |
| `AVERAGE(range)` | Arithmetic mean | `AVERAGE(A1:A5)` |
| `COUNT(range)` | Count numeric values | `COUNT(A1:A5)` |
| `COUNTA(range)` | Count non-empty cells | `COUNTA(A1:A5)` |
| `IF(condition, val_true, val_false)` | Logical test | `IF(C2="Yes",1,2)` |
| `COUNTIF(range, criteria)` | Count cells matching criteria | `COUNTIF(A1:A5,">3")` |
| `SUMSQ(range)` | Sum of squares | `SUMSQ(A1:A5)` |
| `SQRT(number)` | Square root | `SQRT(25)` = 5 |
| `SUMPRODUCT(range1, range2)` | Sum of products | `SUMPRODUCT(A1:A5,B1:B5)` |

## 6 Appendix 3 — Variance and adjusted variance

> **NOTE:**
>
> In Anglo-Saxon literature, one often uses the **adjusted** or **corrected** variance:
>
> \\ s^2=\frac{1}{n-1}\sum\_{i=1}^{n}(x_i-\bar{x})^2 \\
>
> This differs from the variance presented in class:
>
> \\ \sigma^2=\frac{1}{n}\sum\_{i=1}^{n}(x_i-\bar{x})^2 \\

> **TIP:**
>
> \\ s^2=\frac{n}{n-1}\cdot \sigma^2 \\
>
> When \\n\\ is large, \\s^2 \approx \sigma^2\\.

## 7 Appendix 4 — Standard deviation and adjusted standard deviation

> **NOTE:**
>
> The adjusted standard deviation is:
>
> \\ s=\sqrt{s^2}=\sqrt{\frac{1}{n-1}\sum\_{i=1}^{n}(x_i-\bar{x})^2} \\

> **WARNING:**
>
> When the sample size is large, the adjusted standard deviation \\s\\ is very close to the standard deviation \\\sigma\\ seen in descriptive statistics.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Session 10 — {Practical} {Work:} {Statistical} {Inference} in
    {Excel}},
  url = {https://ggilles.dev/teaching/decision-making-stat/session-10.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Session 10 — Practical Work: Statistical Inference in Excel.” <https://ggilles.dev/teaching/decision-making-stat/session-10.html>.
