Quarto is a strong choice because it lets you combine pedagogy, narrative, executable code, visualisations, slides and assessments in one maintainable project. For a course such as financial analysis and corporate strategy, I would design it less as a repository of lecture notes and more as a structured learning environment where students repeatedly observe, predict, experiment, decide and reflect.

1. Start with the learning experience, not the technology

For every chapter, I would use the same learning loop:

Orient

Learning objectives
Expected duration
Prerequisites
A short business situation or provocative question

Activate prior knowledge

Prediction question
Short poll
Diagnostic quiz
“What would you do?” scenario

Explain

Short sections rather than long textbook pages
Diagrams, examples and worked calculations
Progressive disclosure using tabs and collapsible blocks

Let students experiment

Sliders and scenario simulators
Interactive charts
Editable R or Python code
Financial statement exploration

Ask students to apply

Mini-case
Calculation
Decision memo
Data interpretation question

Give immediate feedback

Answer hints
Explanations, not only “correct” or “incorrect”
A model solution that students reveal deliberately

Consolidate

Three key takeaways
A retrieval-practice quiz
A transfer question connecting the concept to another company

This structure is more important than adding as many interactive widgets as possible.

2. Recommended Quarto architecture

I would build the course as a Quarto website, with one page per meaningful learning unit. A Quarto website is configured through _quarto.yml, and its rendered HTML and shared resources are assembled into the _site/ directory.

finance-course/
├── _quarto.yml
├── index.qmd
├── syllabus.qmd
├── glossary.qmd
├── references.bib
├── styles.scss
│
├── modules/
│   ├── 01-financial-diagnosis/
│   │   ├── index.qmd
│   │   ├── lesson.qmd
│   │   ├── lab.qmd
│   │   ├── case.qmd
│   │   └── quiz.qmd
│   │
│   ├── 02-value-creation/
│   └── 03-strategy-finance/
│
├── cases/
├── data/
├── images/
├── exercises/
├── solutions/
└── slides/
    ├── day-1.qmd
    ├── day-2.qmd
    └── day-3.qmd

Suggested navigation
# _quarto.yml
project:
  type: website
  output-dir: _site

website:
  title: "Financial Analysis and Corporate Strategy"
  page-navigation: true

  navbar:
    left:
      - text: "Home"
        href: index.qmd
      - text: "Course"
        menu:
          - syllabus.qmd
          - glossary.qmd
      - text: "Modules"
        menu:
          - modules/01-financial-diagnosis/index.qmd
          - modules/02-value-creation/index.qmd
          - modules/03-strategy-finance/index.qmd

  sidebar:
    style: docked
    search: true
    contents:
      - section: "1. Financial diagnosis"
        contents:
          - modules/01-financial-diagnosis/index.qmd
          - modules/01-financial-diagnosis/lesson.qmd
          - modules/01-financial-diagnosis/lab.qmd
          - modules/01-financial-diagnosis/case.qmd
          - modules/01-financial-diagnosis/quiz.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    css: styles.scss
    toc: true
    toc-depth: 3
    code-fold: true
    code-copy: true
    anchor-sections: true
    smooth-scroll: true

execute:
  freeze: auto
  warning: false
  message: false

3. Design each page as a learning sequence

A consistent page template reduces cognitive load. Students know where they are, what is expected and what comes next.

---
title: "Diagnosing profitability"
description: "Understand the drivers of operating profitability."
---

::: {.callout-note title="Learning objectives"}
By the end of this lesson, you should be able to:

1. Distinguish margin and asset-turnover effects.
2. Decompose return on capital employed.
3. Interpret a change in profitability.
4. Formulate a strategic hypothesis from financial data.
:::

::: {.callout-tip title="Before you begin"}
**Estimated time:** 35 minutes  
**Prerequisite:** Income statement and balance-sheet fundamentals
:::

## Opening situation

A retailer's operating margin has fallen, but its return on capital has
increased.

> How could both observations be true?

Write down one hypothesis before continuing.

## Explore the mechanism

...

## Apply it

...

## Check your understanding

...

## Key takeaways

1. ...
2. ...
3. ...


