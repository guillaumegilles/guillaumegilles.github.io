---
id: 413s2128awtwb5qgt2g5fye
title: Slice
desc: Découper une liste pour en créer une nouvelle
updated: 1655758255610
created: 1648133268824
---

On peut créer une nouvelle [[liste|python.list]] à partir d’une liste déjà existante. C’est ce qu’on appelle découper *slicing* une liste.

on utilise les [[indices|py.dt.list.index]] et la syntaxe est la suivante :

```python
[ start  :  end ]
inclusif   exclusif
```

![list slicing](assets/images/python-list-slicing.png)

```python
heihg = [1.74, 1.89, 1.46, 1.62]
heigh[1:3]
heigh[1:]
heigh[:3]
```

- `heigh[1:3]` retourne les valeurs : `1.89` et `1.46` ;
- `heigh[1:]` retourne toutes les valeurs en commençant à partir de l’indice `1`, soit : `1.89`, `1.46` et `1.62` ;
- `heigh[:3]` retourne toutes les valeurs jusqu’à l’indice `3` sans l’inclure soit : `1.74`, `1.89` et `1.46`.
