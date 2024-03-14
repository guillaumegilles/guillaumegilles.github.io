---
id: aqo4zf1twfs9smm4ju59wfp
title: numeric
desc: "valeurs numériques en R"
updated: 1684257621127
created: 1684233590899
---

un type de données `numeric` est un nombre entier, un réel : **1**, **2.23**, 
etc.

```{r}
> x <- 6.7765765
> mode(x)
[1] "numeric"
```

le type de données, `dbl` est une construction du `numeric` car il s’agit d’une 
valeur numérique décimale.

On peut tester l’appartenance au [[mode|r.dt]] `numeric`grâce à la fonction 
[[r.base.is-numeric]]

```{r}
> is.numeric(x)
[1] TRUE
```

## références

@hussonPourStatistiqueScience2018