---
id: 9dlbxr1wirlvfop1wpp6wxx
title: Code Cell in Quarto
desc: ""
updated: 1709826814248
created: 1709761700356
---

Code cells contain executable code to be run during render, with the output (and
optionally the code) included in the rendered document. Like in [[markdown]] a
code cell start with ```, but language is in {}:

```{python}
#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'}
)
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```

## [Cells options](https://quarto.org/docs/reference/cells/cells-jupyter.html)

Cell options are written in [[YAML|quarto.yaml]] using a specially prefixed
comment `#|`.

### [Attributes](https://quarto.org/docs/reference/cells/cells-jupyter.html#attributes)

| YAML     | Options                                                                     |
| -------- | --------------------------------------------------------------------------- |
| `label:` | Unique label for code cell. Used when other code needs to refer to the cell |

### [Code Output](https://quarto.org/docs/reference/cells/cells-jupyter.html#code-output)

| YAML          | Options                              |
| ------------- | ------------------------------------ |
| `echo: true`  | include source code in output        |
| `echo: false` | do not include source code in output |

### [Figures](https://quarto.org/docs/reference/cells/cells-jupyter.html#figures)

| YAML          | Options            |
| ------------- | ------------------ |
| `fig-cap:`    | Figure caption     |
| `fig-subcap:` | Figure subcaptions |

### [Panel Layout](https://quarto.org/docs/reference/cells/cells-jupyter.html#panel-layout)

| YAML           | Options                                                                         |
| -------------- | ------------------------------------------------------------------------------- |
| `layout-ncol:` | Layout output blocks into columns                                               |
| `column:`      | [Page column](https://quarto.org/docs/authoring/article-layout.html) for output |
