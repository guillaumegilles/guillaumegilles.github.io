---
title: NumPy Array
---

Une array est un type de données spécifique au package [[numpy]] créer à partir
de sous-listes de [[python-list]].

```python
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

np_2darray
>    ([[ 1.73,  1.68,  1.71,  1.89,  1.79],
      [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])

np_2d.shape
>    (2, 5) # 2 rows, 5 columns
```

```python
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
type(np_height)
>    numpy.ndarray
```

Lorsqu'on appelle la fonction `type()`, elle retourne : `numpy.ndarray`. Dans
_ndarray_, `nd` signifie qu'on peut créer des arrays à
[[plusieurs dimensions|py.package.numpy.2d-array]], 2d, 3d, 7d, etc.
