---
title: "For loops in python"
created: 2024-04-16
---

## For loops

Loops are a way to repeatedly execute some code. Here's an example:

```python
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet, end=' ') # print all on same line

>>> Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
```

The `for` loop specifies:

- `for` key word to initiate the loop
- A variable to use, in this case `planet`, which only exist inside the `for`
  loop. It is a temporary variable.
- The set of values to loop over, in this case, `planets`.
- The keyword `in` to link them together.

The object to the right of the `in` can be any object that supports iteration.
Basically, if it can be thought of as a group of things, you can probably loop
over it. We can iterate over the elements of:

- [[python-list]]
- [[python-tuple]]
- [[python-string]]

### Références

[@morrisLearnPythonKaggle]
