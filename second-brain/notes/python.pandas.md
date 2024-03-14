---
id: bam7pb731rxqgj1syflrg7r
title: "🗂 Pandas"
desc: "Présentation et cheat sheet pour le package Pandas"
tags: anki
updated: 1703074564856
created: 1654705589479
---

`pandas` is an fast, powerful, flexible, open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools built on top of the [Python](https://www.python.org/) programming language.

### Références

- [1]: https://learn.deeplearning.ai/pandas/lesson/1/introduction

- [Python for Data Analysis (3e)](https://wesmckinney.com/book/)
- [DeepLearning.AI Pandas](https://learn.deeplearning.ai/pandas/lesson/1/introduction)
- [Kaggle Learn Pandas](https://www.kaggle.com/learn/pandas)
- [pandas website](https://pandas.pydata.org/)
- [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)

## Quelles sont les structures de données de pandas ?

<!-- notecardId: 1701642275234 -->

- `DataFrame`
  ![pandas dataframe](assets/pandas-dataframe.png)
- `Series`

[#Python]() [#Pandas]()

## Importer le _package_ pandas ?

<!-- notecardId: 1701642275264 -->

```python
>>> import pandas as pd
```

Par convention, on utilise le raccourci `pd` pour faire référence à la librairie `pandas` par la suite.

[#Python]() [#Pandas]()

## Lire un fichier CSV (**C**omma-**S**eparated **V**alues)

<!-- notecardId: 1701642275271 -->

```pyhton
>>> df = pd.read_csv("data/titanic.csv")
```

## Afficher les premières lignes d'un DataFrame avec Pandas

<!-- notecardId: 1701642275279 -->

```pyhton
>>> df.head()
```

Par défaut, `pandas` retourne les **5 premières** lignes. On peut modifier cette affichage par défaut, en ajoutant un paramètre à la méthode, `df.head(10)`. [DeepLearning.AI Pandas][1]

## Afficher les dernières lignes d'un DataFrame

<!-- notecardId: 1701642275283 -->

```pyhton
>>> df.tail()
```

Par défaut, `pandas` retourne les **5 dernières** lignes. On peut modifier cette affichage par défaut, en ajoutant un paramètre à la méthode, comme `df.tail(10)`

## Connaître la taille d'un DataFrame.

<!-- notecardId: 1701642275289 -->

```python
>>> df.shape
```

Il n'est pas nécessaire de saisir les `()` après `shape`, car il s'agit d'un **attribut** et non une fonction ou une méthode.

## Générer les statistiques descriptives d'une Series ou d'un DataFrame.

<!-- notecardId: 1701642275301 -->

```python
>>> df.describe()
```

## Générer des informations d'un DataFrame comme l'index, le dtype, les noms de colonnes, les valeurs non nulles, etc.

<!-- notecardId: 1701642275305 -->

```python
>>> df.info()
```

## Retourner la liste des colonnes

<!-- notecardId: 1701642275310 -->

```python
>>> df.columns
```

Il s'agit d'un attribut et non pas une fonction ou une méthode, il ne faut pas ajouter les `()`

## Générer un sous-ensemble d'un DataFrame sous la forme d'un nouveau `DataFrame`

<!-- notecardId: 1701642275314 -->

```python
>>> df[['title of columns', 'blabla']]
```

- `df[]` : notation de Pandas pour sélectionner des colonnes
- `['title of columns', 'blabla']` : une liste Python pour indiquer quelles sont les colonnes sélectionnées

## Sélectionner aléatoirement des lignes d'un DataFrame

<!-- notecardId: 1701642275318 -->

```python
>>> df.sample(5)
```

## Fixer la graine pour la génération aléatoire de 'pd.sample()`

'random_state = 123'

```python
>>> df.sample(5, random_state = 345)
```

## drop()

<!-- notecardId: 1701642275367 -->

> Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level

```python

```

### Références

- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop

---

[panda cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

--- fillna

Dans la grande majorité des datasets on trouve des valeurs manquantes, `Na`, `NaN`. On peut remplacer ces « non-valeurs » grâce à la méthode `fillna()`

```python
compte_cheque['Debit'].fillna(0, inplace = True) # replacing missing values in Debit column with 0
compte_cheque['Credit'].fillna(0, inplace = True) # replacing missing values in Credit column with 0
```

L’argument `inplace=True` modifie directement la variable sans avoir besoin de l’appler à nouveau. Ainsi :

```python
compte_cheque['Debit'] = compte_cheque['Debit'].fillna(0)
```

Devient :

```python
compte_cheque['Debit'].fillna(0, inplace = True)
```

--- pd.options

```python
pd.options.display.float_format = '{:.5f}'.format
pd.options.display.max_rows = 100
```

- `display.max_rows` : [[pt.dt.int]]

  If max_rows is exceeded, switch to truncate view. Depending on `large_repr`,
  objects are either centrally truncated or printed as a summary view. `None`
  value means unlimited.

- `display.float_format` : callable

  The callable should accept a floating point number and return a string with
  the desired format of the number. This is used in some places like
  SeriesFormatter. See `formats.format.EngFormatter` for an example.
  [default: None] [currently: None]

-- read_cvs()

## charger un fichier csv

<!-- notecardId: 1701642275374 -->

```python
df = pd.read_csv('~/filename.csv')
```

des arguements permettent d’apporter plus de fonctionalités à la fonction
`read_csv()` :

- `sep =` permet de sélectionner un autre type de séparateur que la virgule par
  défaut, `,` ;
- `index_col = "column_name"` pour utiliser une colonne du [[py.ds.dataframe]]
  en tant qu’[[index]], plutôt que la valeur par défaut, `0`.
- `parse_dates = ['date']` indique la colonne servant d’indice pour les
  [ds.time-serie]].

```python
compte_cheque = pd.read_csv("~/filename.csv",
                            sep = ";",
                            index_col = "date operation")
```

```{python}
df = pd.read_csv("train.csv", parse_dates = ['date'])
```

### références

- [pandas.org](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

--- replace

## WIP !!!

<!-- notecardId: 1701642275378 -->

```python
import pandas as pd

compte_cheque = compte_cheque.replace(to_replace='NaN', value=0)
```

--- title: value_counts()

Pour compter le nombre de valeurs on peut utiliser la [[Méthode|py.method]] `.value_counts()` :

```python
compte_cheque['Debit', 'Credit'].value_counts()
```
