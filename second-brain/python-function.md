---
title: Function within python
---

Une fonction [[python]] est un morceaux de code réutilisable qui permet de résoudre
une tâche particulière, comme par exemple, `print()`. Une fonction python est
facilement reconaissable grâce aux parenthèses qui permettent de spécifier les
arguments de la fonction.

```python
print("Hello!")
```

Dans cet exemple, on appelle la fonction `print()` avec l’arguments `"Hello!"`,
ce qui retourne la chaîne de caractères : `Hello!`

### Créer une fonction

Pour initialiser (_créer_) une fonction, la syntaxe est la suivante :

```python
def round_to_two_places(num):
    """Return the given number rounded to two decimals places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)
```

- `def` permet de _définir_ la fonction ;
- `round_to_two_places` est le nom de la fontion qu’on souhaite créer ;
- `(num)` est l’argument associé à cette fonction ;
- `:` indique un nouveau bloc de code, qu’on retrouve ensuite avec
  l’[[cs.indentation]] ;
- `"""Return the given[…]` est la documentation de la fonction dans une
  [[python-docsting]] ;
- `>>>` symbolise le [[cs.command]] prompt de python pour représenter un exemple
  d’utilisation de la fonction ;
- `return` indique ce que retourne la fonction.

À noter, qu’une variable créée à l’intérieur d’une focntion est une
[[py.variable]] locale. C’est-à-dire qu’elle n’existe qu’à l’intérieur de cette
fonction. On ne peut pas lire cette variable dans le reste du script.
