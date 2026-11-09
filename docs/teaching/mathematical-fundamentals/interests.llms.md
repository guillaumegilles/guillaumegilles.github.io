## 1 Diagnostic Activity

Answer the following questions from memory before reading further.

1.  Compute the simple interest earned on €1,000 invested at 5% per year for 2 years.
2.  Is compound interest modelled by an arithmetic or geometric sequence?
3.  A monthly interest rate is 0.5%. What is the equivalent annual rate under simple (proportional) conversion?

> **NOTE:**
>
> 1.  \\1{,}000 \times 0.05 \times 2 = €100.\\
> 2.  Geometric — each period multiplies the capital by a constant factor \\(1+i).\\
> 3.  \\0.5\\ \times 12 = 6\\\\ per year.

Use your results to identify topics needing attention.

## 2 Opening Problem

You invest €5,000 at an annual rate of 4%. Bank A compounds the interest once a year; Bank B compounds it every month (same annual rate).

> After 10 years, how much more does Bank B give you than Bank A? Is the difference significant?

Write down your estimate before continuing.

## 3 Core Concepts

Simple interest and compound interest are two different ways of computing, for example, the return on invested capital or the cost of a loan. Each has its practical uses depending on the financial and economic context. They are the direct application of the arithmetic and geometric sequences studied in Module 4.

### 3.1 Simple Interest

> **NOTE:**
>
> With **simple interest**, interest is computed only on the **initial** capital, without reinvestment. The interest is the same for each period, so the acquired capital follows an **arithmetic** sequence.

Let \\C_0\\ be the initial capital, \\i\\ the interest rate per period, and \\n\\ the number of periods. The interest of one period is \\C_0\\i\\ (constant), so:

\\ \text{Interest over } n \text{ periods} = C_0\\i\\n, \qquad C_n = C_0\\(1 + i\\n). \\

> **TIP:**
>
> - short-term loans;
> - one-off investments without reinvestment;
> - late-payment penalties and fees.

#### Worked example

We invest \\100{,}000\\ € at a simple annual rate of \\4\\\\ for \\4\\ years. The yearly interest is constant: \\100{,}000 \times 0.04 = 4{,}000\\ € per year. After \\4\\ years the acquired capital is

\\ C_4 = 100{,}000\\(1 + 0.04 \times 4) = 100{,}000 \times 1.16 = 116{,}000 \text{ €}. \\

### 3.2 Converting Interest Rates

Sometimes the rate and the period are not expressed in the same unit of time. Under the **simple** (proportional) convention, we scale the rate proportionally to the period.

> **TIP:**
>
> An annual rate \\i\_{\text{year}}\\ corresponds to a monthly rate \\i\_{\text{month}} = \dfrac{i\_{\text{year}}}{12}\\, and conversely \\i\_{\text{year}} = 12\\i\_{\text{month}}\\.

> **CAUTION:**
>
> 1.  Convert an annual rate of \\6\\\\ to a monthly rate: \\\dfrac{6\\}{12} = 0.5\\\\ per month.
> 2.  Convert a monthly rate of \\1\\\\ to an annual rate: \\12 \times 1\\ = 12\\\\ per year.
> 3.  A capital of \\5{,}000\\ € invested for \\4\\ months earns \\50\\ € of interest. Find the annual rate. The \\4\\-month rate is \\\dfrac{50}{5000} = 1\\\\, so the monthly rate is \\0.25\\\\ and the annual rate is \\12 \times 0.25\\ = 3\\\\.

### 3.3 Compound Interest

> **NOTE:**
>
> With **compound interest**, the interest earned each period is added to the capital and itself earns interest in the following periods (the “snowball” effect). The acquired capital follows a **geometric** sequence.

> **CAUTION:**
>
> At the end of one period the capital is multiplied by \\(1 + i)\\: the capital \\C_0\\ becomes \\C_1 = C_0 + C_0 i = C_0(1 + i)\\. Repeating, \\C_2 = C_1(1 + i) = C_0(1 + i)^2\\, and by induction
>
> \\ C_n = C_0\\(1 + i)^{\\n}. \\
>
> This is exactly a geometric sequence with first term \\C_0\\ and common ratio \\q = 1 + i\\. The interest earned over \\n\\ periods is \\C_n - C_0 = C_0\big\[(1 + i)^n - 1\big\]\\.

#### Worked example

We invest \\100{,}000\\ € at a compound annual rate of \\5\\\\ for \\10\\ years:

\\ C\_{10} = 100{,}000 \times 1.05^{10} \approx 162{,}889 \text{ €}. \\

For comparison, the **same** capital at a **simple** rate of \\6\\\\ for \\10\\ years gives \\100{,}000(1 + 0.06 \times 10) = 160{,}000\\ €: over a long horizon the compounding effect can outweigh a higher simple rate — but not always, as the final-exam case in Module 8 shows.

