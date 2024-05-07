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

## Connaître la taille d'un DataFrame.

<!-- notecardId: 1701642275289 -->

```python
>>> df.shape
```

Il n'est pas nécessaire de saisir les `()` après `shape`, car il s'agit d'un
**attribut** et non d’une fonction ou une méthode.

## Générer des stats descriptives d'une Series ou d'un DataFrame Pandas.

<!-- notecardId: 1701642275301 -->

```python
>>> df.describe()
```

## Retourne les informations d'un DataFrame comme l'index, le dtype, les noms de

colonnes, les valeurs non nulles, etc.

<!-- notecardId: 1701642275305 -->

```python
>>> df.info()
```

## Retourne la liste des colonnes.

<!-- notecardId: 1701642275310 -->

```python
>>> df.columns
```

Il s'agit d'un attribut et non pas une fonction ou une méthode, il ne faut pas
ajouter les `()`.

## Retourne un sous-ensemble d'un DataFrame sous la forme d'un nouveau `DataFrame`

<!-- notecardId: 1701642275314 -->

```python
>>> df[['title of columns', 'blabla']]
```

- `df[]` : notation de Pandas pour sélectionner des colonnes
- `['title of columns', 'blabla']` : une liste Python pour indiquer quelles sont
  les colonnes sélectionnées.

## Sélectionner aléatoirement des lignes d'un DataFrame.

<!-- notecardId: 1701642275318 -->

```python
>>> df.sample(5)
```

## Fixer la graine du générateur aléatoire de `pd.sample()`

`random_state = 123`

```python
>>> df.sample(5, random_state = 123)
```

## Supprimer des colonnes ou des lignes d’un dataframe Pandas

<!-- notecardId: 1701642275367 -->

`drop()`

> Remove rows or columns by specifying label names and corresponding axis, or
> by specifying directly index or column names. When using a multi-index, labels
> on different levels can be removed by specifying the level

```python
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
```

```python
# Drop columns
>>> df.drop(['B', 'C'], axis=1)
   A   D
0  0   3
1  4   7
2  8  11
```

```python
# Drop columns
>>> df.drop(columns=['B', 'C'])
   A   D
0  0   3
1  4   7
2  8  11
```

```python
# Drop a row by index
>>> df.drop([0, 1])
   A  B   C   D
2  8  9  10  11
```

## charger un fichier `csv` avec Pandas

<!-- notecardId: 1701642275374 -->

```python
df = pd.read_csv('~/filename.csv')
```

## Quels sont les principaux paramètres de la fonction `read_csv()` de Pandas ?

- **`sep =`** permet de sélectionner un autre type de séparateur que la virgule
  par défaut, `,` ;
- **`index_col = "column_name"`** pour utiliser une colonne du en tant qu’index,
  plutôt que la valeur par défaut, `0`.
- **`parse_dates = ['date']`** indique la colonne servant d’indice pour les _time
  series_.

```python
df = pd.read_csv("train.csv",
                 sep = ";",
                 index_col = "index",
                 parse_dates = ['date'])
```

## Comment gérer les `NA/NaN` avec Pandas

On peut remplacer les valeurs manquantes grâce à la méthode `fillna()`.

```python
>>> df
     A    B   C    D
0  NaN  2.0 NaN  0.0
1  3.0  4.0 NaN  1.0
2  NaN  NaN NaN  NaN
3  NaN  3.0 NaN  4.0
```

```python
>>> df.fillna(0)
     A    B    C    D
0  0.0  2.0  0.0  0.0
1  3.0  4.0  0.0  1.0
2  0.0  0.0  0.0  0.0
3  0.0  3.0  0.0  4.0
```
