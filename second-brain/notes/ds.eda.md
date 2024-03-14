---
id: ueogqqwb1fyr3765a3lgq7e
title: analyse exploratoire des données
desc: exploratrory data analysis
updated: 1702850252380
created: 1670186830427
---

### Python

Pour charger les données on utilise la fonction package `pandas` [[py.pandas.read]]

![[py.pandas.read]].

### Etudier les variables

On peut inspecter rapidement un [[dataframe pandas]], grâce à la [[méthode]] `head()`

```python
adult_census.head()
```

A partir de cette visualisation, on peut définir la variable cible, qui est la variable qu'on cherche à prédire. Dans notre cas, il s'agit `<=50K` et `>50K`. Le résultat de la prédictionThe est donc, une [[classification binaire]].

```python
[in]    target_column = "class"
        adult_census[target_column].value_counts()

[out]   <=50K    37155
        >50K     11687
        Name: class, dtype: int64
```

Avec la ùéthode [[head]] on s'aperçoit qu'il y a des données [[math.data.continuous]] et des données [[math.data.categorical]]. Il est donc nécessaire 

```python
numerical_columns = [
    "age",
    "education-num",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
]
categorical_columns = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
all_columns = numerical_columns + categorical_columns + [target_column]

adult_census = adult_census[all_columns]
```

Pour vérifier le nombre de *samples* et le nombre de *variables* ou colonne, grâce à la méthode [[shape]].

```python
[in]    print(
        f"The dataset contains {adult_census.shape[0]} samples and "
        f"{adult_census.shape[1]} columns"
        )

[out]   The dataset contains 48842 samples and 14 columns
```

### Visualiser la distribution des variables

#### hist() et value.count()

Dans un premier temps, on peut regarder la distributioin des *features* grâce à la méthode [[hist() des dataframe pandas]]. Attenttion, celle-ci ne fonctinne que sur les *features* numérique du dataframe.

```python
_ = adult_census.hist(figsize=(20, 14))
```

> In the previous cell, we used the following pattern: _ = func(). We do this to avoid showing the output of func() which in this case is not that useful. We actually assign the output of func() into the variable _ (called underscore). By convention, in Python the underscore variable is used as a "garbage" variable to store results that we are not interested in.

Pour les données catégorielles, on utilise la méthode [[value.counts()]]

```python
[in]    adult_census["sex"].value_counts()

[out]   Male      32650
        Female    16192
        Name: sex, dtype: int64

[in]    adult_census["education"].value_counts()

[out]   HS-grad         15784
        Some-college    10878
        Bachelors        8025
        Masters          2657
        Assoc-voc        2061
        11th             1812
        Assoc-acdm       1601
        10th             1389
        7th-8th           955
        Prof-school       834
        9th               756
        12th              657
        Doctorate         594
        5th-6th           509
        1st-4th           247
        Preschool          83
        Name: education, dtype: int64
```

#### Seaborn

Une autre façon de visualiser les données est d'utiliser un *pairplot* grâce à la librairie [[python.seaborn]] afin d'étudier les variables selon la *target*, à savoir "class".

```python
import seaborn as sns

# We will plot a subset of the data to keep the plot readable and make the
# plotting faster
n_samples_to_plot = 5000
columns = ["age", "education-num", "hours-per-week"]
_ = sns.pairplot(
    data=adult_census[:n_samples_to_plot],
    vars=columns,
    hue=target_column,
    plot_kws={"alpha": 0.2},
    height=3,
    diag_kind="hist",
    diag_kws={"bins": 30},
)
```

### Création "manuelle" de règles de décision

En étudiant le *pairplot* [[python.seaborn]], on eut créer des règle de décisions manuellement afin de prédire le revenue en fonction des variables `hours-per-week` et `age`.features.

```python
_ = sns.scatterplot(
    x="age",
    y="hours-per-week",
    data=adult_census[:n_samples_to_plot],
    hue=target_column,
    alpha=0.5,
)
```

```python
import matplotlib.pyplot as plt

ax = sns.scatterplot(
    x="age",
    y="hours-per-week",
    data=adult_census[:n_samples_to_plot],
    hue=target_column,
    alpha=0.5,
)

age_limit = 27
plt.axvline(x=age_limit, ymin=0, ymax=1, color="black", linestyle="--")

hours_per_week_limit = 40
plt.axhline(y=hours_per_week_limit, xmin=0.18, xmax=1, color="black", linestyle="--")

plt.annotate("<=50K", (17, 25), rotation=90, fontsize=35)
plt.annotate("<=50K", (35, 20), fontsize=35)
_ = plt.annotate("???", (45, 60), fontsize=35)
```

In the region age < 27 (left region) the prediction is low-income. Indeed, there are many blue points and we cannot see any orange points.
In the region age > 27 AND hours-per-week < 40 (bottom-right region), the prediction is low-income. Indeed, there are many blue points and only a few orange points.
In the region age > 27 AND hours-per-week > 40 (top-right region), we see a mix of blue points and orange points. It seems complicated to choose which class we should predict in this region.
It is interesting to note that some machine learning models will work similarly to what we did: they are known as decision tree models. The two thresholds that we chose (27 years and 40 hours) are somewhat arbitrary, i.e. we chose them by only looking at the pairplot. In contrast, a decision tree will choose the "best" splits based on data without human intervention or inspection. Decision trees will be covered more in detail in a future module.

Note that machine learning is often used when creating rules by hand is not straightforward. For example because we are in high dimension (many features in a table) or because there are no simple and obvious rules that separate the two classes as in the top-right region of the previous plot.

To sum up, the important thing to remember is that in a machine-learning setting, a model automatically creates the "rules" from the existing data in order to make predictions on new unseen data.


## Références

- https://lms.fun-mooc.fr/courses/course-v1:inria+41026+session03/courseware/ea2a140204de4e7fbc316fd96a163c7f/a2b98877a11b4fd6aa594cc8035d6149/

- note zettel (qmd) pour un template ml workflow