---
id: nsexwer1py7fu7gd16r1pxo
title: f-string
desc: >-
  F-string ou formatted string permet de créer des chaînes de charactères avec
  plusieurs data types
updated: 1690267070052
created: 1653664137424
---

Pour concaténer deux [[data types|py.dt]] différents, on ne peut pas utiliser l’[[opérateur arithmétique|py.op.arithmetic]] `+`, on utilise donc une *formatted string*.

```python
new_message = 2
print(f"{new_message} new messages!")
```

Pour qu’une *formatted string* soit correcte, il faut :

- le lettre `f` avant la première guillemet ;
- Une chaîne de caractère ;
- Et différents types de données entre accolades `{}`.
 