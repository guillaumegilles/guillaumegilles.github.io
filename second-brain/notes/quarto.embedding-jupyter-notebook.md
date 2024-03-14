---
id: 5r594xvveo34agxay8hp9my
title: Embedding Jupyter Notebook
desc: ""
updated: 1704128355133
created: 1704128209176
---

You can include the output of an external Jupyter notebook in a Quarto
document with the `embed` shortcode. To embed a notebook cell, provide
the path to a Jupyter Notebook and a cell identifier. For example,
this notebook called `penguins.ipynb` has a cell labelled `fig-bill-scatter`[^1]:

```quarto
{{< embed penguins.ipynb#fig-bill-scatter >}}
```

[1]: https://quarto.org/docs/authoring/notebook-embed.html
