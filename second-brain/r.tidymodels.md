---
id: f30gd81m83dibawpsj7a3nu
title: tidymodels
desc: >-
  collection of packages for modeling and machine learning using tidyverse 
  principles.
updated: 1684586241651
created: 1684523531211
---

## Whait is tidymodels

The tidymodels framework is a collection of packages for modeling and machine
learning using [[r.tidyverse]] principles. It is important to clarify that the
group of packages that make up tidymodels do not implement statistical models
themselves. Instead, they focus on making all the tasks around fitting the
model much easier. Those tasks are data pre-processing and results validation.

![Tidy workflow][assets/ds.png]

The following diagram illustrates each modeling step, and lines up the
`tidymodels` packages:

- [[r.tidymodels.rsample]]
- [[r.tidymodels.recipes]]
- [[r.tidymodels.parsnip]]
- [[r.tidymodels.yardstick]]

![Tidymodels workflow][assets/tidymodels.png.png]

## Pre-process


### `rsample`

The `initial_split()` function is specially built to separate the data set into
a training and testing set. By default, it holds 3/4 of the data for training
and the rest for testing. That can be changed by passing the `prop` argument.
This function generates an `rplit` object, not a data frame. The printed output
shows the row count for testing, training, and total.

```R
iris_split <- initial_split(iris, prop = 0.6)
iris_split
## <90/60/150>
```

To access the observations reserved for training, use the `training()` function.
Similarly, use `testing()` to access the testing data.

```R
iris_split %>%
  training() %>%
  glimpse()
## Observations: 90
## Variables: 5
## $ Sepal.Length <dbl> 5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.9, 5.4, 4…
## $ Sepal.Width  <dbl> 3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 3.1, 3.7, 3…
## $ Petal.Length <dbl> 1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.5, 1.5, 1…
## $ Petal.Width  <dbl> 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.1, 0.2, 0…
## $ Species      <fct> setosa, setosa, setosa, setosa, setosa, setosa, set…
```

### `recipes`

In `tidymodels`, the `recipes` package provides an interface that specializes
in data pre-processing. Within the package, the functions that start, or
execute, the data transformations are named after cooking actions. That makes
the interface more user-friendly. For example:

- `recipe()`: starts a new set of transformations to be applied, similar to
the [[r.ggplot]] command. Its main argument is the model’s formula.
- `prep()`: executes the transformations on top of the data that is supplied,
typically the training data.

Each data transformation is a step. Functions correspond to specific types of
steps, each of which has a prefix of `step_`. There are several `step_`
functions; in this example, we will use three of them:

- `step_corr()`: removes variables that have large absolute correlations with
other variables.
- `step_center()`: normalizes numeric data to have a mean of zero.
- `step_scale()`: normalizes numeric data to have a standard deviation of one

Another nice feature is that the step can be applied to a specific variable,
groups of variables, or all variables. The `all_outocomes()` and `all_predictors()`
functions provide a very convenient way to specify groups of variables. For
example, if we want the `step_corr()` to only analyze the predictor variables,
we use `step_corr(all_predictors())`. This capability saves us from having to
enumerate each variable.

In the following example, we will put together the `recipe()`, `prep()`, and
step functions to create a `recipe` object. The `training()` function is used
to extract that data set from the previously created split sample data set.

```R
iris_recipe <- training(iris_split) %>%
  recipe(Species ~.) %>%
  step_corr(all_predictors()) %>%
  step_center(all_predictors(), -all_outcomes()) %>%
  step_scale(all_predictors(), -all_outcomes()) %>%
  prep()
```

If we call the `iris_recipe` object, it will print details about the recipe.
The Operations section describes what was done to the data. One of theoperations
entries in the example explains that the correlation step removed the
`Petal.Length` variable.

```R
iris_recipe
## Data Recipe
## 
## Inputs:
## 
##       role #variables
##    outcome          1
##  predictor          4
## 
## Training data contained 90 data points and no missing data.
## 
## Operations:
## 
## Correlation filter removed Petal.Length [trained]
## Centering for Sepal.Length, Sepal.Width, Petal.Width [trained]
## Scaling for Sepal.Length, Sepal.Width, Petal.Width [trained]
```

