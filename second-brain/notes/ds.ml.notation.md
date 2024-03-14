---
id: 5e6f0tqb27bdzl84rfq2zzj
title: notation en machine learning
desc: références des notation utilisées en machine learning
updated: 1684410744691
created: 1680261909832
---

A correspondence between mathematical notation and notation in programming language.

* Regression

| Notation             | Description                                                                                             | Python       |
|----------------------+---------------------------------------------------------------------------------------------------------+--------------|
| $\mathbf{x}$         | Training example feature values                                                                         | ~x_train~    |
| $\mathbf{y}$         | Training Example  targets                                                                               | ~y_train~    |
| $x^{(i)}$, $y^{(i)}$ | $i_{th}$Training Example                                                                                | ~x_i~, ~y_i~ |
| m                    | Number of training examples                                                                             | ~m~          |
| $w$                  | parameter: weight                                                                                       | ~w~          |
| $b$                  | parameter: bias                                                                                         | ~b~          |
| $f_{w,b}(x^{(i)})$   | The result of the model evaluation at $x^{(i)}$ parameterized by $w,b$: $f_{w,b}(x^{(i)}) = wx^{(i)}+b$ | ~f_wb~       |


On retrouve ces notations dans le notebook [[cs.lang.python.ml.supervised-learning.linear-regression.ipynb]]