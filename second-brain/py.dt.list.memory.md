---
id: 0agf2jlsu9gjaq99qylqgm6
title: Memory
desc: ''
updated: 1648245887735
created: 1648245887735
---

```python
x = ["a", "b", "c"]
y = x
y[1] = "z"
y
```

Dans cet exemple, les variables `y` **et** `x` retournent la liste `["a", "z", "c"]` car les deux variables font références à la même liste dans l’espace mémoire. En effet avec `y = x` on copie la référence à la liste et non pas les valeurs de la liste. Lorsqu’on modifie un élément de la liste, `y` et `x` font toujours référence à la même liste.

Si on veut créer une variable `y` qui pointe vers une nouvelle liste dans l’espace, avec les mêmes données, on utilise la fonction `list()`

```python
x = ["a", "b", "c"]
y = list(x)
```