The testing data can now be transformed using the exact same steps, weights,
and categorization used to pre-process the training data. To do this, another
function with a cooking term is used: `bake()`. Notice that the `testing()`
function is used in order to extract the appropriate data set.

```R
iris_testing <- iris_recipe %>%
  bake(testing(iris_split)) 

glimpse(iris_testing)
## Observations: 60
## Variables: 4
## $ Sepal.Length <dbl> -1.597601746, -1.138960096, 0.007644027, -0.7949788…
## $ Sepal.Width  <dbl> -0.41010139, 0.71517681, 2.06551064, 1.61539936, 0.…
## $ Petal.Width  <dbl> -1.2085003, -1.2085003, -1.2085003, -1.0796318, -1.…
## $ Species      <fct> setosa, setosa, setosa, setosa, setosa, setosa, set…
```

Performing the same operation over the training data is redundant, because that
data has already been prepped. To load the prepared training data into a
variable, we use `juice()`. It will extract the data from the `iris_recipe`
object.

```R
iris_training <- juice(iris_recipe)

glimpse(iris_training)
## Observations: 90
## Variables: 4
## $ Sepal.Length <dbl> -0.7949789, -1.0242997, -1.2536205, -1.3682809, -0.…
## $ Sepal.Width  <dbl> 0.94023245, -0.18504575, 0.26506553, 0.04000989, 1.…
## $ Petal.Width  <dbl> -1.2085003, -1.2085003, -1.2085003, -1.2085003, -1.…
## $ Species      <fct> setosa, setosa, setosa, setosa, setosa, setosa, set…
```

## Train

In R, there are multiple packages that fit the same type of model. It is common
for each package to provide a unique interface. In other words, things such as
an argument for the same model attribute is defined differently for each
package.

For example, the `ranger` and `randomForest` packages fit Random Forest
models. In the `ranger()` function, to define the number of trees we use
`num.trees`. In `randomForest`, that argument is named `ntree`. It is not easy
to switch between packages to run the same model.

Instead of replacing the modeling package, `tidymodels` replaces the interface.
Better said, `tidymodels` provides a single set of functions and arguments to
define a model. It then fits the model against the requested modeling package.

In the example below, the `rand_forest()` function is used to initialize a
Random Forest model. To define the number of trees, the `trees` argument is
used. To use the `ranger` version of Random Forest, the `set_engine()` function
is used. Finally, to execute the model, the `fit()` function is used. The
expected arguments are the **formula** and **data**. Notice that the model runs
on top of the _juiced_ trained data.

```R
iris_ranger <- rand_forest(trees = 100, mode = "classification") %>%
  set_engine("ranger") %>%
  fit(Species ~ ., data = iris_training)
```

The payoff is that if we now want to run the same model against `randomForest`,
we simply change the value in `set_engine()` to “randomForest”.

```R
iris_rf <-  rand_forest(trees = 100, mode = "classification") %>%
  set_engine("randomForest") %>%
  fit(Species ~ ., data = iris_training)
```

It is also worth mentioning that the model is not defined in a single, large
function with a lot of arguments. The model definition is separated into smaller
functions such as `fit()` and `set_engine()`. This allows for a more flexible
and easier to learn interface.

To make predictions the `predict()` function ran against a `parsnip` model and
returns a tibble. By default, the prediction variable is called `.pred_class`.
In the example, notice that the baked testing data is used.

```R
predict(iris_ranger, iris_testing)
## # A tibble: 60 x 1
##    .pred_class
##    <fct>      
##  1 setosa     
##  2 setosa     
##  3 setosa     
##  4 setosa     
##  5 setosa     
##  6 setosa     
##  7 setosa     
##  8 setosa     
##  9 setosa     
## 10 setosa     
## # … with 50 more rows
```

It is very easy to add the predictions to the _baked_ testing data by using
dplyr’s `bind_cols()` function.

