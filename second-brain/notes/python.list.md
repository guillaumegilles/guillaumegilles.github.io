---
id: 5jtutdyj90no8dl8cde4zo9
title: list
desc: ""
updated: 1711630049685
created: 1648129865308
---

Structure de données. de type [[array|computer-science##quest-ce-quune-array]].
Il n’est facile de représenter les tailles, en cm, d’une population dans des variables.

```python
heigh1 = 1.74
heigh2 = 1.89
heigh3 = 1.46
heigh4 = 1.62
```

Ça peut être très fastidieux… Avec python, on peut utiliser un type de données beaucoup plus simple dans ce cas, la **liste**.

```python
[1.74, 1.89, 1.46, 1.62]
```

- Une liste peut être affectée à une [[variable|py.variable]] ;
- Elle peut contenir n’importe quel autres [[type de donnée|cs.lang.python.data-types]] python.

```python
family = [["Helen", 1.56],
          ["Jerry", 1.83],
          ["George", 1.74],
          ["Kramer", 1.89]]
```

Les liste dans [[python]] représente une suite de valeurs.

```python
primes = [2, 3, 5, 7]
planets = [“Mercury”, “Venus”, “Earth”, “Mars”, “Jupiter”, “Saturn”, “Uranus”, “Neptune”]
```

Pour rechercher un élément d’une liste, on peut utiliser des crochets `variable[x]`
où `x` est l’index numérique de la valeur recherché (0, 1, 2, 3, etc.). Dans
Python, les index numériques débutent à 0. Les éléments à la fin des listes sont
accessibles grâce aux entiers négatifs (-1, -2, -3, etc.)

```python
Planets[0]
Planets[2]
Planets[-1]

Out[9]:
  “Mercury”
  “Earth”
  “Neptune”
```

Il est possible de découper une liste

```python
planets[0:3]

Out[9]:
  ['Mercury', 'Venus', 'Earth']
```

Grâce à `[0:3]`, on demande à python de nous retourner tous les éléments d’une
liste, en commençant par le premier, d’index ‘0’ pour s’arrêter au quatrième d’
index ‘3’. Il est important de garder en tête que dernier élément d’index ‘3’ n’
est pas inclus. Python nous retourne donc les trois élément, d’index ‘0’, ‘1’ et ‘2’.

```python
planets[:3]

Out[9]:
  ['Mercury', 'Venus', 'Earth']
```

En laissant le premier élément vide, on sous-entend à python de commercer le
découpage au début de la liste, c’est une autre façon de coder : ‘planets[0:3]’

```python
planets[3:]

Out[11]:
  ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

Dans cet exemple, on demande à python denous retourner tous les éléments de la liste en commencer par celui d’index ‘3’, c’est-à-dire ‘’Mars’’. On peut également utiliser les index négatifs dans le découpe des listes

```python
# All the planets except the first and last
planets[1:-1]

Out[12]:
  ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

# The last 3 planets
planets[-3:]

Out[13]:
  ['Saturn', 'Uranus', 'Neptune']
```

Il est tout à fait possible de modifier une liste, car les listes de python sont [[mutable]]. Il suffit d’assigner à un index une nouvelle valeur.

```python
planets[3] = 'Malacandra'
planets

Out[14]:
 ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

Python dispose de plusieurs fonctions pour les listes, [[fonctions-listes]]

## Les fonctions utiles pour travailler avec les listes

La [[python.function.len]] retourne la longueur d’une liste et la fonction ‘sorted()’ permet de retrouner la liste en ordre alphabétique.

```python
# How many planets are there?
len(planets)

Out[16]:
  8

# The planets sorted in alphabetical order
sorted(planets)

Out[17]:
  ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
```

La [[python.function.sum]] additionne les valeurs d’une liste, alors que ‘min()’ et ‘max()’ retourne, respectivement, le minimum et le maximum d’une liste numérique.

```python
primes = [2, 3, 5, 7]
sum(primes)

Out[18]:
  17

max(primes)

Out[19]:
  7
```
