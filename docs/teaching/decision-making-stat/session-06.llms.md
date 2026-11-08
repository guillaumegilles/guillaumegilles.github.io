This session reviews the main numerical summaries used to describe a dataset before moving to inferential statistics.

## 1 Why this reminder matters

> **NOTE:**
>
> The objective of this session is to perform a reminder of some numerical summaries associated with describing the data. These numerical summaries were covered during the **data description** course (first year, semester 2). Mastering these calculations is essential for the rest of the course.

> **WARNING:**
>
> In this session we do **not** impose any probabilistic hypothesis on the data. We are only interested in **describing** the observations through numerical summaries.

## 2 Terminology

> **NOTE:**
>
> - An **individual** is an element of the population.
> - A **population** is a set of elements sharing one or more characteristics.
> - A population is **finite** if the exact number of individuals can be determined; otherwise it is **infinite**.

## 3 Types of variables

| Type | Description | Examples |
|----|----|----|
| Qualitative — Nominal | Categories with no natural order | Hair color, nationality |
| Qualitative — Ordinal | Categories with a natural order | Satisfaction level (low/medium/high) |
| Quantitative — Discrete | Countable numeric values | Number of people per household |
| Quantitative — Continuous | Any value in an interval | Waiting time, height |

> **NOTE:**
>
> In this session, we focus only on **quantitative/measurable variables**. We do not use the adjective **random** here because the goal is pure description.

> **CAUTION:**
>
> Find the nature of the following variables:
>
> 1.  Hair color of hair salon customers
> 2.  The level of customer satisfaction of a telephone operator
> 3.  The number of people in Parisian households
> 4.  The exact waiting time on the phone before being answered by the technical service of an internet provider

> **CAUTION:**
>
> 1.  Hair color → **qualitative nominal**
> 2.  Satisfaction level → **qualitative ordinal**
> 3.  Number of people per household → **quantitative discrete**
> 4.  Exact waiting time → **quantitative continuous**

## 4 Frequency tables

A frequency table summarizes the data using:

> **TIP:**
>
> - \\k\\: number of distinct modalities
> - \\n_i\\: absolute frequency of modality \\i\\
> - \\f_i = \dfrac{n_i}{n}\\: relative frequency
> - \\N_i = \sum\_{j=1}^{i} n_j\\: cumulative absolute frequency
> - \\F_i = \dfrac{N_i}{n}\\: cumulative relative frequency

### 4.1 What is a modality?

> **NOTE:**
>
> A **modality** is a category or observed value. There are \\k\\ modalities, with \\1 \leq k \leq n\\. For quantitative variables, modalities are arranged in ascending order.

### 4.2 Example 1 — Discrete quantitative variable

Grades (out of 20) of 24 candidates in a competition:

11; 13; 8; 16.5; 11; 7; 13; 12; 11; 12; 12; 8; 11; 8; 12; 11; 7; 16.5; 8; 11; 8; 12; 8; 16.5

A frequency table is:

|   Grade |     7 |     8 |    11 |    12 |    13 |  16.5 |
|--------:|------:|------:|------:|------:|------:|------:|
| \\n_i\\ |     2 |     6 |     6 |     5 |     2 |     3 |
| \\f_i\\ | 0.083 | 0.250 | 0.250 | 0.208 | 0.083 | 0.125 |

### 4.3 Example 2 — Continuous variable

