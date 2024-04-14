---
id: bprh6jbal2snczdrmbnny1f
title: Secret statistique
desc: ''
updated: 1702851604853
created: 1670270445160
---

## Objectif du secret statistique

Le secret statistique garantit le respect (1) de la confidentialité due à la vie privée, personnelle et familiale, pour les personnes physiques et (2) du secret commercial et des affaires, pour les entreprises.

### Pour les entreprises

Pour les données relatives aux entreprises, aucun résultat publié ne concerne **moins de trois entreprises ou établissements**. De plus, aucun résultat n’est diffusé quand une entreprise ou un établissement **contribue à lui seul à plus de 85 % de ce résultat**.

### Pour les particuliers

Pour les particuliers, les données publiées à partir des enquêtes et du recensement de la population **ne doivent pas permettre une identification ni directe ni indirecte** des répondants et de leurs réponses. 

## Références

- [Loi n° 51-711 du 7 juin 1951 sur l'obligation, la coordination et le secret en matière de statistiques](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000888573)
- [Secret statistique](https://www.insee.fr/fr/information/1300624)




# K-nearest neighbors

We will build a classification model using the "K-nearest neighbors" strategy. To predict the target of a new sample, a k-nearest neighbors takes into account its k closest samples in the training set and predicts the majority target of these samples.

## Références

- https://lms.fun-mooc.fr/courses/course-v1:inria+41026+session03/courseware/ea2a140204de4e7fbc316fd96a163c7f/f5a3613d45224fde86a195e91223961d/

###################################

# The `fit` method is called to train the model from the input (features) and target data.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
_ = model.fit(data, target)
```

<png>

The method `fit` is composed of two elements: (i) a learning algorithm and (ii) some model states. The learning algorithm takes the training data and training target as input and sets the model states. These model states will be used later to either predict (for classifiers and regressors) or transform data (for transformers).

Both the learning algorithm and the type of model states are specific to each type of model.

## Références

- https://lms.fun-mooc.fr/courses/course-v1:inria+41026+session03/courseware/ea2a140204de4e7fbc316fd96a163c7f/f5a3613d45224fde86a195e91223961d/

###################################

# Let's use our model to make some predictions using the same dataset.

```python
```