> **IMPORTANT:**
>
> Converting a compound rate between periods is **not** proportional. A monthly compound rate \\i_m\\ corresponds to the annual rate \\i\_{\text{year}} = (1 + i_m)^{12} - 1\\. For \\i_m = 0.5\\\\ this gives \\(1.005)^{12} - 1 \approx 6.17\\\\, not \\6\\\\.

### 3.4 Average Placement Rate

The **average placement rate** is the single rate that would produce the same final result (the same acquired capital) as a set of distinct investments, each with its own rate, amount, and duration. It summarises the overall performance of several combined investments in one figure.

> **TIP:**
>
> \\P = \frac{V_c}{(1 + i)^n}\\
>
> The present value \\P\\ is the initial capital that would produce a future value \\V_c\\ at rate \\i\\ after \\n\\ periods — it lets us compare cash flows at different points in time.

## 4 Worked Example

### 4.1 Worked example — Bank A vs Bank B (the Opening Problem)

We now solve the problem posed in §2 step by step.

**Bank A** — annual compounding (\\k = 1\\):

\\ V_A = 5{,}000 \times (1 + 0.04)^{10} = 5{,}000 \times 1.04^{10} \approx 7{,}401.22 \text{ €}. \\

**Bank B** — monthly compounding (\\k = 12\\):

\\ V_B = 5{,}000 \times \\\left(1 + \frac{0.04}{12}\right)^{10 \times 12} = 5{,}000 \times (1.003\overline{3})^{120} \approx 7{,}453.71 \text{ €}. \\

**Difference**:

\\ 7{,}453.71 - 7{,}401.22 = 52.49 \text{ €}. \\

Monthly compounding yields €52.49 more — a modest but real gain from the compounding frequency.

## 5 Guided Practice

An employee places €3,000 in a savings account offering a compound annual rate of 3.5%, compounded quarterly.

1.  Write the formula for the acquired capital after \\n\\ years.
2.  Calculate the acquired capital after 4 years.
3.  How many years does it take to double the initial capital?

> **TIP:**
>
> With quarterly compounding, \\k = 4\\. Use \\V_c = P\\\left(1 + \dfrac{i}{k}\right)^{nk}\\ with \\P = 3{,}000\\, \\i = 0.035\\, \\k = 4\\. For doubling, solve \\\left(1 + \dfrac{0.035}{4}\right)^{4n} = 2\\.

> **CAUTION:**
>
> **1. Formula:**
>
> \\ V_c = 3{,}000 \times \\\left(1 + \frac{0.035}{4}\right)^{4n} = 3{,}000 \times 1.00875^{4n}. \\
>
> **2. After 4 years** (\\n = 4\\, so the exponent is \\4 \times 4 = 16\\):
>
> \\ V_c = 3{,}000 \times 1.00875^{16} \approx 3{,}000 \times 1.1490 \approx 3{,}447 \text{ €}. \\
>
> **3. Doubling:** solve \\(1.00875)^{4n} = 2\\. Testing \\n = 20\\: \\(1.00875)^{80} \approx 2.002 \approx 2\\. About **20 years**.

## 6 Interactive Exploration

Use the controls below to explore how the principal, rate, number of years, and compounding frequency interact.

``` js
viewof principal = Inputs.range([100, 10000], {
  value: 5000,
  step: 100,
  label: "Principal P (€)"
})

viewof rate = Inputs.range([0, 20], {
  value: 4,
  step: 0.1,
  label: "Annual rate i (%)"
})

viewof periods = Inputs.range([1, 30], {
  value: 10,
  step: 1,
  label: "Number of years n"
})

viewof freq = Inputs.select([1, 2, 4, 12], {
  value: 1,
  label: "Capitalisation frequency k (per year)"
})
```

``` js
i = rate / 100
simpleVal = principal * (1 + i * periods)
compoundVal = principal * Math.pow(1 + i / freq, periods * freq)
cumInterest = compoundVal - principal

timeData = Array.from({length: periods + 1}, (_, t) => ({
  t,
  compound: principal * Math.pow(1 + i / freq, t * freq),
  simple: principal * (1 + i * t)
}))

growthChart = Plot.plot({
  marks: [
    Plot.line(timeData, {x: "t", y: "compound", stroke: "steelblue",
      label: "Compound"}),
    Plot.line(timeData, {x: "t", y: "simple", stroke: "orange",
      strokeDash: [4, 4], label: "Simple"}),
    Plot.dot(timeData, {x: "t", y: "compound", fill: "steelblue", r: 3}),
    Plot.dot(timeData, {x: "t", y: "simple", fill: "orange", r: 3})
  ],
  x: {label: "Year"},
  y: {label: "Capital (€)"},
  color: {legend: true}
})
```

