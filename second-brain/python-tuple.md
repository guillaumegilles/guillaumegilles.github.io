---
title: "Tuples in Python"
created: 2024-04-16
---

## Tuples

Tuples, in [[python]] are almost exactly the same as [[python-list]]. They
differ in just two ways:

1. The syntax for creating them uses parentheses, `()`, instead of square
   brackets, `[]`.

```python
t = (1, 2, 3)
t
>>> (1, 2, 3)
```

2. They cannot be modified, they are **immutable**

## Used as [[python-function]]

Tuples are often used for functions that have multiple return values. For
example, the `as_integer_ratio()` [[python-method]] of float objects returns a
numerator and a denominator in the form of a tuple:

```python
x = 0.125
x.as_integer_ratio()
>>> (1, 8)
```

### Références

[@morrisLearnPythonKaggle]