```R
iris_ranger %>%
  predict(iris_testing) %>%
  bind_cols(iris_testing) %>%
  glimpse()
## Observations: 60
## Variables: 5
## $ .pred_class  <fct> setosa, setosa, setosa, setosa, setosa, setosa, set…
## $ Sepal.Length <dbl> -1.597601746, -1.138960096, 0.007644027, -0.7949788…
## $ Sepal.Width  <dbl> -0.41010139, 0.71517681, 2.06551064, 1.61539936, 0.…
## $ Petal.Width  <dbl> -1.2085003, -1.2085003, -1.2085003, -1.0796318, -1.…
## $ Species      <fct> setosa, setosa, setosa, setosa, setosa, setosa, set…
```

## Validate

Use the `metrics()` function to measure the performance of the model. It will
automatically choose metrics appropriate for a given type of model. The
function expects a tibble that contains the actual results (truth) and what
the model predicted (estimate).

```R
iris_ranger %>%
  predict(iris_testing) %>%
  bind_cols(iris_testing) %>%
  metrics(truth = Species, estimate = .pred_class)
## # A tibble: 2 x 3
##   .metric  .estimator .estimate
##   <chr>    <chr>          <dbl>
## 1 accuracy multiclass     0.917
## 2 kap      multiclass     0.874
```

Because of the consistency of the new interface, measuring the same metrics
against the `randomForest` model is as easy as replacing the model variable
at the top of the code.

```R
iris_rf %>%
  predict(iris_testing) %>%
  bind_cols(iris_testing) %>%
  metrics(truth = Species, estimate = .pred_class)
## # A tibble: 2 x 3
##   .metric  .estimator .estimate
##   <chr>    <chr>          <dbl>
## 1 accuracy multiclass     0.883
## 2 kap      multiclass     0.824
```

It is easy to obtain the probability for each possible predicted value by setting
the `type` argument to `prob`. That will return a tibble with as many variables
as there are possible predicted values. Their name will default to the original
value name, prefixed with `.pred_`.

```R
iris_ranger %>%
  predict(iris_testing, type = "prob") %>%
  glimpse()
## Observations: 60
## Variables: 3
## $ .pred_setosa     <dbl> 0.677480159, 0.978293651, 0.783250000, 0.983972…
## $ .pred_versicolor <dbl> 0.295507937, 0.011706349, 0.150833333, 0.001111…
## $ .pred_virginica  <dbl> 0.02701190, 0.01000000, 0.06591667, 0.01491667,…
```

Again, use `bind_cols()` to append the predictions to the baked testing data set.

```R
iris_probs <- iris_ranger %>%
  predict(iris_testing, type = "prob") %>%
  bind_cols(iris_testing)

glimpse(iris_probs)
## Observations: 60
## Variables: 7
## $ .pred_setosa     <dbl> 0.677480159, 0.978293651, 0.783250000, 0.983972…
## $ .pred_versicolor <dbl> 0.295507937, 0.011706349, 0.150833333, 0.001111…
## $ .pred_virginica  <dbl> 0.02701190, 0.01000000, 0.06591667, 0.01491667,…
## $ Sepal.Length     <dbl> -1.597601746, -1.138960096, 0.007644027, -0.794…
## $ Sepal.Width      <dbl> -0.41010139, 0.71517681, 2.06551064, 1.61539936…
## $ Petal.Width      <dbl> -1.2085003, -1.2085003, -1.2085003, -1.0796318,…
## $ Species          <fct> setosa, setosa, setosa, setosa, setosa, setosa,…
```

Now that everything is in one tibble, it is easy to calculate curve methods.
In this case we are using `gain_curve()`.

```R
iris_probs%>%
  gain_curve(Species, .pred_setosa:.pred_virginica) %>%
  glimpse()
## Observations: 141
## Variables: 5
## $ .level          <chr> "setosa", "setosa", "setosa", "setosa", "setosa"…
## $ .n              <dbl> 0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, …
## $ .n_events       <dbl> 0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, …
## $ .percent_tested <dbl> 0.000000, 1.666667, 5.000000, 6.666667, 8.333333…
## $ .percent_found  <dbl> 0.000000, 5.882353, 17.647059, 23.529412, 29.411…
```

