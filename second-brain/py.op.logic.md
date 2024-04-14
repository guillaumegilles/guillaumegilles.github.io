---
id: l5rbm1zb6lel7c3uk35mh5v
title: opérateurs logiques
desc: 'opérateurs logiques : not / and / or'
updated: 1691128811028
created: 1647608364586
---

## `not`

retourne l’opposé de ce qu’on lui passe en argument.

```python
not True
```

retourne `False`

## `and`

```python
True and False
```

Retourne `False`, car l’opérateur `and` retourne `True` uniquement si, 
**et seulement si**, les deux conditions sont `True`, sinon python retourne `False`.

## `or`

```python
True or False
```

Retourne `True`, car avec l’opérateur `or` si l’une des conditions est `True`, 
python retourne `True`. Pour obtenir `Flase` il faut que toutes les conditions 
soient `Fasle`

## Ordres des opérateurs logiques

Dans la [[syntaxe|python#syntaxe]], il existe un ordre des opérateurs logiques. `not` 
est évalué en premier, puis `and` et finalement `or`.

```python
prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday
```

Dans cet exemple, il est difficile de comprendre rapidement la logique de ces 
conditions. Pour simplifier la lecture, on peut utiliser des parenthèses :

```python
prepared_for_weather = (
    have_umbrella 
    or ((rain_level < 5) and have_hood) 
    or (not (rain_level > 0 and is_workday))
)
```
