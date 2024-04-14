---
id: poslojvfbzmv3uiqsfutp29
title: Index
desc: Accéder aux éléments des listes grâce aux indices
updated: 1655758351917
created: 1648132322984
---

Les [[listes|python.list]] python peuvent devenir rapidement longues pour accéder aux éléments, on utilise l’indice.

![python index list](/assets/images/python-list.png)

Le premier élément se trouve à l’indice 0, le deuxième à l’indice 1, etc.

```python
heihg = [1.74, 1.89, 1.46, 1.62]
heigh[1]
heigh[-3]
```

Les deux commandes `heigh[1]` et `heigh[-3]` retourne le même élément : `1.89`

## Accéder à un élément d’une sous-liste

```python
family = [["Helen", 1.56],
          ["Jerry", 1.83],
          ["George", 1.74],
          ["Kramer", 1.89]]
```

Pour accéder à la taille de George, le deuxieme élément de la troisième sous-liste, la syntaxe est :

```python
family[2][1]
```
