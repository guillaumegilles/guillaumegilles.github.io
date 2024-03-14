---
id: hvrc1j29ik1pxtquliibcbr
title: docsting
desc: ''
updated: 1690144655817
created: 1690141803460
---
Une `docstring` est une chaîne de caractère au début de la définition, 
c’est-à-dire *création* d’un module, d’une [[py.function]], d’une classe ou 
d’une méthode. Ou, plus simplement, c’est la documentation d’un objet python.

Les `docstring` sont entourées de 3 guillements doubles : `"""`

```python
def round_to_two_places(num):
    """Return the given number rounded to two decimals places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)
```

Le `docstring` permet d’obtenir la documentation d’un objet python créée par un 
programmeur grâce à la [[py.function]] [[py.function.help]]. Sans celle-ci, `help()` 
retourne une erreur.

### [PEP 257 - Docstrings convention](https://peps.python.org/pep-0257/)