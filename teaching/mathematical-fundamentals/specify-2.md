Your current index.qmd already provides the institutional information and a clear progression across eight modules. I would preserve that foundation, while turning the homepage into a more learner-oriented entry point with a course roadmap, explicit learning outcomes, preparation instructions and clear links to activities.

One point to verify: the module dates currently run from 17 September to 12 November 2025, while date-modified is 23 July 2026. If this is the 2026 course edition, the session dates should be updated. If the website archives the 2025 edition, the dates are consistent as historical dates.

1. Recommended pedagogical structure

For mathematical fundamentals, I would organise each module around this learning cycle:

Diagnose

One or two prerequisite questions
A short problem that reveals the need for the new method

Understand

Intuitive explanation
Formal definition
Visual representation
Economic or managerial interpretation

Observe

One fully worked example
Explicit justification for every step

Practise

Guided exercise
Hint
Partial solution
Complete solution

Experiment

Interactive graph or simulator
Parameters that students can change
Interpretation questions

Apply

Finance, economics or management problem
Small dataset or decision scenario

Check

Short formative quiz
Error-diagnosis question
Confidence rating

Consolidate

Summary
Formula sheet
Vocabulary
Suggested independent work

The recurring sequence could be presented to students as:

Understand → Calculate → Visualise → Interpret → Apply

This is particularly helpful for students who may perceive mathematics as a collection of disconnected procedures.

2. Proposed course architecture
mathematical-fundamentals/
├── _quarto.yml
├── index.qmd
├── syllabus.qmd
├── assessment.qmd
├── learning-guide.qmd
├── glossary.qmd
├── formula-sheet.qmd
├── revision.qmd
├── references.bib
├── styles.scss
│
├── modules/
│   ├── module-1/
│   │   ├── index.qmd
│   │   ├── lesson.qmd
│   │   ├── practice.qmd
│   │   ├── applications.qmd
│   │   └── quiz.qmd
│   ├── module-2/
│   ├── module-3/
│   ├── module-4/
│   ├── module-5/
│   ├── module-6/
│   ├── module-7/
│   └── module-8/
│
├── exercises/
│   ├── exercise-bank.qmd
│   └── solutions.qmd
│
├── data/
├── images/
├── interactive/
└── slides/


If you prefer a simpler repository, each module can remain a single .qmd page initially:

├── module-1.qmd
├── module-2.qmd
├── module-3.qmd
├── module-4.qmd
├── module-5.qmd
├── module-6.qmd
├── module-7.qmd
└── module-8.qmd


I would begin with this simpler structure and split a module into several pages only when it becomes too long.

3. Revised index.qmd

Below is an adapted version that keeps your institutional information while making the page more engaging and useful to students.

---
title: "Mathematical Fundamentals and Data Analysis"
subtitle: "Mathematical tools for finance, economics, and management"
description: |
  Undergraduate course providing the essential mathematical tools needed
  to analyse and solve quantitative problems in finance, economics, and
  management.
date-modified: 2026-07-23
image: image.png
page-layout: full
toc: true
toc-depth: 2
---

::: {.callout-note title="Welcome to the course"}
This course will help you develop the mathematical reasoning and calculation
skills needed to solve quantitative problems in finance, economics, and
management.

Throughout the course, you will learn to:

- perform calculations accurately;
- translate practical problems into mathematical expressions;
- choose an appropriate calculation method;
- interpret equations, functions, graphs, and numerical results;
- use mathematical tools to support managerial decisions.
:::

## Start Here

Before beginning the first module:

1. Read the syllabus.qmd.
2. Consult the learning-guide.qmd.
3. Complete the initial diagnostic activity.
4. Bookmark the [glossary](glossary.qmd).
5. Download or consult the formula-sheet.qmd.

::: {.callout-tip title="How to study each module"}
Each module follows the same learning sequence:

1. **Understand** the central concepts.
2. **Observe** a worked example.
3. **Practise** using guided exercises.
4. **Visualise** the mathematical relationships.
5. **Apply** the method to finance, economics, or management.
6. **Check** your understanding with a short quiz.
:::

## Course Information

