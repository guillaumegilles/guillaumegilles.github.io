You are probably asking yourself the question, “When and where will I use statistics?”. If you read any newspaper, watch television, or use the Internet, you will see statistical information. There are statistics about crime, sports, education, politics, and real estate. Typically, when you read a newspaper article or watch a television news program, you are given sample information. With this information, you may make a decision about the correctness of a statement, claim, or “fact.” Statistical methods can help you make the “best educated guess.”

Since you will undoubtedly be given statistical information at some point in your life, you need to know some techniques for analyzing the information thoughtfully. Think about buying a house or managing a budget. Think about your chosen profession. The fields of economics, business, psychology, education, biology, law, computer science, police science, and early childhood development require at least one course in statistics.

> ## 1 The business question
>
> A food-truck owner opens a spreadsheet with 120 rows of daily data: `weather`, `temperature`, `customers`, `items sold`, `revenue`, etc. Before computing any number or drawing any chart, what *kind* of information is in each column? Does “weather” behave like “revenue”? Can you average “satisfaction rating”? This module teaches you to look at a dataset and answer those questions, the first step in every statistical analysis. We start with five days small enough to read at a glance, and only then name the concepts.

### 1.1 Numbers that are not numbers

Here are five days from the Wandering Fork dataset. The numbers are a simplified extract chosen so that you can read everything at a glance.

| Day | Weather | Temp. (°C) | Satisfaction (1–5) | Customers | Revenue (€) |
|-----|---------|-----------:|-------------------:|----------:|------------:|
| 1   | Sunny   |         18 |                  4 |        38 |         400 |
| 2   | Cloudy  |         22 |                  3 |        44 |         440 |
| 3   | Rainy   |         16 |                  2 |        47 |         480 |
| 4   | Sunny   |         20 |                  3 |        41 |         440 |
| 5   | Sunny   |         24 |                  3 |        40 |         440 |

Four of the five columns contain numbers, and the spreadsheet will happily average any of them. Would you trust the average of the satisfaction column as much as the average of the revenue column? What could you even compute for the weather column?

## 2 What is Statistics?

> **IMPORTANT:**
>
> The science of statistics deals with the collection, analysis, interpretation, and presentation of data. The goal of statistics is not to perform numerous calculations using the formulas, but to gain an understanding of your data. The calculations can be done using a calculator or a computer. The understanding must come from you. If you can thoroughly grasp the basics of statistics, **you can be more confident in the decisions you make in life**.

### 2.1 Descriptive vs Inferential Statistics

**Descriptive statistics** are about organizing and summarizing data that you already have at hand and make no claim about any larger group. There are two ways to summarize data: 1. Graph representation 2. Numbers, for example, finding an average

On the other hand **Inferential statistics** uses probability to determine how confident we can be that our conclusions are correct. After you have studied probability and probability distributions, you will use formal methods for drawing conclusions from “good” data. The formal methods are called inferential statistics.

> **TIP:**
>
> Decide for each statement whether it only summarises the five days you hold (descriptive) or goes beyond them (inferential), and compute the number in the first one.
>
> 1.  “Over these five days, the average revenue was €?”
> 2.  “Over all 120 days, the average revenue is about the same.”
> 3.  “Day 3 was the best of these five days.”
>
> Check your answer
>
> 1.  Average revenue: $(400 + 440 + 480 + 440 + 440)/5 = 2{,}200/5 = 440$. So €440 only summarises the five days; it is a **descriptive** statistics.
> 2.  The claim about all 120 days is **inferential statistics** because the five days are used to say something about days we did not look at.
> 3.  “Day 3 was the best of these five” is **descriptive statistics**.
>
> In plain words if you have the revenue of all 120 trading days and you compute the average, that is descriptive statistics. But if you have *onlly* 30 days and you estimate the average of **all possible** trading days, that is inferential statistics.

### 2.2 Population, Individual, and Sample

In statistics, we generally want to study a **population**. You can think of a population as a collection of persons, things, or objects under study, in other words, a set of elements being studied. A statistical **individual** is one element of the population.