Callouts, tabsets and collapsible elements are native authoring patterns that help organise explanations without displaying everything simultaneously.

4. Use progressive disclosure

Students should make an attempt before seeing the answer.

## Your turn

A company reports:

- EBIT: €42 million
- Revenue: €350 million
- Capital employed: €210 million

Calculate:

1. Operating margin
2. Capital turnover
3. Return on capital employed

::: {.callout-tip collapse="true" title="Hint"}
Start by calculating:

\[
\text{Operating margin} =
\frac{\text{EBIT}}{\text{Revenue}}
\]

and:

\[
\text{Capital turnover} =
\frac{\text{Revenue}}{\text{Capital employed}}
\]
:::

::: {.callout-note collapse="true" title="Show the solution"}
\[
\text{Operating margin} = 42 / 350 = 12\%
\]

\[
\text{Capital turnover} = 350 / 210 = 1.67
\]

\[
\text{ROCE} = 42 / 210 = 20\%
\]

The same result is obtained from:

\[
12\% \times 1.67 \approx 20\%
\]
:::


The important pedagogical detail is that the hint comes before the complete solution.

5. Add scenario-based interactive visualisations

Quarto supports interactive content through Observable JavaScript, Shiny, Jupyter widgets and R htmlwidgets. Observable runs reactively in the browser and therefore works well for lightweight, serverless exploration, while conventional Shiny is suitable when more substantial server-side computation is required.

For financial education, I would prioritise decision-oriented simulations, rather than charts that are interactive merely because they can be.

Example: value-creation simulator with Observable JS
## Value-creation simulator

Move the controls and identify when growth creates or destroys value.

```{ojs}
viewof roce = Inputs.range([0, 30], {
  value: 14,
  step: 0.5,
  label: "Return on capital employed (%)"
})

viewof wacc = Inputs.range([0, 20], {
  value: 9,
  step: 0.5,
  label: "Cost of capital (%)"
})

viewof capital = Inputs.range([10, 500], {
  value: 100,
  step: 10,
  label: "Capital employed (€m)"
})

spread = roce - wacc
economicProfit = capital * spread / 100

html`
  <div class="metric-grid">
    <div class="metric-card">
      <span class="metric-label">Value spread</span>
      <strong>${spread.toFixed(1)} percentage points</strong>
    </div>
    <div class="metric-card">
      <span class="metric-label">Economic profit</span>
      <strong>€${economicProfit.toFixed(1)}m</strong>
    </div>
  </div>
`


A reactive runtime automatically recomputes dependent outputs when the learner changes an input. 【4-3099d8】

Follow the simulation with interpretation prompts:

```markdown
### Interpret your results

1. Set ROCE below WACC. What happens?
2. Double the capital employed while keeping the negative spread.
3. Does growth create or destroy more value?
4. What strategic actions could improve the outcome?


The widget provides the experience. The questions produce the learning.

6. Build interactive charts with a clear analytical purpose

Good financial course interactions include:

Selecting a company and comparing its margins
Filtering ratios by year
Highlighting deviations from a sector median
Changing revenue-growth assumptions
Testing working-capital scenarios
Simulating acquisition synergies
Exploring the effect of leverage on equity returns
Changing WACC and terminal-growth assumptions in a valuation
Reclassifying expenses and observing the effect on EBITDA

A useful pattern is:

Prediction → interaction → explanation → decision

For example:

“Which company appears to create the most value?”
Student chooses an answer.
Student explores ROCE, WACC and growth.
The course explains why growth alone is not sufficient.
Student recommends a capital-allocation decision.
7. Make executable examples reproducible

Quarto can combine Markdown with executable R, Python, Julia and Observable content, making the analysis reproducible when data or assumptions change.

