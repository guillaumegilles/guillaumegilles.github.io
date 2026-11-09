This session develops the basic rules of probability and shows how to compute conditional probabilities in business situations.

*Suggested pacing: Introduction (10 min), Basic calculation of probabilities (25 min), Detailed example (15 min), Application exercise (40 min).*

## 1 Introduction

### 1.1 Random experiment, sample space, and events

> **NOTE:**
>
> A **random experiment** is an experiment whose outcome cannot be predicted with certainty in advance.

> **NOTE:**
>
> The **sample space** \\\Omega\\ is the set of all possible outcomes of a random experiment.

> **NOTE:**
>
> An **event** is a subset of \\\Omega\\. An **elementary event** contains only one outcome.

Example: when one customer file is selected at random,

- \\\Omega\\ may be the set of all customer files,
- \\A\\ may be the event “the customer is premium”,
- \\B\\ may be the event “the customer bought online last month”.

## 2 Basic calculation of probabilities

### 2.1 Basic rules

> **TIP:**
>
> For any event \\A\\:
>
> - \\P(A) \in \[0,1\]\\
> - \\P(\Omega) = 1\\
> - \\P(\emptyset) = 0\\
> - \\P(\bar{A}) = 1 - P(A)\\

If all outcomes are equally likely, we use **classical probability**:

\\ P(A) = \frac{\text{number of favorable outcomes}}{\text{total number of outcomes}} = \frac{\|A\|}{\|\Omega\|} \\

### 2.2 Addition rule

> **TIP:**
>
> For two events \\A\\ and \\B\\:
>
> \\ P(A \cup B) = P(A) + P(B) - P(A \cap B) \\
>
> If \\A\\ and \\B\\ are mutually exclusive, then:
>
> \\ P(A \cup B) = P(A) + P(B) \\

### 2.3 Conditional probability and independence

> **TIP:**
>
> Provided that \\P(B) \> 0\\,
>
> \\ P(A \mid B) = \frac{P(A \cap B)}{P(B)} \\

> **NOTE:**
>
> Two events \\A\\ and \\B\\ are **independent** if:
>
> \\ P(A \cap B) = P(A) \times P(B) \\
>
> Equivalently, if \\P(B) \> 0\\,
>
> \\ P(A \mid B) = P(A) \\

> **WARNING:**
>
> Do not confuse \\P(A \mid B)\\ with \\P(B \mid A)\\. These two probabilities are usually different.

### 2.4 Total probability formula

> **TIP:**
>
> If \\B_1, B_2, \dots, B_n\\ form a partition of \\\Omega\\, then:
>
> \\ P(A) = \sum\_{i=1}^{n} P(A \mid B_i) \times P(B_i) \\

### 2.5 Bayes’ theorem

> **TIP:**
>
> If \\B_1, B_2, \dots, B_n\\ form a partition of \\\Omega\\, then:
>
> \\ P(B_k \mid A) = \frac{P(A \mid B_k) \times P(B_k)}{\sum\_{i=1}^{n} P(A \mid B_i) \times P(B_i)} \\

> **IMPORTANT:**
>
> When a probability question involves several sources, groups, or machines, draw a **tree diagram** or identify a **partition** before calculating.

## 3 Detailed example

A bank studies 200 clients:

- 120 use the mobile app,
- 80 have a premium account,
- 50 both use the app and have a premium account.

Let:

- \\A\\ = “the client uses the mobile app”,
- \\B\\ = “the client has a premium account”.

### 3.1 Union

\\ P(A) = \frac{120}{200} = 0.60, \qquad P(B) = \frac{80}{200} = 0.40, \qquad P(A \cap B) = \frac{50}{200} = 0.25 \\

Using the addition rule:

\\ P(A \cup B) = 0.60 + 0.40 - 0.25 = 0.75 \\

So the probability that a client uses the app or has a premium account is **0.75**.

### 3.2 Conditional probability

The probability that a client has a premium account given that they use the app is:

\\ P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{0.25}{0.60} \approx 0.417 \\

So about **41.7%** of app users have a premium account.

## 4 Application exercise

> > **CAUTION:**
> >
> > A factory has 3 machines (\\M_1\\, \\M_2\\, \\M_3\\) producing 40%, 35%, and 25% of output respectively. Defect rates are 2%, 3%, and 5%.
> >
> > 1.  What is the overall probability of picking a defective part?
> > 2.  Given a defective part, what is the probability it came from \\M_3\\?

> > **CAUTION:**
> >
> > Let \\D\\ be the event “the part is defective”.
> >
> > **1. Overall probability of a defect**
> >
> > Using total probability:
> >
> > \\ P(D) = 0.4 \times 0.02 + 0.35 \times 0.03 + 0.25 \times 0.05 \\
> >
> > \\ P(D) = 0.008 + 0.0105 + 0.0125 = 0.031 \\
> >
> > So the overall probability of a defective part is **0.031**, or **3.1%**.
> >
> > **2. Probability that a defective part came from \\M_3\\**
> >
> > By Bayes’ theorem:
> >
> > \\ P(M_3 \mid D) = \frac{P(D \mid M_3)P(M_3)}{P(D)} = \frac{0.25 \times 0.05}{0.031} \\
> >
> > \\ P(M_3 \mid D) = \frac{0.0125}{0.031} \approx 0.403 \\
> >
> > So the probability is about **0.403**, or **40.3%**.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Session 2 — {Calculation} of {Probabilities}},
  url = {https://ggilles.dev/teaching/decision-making-stat/session-02.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Session 2 — Calculation of Probabilities.” <https://ggilles.dev/teaching/decision-making-stat/session-02.html>.
