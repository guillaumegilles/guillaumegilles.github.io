This session is a **computer lab**. Students reuse the tools from Sessions 1 to 4 in Excel; **no new theory** is introduced.

## 1 Session goals

> **WARNING:**
>
> The objective is to **apply** previously studied formulas, not to introduce new notions. Before opening the Excel files, review the lecture notes from Sessions 1, 3, and 4.

By the end of the session, you should be able to:

- choose the correct Excel function for a combinatorial or probabilistic calculation,
- distinguish exact probabilities from cumulative probabilities,
- compare exact binomial values with Poisson and Normal approximations,
- interpret numerical outputs in a business context.

> **IMPORTANT:**
>
> Even in Excel, the first step is always the same: **identify the model** before entering a formula.

## 2 Exercise 1 — Combinatorial Analysis

### 2.1 Context and mission

Review the context of the application exercise in **Session 1**. Then open the file `PW - Session 05 - Exercise1.xlsx`.

> **TIP:**
>
> For combinatorial analysis:
>
> \\ P_n = n! \\
>
> \\ A_n^k = \frac{n!}{(n-k)!} \\
>
> \\ C_n^k = \binom{n}{k} = \frac{n!}{k!(n-k)!} \\

> **CAUTION:**
>
> After reading the Session 1 lecture and Appendix 1, complete the following tables in `PW - Session 05 - Exercise1.xlsx`:
>
> - **Table 1:** compute permutations \\P_n = n!\\ for the proposed values of \\n\\.
> - **Table 2:** compute arrangements \\A_n^k\\ for the proposed pairs \\(n,k)\\.
> - **Table 3:** compute combinations \\C_n^k\\ for the proposed pairs \\(n,k)\\.
>
> **Goal:** perform and interpret the formulas of combinatorial analysis in Excel.
>
> **To go further:** complete **Table 4** and produce the graph of \\C(n,k)\\ as a function of \\k\\ for a fixed value of \\n\\.

> **CAUTION:**
>
> A practical Excel strategy is:
>
> - for permutations: `=FACT(n)` or `=PERMUT(n,n)`;
> - for arrangements: `=PERMUT(n,k)`;
> - for combinations: `=COMBIN(n,k)`.
>
> Example with cell references:
>
> - Table 1: `=FACT(B2)`
> - Table 2: `=PERMUT(B2,C2)`
> - Table 3: `=COMBIN(B2,C2)`
>
> Interpretation reminders:
>
> - permutations count **all possible orderings** of \\n\\ objects;
> - arrangements count **ordered selections** of \\k\\ objects among \\n\\;
> - combinations count **unordered selections** of \\k\\ objects among \\n\\.

## 3 Exercise 2 — Discrete Random Variables

### 3.1 Context and mission

Review the context of the application exercise in **Session 3**. Then open the file `PW - Session 05 - Exercise2.xlsx`.

### 3.2 Binomial and Poisson calculations

> **TIP:**
>
> For a binomial random variable \\X \sim B(n,p)\\:
>
> \\ P(X=k) = \binom{n}{k}p^k(1-p)^{n-k} \\
>
> For a Poisson random variable \\X \sim \mathcal{P}(\lambda)\\:
>
> \\ P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!} \\
>
> For cumulative probabilities, compute \\P(X \leq k)\\.

> **CAUTION:**
>
> After reading the Session 3 lecture and Appendices 2 and 3, complete Tables 1, 2, 3.1, 3.2, and 3.3 of `PW - Session 05 - Exercise2.xlsx`:
>
> - **Table 1:** Binomial distribution — compute \\P(X=k)\\ using `BINOM.DIST`
> - **Table 2:** Cumulative binomial distribution — compute \\P(X \leq k)\\ using `BINOM.DIST` with `cumulative=TRUE`
> - **Table 3.1:** Poisson distribution — compute \\P(X=k)\\ using `POISSON.DIST`
> - **Table 3.2:** Cumulative Poisson distribution — compute \\P(X \leq k)\\ using `POISSON.DIST` with `cumulative=TRUE`
> - **Table 3.3:** compare binomial values with their Poisson approximation
>
> **Goal:** perform and interpret the formulas of the discrete random variable and the Binomial–Poisson approximation.
>
> **To go further:** complete Tables 4.1 and 4.2 with a graphical illustration of the Binomial–Poisson approximation.

> **CAUTION:**
>
> Typical Excel formulas are:
>
> - exact binomial probability: `=BINOM.DIST(k,n,p,FALSE)`
> - cumulative binomial probability: `=BINOM.DIST(k,n,p,TRUE)`
> - exact Poisson probability: `=POISSON.DIST(k,lambda,FALSE)`
> - cumulative Poisson probability: `=POISSON.DIST(k,lambda,TRUE)`
>
> For the approximation table, first compute:
>
> \\ \lambda = np \\
>
> then compare:
>
> \\ B(n,p) \approx \mathcal{P}(np) \\
>
> when \\n\\ is large and \\p\\ is small.
>
> Interpretation: the approximation is usually good when the binomial setting has **many trials** and a **small success probability**.

