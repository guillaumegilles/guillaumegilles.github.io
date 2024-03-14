---
id: f30gd81m83dibawpsj7a3nu
title: tidymodels
desc: "collection of packages for modeling and machine learning using tidyverse 
principles."
updated: 1684586241651
created: 1684523531211
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