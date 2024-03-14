---
id: fvuewfpf48hu6w9wkh5udnp
title: opérateurs de comparaison
desc: ''
updated: 1691129167558
created: 1647607777654
---

Les opérateurs de comparaison retourne un [[booléen|py.dt.bool]]. On peut
imaginer qu’ils répondent à une question fermée par oui ou par non.

| Opérateurs | Description                       |
| ---------- | --------------------------------- |
| a == b     | `a` est égal à `b` ?              |
| a != b     | `a` est différent de `b` ?        |
| a < b      | `a` est inférieur à `b` ?         |
| a > b      | `a` est supérieur à `b` ?         |
| a <= b     | `a` est inférieur ou égal à `b` ? |
| a >= b     | `a` est supérieur ou égal à `b` ? |

## On peut facilement comparer des chaînes de charactère

```python
print("apple" == "apple")
print("home" == "homes")
```

Dans le premier cas, python retoune `True` et dans le section `False`.

## Combiner les opérateurs

On peut combiner les opérateurs de comparison grâce aux [[py.op.logic]].
