---
title: "Cross Validation: validation croisée"
---
## Pouvez-vous expliquer le principe de la validation croisée ?

La validation croisée est une méthode de machine learning dans laquelle, le jeu de données **d’entraînement** est divisé en plusieurs partitions (généralement entre 5 ou 10). À chaque phase d'entraînement, l’algorithme écarte un bloc de *validation* afin de « vérifier » sa performance sur ce bloc. Ce processus est répété le nombre de partition déterminée préalablement (pour rappel, 5 ou 10).

![](~/Downloads/cross-validation.webp)

La validation croisée apporte de nombreux bénéfices :

1. **évaluation du modèle :** on peut évaluer, plus fidélement, la performance 
d’un modèle sur un jeu de données nouveau pour l’algorithme ;
2. **éviter le sur-apprentissage :** on peut ainsi déterminer si le modèle entre 
dans une phase de sur-apprentissage ;
3. **réglage des hyperparamètres :** en augmentant le nombre de partitions tout 
en choississant des hyperparamètres différents, on peut chercher à optimiser le
modèle ;
4. **comparaison des modèles :** en utilisant le même jeu de données, on peut 
évaluer différents modèles.


---
R

## validaion croisée sur le `training set`

On utilise la fonction `v_fold_vc()` de **rsample** pour effectuer une validation 
croisée à 10 blocs sur le jeu d’entraînement.

Chaque bloc de validation croisée est constitué de `1079` observations 
d’entraînement, *Analysis*, et `120` observations de validation, *Assess*. On 
peut le vérifier en regardant le bloc numéro 5 : `folds_train$splits[[5]]`

```{r}
folds_train <- vfold_cv(vin_train, v = 10, repeats = 1)  # 10-fold cross-validation

folds_train$splits[[5]]
```