Python example
```{python}
#| label: fig-margin
#| fig-cap: "Operating-margin evolution"
#| echo: true

import pandas as pd
import plotly.express as px

df = pd.read_csv("../../data/company-ratios.csv")

fig = px.line(
    df,
    x="year",
    y="operating_margin",
    color="company",
    markers=True
)

fig.update_yaxes(tickformat=".1%")
fig.show()


## R example

```markdown
```{r}
#| label: tbl-ratios
#| echo: true

library(dplyr)
library(gt)

ratios |>
  mutate(
    operating_margin = ebit / revenue,
    asset_turnover = revenue / capital_employed,
    roce = ebit / capital_employed
  ) |>
  gt() |>
  fmt_percent(
    columns = c(operating_margin, roce),
    decimals = 1
  )


I would provide three modes:

- **Read:** students see the explanation and result
- **Inspect:** students reveal the code
- **Modify:** students change a parameter or complete missing code

Not every student needs to become a programmer. Code should support the discipline, not overshadow it.

---

# 8. Use browser-based coding labs selectively

Shinylive can embed a Shiny application, and optionally its editable source code, directly in a Quarto document. Its editor and viewer components let students modify code and rerun the application in the learning page. 【5-f01c4e】

This is appropriate for exercises such as:

- Completing a ratio-calculation function
- Changing a valuation assumption
- Testing sensitivity to WACC
- Cleaning a small financial dataset
- Reproducing a chart
- Identifying an error in a calculation

However, I would not use browser-based execution everywhere. Large in-browser applications can take time to load and may perform poorly on mobile devices. 【6-48a868】【7-9dacb2】

A sensible hierarchy is:

1. Static explanation
2. Client-side Observable input
3. Lightweight widget
4. Shinylive coding exercise
5. Server-backed Shiny application only when genuinely necessary

---

# 9. Create formative assessments, not just end-of-course quizzes

An engaging course should test students frequently but with low stakes.

## Types of assessment

### Retrieval questions

Ask for a concept from memory:

> What are the two components of ROCE decomposition?

### Interpretation questions

Provide a chart:

> The margin is stable but capital turnover is falling. What is the most plausible financial consequence?

### Calculation questions

Provide a small dataset and ask for a result.

### Error diagnosis

Show an incorrect solution:

> A student divides EBIT by equity to calculate ROCE. Explain the problem.

### Strategic transfer

Ask students to connect finance and strategy:

> Under what conditions could a low-margin business still produce an attractive ROCE?

### Confidence rating

After answering:

> How confident are you: low, moderate or high?

This exposes the difference between a lucky answer and genuine understanding.

Community extensions can add multiple-choice behaviour, including Reveal.js quiz interactions, but they should be assessed for maintenance, accessibility and compatibility before becoming a core dependency. Quarto maintains an extensions directory, while quiz implementations may be third-party projects. 【8-203014】【9-dfea64】

---

# 10. Build rich case studies

For an advanced finance course, the central learning object should be a **case**, not a chapter.

## Example case structure

```text
Case: Should the company acquire its competitor?

1. Situation
2. Available information
3. Financial statements
4. Strategic context
5. Initial decision
6. Analysis workspace
7. New information
8. Revised decision
9. Model solution
10. Reflection


Use staged information release:

::: {.panel-tabset}

## Situation

You are advising the investment committee...

## Financial information

The target reports...

## Strategic information

The target owns...

## Your recommendation

Prepare a recommendation of no more than 150 words.

:::


Then introduce twists:

Synergies are delayed
Working-capital requirements increase
The target loses a major client
Debt financing becomes more expensive
Management identifies an intangible strategic capability

This makes financial analysis a decision process under uncertainty.

11. Connect the website with interactive slides

Quarto can generate Reveal.js presentations containing fragments, animations, previews, widgets and interactive Observable or Shiny components.

I would use:

Website pages for preparation and independent learning
Reveal.js slides for live facilitation
Cases for group application
Short quizzes for retrieval and feedback
Downloadable PDF summaries only as a revision aid

A live session might follow this sequence:

5 min   Opening decision
10 min  Individual prediction
15 min  Concept explanation
20 min  Interactive demonstration
30 min  Group case
10 min  Debrief
5 min   Exit question


The slide deck should link back to the corresponding course page so students can revisit the model after class.

12. Add motivation and orientation features

I would add the following to the homepage:

A visual course map
“Start here” button
Progress checklist for each module
Estimated completion time
Assessment deadlines
Recently updated content
A glossary
A downloadable dataset
A “continue learning” link

