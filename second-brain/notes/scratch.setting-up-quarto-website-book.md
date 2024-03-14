---
id: 21h75ywz4fcthc3c7vu59bj
title: Setting up Quarto Website Book
desc: ""
updated: 1706996406023
created: 1705786420353
---

> Setting and running a website or a book with quarto is a rather easy endeavor. But sometimes you would like to set and run a book inside a website, and thing get bit trickier. In this blog post I'll share with you how I have created several book projects, as materials for my courses in business school, and integrated them in my own website.

creatin a website with book inside it in github
[[quarto.website]]

1. github pages are taken from `doc` : https://quarto.org/docs/publishing/github-pages.html
2. prevent render in the \_quarto.yml of the subdirectoey of the book:https://quarto.org/docs/websites/#render-targets
3. create a répertoire pour le render du book : output-dir: ../docs/decision-making-stat
4. render seperately books in each répertoire
5. direct link from quarto.yml to the book section

- [Creating a Book](https://quarto.org/docs/books/)
- https://github.com/quarto-dev/quarto-cli/discussions/3505?sort=top
- https://github.com/rstudio/r-manuals/tree/main

IS this a good `_quarto.yml` parameters :

```YAML
project:
  type: book
  output-dir: ../docs/decision-making-stat
```

When using `quarto render` or `quarto preview` inside the root file of a website, Quarto generates all `.qmd` at the root level and the sub-directories, included directory dedicated for book projects. To prevent that:

1. exclud book directory from the website \_quarto.yml

use `_metadata.yml` instead of `_quato.yml`

## But in fact, i don’t need a book project,

book project isn’t the solution to my problem, since you can create pretty much every features a book within a website

Example : arrow back and forth between chapter

```yaml
website:
  page-navigation: true

  # Other YAML options excluded for calrity

  sidebar:
    - id: introduction-business-statistics
      title: "Introduction to Business Statistics"
      align: left
      collapse-level: 2
      style: "floating"
      contents:
        - introduction-business-statistics/index.qmd
        - introduction-business-statistics/sampling-and-data.qmd
        - introduction-business-statistics/definitions-statistics-probability-key-terms.qmd
```

I tried to fit a square into a hole...