- **Department:** Operations Management and Decision Science
- **Semester:** 01
- **Teaching campuses:** Aix-en-Provence, Angers, Bordeaux,
  Boulogne-Billancourt, Lyon, and Strasbourg
- **Total contact hours:** 30
- **ECTS credits:** 4
- **Language of instruction:** French and/or English
- **Open to exchange students:** No
- **Expected personal work:** 50 hours

## General Presentation

This course provides the mathematical foundations required to analyse and
solve quantitative problems in finance, economics, and management.

The course covers:

- numerical calculations and the properties of real numbers;
- algebraic expressions, powers, square roots, fractions, and percentages;
- first-degree and second-degree equations;
- systems of equations and inequalities;
- graphical representations and the interpretation of functions;
- arithmetic and geometric sequences;
- simple and compound interest;
- polynomial, logarithmic, and exponential functions;
- average and instantaneous rates of change;
- an intuitive introduction to derivatives and optimization.

The emphasis is not only on obtaining a numerical result. Students will also
learn to select an appropriate method, explain their reasoning, verify their
calculations, and interpret the result in context.

## Learning Outcomes

By the end of the course, students should be able to:

1. Apply the order of operations and manipulate numerical expressions.
2. Work confidently with fractions, percentages, powers, and square roots.
3. Expand, factor, and simplify algebraic expressions.
4. Solve equations, inequalities, and simple systems.
5. Read, construct, and interpret graphs.
6. Analyse arithmetic and geometric sequences.
7. Calculate simple and compound interest.
8. Identify the domain and main properties of common functions.
9. Interpret average and instantaneous rates of change.
10. Use elementary derivatives to solve simple optimization problems.
11. Apply mathematical reasoning to finance, economics, and management.
12. Evaluate whether a calculated result is plausible and relevant.

## Targeted Competencies

### 2. Intellectual abilities

**2.3:** Choose relevant calculation methods and problem-solving tools.

Students will learn to:

- identify the mathematical structure of a problem;
- select an appropriate procedure;
- explain the main stages of a calculation;
- verify and interpret the result.

### 5. Technological skills

**5.2:** Use tools dedicated to information research, information processing,
and business communication.

Students may use digital tools to:

- perform and verify calculations;
- construct tables and graphs;
- explore how results change when assumptions change;
- communicate quantitative findings clearly.

::: {.callout-important title="Using calculators and digital tools"}
Digital tools support mathematical reasoning, but they do not replace it.

You should always be able to explain:

1. what you are calculating;
2. why the selected method is appropriate;
3. what the result means;
4. whether the result is plausible.
:::

## Course Roadmap

### Module 1: [Essential Mathematical Calculations for Economics and Management](module-1.qmd)

**Fundamental operations and numerical reasoning**

Topics include:

- order of operations;
- positive and negative numbers;
- absolute value;
- powers and square roots;
- fractions;
- ratios and proportionality;
- percentages and percentage changes;
- index numbers.

**Application question:** How can we calculate and interpret a change in
price, revenue, cost, or market share?

---

### Module 2: [Mastering Equations for Better Decision-Making](module-2.qmd)

**Algebraic expressions and first-degree equations**

Topics include:

- algebraic notation;
- expanding expressions;
- factoring expressions;
- notable identities;
- simplifying expressions;
- solving first-degree equations;
- translating practical problems into equations.

**Application question:** At what sales volume does a company reach its
break-even point?

---

### Module 3: [Curve Analysis in Economics and Management](module-3.qmd)

**Graphs, lines, systems, and inequalities**

Topics include:

- reading coordinates and scales;
- affine functions and straight lines;
- slope and intercept;
- signs and variations;
- intersections of lines;
- first-degree systems;
- first-degree inequalities;
- graphical and algebraic solutions.

**Application question:** At what level of activity do two pricing or cost
models produce the same result?

---

### Module 4: [Introduction to Financial-Mathematics Tools](module-4.qmd)

**Arithmetic and geometric sequences**

Topics include:

- definition of a numerical sequence;
- explicit and recursive forms;
- arithmetic sequences;
- geometric sequences;
- calculation of terms;
- interpretation of growth patterns.