``` js
html`
<div style="margin-bottom:1rem">${growthChart}</div>
<div class="metric-grid">
  <div class="metric-card">
    <span class="metric-label">Simple interest value</span>
    <strong>${simpleVal.toFixed(2)} €</strong>
  </div>
  <div class="metric-card">
    <span class="metric-label">Compound interest value</span>
    <strong>${compoundVal.toFixed(2)} €</strong>
  </div>
  <div class="metric-card">
    <span class="metric-label">Cumulative interest earned</span>
    <strong>${cumInterest.toFixed(2)} €</strong>
  </div>
  <div class="metric-card">
    <span class="metric-label">Gain over simple interest</span>
    <strong>${(compoundVal - simpleVal).toFixed(2)} €</strong>
  </div>
</div>
`
```

### 6.1 Investigation

1.  Set \\k = 1\\ (annual). Now set \\k = 12\\ (monthly), keeping all other parameters fixed. How much extra does monthly compounding earn after 10 years?
2.  Keep \\k = 1\\ and increase \\n\\ from 5 to 30. Does the gap between compound and simple interest grow slowly or quickly?
3.  Which has more impact on the final compound value: doubling the rate or doubling the number of years? Test with the sliders.
4.  Set \\i = 0\\ (zero rate). What do both formulas give? Why?

## 7 Applied Problem

A firm needs to repay a loan of €200,000 in 8 years. Two banks compete for the business. **Bank A** offers a simple annual rate of 7%. **Bank B** offers a compound annual rate of 5.5%.

1.  Calculate the total amount repaid to each bank after 8 years.
2.  Which bank offers the better deal?
3.  Bank A also offers to apply its rate monthly under simple (proportional) conversion. What is the monthly rate? What is the total repayment?
4.  Bank B offers monthly compounding at the same annual rate. What is the effective annual compound rate? Is it higher or lower than 5.5%?

## 8 Common Errors

> **WARNING:**
>
> A student converts a monthly compound rate of 0.5% to an annual rate as \\0.5\\ \times 12 = 6\\\\.
>
> This is only valid for **simple** (proportional) rates. For **compound** rates, the correct conversion is:
>
> \\ i\_{\text{year}} = (1 + i\_{\text{month}})^{12} - 1 = (1.005)^{12} - 1 \approx 6.17\\. \\
>
> Always use the compound-rate conversion formula when interest is reinvested each period.

## 9 Check Your Understanding

1.  €8,000 invested at 3% simple interest for 5 years. What is the acquired capital?
2.  What does it mean economically when the capitalisation frequency \\k\\ increases while the annual rate stays fixed?
3.  €10,000 invested at 4% compound (annual) for 8 years. Calculate the acquired capital.
4.  A student computes the annual compound rate equivalent to a monthly rate of 1% as \\1\\ \times 12 = 12\\\\. What is the correct answer?
5.  Which repayment is smaller: €100,000 at 6% simple for 10 years, or €100,000 at 5% compound for 10 years?

## 10 Summary

1.  Simple interest applies the rate to the original capital only (\\V_s = P(1+in)\\); compound interest applies it to the growing capital (\\V_c = P(1+i/k)^{nk}\\) — the difference grows with time and rate.
2.  Simple interest rates convert proportionally across periods; compound rates do not — converting \\i_m\\ to an annual rate requires \\(1+i_m)^{12} - 1\\, which always gives a higher annual rate.
3.  The capitalisation frequency \\k\\ matters: more frequent compounding (quarterly, monthly, daily) produces a higher final value for the same nominal annual rate, because interest starts earning interest sooner.

## 11 Independent Work

- Complete simple-interest exercises 1–5 in the exercise bank.

- Complete compound-interest exercises 1–5.

- Work through the loan comparison problem.

- Record errors in your error log.

- Review glossary entries for: *simple interest*, *compound interest*, *capitalisation frequency*, *present value*, *acquired capital*.

  ## 12 Module 5 — Financial Mathematics

  **Simple interest — future value**

  \\ V_s = P\\(1 + i\\n) \\

  \\P\\ = principal, \\i\\ = interest rate per period, \\n\\ = number of periods. Interest is computed only on the original principal each period.

  ------------------------------------------------------------------------

  **Compound interest — future value**

  \\ V_c = P\\\left(1 + \frac{i}{k}\right)^{nk} \\

  \\k\\ = capitalisation frequency (e.g., \\k=12\\ for monthly). Interest earns interest; the gap over simple interest grows with time.

  ------------------------------------------------------------------------

  **Present value (annual compounding)**

  \\ P = \frac{V_c}{(1 + i)^n} \\

  The initial capital that produces a future value \\V_c\\ at rate \\i\\ after \\n\\ years. Used to compare cash flows at different points in time.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {5️⃣ {Interests}},
  url = {https://ggilles.dev/teaching/mathematical-fundamentals/interests.html},
  langid = {en},
  abstract = {\#\#\#\# Learning objectives - Compute simple interest and
    the acquired capital. - Compute compound interest and analyse simple
    financial situations. - Convert an interest rate from one period to
    another. - Recognise which regime (simple or compound) applies to a
    situation.}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “5️⃣ Interests.” <https://ggilles.dev/teaching/mathematical-fundamentals/interests.html>.
