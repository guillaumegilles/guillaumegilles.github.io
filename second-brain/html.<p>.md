---
id: go02nqvflsbqbzu8ltm3zin
title: <p>
desc: Insérer un paragraphe de texte avec l'élément <p>
updated: 1697433574230
created: 1646249871916
---

L'élément HTML `<p>` permet d'insérer un paragraphe de texte. Ces paragraphes sont des blocs de texte séparés par un espace vertical. *Atttention* Les balises `<p>` sont des éléments de bloc, les paragraphes se fermeront automatiquement si un autre élément de bloc est analysé avant la balise de fermeture `</p>`.

```html
<p>Geckos are a group of usually small, usually nocturnal lizards. They are found on every continent except Australia.</p>
 
<p>Some species live in houses where they hunt insects attracted by artificial light.</p>
```

**Note** :
1. L'attribut `align` dans les paragraphes est obsolète et ne doit pas être utilisé.
2. Pour modifier l'espacement entre les paragraphes, on utilise la propriété CSS `margin`. Il ne faut pas insérer de paragraphes vides ou d'éléments `<br>` afin de créer un espace.

**Références**

- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p
