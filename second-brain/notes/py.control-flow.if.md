---
id: xfw8pt7lm72rdvlekx3x2in
title: if statement
desc: control flow avec if
updated: 1691042748458
created: 1647854458152
---

la déclararion (*statement*) conditionnelle `if` permet de contrôler l’exécution 
d’un [[bloc de code|python#bloc-de-code]] selon la valeur d’un [[booléen|py.dt.bool]].

### si *et seulement si*

```python
def inspect(x):
    if x == 0:
        print(x, "is zero")
```

En python, le bloc de code `True` doit toujours être présent, mais le bloc 
`False` est optionnel.

### si *ou sinon* avec **elif**

```python
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
```

Les blocs `elif` sont optionnels, ils permettent d’ajouter des conditions, si 
nécessaires.

> If you’re comparing the same value to several constants, or checking for 
> specific types or attributes, you may also find the `match` statement useful.

### si *ou sinon..., sinon* avec **else**

```python
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")
```

## Références :

- [Kaggle learn](https://www.kaggle.com/code/colinmorris/booleans-and-conditionals/#Conditionals)
- [Python documenttion](https://docs.python.org/3/tutorial/controlflow.html#if-statements)