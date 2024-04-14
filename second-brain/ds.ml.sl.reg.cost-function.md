---
id: sct3kh4vxcxx3ax6l86zdti
title: Fonction coût d’un modèle linéaire
desc: Évaluer la marge d’erreur d’un modèle linéaire avec la fonction coût
updated: 1656514166383
created: 1656493875108
---

L’objectif d’une [[régression linéaire|ds.ml.sl.reg]] est de trouver la droite la plus appropriée pour le nuage de points. On peut se sevir de la fonction coût qui permet de mesurer le degré d’erreur de la droite.

D’abord, on compare la prédiction $ŷ$ avec la target $y$. Cette différence s’appel l’**erreur**.

$ŷ - y$

On élève cette différence au carré $^2$ pour éliminer les nombres négatifs et on fait la somme de toutes les targets.

$\sum\limits_{i = 0}^{m} (ŷ^{i} - y^{i})^2$

Dans ce cas le résultat de la fonction coût est proportionel à la taille, $m$, du jeu de données. La fonction coût devient plus grande lorsque $m$ augmente. Par convention, on calcul donc la **moyenne de l’erreur au carré**. *Pour faciliter certains calculs ultérieurement, on divise par $2m$, soit : $\frac{1}{2m}$

La fonction coût devient :

$J(w,b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (ŷ^{(i)} - y^{(i)})^2$

Puisque $ŷ^{(i)}$ est la prédiction du [[ml.sl.reg.model.math]], on peut réécrire la fonction coût ainsi :

> $J(w,b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2$

On peut appeler cette fonction coût de plusieurs façon :

- **Mean Squared Error (MSE)** ;
- Squared error cost function ;
- Quadratic cost function ;
- Sum of squared errors.

### Références

- https://www.coursera.org/learn/machine-learning/lecture/1Z0TT/cost-function-formula
- https://www.coursera.org/learn/machine-learning/lecture/FthLz/cost-function-intuition