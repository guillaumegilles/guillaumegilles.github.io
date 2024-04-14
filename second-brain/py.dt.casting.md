---
id: ua74jjga4g2d9bifk5x6uz0
title: casting
desc: ''
updated: 1691124944421
created: 1648128926545
---

*casting* permet de convertir un type de donnée en autre type de donnée, comme 
par exemple [[True|py.dt.bool]] en [[1|py.dt.int]].

```python
print("I started with " + saving + " €. Awesome!")
```

Cette commande renvoie une erreur, car la [[Variable|py.variable]] `saving` est 
[[numérique|py.dt.int]]. On ne peut pas ajouter des [[chaînes de charactère|py.dt.str]] 
avec des nombres. En utilisant, le *casting* on convertit, momentanément, 
le type de données pour permettre la [[py.dt.str.concatenation]] :

- [[py.base.int]]
- [[py.base.float]]
- [[py.base.str]]
- [[py.base.bool]]

```python
print("I started with " + str(saving) + " €. Awesome!")
```
