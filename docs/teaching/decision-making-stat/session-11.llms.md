This session introduces the **ANOVA test**, a method used to compare several group means with a single global test.

## 1 Introduction

### 1.1 Introductory example

We want to study the effect of four Merchandising Display systems on sales in stores. A test in one store for five weeks gives the following values (sales in thousands of euros):

| Week | A1 (Gondola) | A2 (Lower Gondola) | A3 (Eye level) | A4 (Stoop level) |
|------|-------------:|-------------------:|---------------:|-----------------:|
| 1    |           87 |                 85 |             98 |               93 |
| 2    |           92 |                 91 |            105 |               96 |
| 3    |           84 |                 88 |            102 |               90 |
| 4    |           90 |                 79 |             96 |               89 |
| 5    |           88 |                 82 |            100 |               94 |

We want to test whether the Merchandising Display system has an impact on sales.

> **NOTE:**
>
> The **ANOVA test** is used to study the link between:
>
> - a **quantitative** variable (for example, sales),
> - a **qualitative** variable (for example, the display system with several modalities).
>
> In practice, ANOVA answers the question: **are all group means equal?**

### 1.2 Why not use multiple t-tests?

With \\4\\ groups, there are \\6\\ pairwise comparisons. If each comparison is performed at the \\5\\\\ level, the probability of accepting \\H_0\\ six times is:

\\ (0.95)^6 \approx 0.735 \\

So the probability of wrongly rejecting at least one null hypothesis becomes:

\\ 1-0.735 \approx 0.265 \\

> **WARNING:**
>
> Multiplying pairwise t-tests inflates the overall Type I error. ANOVA avoids this problem by using **one global test** for all means.

### 1.3 Advantages and limitation

> **TIP:**
>
> - One test is enough.
> - A single significance level \\\alpha\\ is used.
> - All group means are tested simultaneously.

> **WARNING:**
>
> ANOVA tells us **that** at least one mean is different, but not **which** groups differ. Additional post-hoc comparisons are needed for that.

## 2 ANOVA test formulation

### 2.1 Hypotheses

> **NOTE:**
>
> \\ H_0: m_1=m_2=\cdots=m_k \qquad \text{vs.} \qquad H_1:\text{ at least two means are different} \\
>
> Here, \\m_j\\ denotes the unknown theoretical mean of group \\j\\.

### 2.2 Notations

- \\k\\: number of groups,
- \\n_j\\: number of observations in group \\j\\,
- \\n=\sum\_{j=1}^{k} n_j\\: total number of observations,
- \\x\_{i,j}\\: value measured for the \\i\\-th observation in group \\j\\,
- \\\bar{x}\_j=\dfrac{1}{n_j}\sum\_{i=1}^{n_j}x\_{i,j}\\: mean of group \\j\\,
- \\\bar{x}=\dfrac{1}{n}\sum\_{j=1}^{k}\sum\_{i=1}^{n_j}x\_{i,j}\\: overall mean.

> **WARNING:**
>
> The overall mean is **not always equal** to the simple average of the group means. It is a **weighted average** when group sizes are different.

## 3 Variance decomposition

### 3.1 Between-group variability

> **TIP:**
>
> \\ SSD\_{inter}=\sum\_{j=1}^{k} n_j(\bar{x}\_j-\bar{x})^2 \\

### 3.2 Within-group variability

> **TIP:**
>
> \\ SSD\_{intra}=\sum\_{j=1}^{k}\sum\_{i=1}^{n_j}(x\_{i,j}-\bar{x}\_j)^2 =\sum\_{j=1}^{k} n_j s_j^2 \\
>
> where \\s_j^2\\ is the variance inside group \\j\\.

### 3.3 Average squares and test statistic

> **TIP:**
>
> \\ AS\_{inter}=\frac{SSD\_{inter}}{k-1} \qquad \text{and} \qquad AS\_{intra}=\frac{SSD\_{intra}}{n-k} \\
>
> \\ U\_{obs}=\frac{AS\_{inter}}{AS\_{intra}} \\

Under \\H_0\\, the statistic follows a Fisher distribution:

\\ U\_{obs} \sim \mathcal{F}(v_1,v_2) \\

with:

- \\v_1=k-1\\ numerator degrees of freedom,
- \\v_2=n-k\\ denominator degrees of freedom.

### 3.4 Decision rule

> **TIP:**
>
> Reject \\H_0\\ at risk \\\alpha\\ if:
>
> \\ U\_{obs}\>f \\
>
> where \\f=F\_{\alpha}(v_1,v_2)\\ is the critical value read in the Fisher table.

> **IMPORTANT:**
>
> For every ANOVA exercise, use the same five-step method:
>
> 1.  identify \\k\\, the \\n_j\\, and the hypotheses,
> 2.  compute the group means and the overall mean,
> 3.  compute \\SSD\_{inter}\\ and \\SSD\_{intra}\\,
> 4.  compute \\U\_{obs}\\ and the critical value,
> 5.  conclude in words.