**Application question:** How can we model a quantity that increases by a
fixed amount or by a fixed percentage?

---

### Module 5: [Application of Financial Mathematics](module-5.qmd)

**Simple and compound interest**

Topics include:

- principal, interest rate, and duration;
- simple interest;
- compound interest;
- present and future value;
- comparison of investment scenarios;
- interpretation of financial results.

**Application question:** How does capitalization affect the future value of
an investment?

---

### Module 6: [Functions Useful in Economics and Management](module-6.qmd)

**Domains, common functions, and second-degree equations**

Topics include:

- meaning of a function;
- independent and dependent variables;
- domain of definition;
- forbidden values;
- affine functions;
- polynomial functions;
- logarithmic functions;
- exponential functions;
- second-degree equations.

**Application question:** Which type of function best represents a given
economic or managerial phenomenon?

---

### Module 7: [Introduction to Optimization](module-7.qmd)

**Rates of change, derivatives, and elementary optimization**

Topics include:

- average rate of change;
- instantaneous rate of change;
- intuitive meaning of a derivative;
- derivatives of affine and polynomial functions;
- increasing and decreasing functions;
- maximum and minimum values;
- simple optimization problems.

**Application question:** Which price, quantity, or production level maximizes
profit or minimizes cost?

---

### Module 8: [Revision and Final-Exam Preparation](module-8.qmd)

**Consolidation and exam strategy**

Activities include:

- concept review;
- mixed calculations;
- interpretation of graphs;
- applied problems;
- common-error analysis;
- practice examination;
- correction and discussion;
- personal revision planning.

**Final question:** Can you identify the appropriate mathematical method
without being told which chapter the problem comes from?

## Learning Progress

Use this checklist to monitor your progress.

- [ ] Module 1: Numerical calculations
- [ ] Module 2: Algebra and equations
- [ ] Module 3: Graphs, systems, and inequalities
- [ ] Module 4: Numerical sequences
- [ ] Module 5: Financial mathematics
- [ ] Module 6: Common functions
- [ ] Module 7: Derivatives and optimization
- [ ] Module 8: Revision and exam preparation

## Assessment

| Examination | Weight | Assessment mode | Duration |
|---|---:|---|---:|
| Continuous assessment | 50% | Individual written examination | 45 minutes |
| Final examination | 50% | Individual written examination | 90 minutes |

The assessments may evaluate the ability to:

- perform calculations accurately;
- select an appropriate mathematical method;
- present the main stages of a solution;
- interpret equations, tables, and graphs;
- apply mathematical tools to an unfamiliar problem;
- verify the plausibility of a result.

See the assessment.qmd for detailed instructions and
assessment criteria.

## Expected Personal Work

Students are expected to:

- review prerequisite material before each session;
- complete the preparation activity;
- attempt the exercises before consulting the solutions;
- correct errors and record their causes;
- revise definitions and methods regularly;
- complete the proposed revision activities.

**Expected personal workload:** 50 hours.

A regular weekly workload will generally be more effective than intensive
revision immediately before an assessment.

## Course Resources

- learning-guide.qmd
- [Glossary of mathematical terms and symbols](glossary.qmd)
- formula-sheet.qmd
- exercises/exercise-bank.qmd
- revision.qmd
- assessment.qmd

## Recommended Literature

- Ian Jacques, *Mathematics for Economics and Business*, 5th edition,
  Pearson Education Limited, 2006.
- Jean-Luc Dorier and Marc Duc-Jacquet, *Mathématiques pour l'économie et la
  gestion*, 1st edition, Gualino Éditeur, 1996.
- Stéphane Rossignol, *Mathématiques en économie-gestion*, 2nd edition,
  Dunod Éditions, 2022.

4. Recommended template for every module

Each module-x.qmd can follow the same structure. This consistency is particularly important for students who lack confidence in mathematics.

---
title: "Module 1: Essential Mathematical Calculations"
subtitle: "Numbers, fractions, percentages, and proportionality"
description: |
  Learn how to perform and interpret the calculations most frequently used
  in economics, finance, and management.
---

## Module Overview