The curve methods include an `autoplot()` function that easily creates a ggplot2
visualization.

```R
iris_probs%>%
  gain_curve(Species, .pred_setosa:.pred_virginica) %>%
  autoplot()
```

![](assets/gain_curve-1.png)

This is an example of a `roc_curve()`. Again, because of the consistency of the
interface, only the function name needs to be modified; even the argument values
remain the same.

```R
iris_probs%>%
  roc_curve(Species, .pred_setosa:.pred_virginica) %>%
  autoplot()
```

![](assets/roc_curve-1.png)

To measured the combined single predicted value and the probability of each possible
value, combine the two prediction modes (with and without `prob` type). In this
example, using dplyr’s vselect()` makes the resulting tibble easier to read.

```R
predict(iris_ranger, iris_testing, type = "prob") %>%
  bind_cols(predict(iris_ranger, iris_testing)) %>%
  bind_cols(select(iris_testing, Species)) %>%
  glimpse()
## Observations: 60
## Variables: 5
## $ .pred_setosa     <dbl> 0.677480159, 0.978293651, 0.783250000, 0.983972…
## $ .pred_versicolor <dbl> 0.295507937, 0.011706349, 0.150833333, 0.001111…
## $ .pred_virginica  <dbl> 0.02701190, 0.01000000, 0.06591667, 0.01491667,…
## $ .pred_class      <fct> setosa, setosa, setosa, setosa, setosa, setosa,…
## $ Species          <fct> setosa, setosa, setosa, setosa, setosa, setosa,…
```

Pipe the resulting table into `metrics()`. In this case, specify `.pred_class`
as the estimate.

```R
predict(iris_ranger, iris_testing, type = "prob") %>%
  bind_cols(predict(iris_ranger, iris_testing)) %>%
  bind_cols(select(iris_testing, Species)) %>%
  metrics(Species, .pred_setosa:.pred_virginica, estimate = .pred_class)
## # A tibble: 4 x 3
##   .metric     .estimator .estimate
##   <chr>       <chr>          <dbl>
## 1 accuracy    multiclass     0.917
## 2 kap         multiclass     0.874
## 3 mn_log_loss multiclass     0.274
## 4 roc_auc     hand_till      0.980
```

## References

- https://rviews.rstudio.com/2019/06/19/a-gentle-intro-to-tidymodels/

---

[Get started with tidymodels and #TidyTuesday Palmer penguins](https://juliasilge.com/blog/palmer-penguins/)

This week’s #TidyTuesday dataset is from palmerpenguins, observations of Antarctic 
penguins who live on the Palmer Archipelago. You can read more about how this 
dataset came to be in this post on the RStudio Education blog. Our modeling goal 
here is to predict the sex of the penguins using a classification model, based 
on other observations in the dataset.

```{r}
library(tidyverse)
library(palmerpenguins)

penguins
```

If you try building a classification model for species, you will likely find an 
almost perfect fit, because these kinds of observations are actually what 
distinguish different species. Sex, on the other hand, is a little messier.

```{r}
penguins %>%
  filter(!is.na(sex)) %>%
  ggplot(aes(flipper_length_mm, bill_length_mm, color = sex, size = body_mass_g)) +
  geom_point(alpha = 0.5) +
  facet_wrap(~species)
```

It looks like female penguins are smaller with different bills, but let’s get 
ready for modeling to find out more! We will not use the island or year information 
in our model.

```{r}
penguins_df <- penguins %>%
  filter(!is.na(sex)) %>%
  select(-year, -island)

```

# build a model

On commence par charger le package `tidymodels`et séparer le jeu de données en 
`training_set`et `test_set`. Par défaut, test_set est 1/4 du jeu de données et 
le training_set est 3/4.

```{r}
library(tidymodels)