To study the population, we select a **sample**. The idea of sampling is to select a portion, or a subset, of the larger population and study that portion, **the sample**, to gain information about the population. Data are the result of sampling from a population.

> **TIP:**
>
> Look at the table of the five days above and fill in the blanks. Be Careful, the `Day` column only labels the rows; it is not a variable we analyse.
>
> 1.  What is one row?
> 2.  How many individuals are there?
> 3.  If these five days are *all* we care about, how many members does the population have?
>
> Check your answer
>
> - A row is one **statistical individual**. Reading across one row describes one individual.
> - There are **5** individuals.
> - The population has **5** individuals. In the real dataset, the Harbour truck’s population is 120 days.

In plain words the population is everything you want to talk about and an individual is one item of it.

> **CAUTION:**
>
> In statistics, a population is usually written as an uppercase $N$ for the population **size** (number of individuals) : e.g., $N = 250{,}000$. And for contrast, a sample uses lowercase $n$ for size, for example $n = 5$ for the example above.
>
> In case we would like to talk about the third individual of the dataset we would write, $N_3$ for population and $n_3$ for sample.

Because it takes a lot of time and money to examine an entire population, sampling is a very practical technique. If you wished to compute the overall grade point average at your school, it would make sense to select a sample of students who attend the school.

The data collected from the sample would be the students’ grade point averages. In presidential elections, opinion poll samples of 1,000–2,000 people are taken. The opinion poll is supposed to represent the views of the people in the entire country. Manufacturers of canned soda drinks take samples to determine if a 33 cl can contains really 33 cl of soda drink.

### 2.3 What is a Statistic

A **statistic** (be careful singular) is a number that represents a property of the Sample. For example, if we consider one math class to be a sample of the population of all math classes, then the average number of points earned by students in that one math class at the end of the term is an example of a statistic.

The statistic is an estimate of a population **parameter**, in this case the mean. A parameter is a numerical characteristic of the whole population that can be estimated by a statistic. Since we considered all math classes to be the population, then the average number of points earned per student over all the math classes is an example of a parameter.

One of the main concerns in the field of statistics is how accurately a statistic estimates a parameter. **The accuracy of statistics depends on how well the sample represents the population**.

The sample must contain the characteristics of the population in order to be a representative sample. We are interested in both the sample statistic and the population parameter in inferential statistics.

### 2.4 Variables

A variable is a characteristic or measurement that can be determined for each member of a population. Variables may be **numerical** or **categorical**.

#### Numerical

Numerical variables take on values with equal units such as weight in kg and time in hours. If we let $X$ equal the number of points earned by one math student at the end of a term, then $X$ is a numerical variable.

We could do some math with values of $X$ like calculate the average number of points earned, for example.

#### Categorial

Categorical variables place the person or thing into a category. If we let $Y$ be a person’s party affiliation, then some examples of $Y$ include Republican, Democrat, and Independent. $Y$ is a categorical variable.

It makes no sense to do math with values of $Y$, calculating an average party affiliation makes no sense.

> **CAUTION:**
>
> Lowercase $x$ for the variable measured, with subscripts for individuals (or $Y$, $X$ when we talk about the \[\[Random Variable\]\]). A **variable** is a characteristic observed on each individual (e.g., `weather`, `daily_revenue_eur`).

> **TIP:**
>
> Determine what the key terms refer to in the following study.
>
> > We want to know the average (mean) amount of money first year college students spend at ABC College on school supplies that do not include books. We randomly surveyed 100 first year students at the college. Three of those students spent 150€, 200€, and 225€, respectively.
>
> Check your answer
>
> - The **population** is all first year students attending ABC College this term.
> - The **sample** could be all students enrolled in one section of a beginning statistics course at ABC College (although this sample may not represent the entire population).
> - The **parameter** is the average (mean) amount of money spent (excluding books) by first year college students at ABC College this term: the population mean.
> - The **statistic** is the average (mean) amount of money spent (excluding books) by first year college students in the sample.
> - The **variable** could be the amount of money spent (excluding books) by one first year student. Let $X$ = the amount of money spent (excluding books) by one first year student attending ABC College.

### 2.5 Data