::: {.callout-note title="Learning objectives"}
By the end of this module, you should be able to:

1. Apply the order of operations.
2. Calculate with positive and negative numbers.
3. Simplify fractions.
4. Work with powers and square roots.
5. Calculate percentages and percentage changes.
6. Solve proportionality problems.
7. Interpret calculations in context.
:::

::: {.callout-tip title="Before you begin"}
**Estimated study time:** 3 hours 45 minutes  
**Prerequisites:** Basic arithmetic  
**Materials:** Calculator, notebook, and formula sheet
:::

## 1. Diagnostic Activity

Attempt these questions without consulting the lesson.

1. Calculate \(4 + 3 \times 5\).
2. Calculate \(25\%\) of 240.
3. A price rises from €80 to €92. Calculate the percentage increase.
4. Simplify \(\frac{18}{24}\).

::: {.callout-note collapse="true" title="Check your answers"}
1. \(19\)
2. \(60\)
3. \(15\%\)
4. \(\frac{3}{4}\)
:::

Use your results to identify the topics that require particular attention.

## 2. Opening Problem

A company increases the price of a product by \(20\%\). During a promotional
campaign, it then reduces the new price by \(20\%\).

> Does the product return to its original price?

Write down your prediction before continuing.

## 3. Core Concepts

### 3.1 Order of operations

Explain the concept here.

### 3.2 Fractions

Explain the concept here.

### 3.3 Percentages

Explain the concept here.

## 4. Worked Example

Consider a product initially priced at €100.

A \(20\%\) increase gives:

\[
100 \times 1.20 = 120.
\]

A subsequent \(20\%\) decrease gives:

\[
120 \times 0.80 = 96.
\]

The final price is €96, not €100.

::: {.callout-important title="Interpretation"}
The two percentage changes are applied to different reference values.

The increase is calculated from €100, while the decrease is calculated from
€120.
:::

## 5. Guided Practice

A company's revenue increases from €400,000 to €460,000.

1. Calculate the absolute change.
2. Calculate the relative change.
3. Express the relative change as a percentage.
4. Interpret the result in one sentence.

::: {.callout-tip collapse="true" title="Hint"}
The percentage change is:

\[
\frac{\text{new value} - \text{initial value}}
     {\text{initial value}}
\times 100.
\]
:::

::: {.callout-note collapse="true" title="Show the solution"}
The absolute change is:

\[
460\,000 - 400\,000 = 60\,000.
\]

The relative change is:

\[
\frac{60\,000}{400\,000} = 0.15.
\]

Therefore, revenue increased by:

\[
0.15 \times 100 = 15\%.
\]
:::

## 6. Interactive Exploration

Add the module's interactive activity here.

Questions should appear after the activity:

1. Which parameter did you change?
2. How did the result respond?
3. Is the relationship linear or nonlinear?
4. Can you explain the result without referring to the graph?

## 7. Applied Problem

Present a finance, economics, or management situation here.

## 8. Common Errors

::: {.callout-warning title="Common error"}
Dividing the change by the final value instead of the initial value.

For a change from \(80\) to \(100\), the correct calculation is:

\[
\frac{100-80}{80} = 25\%.
\]

The initial value is the reference value.
:::

## 9. Check Your Understanding

Include five short questions:

1. One calculation question
2. One conceptual question
3. One graphical question
4. One applied question
5. One error-diagnosis question

## 10. Summary

At the end of this module, you should remember that:

1. ...
2. ...
3. ...

## 11. Independent Work

- Complete exercises 1 to 10.
- Correct your answers using the detailed solutions.
- Record errors in your error log.
- Review the glossary entries associated with this module.

## 12. Continue

[Continue to Module 2](module-2.qmd)

5. Tailored interactive activity for each module
Module 1: Percentage-change simulator

Let students change:

initial value;
percentage increase;
percentage decrease.

Then ask them to investigate why an increase of x%x\% followed by a decrease of x%x\% does not generally return to the initial value.

## Explore Successive Percentage Changes

