---
id: 24w0gx54yg7nu7zxskcnvk3
title: random
desc: 'numpy.random'
updated: 1691385596890
created: 1691385175428
---

## `numpy.random.default_rng`

`default_rng` is the recommended constructor for the random number class Generator. 
Here are several ways we can construct a random number generator using 
`default_rng` and the Generator class.

### Generate a random float

```python
>>> import numpy as np
>>> rng = np.random.default_rng(12345)
>>> print(rng)
Generator(PCG64)

>>> rfloat = rng.random()
>>> rfloat
0.22733602246716966

>>> type(rfloat)
<class 'float'>
```

### Generate 3 random integers between 0 (inclusive) and 10 (exclusive)

```python
>>> import numpy as np
>>> rng = np.random.default_rng(12345)
>>> rints = rng.integers(low=0, high=10, size=3)
>>> rints
array([6, 2, 7])

>>> type(rints[0])
<class 'numpy.int64'>
```

### Specify a seed so that we have reproducible results

```python
>>> import numpy as np
>>> rng = np.random.default_rng(seed=42)
>>> print(rng)
Generator(PCG64)

>>> arr1 = rng.random((3, 3))
>>> arr1
array([[0.77395605, 0.43887844, 0.85859792],
       [0.69736803, 0.09417735, 0.97562235],
       [0.7611397 , 0.78606431, 0.12811363]])
```

If we exit and restart our Python interpreter, we’ll see that we generate the 
same random numbers again:

```python
>>> import numpy as np
>>> rng = np.random.default_rng(seed=42)
>>> arr2 = rng.random((3, 3))
>>> arr2
array([[0.77395605, 0.43887844, 0.85859792],
       [0.69736803, 0.09417735, 0.97562235],
       [0.7611397 , 0.78606431, 0.12811363]])
```


## Références

- [NumPy documentation](https://numpy.org/doc/stable/reference/random/generator.html)