**Data** are the actual values of the variable. They may be numbers or they may be words. **Datum** is a single value. Data may come from a population or from a sample and most data can be put into two categories, **qualitative** or **quantitative**.

#### Qualitative Data

Qualitative data are the result of categorizing or describing attributes of a population. Qualitative data are also often called *categorical data*.

Hair color, blood type, ethnic group, the car a person drives, and the street a person lives on are examples of qualitative (categorical) data. Qualitative (categorical) data are generally described by words or letters. For instance, hair color might be black, dark brown, light brown, blonde, gray, or red. Blood type might be AB+, O-, or B+.

#### Quantitative Data

Quantitative data are always numbers. Quantitative data are the result of **counting** or **measuring** attributes of a population. Amount of money, pulse rate, weight, number of people living in your town, and number of students who take statistics are examples of quantitative data. Quantitative data may be either **discrete** or **continuous**.

##### Quantitative Discrete Data

All data that are the result of counting are called **quantitative discrete data**. These data take on only certain numerical values. If you count the number of phone calls you receive for each day of the week, you might get values such as zero, one, two, or three.

##### Quantitative Continuous Data

Data that are not only made up of counting numbers, but that may include fractions, decimals, or irrational numbers, are called **quantitative continuous data**. Continuous data are often the results of measurements like lengths, weights, or times. A list of the lengths in minutes for all the phone calls that you make in a week, with numbers like $2.4$, $7.5$, or $11.0$, would be quantitative continuous data.

> **CAUTION:**
>
> Lowercase $x$ are used to represent data values, with subscripts for individuals. Therefore $x_i$ is the value of a variable for the $i$-th individual. For example, the revenue for the first and third individuals are $x_1 = 400€$ and $x_3 = 480€$.

Researchers often prefer to use **quantitative data** over qualitative (categorical) data because it lends itself more easily to mathematical analysis. For example, it does not make sense to find an average hair color or blood type.

> **TIP:**
>
> > You go to the supermarket and purchase three cans of soup (500 gs tomato bisque, 450 g lentil, and 550 g Italian wedding), two packages of nuts (walnuts and peanuts), four different kinds of vegetable (broccoli, cauliflower, spinach, and carrots), and two desserts (300 g pistachio ice cream and 600 g ounces chocolate chip cookies).
>
> Name **data sets** that are quantitative discrete, quantitative continuous, and qualitative (categorical).
>
> Check your answer
>
> One Possible Solution: - The three cans of soup, two packages of nuts, four kinds of vegetables and two desserts are **quantitative discrete data** because you count them. - The weights of the soups (500 g, 450 g, and 550 g) are **quantitative continuous data** because you measure weights as precisely as possible. - Types of soups, nuts, vegetables and desserts are **qualitative (categorical) data** because they are categorical.

A statistics professor collects information about the classification of her students as first-year students, sophomores, juniors, or seniors. The data she collects are summarized in the pie chart Figure 1.2. What type of data does this graph show?

``` js
data = [
  { category: "A", value: 30 },
  { category: "B", value: 25 },
  { category: "C", value: 20 },
  { category: "D", value: 15 },
  { category: "E", value: 10 }
]

Plot.plot({
  height: 300,
  marks: [
    Plot.arc(data, Plot.groupZ({
      y: "sum"
    }, {
      x: 1,
      y: "value",
      fill: "category",
      stroke: "white",
      theta: d => (d.value / d3.sum(data, d => d.value)) * 2 * Math.PI,
      innerRadius: 0
    })),
    Plot.text(data, Plot.groupZ({
      x: "mean"
    }, {
      x: 1,
      y: "value",
      theta: d => (d.value / d3.sum(data, d => d.value)) * 2 * Math.PI,
      text: "category",
      fontSize: 12
    }))
  ],
  color: { legend: true }
})
```

**Try it.** Classify each column of the five-day extract. For a qualitative variable, say nominal or ordinal; for a quantitative one, say discrete or continuous.

| Variable | Categories or numbers? | Nominal / ordinal, or discrete / continuous? |
|----|----|----|
| `weather` | ? | ? |
| `satisfaction_rating` | ? | ? |
| `customer_count` | ? | ? |
| `temperature_c` | ? | ? |
| `daily_revenue_eur` | ? | ? |