```{ojs}
viewof initialValue = Inputs.range([10, 1000], {
  value: 100,
  step: 10,
  label: "Initial value"
})

viewof increaseRate = Inputs.range([0, 100], {
  value: 20,
  step: 1,
  label: "Increase (%)"
})

viewof decreaseRate = Inputs.range([0, 100], {
  value: 20,
  step: 1,
  label: "Decrease (%)"
})

valueAfterIncrease =
  initialValue * (1 + increaseRate / 100)

finalValue =
  valueAfterIncrease * (1 - decreaseRate / 100)

overallChange =
  100 * (finalValue - initialValue) / initialValue

html`
  <div class="metric-grid">
    <div class="metric-card">
      <span class="metric-label">Initial value</span>
      <strong>${initialValue.toFixed(2)}</strong>
    </div>

    <div class="metric-card">
      <span class="metric-label">After the increase</span>
      <strong>${valueAfterIncrease.toFixed(2)}</strong>
    </div>

    <div class="metric-card">
      <span class="metric-label">Final value</span>
      <strong>${finalValue.toFixed(2)}</strong>
    </div>

    <div class="metric-card">
      <span class="metric-label">Overall change</span>
      <strong>${overallChange.toFixed(2)}%</strong>
    </div>
  </div>
`


Follow it with:

```markdown
### Investigation

1. Set both rates to \(20\%\). What is the overall change?
2. Repeat with \(10\%\), \(30\%\), and \(50\%\).
3. Does the initial value affect the overall percentage change?
4. Find a decrease that exactly reverses an increase of \(25\%\).
5. Explain why this decrease is not \(25\%\).

Module 2: Break-even equation

Students manipulate:

R(q)=pqR(q)=pq

and:

C(q)=F+vq.C(q)=F+vq.

The activity should show revenue, cost and profit as quantity changes.

Key question:

At what quantity does revenue equal total cost?

Module 3: Intersection of two lines

Let students adjust the slope and intercept of two lines:

y1=a1x+b1y_1=a_1x+b_1 y2=a2x+b2.y_2=a_2x+b_2.

Students should see the graphical intersection and compare it with the algebraic solution.

Possible application:

comparing two mobile-phone plans;
comparing two transportation contracts;
comparing an internal-production option with outsourcing.
Module 4: Sequence explorer

Let students choose:

initial term;
common difference;
common ratio;
number of periods.

Display arithmetic and geometric sequences side by side.

Key question:

Under what conditions does a geometric sequence eventually exceed an arithmetic sequence?

Module 5: Compound-interest calculator

Inputs:

capital;
annual interest rate;
number of periods;
capitalization frequency.

Outputs:

simple-interest value;
compound-interest value;
cumulative interest;
chart of value over time.

Students should first predict which effect will be largest: rate, duration or capitalization frequency.

Module 6: Function family explorer

Let students select:

affine;
quadratic;
exponential;
logarithmic.

Parameters can be modified with sliders. The graph should update while showing:

domain;
intercepts;
variations;
selected values;
economic interpretation.
Module 7: Profit-maximisation simulator

For example:

R(q)=60q−0.2q2R(q)=60q-0.2q^2 C(q)=500+20qC(q)=500+20q P(q)=R(q)−C(q).P(q)=R(q)-C(q).

Students move qq, observe profit and then compare the experimental maximum with the derivative-based solution.

Module 8: Mixed-method challenge

Instead of identifying exercises by chapter, present mixed problems and ask students to choose the method:

percentage;
equation;
system;
sequence;
compound interest;
function;
derivative.

This tests mathematical recognition rather than procedural imitation.

6. Treat errors as learning resources

Mathematical errors should be explicitly integrated into the course. Each module should include an error clinic.

## Error Clinic

A student writes:

\[
3(x+4)=3x+4.
\]

### Your task

1. Identify the error.
2. Correct the calculation.
3. Explain the distributive property in words.

::: {.callout-note collapse="true" title="Explanation"}
The factor \(3\) must multiply every term inside the parentheses:

\[
3(x+4)=3x+12.
\]

The original expression omitted the multiplication of \(4\) by \(3\).
:::


Useful error categories include:

