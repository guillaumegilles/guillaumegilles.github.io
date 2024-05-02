---
# Foam YAML metadata
title: "📇 Pandas"
type: Anki card
tags: [Anki, Pandas, Python]
# Foam template YAML metadata
---

## Quelles sont les structures de données de pandas ?

<!-- notecardId: 1701642275234 -->

- `DataFrame`
  ![Pandas dataframe](/assets/images/pandas-dataframe.png)
- `Series`
  ![Pandas series](/assets/images/pandas-series.png)

## Importer le _package_ pandas ?

<!-- notecardId: 1701642275264 -->

```python
>>> import pandas as pd
```

Par convention, on utilise le raccourci `pd` pour faire référence à la librairie
`pandas` par la suite.

## Lire un fichier CSV (**C**omma-**S**eparated **V**alues)

<!-- notecardId: 1701642275271 -->

```python
>>> df = pd.read_csv("data/titanic.csv")
```

## Afficher les premières lignes d'un DataFrame avec Pandas

<!-- notecardId: 1701642275279 -->

```python
>>> df.head()
```

La méthode `.head()` de Pandas retourne, par défaut, les **5 premières** lignes.
On peut modifier cette affichage en ajoutant un paramètre à la méthode,
`df.head(10)`.

## Afficher les dernières lignes d'un DataFrame grâce à Pandas

<!-- notecardId: 1701642275283 -->

```python
>>> df.tail()
```

La méthode `.tail()` de Pandas retourne, par défaut, les **5 dernières** lignes.
On peut modifier cette affichage en ajoutant un paramètre à la méthode, comme
`df.tail(10)`.