Check your answer

| Variable | Categories or numbers? | Subtype |
|----|----|----|
| `weather` | categories (qualitative) | nominal: no natural order |
| `satisfaction_rating` | categories (qualitative) | ordinal: 1 \< 2 \< 3 \< 4 \< 5 |
| `customer_count` | numbers (quantitative) | discrete: you count customers |
| `temperature_c` | numbers (quantitative) | continuous: any value in an interval |
| `daily_revenue_eur` | numbers (quantitative) | continuous |

`satisfaction_rating` is written with numbers but behaves like ordered categories.

- Categories or numbers?
  - Categories (**qualitative**): is there a natural order?
    - No → **nominal** (`weather`)
    - Yes → **ordinal** (`satisfaction_rating`)
  - Numbers (**quantitative**): countable or measured?
    - Countable → **discrete** (`customer_count`)
    - Measured on a scale → **continuous** (`temperature_c`, `daily_revenue_eur`)

> **NOTE:**
>
> A qualitative variable is **nominal** if its categories have no natural order (e.g., `weather`, `promo_active`). It is **ordinal** if the categories have a natural order (e.g., `satisfaction_rating`: 1 \< 2 \< 3 \< 4 \< 5). The order matters, but the *distances* between categories are not necessarily equal.

> **NOTE:**
>
> A quantitative variable is **discrete** if its possible values are countable (e.g., `customer_count`: 39, 38, 38, …). It is **continuous** if it can take any value in an interval (e.g., `daily_revenue_eur`, `temperature_c`).

### 2.6 Levels of measurement

**Try it.** For each question about the five-day extract, say whether it makes sense and, if it does, give the result.

| Question | Makes sense? | Result |
|----|----|----|
| Most frequent `weather` | ? | ? |
| Middle value (median) of `satisfaction_rating` | ? | ? |
| Average `temperature_c` | ? | ? |
| Revenue on day 3 divided by revenue on day 1 | ? | ? |
| Day 5 (24 °C) is “one and a half times as warm” as day 3 (16 °C) | ? | ? |

Check your answer

| Question | Makes sense? | Result |
|----|----|----|
| Most frequent `weather` | yes (count, mode) | Sunny (3 of 5 days) |
| Median of `satisfaction_rating` | yes (order exists) | sorted 2, 3, 3, 3, 4 → 3 |
| Average `temperature_c` | yes (differences are meaningful) | $100/5 = 20$ °C |
| Revenue day 3 ÷ day 1 | yes (true zero) | $480/400 = 1.2$ |
| “1.5 times as warm” | **no** | $24/16 = 1.5$ is computed, but 0 °C is not “no temperature” |

Each question needed a little more from the data than the one before: counting, then order, then differences, then a true zero.

**See it.** Each level keeps everything the level above it allows and adds one permission:

| Level | Count, mode | Order, median | Differences, mean | Ratios |
|----|:--:|:--:|:--:|:--:|
| Nominal (`weather`) | ✓ | ✗ | ✗ | ✗ |
| Ordinal (`satisfaction_rating`) | ✓ | ✓ | ✗ | ✗ |
| Interval (`temperature_c`) | ✓ | ✓ | ✓ | ✗ |
| Ratio (`daily_revenue_eur`) | ✓ | ✓ | ✓ | ✓ |

In plain words: each level of measurement adds one thing you may do with the values — count, then order, then subtract, then divide.

> **TIP:**
>
> | Level | Example | Allowed operations |
> |----|----|----|
> | **Nominal** | `weather`, `promo_active` | Count, mode, `=`, `≠` |
> | **Ordinal** | `satisfaction_rating`, `month` | Everything nominal + order (`<`, `>`), median, percentiles |
> | **Interval** | Temperature in °C (no true zero) | Everything ordinal + addition/subtraction of differences, mean, standard deviation |
> | **Ratio** | `daily_revenue_eur`, `customer_count`, `temperature` in Kelvin | Everything interval + multiplication/division, ratios, geometric mean, coefficient of variation |
>
> In plain words: you can always count and find the mode. With ordinal data you can also sort and find the median. With interval data you can add and subtract differences (so the mean makes sense). With ratio data you can also multiply and divide (so ratios like “twice as much” and the coefficient of variation make sense). Most business data are ratio.