calculation error;
transcription error;
incorrect formula;
incorrect reference value;
sign error;
incorrect distribution;
invalid division;
domain error;
graphical-reading error;
correct calculation but incorrect interpretation.

Students could maintain an error log containing:

the original error;
its cause;
the corrected method;
a rule for avoiding it in future.
7. Add multiple representations

Every major concept should appear, where relevant, in four forms:

Verbal
Symbolic
Numerical
Graphical

For example, an affine cost function could be represented as follows:

Verbal representation

Total cost consists of a fixed cost of €500 and a variable cost of €20 per unit.

Symbolic representation
C(q)=500+20q.C(q)=500+20q.
Numerical representation
Quantity	Total cost0	€500
10	€700
20	€900
30	€1,100
Graphical representation

A straight line with:

vertical intercept 500500;
slope 2020.

Then ask:

What does the slope mean in the business context?

This translation between representations is one of the most valuable competencies students can develop.

8. Proposed _quarto.yml
project:
  type: website
  output-dir: _site

website:
  title: "Mathematical Fundamentals and Data Analysis"
  description: "Mathematical tools for finance, economics, and management"
  page-navigation: true
  back-to-top-navigation: true

  navbar:
    background: primary
    left:
      - text: "Home"
        href: index.qmd

      - text: "Course"
        menu:
          - text: "Syllabus"
            href: syllabus.qmd
          - text: "Learning Guide"
            href: learning-guide.qmd
          - text: "Assessment"
            href: assessment.qmd

      - text: "Resources"
        menu:
          - text: "Glossary"
            href: glossary.qmd
          - text: "Formula Sheet"
            href: formula-sheet.qmd
          - text: "Exercise Bank"
            href: exercises/exercise-bank.qmd
          - text: "Revision Centre"
            href: revision.qmd

  sidebar:
    style: docked
    search: true
    collapse-level: 1
    contents:
      - section: "Course Information"
        contents:
          - index.qmd
          - syllabus.qmd
          - learning-guide.qmd
          - assessment.qmd

      - section: "Course Modules"
        contents:
          - module-1.qmd
          - module-2.qmd
          - module-3.qmd
          - module-4.qmd
          - module-5.qmd
          - module-6.qmd
          - module-7.qmd
          - module-8.qmd

      - section: "Learning Resources"
        contents:
          - glossary.qmd
          - formula-sheet.qmd
          - exercises/exercise-bank.qmd
          - revision.qmd

  page-footer:
    left: "Mathematical Fundamentals and Data Analysis"
    right: "Operations Management and Decision Science"

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    css: styles.scss
    toc: true
    toc-depth: 3
    number-sections: false
    code-fold: true
    code-summary: "Show the code"
    code-copy: true
    code-overflow: wrap
    anchor-sections: true
    smooth-scroll: true
    link-external-newwindow: true

execute:
  freeze: auto
  warning: false
  message: false

lang: en


If pages are served in both French and English, I would avoid mixing both languages within the same teaching page. A clearer solution is to have parallel language sections, such as:

/en/index.qmd
/en/module-1.qmd

/fr/index.qmd
/fr/module-1.qmd


This makes navigation, mathematical vocabulary and accessibility more consistent.

9. A realistic production plan

I would not develop all eight modules simultaneously.

First iteration

Build Module 1 completely, including:

learning objectives;
diagnostic activity;
explanations;
worked examples;
guided exercises;
one interactive simulator;
one applied problem;
one error clinic;
formative quiz;
summary;
independent work.
Student test

Ask a small group to complete it and observe:

where they stop;
where they scroll past content;
which instructions they misunderstand;
whether they attempt exercises before revealing solutions;
whether the interactive activity improves understanding;
how the page performs on a mobile device.
Second iteration

Use the evidence to create a standard template and apply it to Modules 2 to 7.

Final iteration

Develop Module 8 only after the other modules are stable. Its revision activities should reflect the actual concepts, terminology and errors encountered during the course.

The key adaptation is to present mathematics not as a sequence of formulas, but as a progression from problem recognition to modelling, calculation, visualisation and interpretation. This supports both mathematical understanding and the targeted competency of selecting an appropriate problem-solving tool.