Avoid heavy gamification. Instead, use meaningful progress signals:

## Module checklist

- [ ] Complete the diagnostic activity
- [ ] Study the ROCE decomposition
- [ ] Test the value-creation simulator
- [ ] Analyse the company case
- [ ] Submit the decision memo
- [ ] Complete the retrieval quiz


Quarto itself will not automatically turn this into LMS-grade completion tracking. If tracking is necessary, I would connect the course to the institution’s LMS rather than building a fragile custom tracking system.

13. Prioritise accessibility and usability

Interactive does not automatically mean accessible. I would establish these requirements:

Every image has meaningful alternative text
Charts use labels as well as colour
Interactions are keyboard-operable
Answers do not depend exclusively on hovering
Sufficient colour contrast
Clear focus indicators
Mobile-responsive page layouts
Downloadable data behind visualisations
Equations accompanied by verbal interpretations
Transcripts for audio and video
No essential learning hidden only inside an animation
A non-interactive alternative for every critical activity

I would also test every module at three widths:

Desktop
Tablet
Mobile phone
14. Apply a restrained visual system

A course site should look coherent, not decorative.

/* styles.scss */

$primary: #16324f;
$secondary: #2a6f97;
$success: #2f855a;
$warning: #d97706;

.metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-block: 1.5rem;
}

.metric-card {
  border: 1px solid #d9e2ec;
  border-radius: 0.75rem;
  padding: 1.25rem;
  background: #ffffff;
}

.metric-label {
  display: block;
  color: #52606d;
  font-size: 0.9rem;
  margin-bottom: 0.4rem;
}

.learning-objectives {
  border-left: 0.35rem solid $secondary;
  padding-left: 1rem;
}

@media (prefers-reduced-motion: reduce) {
  * {
    scroll-behavior: auto !important;
    transition: none !important;
    animation: none !important;
  }
}


I would restrict the system to:

One primary colour
One accent colour
One warning colour
One success colour
Two font families at most
Consistent spacing
Consistent callout meanings
15. Develop the course in phases
Phase 1: Minimum viable course

Build:

Home page
Syllabus
Course navigation
One complete module
One case study
One interactive chart
One formative assessment
One solution page

Test this with a small group of students before producing the rest.

Phase 2: Standardise

Create reusable templates for:

Lessons
Labs
Cases
Quizzes
Solutions
Slide decks
Phase 3: Add meaningful interactivity

Add only interactions that address observed learning difficulties.

For example:

Learning difficulty	Appropriate interactionStudents confuse margin and turnover	ROCE decomposition simulator
Students mechanically calculate ratios	Interpretation and comparison task
Students do not understand valuation sensitivity	WACC-growth sensitivity interface
Students ignore cash conversion	Interactive operating-cycle diagram
Students struggle to connect finance and strategy	Branching acquisition case
Phase 4: Automate quality control

Use Git and automated publishing to:

Render the site after changes
Detect broken links
Check code execution
Validate data availability
Deploy a preview
Publish only after checks pass
My recommended technology stack

For a robust first version:

Quarto website for the course shell
HTML pages for lessons
Reveal.js for classroom slides
Python or R for reproducible analysis
Observable JS for lightweight reactive simulations
Plotly or htmlwidgets for exploratory charts
Shinylive only for selected editable applications
SCSS for visual consistency
GitHub or GitLab for version control
GitHub Pages, Quarto Pub, Netlify or institutional hosting for deployment
Existing LMS for authentication, submissions, grading and progress tracking

Quarto’s central advantage is that the same source environment can produce websites, presentations, reports, books and other publication formats, while supporting computation and scientific authoring features such as equations, references and cross-references.

The core design principle

The best Quarto course is not the one with the most widgets. It is the one where every interactive element causes the learner to perform a useful cognitive action:

predict,
compare,
calculate,
classify,
diagnose,
decide,
justify,
or revise.

For your three-day**“Analyse financière et stratégie de l’entreprise”** course, I would centre the site on three progressively richer business cases, with short lessons and simulators supplying the concepts students need to resolve each case.
