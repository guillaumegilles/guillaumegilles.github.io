---
id: u3781kne9dosm3y5shogkza
title: "Mettre en surbrillance des lignes de code"
desc: ""
updated: 1704123798354
created: 1704123598648
---

ou may want to highlight specific lines of code output (or even highlight distinct lines over a progression of steps). You can do this using the `code-line-number` attribute of code blocks. For example:

```{.python code-line-numbers="6-8"}
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```

## References

- [Reveal.js: Line Highlighting](https://quarto.org/docs/presentations/revealjs/#line-highlighting)