## 4 Conclusion

- **\\H_0\\ rejected**: the data confirm that all means are not equal, so there is a link between the variables.
- **\\H_0\\ not rejected**: the data do not confirm a difference between the means at the chosen risk level.

## 5 Application exercise

### 5.1 ANOVA on academic performance by baccalauréat type

> **CAUTION:**
>
> A data analyst at a French business school wants to determine whether academic performance of first-year students depends on their baccalauréat type (Bac ES, Bac S, or Bac STG).
>
> He observes 18 first-year students: 7 from Bac ES, 6 from Bac S, and 5 from Bac STG. Performance is measured by the average grade across all subjects.
>
> | Bac ES | Bac S | Bac STG |
> |-------:|------:|--------:|
> |   12.5 |  15.0 |    11.0 |
> |   10.5 |  13.5 |     9.5 |
> |   11.0 |  14.0 |    12.0 |
> |   13.0 |  12.5 |    10.5 |
> |   11.5 |  15.5 |     8.5 |
> |   12.0 |  13.0 |         |
> |   10.0 |       |         |
>
> Can we say, with a \\5\\\\ risk, that the type of baccalauréat does not have the same effect on academic performance?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\k=3\\
> - \\n_1=7\\, \\n_2=6\\, \\n_3=5\\, hence \\n=18\\
> - \\H_0: m_1=m_2=m_3\\
> - \\H_1\\: at least two means are different
>
> **Step 2 — Group means and overall mean**
>
> \\ \bar{x}\_1=\frac{80.5}{7}=11.5, \qquad \bar{x}\_2=\frac{83.5}{6}\approx 13.917, \qquad \bar{x}\_3=\frac{51.5}{5}=10.3 \\
>
> \\ \bar{x}=\frac{80.5+83.5+51.5}{18}=\frac{215.5}{18}\approx 11.972 \\
>
> **Step 3 — Between-group variability**
>
> \\ SSD\_{inter}=7(11.5-11.972)^2+6(13.917-11.972)^2+5(10.3-11.972)^2\approx 38.228 \\
>
> So:
>
> \\ AS\_{inter}=\frac{38.228}{3-1}\approx 19.114 \\
>
> **Step 4 — Within-group variability**
>
> The within-group variances are approximately:
>
> \\ s_1^2=1.000, \qquad s_2^2\approx 1.118, \qquad s_3^2=1.460 \\
>
> Hence:
>
> \\ SSD\_{intra}=7\times 1.000+6\times 1.118+5\times 1.460\approx 21.008 \\
>
> and:
>
> \\ AS\_{intra}=\frac{21.008}{18-3}=\frac{21.008}{15}\approx 1.401 \\
>
> **Step 5 — Test statistic**
>
> \\ U\_{obs}=\frac{19.114}{1.401}\approx 13.647 \\
>
> At the \\5\\\\ level, with \\v_1=2\\ and \\v_2=15\\:
>
> \\ f=F\_{5\\}(2,15)\approx 3.68 \\
>
> Since:
>
> \\ 13.647\>3.68 \\
>
> we reject \\H_0\\.
>
> **Conclusion:** with a \\5\\\\ risk, the data confirm that the type of baccalauréat has an influence on academic performance.
>
> > **WARNING:**
> >
> > This result tells us that **at least one** mean is different. It does not tell us exactly **which** pairs of groups differ.

### 5.2 Exercise 2 — Effect of training method on exam scores

