---
id: fhyra02mly9qdv74l84004b
title: Manipulation
desc: ''
updated: 1648155862450
created: 1648155862450
---

Une [[liste|py.dt.list]] python n’est pas immuable, on peut la manipuler :

1. Modifier un élément 

```python
heihg = [1.74, 1.89, 1.46, 1.62]
heigh[1] = 1.87
```

Le deuxième élément de la liste, d’indice `1`, est désormais remplacé par `1.87`

2. Ajouter ou retirer un élément

```python
heihg = [1.74, 1.89, 1.46, 1.62]
heigh + [1.87]
```

On ajoute un nouveau élément, `1.87` qui se place en fin de liste à l’indice `4` dans notre exemple.

```python
heihg = [1.74, 1.89, 1.46, 1.62]
del(heigh[1])
```

En utilisant la fonction python [[del()|py.function.del]] on peut supprimer des éléments d’une liste en précisant l’indice.
