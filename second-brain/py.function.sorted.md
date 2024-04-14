---
id: xgckcm2k64sxw5zvn79q4eu
title: sorted()
desc: ''
updated: 1648332082605
created: 1648332082605
---

On peut ranger en ordre croissant ou décroissant les éléments d’une [[liste|python.list]] grâce à la fonction `psorted()`. Cette fonction possède plusieurs arguments :

- `iterable` est la variable contenant la liste ;
- `key=None`
- `reverse=False` permet de ranger en odre croissant. La fonction `sorted()` est définie croissante par défaut. Pour qu’elle retourne un ordre décroissant, on passe l’argument `reverse=True`.


```python
In [1]:
help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
```
