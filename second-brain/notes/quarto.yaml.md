---
id: n3emms0vdhc4mgp1q7ry9kh
title: YAML options
desc: ""
updated: 1709844491974
created: 1709761268006
---

At the top of Quarto documents there is a `YAML` block with document level
options.

```code
---
title: "Quarto Basics"
format:
  html:
    code-fold: true
jupyter: python3
---
```

## Cheatsheet

### [HTML Output Format](https://quarto.org/docs/reference/formats/html.html#title-author)

Quarto supports rendering notebooks to dozens of different
[output formats](https://quarto.org/docs/output-formats/all-formats.html). By
default, the `html` format is used, but you can specify an alternate format (or
formats) within document options.

#### [Title and Author](https://quarto.org/docs/reference/formats/html.html#title-author)

| YAML      | Actions                      |
| --------- | ---------------------------- |
| `title:`  | ajouter un titre au document |
| `author:` | ajouter le nom de l’auteur   |

#### [Format Options]

| YAML      | Actions                     |
| --------- | --------------------------- |
| `format:` | specify an alternate format |

- `format:`
  - `html`
  - `ipynb`
- `toc:` _génère une table des matières_
  - `false` (par défaut)
  - `true`
- `number-sections:` _affiche une numérotation à chaque titre_

  - `false` (par défaut)
  - `true`

- execute:
  - echo: false # hide the code in the rendered version of the document

## [Code Folding](https://quarto.org/docs/get-started/computations/vscode.html#code-folding)

Rather than hiding code entirely, you might want to fold it and allow readers to view it at their discretion. You can do this via the code-fold option. Remove the echo option we previously added and add the code-fold HTML format option.

- `format:`
  - `html:`
    - `code-fold: true`

You can also provide global control over code folding:

- `format:`
  - `html:`
    - `code-fold: true`
    - `code-tools: true`

## [Figures](https://quarto.org/docs/get-started/computations/vscode.html#figures)
