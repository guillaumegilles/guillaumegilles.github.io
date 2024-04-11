# Quarto

An open-source scientific and technical publishing system

- Author using [[jupyter]] notebooks or with plain text markdown in your
  favorite editor.
- Create dynamic content with [[python]], [[r]], Julia, and Observable.
- Publish reproducible, production quality articles,
  [[quarto-revealjs]], dashboards, [[quarto-website]], blogs, and books in HTML,
  PDF, MS Word, ePub, and more.
- Share knowledge and insights organization-wide by publishing to Posit Connect,
  Confluence, or other publishing systems.
- Write using [Pandoc](https://pandoc.org/) markdown, including equations,
  citations, crossrefs, figure panels, callouts, advanced layout, and more.

## How it works

When you render a `.qmd` file with Quarto, the executable code blocks are
processed by [[jupyter]], and the resulting combination of code, markdown, and
output is converted to plain markdown. Then, this markdown is processed by
[[pandoc]], which creates the finished format.

![Quarto How It Works](../assets/images/qmd-how-it-works.png)

## [Markdown Basics in Quarto](https://quarto.org/docs/authoring/markdown-basics.html)

Quarto is based on [[markdown-pandoc]] and uses its variation of markdown as its
underlying document syntax.

## Building Blocks of a Quarto Document

1. [[quarto.yaml]]
2. [[quarto.markdown]]
3. [[quarto.code-cell]]

## Cheatsheet

| Actions                           | VSCode command  | Keybindings        |
| --------------------------------- | --------------- | ------------------ |
| render and preview                | Quarto: Preview | `Ctrl+Shift+K`     |
| add a code cell                   |                 | `Ctrl+Shift+I`     |
| execute (run) the current cell    |                 | `Ctrl+Shift+Enter` |
| execute (run) the current line(s) |                 | `Ctrl+Enter`       |
| execute (run) **next** cells      |                 | `Ctrl+Alt+N`       |
| execute (run) **previous** cells  |                 | `Ctrl+Alt+P`       |
| execute (run) all cells           |                 | `Ctrl+Alt+R`       |
| execute (run) cells **above**     |                 | `Ctrl+Alt+Shift+P` |
| execute (run) cells **below**     |                 | `Ctrl+Alt+Shift+N` |

[Code Cells: Jupyter](https://quarto.org/docs/reference/cells/cells-jupyter.html)

[Bibliography Generation](https://quarto.org/docs/authoring/footnotes-and-citations.html#bibliography-generation)

### References

::: {#refs}
:::
