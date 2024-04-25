---
title: "Supervised Learning: apprentissage supervisé"
updated: 1702851047850
created: 1680261152504
---

Dans l'apprentissage automatique supervisé, les données sont annotées,
_classées_ ou _labellisées_. L'objectif est d’inférer (_prédire_) une fonction
ou une relation à partir de **données d’apprentissage labellisées**. En termes
mathématiques, nous disposons d'un [[ds.data.dataset]] que nous appellerons
$X$, avec $n$ observations. Et une cible $Y$, qui donne une caractéristique
pour chaque observation. L'objectif de l'apprentissage automatique supervisé
est de prédire $Y$ à partir de $X$.

On distingue :

- la [[regression]] pour un label **quantitatif** ;
- la [[classification]] pour un label **qualitatif**.

## algorithmes

- modèle linéaire généralisé
  - régression linéaire
  - régression de Poisson
  - régression logistique (**classification**)
- méthodes régularisées
  - ridge
  - lasso
  - elasticnet
  - lars
- méthodes bayésiennes (**classification** ?)
- méthodes splines
  - régression spline
  - GAM
- méthodes de moyennage local
  - [[ds.ml.sl.reg.k-nn]]
  - noyeau de lissage
  - CART
- méthodes d’aggrégation
  - bagging (dont random forest)
  - gradient boosting
- méthodes à noyeau
  - SVM (**classification**)
  - SVR (**régression**)
- réseaux de neuronnes
  - DNN
  - CNN
  - RNN
- autres méthodes
  - analyse descrimantes linéaires (**classification**)
  - PLS
  - méthode à direction révélatrice (_index model_)

Overall, cross-validation is a valuable technique for model evaluation, hyperparameter tuning, and assessing the generalization ability of machine learning models. It helps to ensure that the model's performance is reliable and consistent across different datasets or unseen data.