set.seed(123)
penguin_split <- initial_split(penguins_df, strata = sex)
penguin_train <- training(penguin_split)
penguin_test <- testing(penguin_split)
```

Next, let’s create bootstrap resamples of the training data, to evaluate our 
models.

```{r}
set.seed(123)
penguin_boot <- bootstraps(penguin_train)
penguin_boot
```

Let’s compare two different models, a logistic regression model and a random 
forest model. We start by creating the model specifications.

```{r}
glm_spec <- logistic_reg() %>%
  set_engine("glm")

glm_spec
```

```{r}
rf_spec <- rand_forest() %>%
  set_mode("classification") %>%
  set_engine("ranger")

rf_spec
```

Next let’s start putting together a tidymodels workflow(), a helper object to 
help manage modeling pipelines with pieces that fit together like Lego blocks. 
Notice that there is no model yet: Model: None.

```{r}
penguin_wf <- workflow() %>%
  add_formula(sex ~ .)

penguin_wf
```

Now we can add a model, and the fit to each of the resamples. First, we can fit 
the logistic regression model.

```{r}
glm_rs <- penguin_wf %>%
  add_model(glm_spec) %>%
  fit_resamples(
    resamples = penguin_boot,
    control = control_resamples(save_pred = TRUE)
  )

glm_rs
```

Second, we can fit the random forest model.

```{r}
rf_rs <- penguin_wf %>%
  add_model(rf_spec) %>%
  fit_resamples(
    resamples = penguin_boot,
    control = control_resamples(save_pred = TRUE)
  )

rf_rs
``` 

We have fit each of our candidate models to our resampled training set!

## evaluate the model

Now let’s check out how we did.

```{r}
collect_metrics(rf_rs)
```

Pretty nice! The function collect_metrics() extracts and formats the .metrics 
column from resampling results like the ones we have here.

```{r}
collect_metrics(glm_rs)
```

So… also great! If I am in a situation where a more complex model like a random 
forest performs the same as a simpler model like logistic regression, then I 
will choose the simpler model. Let’s dig deeper into how it is doing. For example, 
how is it predicting the two classes?

```{r}
glm_rs %>%
  conf_mat_resampled()
```

About the same, which is good. We can also make an ROC curve.

```{r}
glm_rs %>%
  collect_predictions() %>%
  group_by(id) %>%
  roc_curve(sex, .pred_female) %>%
  ggplot(aes(1 - specificity, sensitivity, color = id)) +
  geom_abline(lty = 2, color = "gray80", size = 1.5) +
  geom_path(show.legend = FALSE, alpha = 0.6, size = 1.2) +
  coord_equal()
```

This ROC curve is more jagged than others you may have seen because the dataset 
is small.

It is finally time for us to return to the testing set. Notice that we have not 
used the testing set yet during this whole analysis; the testing set is precious 
and can only be used to estimate performance on new data. Let’s fit one more time 
to the training data and evaluate on the testing data using the function last_fit().

```{r}
penguin_final <- penguin_wf %>%
  add_model(glm_spec) %>%
  last_fit(penguin_split)

penguin_final
```

The metrics and predictions here are on the testing data.

```{r}
collect_metrics(penguin_final)
```

```{r}
collect_predictions(penguin_final) %>%
  conf_mat(sex, .pred_class)
```

The coefficients (which we can get out using tidy()) have been estimated using 
the training data. If we use exponentiate = TRUE, we have odds ratios.

```{r}
penguin_final$.workflow[[1]] %>%
  tidy(exponentiate = TRUE)
```

- The largest odds ratio is for bill depth, with the second largest for bill 
length. An increase of 1 mm in bill depth corresponds to almost 4x higher odds 
of being male. The characteristics of a penguin’s bill must be associated with 
their sex.
- We don’t have strong evidence that flipper length is different between male 
and female penguins, controlling for the other measures; maybe we should explore 
that by changing that first plot!

```{r}
penguins %>%
  filter(!is.na(sex)) %>%
  ggplot(aes(bill_depth_mm, bill_length_mm, color = sex, size = body_mass_g)) +
  geom_point(alpha = 0.5) +
  facet_wrap(~species)