source : [chatGPT](https://chat.openai.com/c/f2e00c75-4e80-4f5d-ac60-904091dae27e)

  Cross-validation is a useful technique for assessing the performance and generalization ability of a machine learning model. Here are some key benefits and use cases of cross-validation:

  1. **Model evaluation:** Cross-validation provides an unbiased estimate of how well a model will perform on unseen data. By assessing the model's performance on multiple subsets of the data, cross-validation helps to identify potential issues such as overfitting or underfitting.

  2. **Hyperparameter tuning:** Cross-validation is commonly used to tune the hyperparameters of a model. By evaluating the model's performance on different parameter settings across multiple folds, you can select the best combination of hyperparameters that optimize the model's performance.

  3. **Feature selection:** Cross-validation can aid in feature selection by evaluating the model's performance when different subsets of features are used. This helps to identify the most relevant and informative features for the model.

  4. **Model comparison:** Cross-validation allows you to compare the performance of different models or algorithms on the same dataset. By evaluating each model's performance across multiple folds, you can determine which model is the most effective for your specific task.

  5. **Assessing generalization ability:** Cross-validation provides an estimate of how well the model will generalize to new, unseen data. This is especially important when the available dataset is limited or imbalanced, as it helps to validate the model's performance beyond the training data.

  6. **Detecting data issues:** Cross-validation can help identify potential data issues such as data leakage or sample bias. By evaluating the model's performance across different subsets of the data, you can gain insights into the stability and consistency of the model's predictions.



## validation croisée avec [[r.tidymodels]]

To perform cross-validation using the `tidymodels` package in R, you can follow these steps:

1. Install and load the necessary packages:

```{r}
install.packages("tidymodels")
library(tidymodels)
```

2. Load your dataset into R or create a sample dataset for demonstration purposes. Let's assume you have a dataset named `mydata` with predictors stored in a data frame or matrix `X` and the corresponding response variable in a vector `y`.

3. Choose a machine learning algorithm to evaluate using cross-validation. For this example, let's use the random forest algorithm implemented in the `randomForest` package.

```{r}
library(randomForest)
```

4. Create a recipe using the `recipe()` function from `tidymodels`. A recipe specifies the data preprocessing steps and variable roles.

```R
my_recipe <- recipe(y ~ ., data = mydata)
```

5. Specify the resampling strategy using the `vfold_cv()` function from `tidymodels`. This function generates a set of training and validation splits for cross-validation. You can specify the number of folds (`v`) and the number of repeats (`repeats`).

```R
folds <- vfold_cv(mydata, v = 10, repeats = 1)  # 10-fold cross-validation
```

6. Define the machine learning model using the `rand_forest()` function from the `parsnip` package, which is part of `tidymodels`.

```R
my_model <- rand_forest()  # Random forest model
```

7. Create a workflow using the `workflow()` function from `tidymodels`. A workflow combines the recipe and model specifications.

```R
my_workflow <- workflow() %>%
  add_recipe(my_recipe) %>%
  add_model(my_model)
```

8. Fit and evaluate the model using the `fit_resamples()` function from `tidymodels`. This function performs the cross-validation and computes evaluation metrics.

```R
res <- fit_resamples(my_workflow, folds)
```

9. After performing cross-validation, you can access various performance metrics and model evaluation results using functions like `collect_metrics()` and `collect_predictions()`.

```R
collect_metrics(res)
collect_predictions(res)
```

These are the basic steps for performing cross-validation using `tidymodels` in R. You can further customize the workflow, model, and evaluation metrics based on your specific needs. `tidymodels` provides a comprehensive framework for machine learning that allows for seamless integration of preprocessing, modeling, and evaluation.


```{r}
don=readRDS("don.RDS")
####packages utilisés
library(rpart)
library(randomForest)
#### VC
nb <- 5
set.seed(1234)
blocs <- sample(rep(1:nb,length=nrow(don)))
RES <- data.frame(Y=don$Y)
##################################
for(ii in 1:nb){
  donA <- don[blocs!=ii,]
  donT <- don[blocs==ii,]
  ########################
  algo1 <- lm(Y~T6+T18+Vx+maxO3v,data=donA)
  RES[blocs==ii,"expert"] <- predict(algo1,donT)
  ########################
  algo2 <- lm(Y~.,data=donA)
  RES[blocs==ii,"mco"] <- predict(algo2,donT)
  ########################
  algo3 <- lm(Y~maxO3v,data=donA)
  RES[blocs==ii,"persistance"] <- predict(algo3,donT)
  ########################
  algo4 <- rpart(Y~.,data=donA)
  RES[blocs==ii,"arbre"] <- predict(algo4,donT)
  ########################
  algo5 <- randomForest(Y~.,data=donA)
  RES[blocs==ii,"foret"] <- predict(algo5,donT)
}
```


Cross-validation is a widely used technique in machine learning and data analysis for assessing the performance of a model and estimating its generalization ability. In R, you can perform cross-validation using the `caret` package, which provides a unified interface for various machine learning algorithms. Here's an example of how to perform cross-validation in R:

1. Install and load the `caret` package (if not already installed):

```R
install.packages("caret")
library(caret)
```

2. Load your dataset into R or create a sample dataset for demonstration purposes. Let's assume you have a dataset named `mydata` with predictors stored in a matrix or data frame `X` and the corresponding response variable in a vector `y`.

3. Define the number of folds for cross-validation. The most common choice is 10-fold cross-validation, where the data is split into 10 equally sized subsets.

```R
num_folds <- 10
```

4. Create a cross-validation partitioning scheme using the `createFolds()` function from `caret`. This function randomly splits the data into the specified number of folds.

```R
folds <- createFolds(y, k = num_folds)
```

5. Choose a machine learning algorithm to evaluate using cross-validation. For example, let's use the random forest algorithm implemented in the `randomForest` package.

```R
library(randomForest)
```

6. Define the model parameters and create a training control object using the `trainControl()` function from `caret`. This object specifies the cross-validation settings and any additional configurations for the training process.

```R
ctrl <- trainControl(method = "cv", index = folds)
```

7. Train the model using the `train()` function from `caret`, specifying the algorithm, predictors, and response variable.

```R
model <- train(X, y, method = "rf", trControl = ctrl)
```

8. After training, you can access various performance metrics and model evaluation results using the `summary()` function.

```R
summary(model)
```

This is a basic example of performing cross-validation in R using the `caret` package. The specific steps may vary depending on your dataset and the machine learning algorithm you choose to use. It's also worth noting that there are other packages and functions in R that can perform cross-validation, such as `rsample`, `cvms`, and `mlr3`. Feel free to explore them based on your specific needs.

```{r}
set.seed(123)
penguin_boot <- bootstraps(penguin_train)
penguin_boot
```

- Plus d’option à : https://www.rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf
