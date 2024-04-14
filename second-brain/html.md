---
id: s7wdaw735t18m40j3w6p5pu
title: HTML
desc: HyperText Marukup Language
updated: 1698993328091
created: 1680261152396
---

HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentation (CSS) or functionality/behavior (JavaScript).

## Éléments

HTML uses "markup" to annotate text, images, and other content for display in a Web browser. HTML markup includes special "elements". Un élément est une partie d'une page web. Il est typiquement constitué d'une **balise ouvrante** (_opening tag_) pouvant contenir des [[html#attributs]], d'un **contenu textuel** et d'une **balise fermante** (_closing tag_).

![HTML element](/assets/anatomy-of-an-html-element.png)

Les éléments sont :

- <head>
- <title>
- <body>
- <header>

## Attributs

Un attribut permet de fournir des informations supplémentaires sur [[html#éléments]]. Il doit être inclu dans la balise ouvrante :

```html
<a href="https//example.com">Website</a>
```

Pour reconnaître un attribut, on fait attention à :

- L'attribut se trouve dans la balise ouvrante ;
- Il est suivit par le signe `=` ;
- La valeur de l'attribut est contenu entre guillaumets `"example"`

## Commentaires

Les commentaires HTML commencent par `<!--` et se terminent par `-->`.

```html
<!-- Fill out this section after waking up -->
```

```html
<!--
    this is an html comment
-->
```

## CSS

En HTML, il n'est pas recommandé d'inclure les style dans les balises HTML. On utilise donc deux fichiers distincts. Le premier, `index.html` est utilisé pour le contenu en HTML. Le deuxième, `stlye.css` est utilisé pour la mise en forme de la page web. Pour inclure le fichier CSS dans le fichier HTML on utilise l'élément [[html.<link>]] qu'on insère dans l'élément `<head>`.

```html
<head>
  <link href="style.css" rel="stylesheet" />
</head>
```

## Références

- [mdn web docs: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [mdn web docs: Element](https://developer.mozilla.org/en-US/docs/Glossary/Element)
