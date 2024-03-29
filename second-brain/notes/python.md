---
id: 2hlm3ji51oz29h8eokj1lzk
title: Python
desc: "Langage de programmation Python"
updated: 1701039495491
created: 1648117073423
---

## syntaxe

### nom de variables

Pour déclarer les [[variables|computer-science#variables]] il existe plusieurs conventions. En
python, on utilise le **snake case**. Les noms de variables sont en minuscules et
les espaces sont représentés par des `_`.

```python
nom_prenom = "Guillaume Gilles"
```

### nom des constantes

Pour déclarer une constante, la syntaxe est une capitale

```python
SEED = 2023
```

### bloc de code

un bloc de code est facilement reconnaissable grâce aux deux-points, `:` et l’
[[cs.indentation]].

```python
if spam_amount > 0:
    print("Buy more honey!")
```

En python, l’[[cs.indentation]] est de **4** espaces.

## Libraries

Pour enrichir les fonctionalités de Python, on peut utiliser des [[[fonctions|py.function]], des [[méthodes|py.method]] et on peut avoir besoin de [[type de données|py.dt]] spécifique. Pour ça, il existe des **packages**, paquets. On peut imaginer ces modules supplémentaires comme des dossiers dans lesquels des scripts python sont répertoriés. Il existe des centaines de packages :

- NumPy ;
- Matplotlib
- scikit learn
- [[py.math]]

### Pour importer un package

```python
import numpy as np
```

> `as np` permet de simplifier la syntaxe suivante

### Pour utiliser une fonctionalité de `NumPy` :

```python
np.array([1, 2, 3])
```

### Si on ne souhaite que quelques fonctionalités d’un package, on peut utiliser la syntaxe :

```python
from numpy import array
array([1, 2, 3])
```

Dans ce cas il n’est plus nécessaire de spécifier `np.array` comme avant.
