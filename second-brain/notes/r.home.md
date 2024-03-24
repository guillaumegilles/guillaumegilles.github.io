---
id: soqsg19iwcr1loa3yqv4vm5
title: "R.home()"
desc: >-
  Return the R home directory, or the full path to a component of the R
  installation.
updated: 1710870919662
created: 1704740517355
---

```R
> R.home()
[1] "C:/Produits/R/R-40~1.4"
```

A character string giving the R home directory or path to a particular component.
Normally the components are all subdirectories of the R home directory, but this
need not be the case in a Unix-like installation.

The R home directory is the top-level directory of the R installation being run.

The R home directory is often referred to as `R_HOME`, and is the value of an
environment variable of that name in an R session. It can be found outside an R
session by `R RHOME`.