#### Notation decoder: the four levels

| Symbol | Read aloud | In our example (five-day extract) |
|----|----|----|
| `=`, `≠` | “equals”, “is different from” | Day 1 and day 4 are both Sunny; Sunny ≠ Rainy |
| `<`, `>` | “is less than”, “is greater than” | rating on day 3 (2) \< rating on day 1 (4) |
| $x_i - x_j$ | “x sub i minus x sub j” | temperature: $22 - 18 = 4$ °C warmer |
| $x_i / x_j$ | “x sub i divided by x sub j” | revenue: $480/400 = 1.2$ times as much |
| Nominal, ordinal, interval, ratio | the four levels | `weather`, `satisfaction_rating`, `temperature_c`, `daily_revenue_eur` |

**Whole table as a sentence:** “a nominal variable can only be counted and compared with equals; an ordinal one can also be ordered with less than and greater than; an interval one can also be subtracted; a ratio one can also be divided.”

**A common trap.** `satisfaction_rating` is stored as the numbers 1, 2, 3, 4, 5, but it is **ordinal**, not ratio. The step from 1 to 2 is not necessarily the same as from 4 to 5. Computing an arithmetic mean of satisfaction ratings is technically questionable — the median is safer. Module 4 discusses this in detail.

## 3 Worked example

We use the **Harbour 30-day subset** (sheet `harbour_30d`) to illustrate the concepts of this module.

| Column | Type | Level | Example values (first 5 days) |
|----|----|----|----|
| `weather` | Qualitative, nominal | Nominal | Cloudy, Sunny, Rainy, Cloudy, Sunny |
| `temperature_c` | Quantitative, continuous | Interval | 21.9, 20.4, 16.4, 18.5, 24.1 |
| `customer_count` | Quantitative, discrete | Ratio | 39, 38, 38, 38, 53 |
| `daily_revenue_eur` | Quantitative, continuous | Ratio | 460.48, 500.02, 418.65, 508.80, 646.19 |
| `satisfaction_rating` | Qualitative, ordinal | Ordinal | 3, 4, 2, 3, 4 |

**Step 1 — population and individual.** The population is the 30 trading days of the Harbour truck (finite). Each row is one statistical individual (one franchise-day).

**Step 2 — variable classification.** `weather` is qualitative nominal (categories with no order). `temperature_c` is quantitative continuous (any value in an interval). `customer_count` is quantitative discrete (countable integers). `daily_revenue_eur` is quantitative continuous (ratio level, true zero). `satisfaction_rating` is qualitative ordinal (ordered categories, unequal steps).

**Step 3 — allowed operations.** For `weather` you can count and find the mode (Sunny appears most often). For `temperature_c` you can compute the mean and standard deviation (interval level). For `daily_revenue_eur` you can also compute ratios (e.g., “day 5 revenue is 1.5× day 3 revenue”) and the coefficient of variation (ratio level).

## 4 Proof / derivation

> **CAUTION:**
>
> Let a qualitative variable have $k$ categories with absolute frequencies $n_1, \dots, n_k$ and total $n = \sum_{i=1}^{k} n_i$. The relative frequency of category $i$ is $f_i = n_i / n$. Summing over all categories: $$\sum_{i=1}^{k} f_i
> = \sum_{i=1}^{k} \frac{n_i}{n}
> = \frac{1}{n}\sum_{i=1}^{k} n_i
> = \frac{n}{n}
> = 1.$$ In percentages, $\sum f_i \times 100\% = 100\%$. This is exactly the same property we saw for percentage distributions in the Excel warm-up (Module 1’s derivation), now applied to categories instead of line items. If your frequency table’s percentages do not sum to (very close to) 100%, a category was missed or a count was wrong.

## 5 Visual intuition