> **CAUTION:**
>
> A training manager tests three teaching methods (A: traditional classroom, B: online self-paced, C: blended learning) on groups of employees. The exam scores (out of 20) are:
>
> | Traditional (A) | Online (B) | Blended (C) |
> |----------------:|-----------:|------------:|
> |              12 |         15 |          14 |
> |              10 |         14 |          16 |
> |              11 |         16 |          15 |
> |              13 |         13 |          17 |
> |              12 |         15 |          14 |
> |              11 |            |          16 |
>
> Can we say, with a \\5\\\\ risk, that the teaching method has an influence on exam scores?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\k=3\\
> - \\n_1=6\\, \\n_2=5\\, \\n_3=6\\, hence \\n=17\\
> - \\H_0: m_1=m_2=m_3\\
> - \\H_1\\: at least two means are different
>
> **Step 2 — Group means and overall mean**
>
> \\ \bar{x}\_1=\frac{69}{6}=11.5, \qquad \bar{x}\_2=\frac{73}{5}=14.6, \qquad \bar{x}\_3=\frac{92}{6}\approx 15.333 \\
>
> \\ \bar{x}=\frac{69+73+92}{17}=\frac{234}{17}\approx 13.765 \\
>
> **Step 3 — Between-group variability**
>
> \\ SSD\_{inter}=6(11.5-13.765)^2+5(14.6-13.765)^2+6(15.333-13.765)^2 \\
>
> \\ \approx 6\times 5.130+5\times 0.697+6\times 2.459 = 30.78+3.49+14.75\approx 49.02 \\
>
> \\ AS\_{inter}=\frac{49.02}{3-1}\approx 24.51 \\
>
> **Step 4 — Within-group variability**
>
> Within-group variances:
>
> \\ s_1^2=\frac{5.50}{6}\approx 0.917, \qquad s_2^2=\frac{5.20}{5}=1.040, \qquad s_3^2=\frac{7.33}{6}\approx 1.222 \\
>
> \\ SSD\_{intra}=6\times 0.917+5\times 1.040+6\times 1.222\approx 5.50+5.20+7.33=18.03 \\
>
> \\ AS\_{intra}=\frac{18.03}{17-3}=\frac{18.03}{14}\approx 1.288 \\
>
> **Step 5 — Test statistic**
>
> \\ U\_{obs}=\frac{24.51}{1.288}\approx 19.03 \\
>
> At the \\5\\\\ level, with \\v_1=2\\ and \\v_2=14\\:
>
> \\ f=F\_{5\\}(2,14)\approx 3.74 \\
>
> Since \\19.03\>3.74\\, we reject \\H_0\\.
>
> **Conclusion:** with a \\5\\\\ risk, the teaching method has a significant influence on exam scores. The blended method seems to achieve the highest average (\\\approx 15.3\\), while the traditional classroom method gives the lowest (\\11.5\\).

### 5.3 Exercise 3 — Effect of fertiliser type on crop yield

> **CAUTION:**
>
> An agronomist tests four types of fertiliser (A, B, C, D) on plots of identical size. The yield (in kg) measured over five plots per fertiliser is:
>
> | Fert. A | Fert. B | Fert. C | Fert. D |
> |--------:|--------:|--------:|--------:|
> |      22 |      28 |      31 |      25 |
> |      25 |      30 |      29 |      23 |
> |      20 |      27 |      32 |      26 |
> |      23 |      31 |      30 |      24 |
> |      25 |      29 |      28 |      27 |
>
> Can we say, with a \\5\\\\ risk, that the type of fertiliser affects yield? And at a \\1\\\\ risk?

> **CAUTION:**
>
> **Step 1 — Formulation**
>
> - \\k=4\\, \\n_j=5\\ for all groups, \\n=20\\
> - \\H_0: m_A=m_B=m_C=m_D\\
> - \\H_1\\: at least two means are different
>
> **Step 2 — Group means and overall mean**
>
> \\ \bar{x}\_A=\frac{115}{5}=23, \quad \bar{x}\_B=\frac{145}{5}=29, \quad \bar{x}\_C=\frac{150}{5}=30, \quad \bar{x}\_D=\frac{125}{5}=25 \\
>
> \\ \bar{x}=\frac{115+145+150+125}{20}=\frac{535}{20}=26.75 \\
>
> **Step 3 — Between-group variability**
>
> \\ SSD\_{inter}=5(23-26.75)^2+5(29-26.75)^2+5(30-26.75)^2+5(25-26.75)^2 \\
>
> \\ =5\times 14.0625+5\times 5.0625+5\times 10.5625+5\times 3.0625=163.75 \\
>
> \\ AS\_{inter}=\frac{163.75}{4-1}\approx 54.583 \\
>
> **Step 4 — Within-group variability**
>
> Within-group variances:
>
> \\ s_A^2=\frac{18}{5}=3.60, \quad s_B^2=\frac{10}{5}=2.00, \quad s_C^2=\frac{10}{5}=2.00, \quad s_D^2=\frac{10}{5}=2.00 \\
>
> \\ SSD\_{intra}=5\times 3.60+5\times 2.00+5\times 2.00+5\times 2.00=18+10+10+10=48 \\
>
> \\ AS\_{intra}=\frac{48}{20-4}=\frac{48}{16}=3.00 \\
>
> **Step 5 — Test statistic**
>
> \\ U\_{obs}=\frac{54.583}{3.00}\approx 18.19 \\
>
> With \\v_1=3\\ and \\v_2=16\\:
>
> \\ F\_{5\\}(3,16)\approx 3.24 \qquad \text{and} \qquad F\_{1\\}(3,16)\approx 5.29 \\
>
> Since \\18.19\>3.24\\ and \\18.19\>5.29\\, we **reject** \\H_0\\ at both risk levels.
>
> **Conclusion:** the type of fertiliser has a highly significant effect on yield. Fertilisers B and C produce the highest average yields (\\29\\ and \\30\\ kg respectively) compared to A (\\23\\ kg) and D (\\25\\ kg).
