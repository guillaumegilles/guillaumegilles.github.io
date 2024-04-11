# [Scholarly Writing](https://quarto.org/docs/authoring/footnotes-and-citations.html)

## Export Zotero collection in [[quarto]]

1. Install [zotero-better-bibtex](https://retorque.re/zotero-better-bibtex/installation/index.html)
   add-on.
2. `Export Collection...` ou `Export Library...` depuis _Zotero_ pour créer un
   [Automatic Export avec Better BibTex](https://retorque.re/zotero-better-bibtex/exporting/auto/index.html).

## [Citation layout](https://quarto.org/docs/authoring/article-layout.html#global-options)

In a document [[quarto-yaml]], add `citation-location:` keyword:

```yaml
---
bibliography: references.bib
citation-location: margin
---
```
