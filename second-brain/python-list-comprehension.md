---
title: "List comprehension in Python"
created: 2024-04-16
---

## List comprehension

List comprehension in [[python]] is a feature allowing writting [[python-for-loops]]
or [[python-while-loop]] inside [[python-list]], for example:

```python
squares = [n**2 for n in range(10)]
squares
>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Without _list comprehension_ it should have looked like that:

```python
squares = []
for n in range(10):
    squares.append(n**2)
squares
>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Other examples

```python
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets
>>> ['Venus', 'Earth', 'Mars']
```

```python
# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets
>>> ['VENUS!', 'EARTH!', 'MARS!']
```

### Références

[@morrisLearnPythonKaggle]
