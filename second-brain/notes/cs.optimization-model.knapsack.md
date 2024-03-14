---
id: ud68uo2x4po4giydz7crqzq
title: Knapsack
desc: ''
updated: 1649864399779
created: 1649854733836
---

Il existe 2 variantes pour le problème du sac à dos :
- 0/1 Knapsack
- fractional 



- Chaque objet est représenté par une paire, `<value, weight>` ;
- Le knapsack ne peut supporter un poid, *weight* supérieur à `w` ;
- Un vecteur, `l`, de longueur `n` qui représente la disponibilité, ou non, des objets ;
- Un vecteur, `V`, de longueur `n` qui indique si un objet est prit ou pas. Si `V[i] = 1` alors l’objet `l[i]` est pris. Si `V[i] = 0` alors l’objet `l[i]` **n’**est **pas** pris.

On cherche à maximiser `V` :

$$
\sum_{i = 0}^{n-1} V[i] * l[i].value
$$

Sous la contrainte de :

$$
\sum_{i = 0}^{n-1} V[i] * l[i].weight \le w
$$




## Références

1. https://developers.google.com/optimization/bin/knapsack