Monthly net salary data for 24 candidates may be summarized into classes such as \\\[1500,2000\[\\, \\\[2000,2500\[\\, and so on.

> **WARNING:**
>
> For a continuous variable, the modalities are **class intervals**, not exact values.

## 5 Numerical summaries

### 5.1 Mean

> **TIP:**
>
> For raw data:
>
> \\ \bar{x} = \frac{1}{n}\sum\_{i=1}^{n} x_i \\
>
> For grouped data:
>
> \\ \bar{x} = \frac{1}{n}\sum\_{i=1}^{k} x_i n_i = \sum\_{i=1}^{k} x_i f_i \\
>
> For continuous classes, use the **class midpoint** \\c_i\\ in place of \\x_i\\.

### 5.2 Variance and standard deviation

> **TIP:**
>
> Variance:
>
> \\ \sigma^2 = \frac{1}{n}\sum\_{i=1}^{k} n_i(x_i-\bar{x})^2 = \frac{1}{n}\sum\_{i=1}^{k} n_i x_i^2 - \bar{x}^2 \\
>
> Standard deviation:
>
> \\ \sigma = \sqrt{\sigma^2} \\

### 5.3 Coefficient of variation

> **TIP:**
>
> \\ CV = \frac{\sigma}{\bar{x}} \times 100\\ \\
>
> Interpretation guide:
>
> - \\CV \< 15\\\\: low variability
> - \\15\\ \leq CV \leq 35\\\\: moderate variability
> - \\CV \> 35\\\\: high variability

> **WARNING:**
>
> The coefficient of variation is mainly meaningful for variables measured on a **strictly positive scale**. For temperatures in degrees Celsius, the interpretation must be made with caution because the origin is arbitrary and the mean can be close to \\0\\.

> **IMPORTANT:**
>
> For grouped data, never forget the **class midpoint**. It is the standard approximation used to compute the mean and the variance.

## 6 Handling open classes

When the first or last class is open, we close it by convention.

> **NOTE:**
>
> - The first open class receives the width of the second class.
> - The last open class receives the width of the second-to-last class.
> - If this convention goes outside the definition domain of the variable, use the domain to close the class.

### 6.1 Examples

- If the first two classes are \\\[\<4500\[\\ and \\\[4500,5500\[\\, then the first class becomes \\\[3500,4500\[\\.
- If the last class is \\\[\geq 8000\[\\ and the previous width is \\2500\\, then it becomes \\\[8000,10500\[\\.

## 7 Exercises

### 7.1 Exercise 1 — Morning temperature

> **CAUTION:**
>
> We studied the morning temperature (measured between 7am and 7:30am) over 200 randomly chosen winter days from the last 20 years. The data are summarized below.
>
> | Temperature (°C) | Number of days |
> |------------------|---------------:|
> | \[-10, -5\[      |             12 |
> | \[-5, 0\[        |             38 |
> | \[0, 5\[         |             62 |
> | \[5, 10\[        |             55 |
> | \[10, 15\[       |             33 |
>
> Calculate the mean, standard deviation, and coefficient of variation. Comment on the homogeneity of the data.

> **CAUTION:**
>
> Use the class midpoints:
>
> \\ -7.5,\\-2.5,\\2.5,\\7.5,\\12.5 \\
>
> with frequencies \\12,38,62,55,33\\.
>
> Mean:
>
> \\ \bar{x} = \frac{12(-7.5)+38(-2.5)+62(2.5)+55(7.5)+33(12.5)}{200} = 3.975 \\
>
> Standard deviation:
>
> \\ \sigma \approx 5.652 \\
>
> Coefficient of variation:
>
> \\ CV = \frac{5.652}{3.975}\times 100\\ \approx 142.2\\ \\
>
> Comment: the dispersion is **very high**. The data are clearly **heterogeneous**. Since the variable is temperature in °C, this large CV must also be interpreted with caution.

### 7.2 Exercise 2 — Morning wind speed

> **CAUTION:**
>
> We studied the morning wind speed (measured between 7am and 7:30am, in km/h) over 240 randomly chosen winter days from the last 20 years. The data are summarized below.
>
> | Wind speed (km/h) | Number of days |
> |-------------------|---------------:|
> | \[0, 20\[         |             48 |
> | \[20, 40\[        |             72 |
> | \[40, 60\[        |             60 |
> | \[60, 80\[        |             42 |
> | \[80, 100\[       |             18 |
>
> Calculate the mean, standard deviation, and coefficient of variation. Comment.

> **CAUTION:**
>
> Use the class midpoints:
>
> \\ 10,\\30,\\50,\\70,\\90 \\
>
> with frequencies \\48,72,60,42,18\\.
>
> Mean:
>
> \\ \bar{x} = \frac{48(10)+72(30)+60(50)+42(70)+18(90)}{240} = 42.5 \\
>
> Standard deviation:
>
> \\ \sigma \approx 23.953 \\
>
> Coefficient of variation:
>
> \\ CV = \frac{23.953}{42.5}\times 100\\ \approx 56.4\\ \\
>
> Comment: the variability is **high** (\\CV\>35\\\\), so the wind speed data are **heterogeneous**.