Think of the population as a bag of coloured balls. A **qualitative** variable is the colour of each ball — you can sort them into piles (nominal) or line them up by shade (ordinal). A **quantitative** variable is a number written on each ball — you can count them (discrete) or measure them on a ruler (continuous). The level of measurement tells you which ruler you are allowed to use: a ruler with no numbers (nominal), a ruler with only order marks (ordinal), a ruler with equal spacing but no true zero (interval), or a ruler with a true zero (ratio).

## 6 Interactive demo

> **IMPORTANT:**
>
> TODO: an interactive variable-type classifier (drag a column name to its type and level) would be a good OJS demo for this module.

## 7 Exercises

All exercises below are done by hand; the Excel ones are in the [homework](#homework-excel-lab).

**Exercise 1 (Classify the variables)** For each column of the Wandering Fork dataset, state: (a) qualitative or quantitative? (b) if qualitative: nominal or ordinal? (c) if quantitative: discrete or continuous? (d) level of measurement?

Solution

See the data dictionary table in the Theory section above. For example: `weather` → qualitative, nominal, nominal level; `customer_count` → quantitative, discrete, ratio level; `satisfaction_rating` → qualitative, ordinal, ordinal level.

**Exercise 2 (Population and individual)** A marketing manager wants to know the average basket size of customers who visited the shop last month. The shop had 2,450 transactions last month. What is the population? What is the statistical individual? What is the variable of interest?

Solution

Population = the 2,450 transactions (finite). Statistical individual = one transaction. Variable of interest = basket size (quantitative, continuous, ratio level).

**Exercise 3 (Levels of measurement and allowed operations)** For each variable, say whether the operation makes sense: (a) Mean of `weather`. (b) Median of `satisfaction_rating`. (c) Ratio of two `daily_revenue_eur` values (e.g., “today’s revenue is 1.3× yesterday’s”). (d) Difference of two `temperature_c` values (e.g., “today is 3°C warmer than yesterday”).

Solution

1.  No — `weather` is nominal, no mean. (b) Yes — ordinal data have a median. (c) Yes — revenue is ratio, ratios are meaningful.
2.  Yes — temperature in °C is interval, differences are meaningful (but ratios are not, because 0°C is not “no temperature”).

**Exercise 4 (Descriptive vs inferential)** A company surveys 500 customers and finds that 62% are satisfied. Is this descriptive or inferential? What if the company has 10,000 customers total and uses the 62% to estimate how many of the 10,000 are satisfied?

Solution

The 62% from the 500 surveyed is descriptive (it summarises the sample). Using it to estimate the 10,000 is inferential (it draws a conclusion about the population).

**Exercise 5 (Formula to words)** In the five-day extract, let $x_i$ be the revenue, $t_i$ the temperature and $n_i$ the number of days in a category. Read each expression aloud as one sentence and say which level of measurement it needs. (a) $x_3 / x_1 = 1.2$. (b) $t_2 - t_1 = 4$. (c) $f_{\text{Sunny}} =
n_{\text{Sunny}} / n = 3/5$.

Solution

1.  “Revenue on day 3 is 1.2 times revenue on day 1” — a ratio, so the ratio level. (b) “Day 2 was 4 °C warmer than day 1” — a difference, so at least the interval level. (c) “The relative frequency of Sunny is the number of Sunny days divided by the total number of days, which is 3 out of 5” — counting only, so any level, even nominal.

**Exercise 6 (Words to formula)** Write in symbols: (a) “revenue on day 3 is 1.2 times revenue on day 1”; (b) “the relative frequency of category $i$ is its count divided by the total”; (c) “the $k$ relative frequencies add up to 1”.

Solution

1.  $x_3 = 1.2\,x_1$ (with $x_1 = 400$ and $x_3 = 480$).
2.  $f_i = n_i / n$. (c) $\sum_{i=1}^{k} f_i = 1$.

## 8 Common mistakes

> **WARNING:**
>
> - **Treating ordinal numbers as ratio.** `satisfaction_rating` is 1–5, but `=AVERAGE` on it is questionable; use the median.
> - **Forgetting to lock the total in a percentage distribution.** The denominator must be absolute (`$D$8`) or a structured reference (`tblFork[daily_revenue_eur]`), otherwise copying the formula shifts the total.
> - **Confusing the population with the sample.** The 120 Harbour days are a *finite population* in this course. In real life, they would often be a *sample* of all possible trading days.
> - **Using `COUNT` when you need `COUNTA`.** `COUNT` only counts numbers; `COUNTA` counts everything non-empty (text, dates, errors).

## 9 Exit check

Five minutes, no calculator needed.

1.  In one sentence, what is the difference between descriptive and inferential statistics?
2.  A shop lists the 200 sales of last Saturday with the amount of each sale. What are the population, the individual and the variable?
3.  Read $x_3 / x_1 = 1.2$ aloud as a sentence, where $x_i$ is the revenue on day $i$. Which level of measurement does it need?
4.  The ratings of five days are 4, 3, 2, 3, 3. Compute the median, and say why the mean is less safe.
5.  Why is temperature in °C an interval variable and not a ratio variable?

Answers

1.  Descriptive statistics summarise the data you hold; inferential statistics use a sample to draw conclusions about a larger population you did not fully observe.
2.  Population: the 200 sales (finite); individual: one sale; variable: the amount of the sale.
3.  “Revenue on day 3 is 1.2 times revenue on day 1.” A ratio needs the ratio level (a true zero).
4.  Sorted: 2, 3, 3, 3, 4, so the median is 3. Ratings are ordinal: the distances between 1, 2, 3, 4, 5 are not necessarily equal, so an average of them is questionable.
5.  Differences of temperatures are meaningful (4 °C warmer), but 0 °C is not “no temperature”, so “24 °C is 1.5 times as warm as 16 °C” has no meaning.

## 10 Homework — Excel lab

Reproduce, in Excel, what you did by hand in class, with `SUM`, `COUNT`, `COUNTA`, `AVERAGE` and `IF`, then apply them to the full dataset.

**Estimated time:** about 45–60 minutes. Any spreadsheet application works, at home or in a campus computer room.

**Follow-up:** a 10-minute debrief at the start of [Module 2](module-02.qmd). Bring your Step 0 results and any question on Homework 1–2.

### 10.1 Using Excel

The complete list of function names, with their French equivalents, is on the [Excel functions](../../teaching/data-description/excel-functions.llms.md) page.

| Concept | Excel function / steps |
|----|----|
| Open the data | **Data → Get Data → From Text/CSV** (for `.csv`) or double-click `wandering-fork.xlsx` |
| Cell reference | `A1` (relative), `$A$1` (absolute), `$A1` or `A$1` (mixed); press F4 to cycle |
| Sum of a range | `=SUM(range)` |
| Count of numbers | `=COUNT(range)` |
| Count of non-empty cells | `=COUNTA(range)` |
| Average | `=AVERAGE(range)` |
| Conditional value | `=IF(condition, value_if_true, value_if_false)` |
| Sort | Select the table → **Data → Sort** |
| Filter | Select the table → **Data → Filter** (or **Table → Filter**) |
| English vs French locale | English Excel uses commas between arguments (`SUM(A1,A2)`); French Excel uses semicolons (`SOMME(A1;A2)`). Function names also differ — see the Excel functions page. |

> **TIP:**
>
> Type `=AVERAGE(` in a cell. If Excel suggests `AVERAGE`, you are in English locale. If it suggests `MOYENNE`, you are in French locale. The course writes all formulas with English names; use the Excel functions page to translate.

### 10.2 Step 0 — check your class results

1.  Type the five revenues 400, 440, 480, 440, 440 in `A2:A6` and the five weather values Sunny, Cloudy, Rainy, Sunny, Sunny in `B2:B6`.
2.  Compute `=SUM(A2:A6)`, `=COUNT(A2:A6)`, `=COUNTA(A2:A6)` and `=AVERAGE(A2:A6)`; then `=COUNT(B2:B6)` and `=COUNTA(B2:B6)`.
3.  In `C2` type `=IF(B2="Sunny",1,0)`, copy it down to `C6`, and compute `=SUM(C2:C6)`.
4.  Compare every result with your hand computation.

Expected results

| Indicator                             | Revenue (`A2:A6`) | Weather (`B2:B6`) |
|---------------------------------------|------------------:|------------------:|
| `SUM`                                 |             2,200 |                 — |
| `COUNT`                               |                 5 |                 0 |
| `COUNTA`                              |                 5 |                 5 |
| `AVERAGE`                             |               440 |                 — |
| `SUM` of the `IF` column (Sunny days) |                 — |                 3 |

`COUNT` finds no numbers in the weather column, while `COUNTA` counts the five non-empty cells.

### 10.3 Homework 1 (Excel) — Open the dataset and explore

Open `wandering-fork.xlsx`. (a) Filter `franchise` to “Harbour”. How many rows? (b) In column N (`daily_revenue_eur`), compute `=SUM`, `=COUNT`, `=COUNTA`, `=AVERAGE` for the filtered rows. (c) Sort by `daily_revenue_eur` descending. What is the highest revenue day for Harbour?

Solution

1.  120 rows (all Harbour days). (b) `SUM` ≈ 49,618.46, `COUNT` = 120, `COUNTA` = 120, `AVERAGE` ≈ 413.49. (c) The highest Harbour revenue is €1,050.00 (day 80).

### 10.4 Homework 2 (Excel) — English vs French function names

Your colleague uses French Excel. You send them the formula `=AVERAGE(N2:N121)`. What must they change it to?

Solution

`=MOYENNE(N2:N121)` (function name) and the argument separator becomes a semicolon if the range is written with cell references: `=MOYENNE(N2;N121)` — but structured references like `tblFork[daily_revenue_eur]` work the same in both locales. See the QExcel functions page for the full list.

## 11 Further reading

| Source | Where | What it adds | Time | Verified |
|----|----|----|----|----|
| OpenStax IBS 2e | §1.1 *Definitions of Statistics, Probability, and Key Terms* (book pages 5–10) | Formal definitions of population, sample, parameter, statistic | ~5 pages | checked against the PDF contents (T046) |
| OpenStax IBS 2e | §1.2 *Data, Sampling, and Variation in Data and Sampling* (book pages 10–22) | Sampling methods, variation, qualitative vs quantitative | ~12 pages | checked against the PDF contents (T046) |
| OpenStax IBS 2e | §1.3 *Levels of Measurement* (book pages 22–30) | The four levels with examples | ~8 pages | checked against the PDF contents (T046) |
| Khan Academy | Unit *Study design* in the [Statistics and probability course](https://www.khanacademy.org/math/statistics-probability); look for lessons on statistical questions, sampling methods, and types of studies | Videos and practice on population vs sample, observational studies vs experiments | ~30–45 min (estimate) | link check pending (T048) |

OpenStax IBS 2e: Alexander Holmes, Barbara Illowsky and Susan Dean, *Introductory Business Statistics 2e*, OpenStax, Rice University, <https://openstax.org/details/books/introductory-business-statistics-2e>, licensed under CC BY-NC-SA 4.0. Sections are cited, not reproduced.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {1️⃣ {What} Are Statistics?},
  url = {https://ggilles.dev/teaching/data-description/statistics.html},
  langid = {en},
  abstract = {**By the end of this module, you will be able to:** -
    Distinguish descriptive statistics (summarising what happened) from
    inferential statistics (drawing conclusions about a larger
    population). - Identify the population, the statistical individual,
    and the variable in a business context. - Classify a variable as
    qualitative (nominal or ordinal) or quantitative (discrete or
    continuous). - State the four levels of measurement (nominal,
    ordinal, interval, ratio) and explain which arithmetic operations
    each allows. - Read aloud simple notation such as \$x\_i\$, \$n\$,
    \$f\_i = n\_i/n\$ and \$\textbackslash sum\$, and write it from a
    sentence. - Open the Wandering Fork dataset, recognise its grain
    (one row = one franchise-day), and perform basic Excel operations:
    cell references, sorting, filtering, and the functions `SUM`,
    `COUNT`, `COUNTA`, `AVERAGE`, `IF` (homework).}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “1️⃣ What Are Statistics?” <https://ggilles.dev/teaching/data-description/statistics.html>.