```

Yes, the male and female penguins are much more separated now.





---- EXAM certification DS ENSAE

---

title: "exam"
author: "Guillaume Gilles"
date: "2023-05-22"
output:
html_document:
toc: TRUE # table of content true
toc_depth: 3 # up to three depths of headings
toc_float: TRUE # table of content follow the navigation up & down
number_sections: TRUE # if you want number sections at each table header

---

## séparer les données en `training set` et `test set`

Avec `initial_split` on sépare le dataset en 2, d’un côté, le jeu
d’entraînement `vin_train` et de l’autre, le jeu de test, `vin_train`.

```{r}
set.seed(789)
vin_split <- initial_split(vin, strata = quality)
vin_train <- training(vin_split)
vin_test <- testing(vin_split)

vin_split
```

## Modèlisation

Pour la modélisation, j’utilise tidymodels.

### définir un workflow

Dans un premier temps, je défini un _workflow_ qui va me permettre de spécifier
la variable à prédire, `quality` à partir de quelles variables potentiellement
explicatives, toutes mon cas, `~ .`

```{r}
vin_wf <- workflow() %>%
  add_formula(quality ~ .)

vin_wf
```

### régression logistique

La régression logistique est un modèle de régression statistique utilisé pour les
problèmes de classification. La fonction mathématique associée attribue tout
nombre réel à une valeur comprise entre 0 et 1.

Premier modèle, la régression logistique. Je défini les spécificités du modèle
`glm_spec` pour ajouter ensuite le _worflow_ précédement initialisé.

```{r}
glm_spec <- logistic_reg() %>%
  set_engine("glm")

glm_spec

glm_wf <- vin_wf %>%
  add_model(glm_spec)

glm_wf
```

### ridge

la régression ridge ajoute une **pénalité proportionnelle à la somme**
**des carrés des coefficients** (norme L2) à la fonction de perte des moindres
carrés ordinaires (MCO). L'objectif est de réduire les coefficients vers zéro
sans les éliminer complètement.

Je fais de même pour le ridge…

Attention, cette fois, il faut spécifier la problématique de prédiction, soit
`regression`, ou `classification` dans ce cas, puisque ridge et d’autre algorithmes,
lasso, K-NN, forêts aléatoires, XGBosst, SVM, etc. peuvent traiter les 2 problématiques.

```{r}
ridge_spec <- logistic_reg(penalty = tune(), mixture = 0) %>%
  set_engine("glmnet") %>%
  set_mode("classification") %>%
  set_args(maxit = 10000)

ridge_spec

ridge_wf <- vin_wf %>%
  add_model(ridge_spec)

ridge_wf
```

### lasso

la régression Lasso, similaire à la régression ridge, ajoute une
pénalité à la fonction de perte. Cependant, au lieu de la somme des coefficients
au carré, elle utilise la **somme des valeurs absolues des coefficients**
(norme L1). La régression Lasso effectue une sélection des caractéristiques en
ramenant certains coefficients à exactement zéro, les éliminant ainsi du modèle.

```{r}
lasso_spec <- logistic_reg(penalty = tune(), mixture = 1) %>%
  set_engine("glmnet") %>%
  set_mode("classification") %>%
  set_args(maxit = 10000)

lasso_spec

lasso_wf <- vin_wf %>%
  add_model(lasso_spec)

lasso_wf
```

### K-NN

Algorithme d'apprentissage automatique **non paramétrique**, il repose sur l'idée
que les points de données appartenant à la même classe ou catégorie sont
généralement proches les uns des autres.

```{r}
knn_spec <- nearest_neighbor(
  mode = "classification",
  engine = "kknn",
  weight_func = "rectangular")

knn_spec

knn_wf <- vin_wf %>%
  add_model(knn_spec)

knn_wf
```

### random forest

Le principe des forêts aléatoire est de constituer à l’aide de la technique du
_bootstrapping_ une forêt d’arbres avec un faible biais et une grande variance.
En faisant la moyenne de ces arbres, on réduit la variance, tout en conservant
un biais faible.

```{r}
rf_spec <- rand_forest() %>%
  set_mode("classification") %>%
  set_engine("ranger")