## 4 Exercise 3 — Continuous Random Variables

### 4.1 Mission 1.1 — Binomial distribution for large \\n\\

Review the context of the application exercise in **Session 4**. Then open `PW - Session 05 - Exercise3.xlsx`.

> **TIP:**
>
> When \\n\\ is large and the binomial conditions are satisfied,
>
> \\ B(n,p) \approx \mathcal{N}(np,\\np(1-p)) \\
>
> so the mean is \\\mu=np\\ and the standard deviation is
>
> \\ \sigma = \sqrt{np(1-p)}. \\

> **CAUTION:**
>
> After reading the Session 4 lecture and Appendices 2 and 4, complete Tables 1.1 to 2.4 of `PW - Session 05 - Exercise3.xlsx`:
>
> - **Tables 1.1–1.3:** study the binomial distribution for large \\n\\
> - **Tables 2.1–2.4:** compute the Binomial–Normal approximation using `NORM.DIST`
>
> **Goal:** perform and interpret the formulas for the continuous random variable and the Binomial–Normal approximation.

> **CAUTION:**
>
> A useful Excel workflow is:
>
> 1.  compute the binomial parameters \\n\\ and \\p\\;
> 2.  derive the Normal parameters \\\mu=np\\ and \\\sigma=\sqrt{np(1-p)}\\;
> 3.  use `NORM.DIST` to approximate probabilities.
>
> For a cumulative approximation:
>
> `=NORM.DIST(x, mean, standard_dev, TRUE)`
>
> For an exact binomial value \\P(X=k)\\, a continuity correction is often used:
>
> \\ P(X=k) \approx P(k-0.5 \leq Y \leq k+0.5) \\
>
> with \\Y \sim \mathcal{N}(np,np(1-p))\\.

### 4.2 Mission 1.2 — Quantiles of the Normal distribution

> **CAUTION:**
>
> After reading Appendix 5, complete **Table 3**:
>
> - compute \\D_1\\, \\Q_1\\, the **Median**, \\Q_3\\, and \\D_9\\ for the Normal distribution using `NORM.INV`.
>
> **Goal:** perform and interpret the quantile formulas for the Normal distribution.

> **CAUTION:**
>
> Use the following probabilities:
>
> - \\D_1\\: probability \\0.10\\
> - \\Q_1\\: probability \\0.25\\
> - Median: probability \\0.50\\
> - \\Q_3\\: probability \\0.75\\
> - \\D_9\\: probability \\0.90\\
>
> Typical Excel formulas:
>
> - `=NORM.INV(0.10,mean,standard_dev)`
> - `=NORM.INV(0.25,mean,standard_dev)`
> - `=NORM.INV(0.50,mean,standard_dev)`
> - `=NORM.INV(0.75,mean,standard_dev)`
> - `=NORM.INV(0.90,mean,standard_dev)`
>
> Interpretation: `NORM.INV(p, mean, standard_dev)` returns the value \\x\\ such that
>
> \\ P(X \leq x)=p. \\

## 5 Appendices

### 5.1 Appendix 1 — Excel Functions for Combinatorial Analysis

> **NOTE:**
>
> - `COMBIN(number, number_chosen)` — returns \\C_n^k\\, the number of combinations
> - `PERMUT(number, number_chosen)` — returns \\A_n^k\\, the number of arrangements without repetition
> - `FACT(number)` — returns \\n!\\

### 5.2 Appendix 2 — `BINOM.DIST`

> **NOTE:**
>
> `BINOM.DIST(number_s, trials, probability_s, cumulative)`
>
> - `number_s`: number of successes
> - `trials`: number of independent trials
> - `probability_s`: probability of success per trial
> - `cumulative`: `TRUE` for \\P(X \leq k)\\, `FALSE` for \\P(X = k)\\

### 5.3 Appendix 3 — `POISSON.DIST`

> **NOTE:**
>
> `POISSON.DIST(x, mean, cumulative)`
>
> - `x`: number of events
> - `mean`: expected value \\\lambda\\
> - `cumulative`: `TRUE` for \\P(X \leq x)\\, `FALSE` for \\P(X = x)\\

### 5.4 Appendix 4 — `NORM.DIST`

> **NOTE:**
>
> `NORM.DIST(x, mean, standard_dev, cumulative)`
>
> - `x`: value at which to evaluate
> - `mean`: \\\mu\\
> - `standard_dev`: \\\sigma\\
> - `cumulative`: `TRUE` for \\F(x)=P(X \leq x)\\, `FALSE` for the density \\f(x)\\

### 5.5 Appendix 5 — `NORM.INV`

> **NOTE:**
>
> `NORM.INV(probability, mean, standard_dev)`
>
> - `probability`: a probability value \\p\\
> - returns the value \\x\\ such that \\P(X \leq x)=p\\