rf_spec

rf_wf <- vin_wf %>%
  add_model(rf_spec)

rf_wf
```

### XGBoost

L'idée principale de XGBoost est d'entraîner itérativement une séquence de modèles
faibles, chacun d'entre eux tentant de corriger les erreurs commises par les
modèles précédents. Les modèles sont entraînés de manière croissante, ce qui
signifie que chaque nouveau modèle est entraîné pour minimiser les erreurs des
modèles précédents.

```{r}
xgb_spec <- boost_tree(trees = 100, tree_depth = 6) %>%
  set_engine("xgboost") %>%
  set_mode("classification")

xgb_spec

xgb_wf <- vin_wf %>%
  add_model(xgb_spec)

xgb_wf
```

### Support Vector Machine

Avec SVM on essaie de faire passer un _hyperplan_ dans un espace multidimensionnel
pour séparer en 2 classes. Ensuite, les points sont classés selon s’ils sont sur
le côté positif ou négatif de l’hyperplan.

```{r}
svm_spec <- svm_linear() %>%
  set_engine('LiblineaR') %>%
  set_mode("classification")

svm_spec

svm_wf <- vin_wf %>%
  add_model(svm_spec)

svm_wf
```

## fit avec `fit_resamples()`

Il est temps d’entraîner les modèles initialement définis, grâce à la fonction
`fit_resample()` du package **tune**.

### régression logistique

les objets `glm_res$.metrics[[2]]` et `glm_res$.predictions[[2]]` permettent de
vérifier l’accuracy ainsi que l’aire sous la courbe ROC et les différentes
prédictions dans le bloc numéro 2 de la validation croisée.

```{r}
glm_res <- fit_resamples(
  object = glm_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )

glm_res$.metrics[[2]]
glm_res$.predictions[[2]]
```

### Ridge

```{r}
# ridge_res <- fit_resamples(
#   object = ridge_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

### Lasso

```{r}
# lasso_res <- fit_resamples(
#   object = lasso_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

### K-NN

```{r}
# knn_res <- fit_resamples(
#   object = knn_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
# )
```

### random forest

```{r}
rf_res <- fit_resamples(
  object = rf_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )
```

### XGBoost

```{r}
xgb_res <- fit_resamples(
  object = xgb_wf,
  resamples = folds_train,
  control = control_resamples(save_pred = TRUE)
  )
```

### SVM

```{r}
# svm_res <- fit_resamples(
#   object = svm_wf,
#   resamples = folds_train,
#   control = control_resamples(save_pred = TRUE)
#   )
```

## Évaluation des modèles

Maintenant que tous les modèles sont entraînés, on peut évaluer les performances
de chacun et choisir le modèles que l’on préfère.

```{r}
collect_metrics(glm_res)
# collect_metrics(ridge_res)
# collect_metrics(lasso_res)
# collect_metrics(knn_res)
collect_metrics(rf_res)
collect_metrics(xgb_res)
# collect_metrics(svm_res)
```

### matrice de confusion

Le meilleur modèle (entre ceux qui fonctionnent…) est la **random forest**.

Il s’agit de la matrice de confusion sur le modèle de la forêt aléatoire.

```{r}
rf_res %>%
  conf_mat_resampled()
```

## il est temps de réaliser la prédiction final sur le `test set`

```{r}
vin_final <- rf_wf %>%
  last_fit(vin_split)

vin_final
```

Les performances et les prédictions du modèle final avec une forêt aléatoire.

```{r}
collect_metrics(vin_final)
```

```{r}
collect_predictions(vin_final) %>%
  conf_mat(quality, .pred_class)
```

## Les éléments qui manque :

1. plussieurs de mes modèles ne fonctionne pas à cause d’une erreur dans le code que je n’arrive pas à résoudre à temps…
2. Je n’ai pas fais le _feature engineering_, comme mettre les variable au carré, au cube, etc.
3.
