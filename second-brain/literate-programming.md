---
id: zd3zm1k87veoom4o1k14z7k
title: Literate Programming
desc: ""
updated: 1704127725975
created: 1689967941437
---

| Année | Tech                     | Author             |
| ----- | ------------------------ | ------------------ |
| 1978  | TeX                      | Donald Knuth       |
| 1984  | Literate Programming     | Donald Knuth       |
| 1988  | Mathematica Notebooks    | Stephem Wolfram    |
| 2001  | IPython                  | Fernando Perez     |
| 2003  | Emacs org-mode Notebooks | Carsten Dominik    |
| 2004  | [[markdown]]             | John Gruber        |
| 2005  | Sage Notebook            | Willian Stein      |
| 2006  | Pandoc                   | John MacFarlane    |
| 2009  | GitHub Flavored Markdown | Tom Preston-Werner |
| 2011  | iPython Notebook         | Fernando Perez     |
| 2012  | knitr                    | Yihui Xie          |
| 2014  | Project Jupyter          | Fernando Perez     |

- Dive in literate programming paradigm

> floating TOC on the side

> footnotes

> abstrat = adjusted center in the middle of the page

- Abstract

sdfqsdfqsdf

- What is literate programing

\*\* Its origin

knuth, author of "The art of computer programming" fondation paper in 1984

\*\* Influence in today notebook

you can see influences of literate programming in jupyter notebook or google collab

So, i can start with literate programming; let's take of look of a workflow with emacs org mode

- Setting up the environment

\*\* Programming language compiler

As demonstrate bu Khuth, the machine need '2' compiler:

1. the compiler for the writing document : org mode (the "writing" language, in our case is an `.org` file)
2. the compiler for the programming language embbed in the writing doc, i.e, javascript, python, etc.

\*\* Org Mode

\*\*\* integration between Org Mode and programing language

> For the purpose of this blog, I'll use python code to illustrate the configuration required.

If you’re following along in Emacs, you’ll need to enable the integration between Org Mode and JavaScript. You can do this by adding the following line to your Emacs config:

```
(require 'ob-js)
```

You also need to have Node.JS installed on your computer. This is the normal situation for any programming language you want to support in Org-mode. First, you need the tools to execute that language installed on your computer. Then, you need to tell Emacs how to call it by adding something like that require statement to your Emacs config.

- Footnotes

* [Literate Programming: Empower Your Writing with Emacs Org-Mode](https://www.worthe-it.co.za/blog/2018-05-28-literate-programming.html)

- Ressources

* https://www.youtube.com/playlist?list=PLVtKhBrRV_ZkPnBtt_TD1Cs9PJlU0IIdE
* http://www.literateprogramming.com/knuthweb.pdf
* https://orgmode.org/worg/org-contrib/babel/intro.html
* https://www.jstatsoft.org/article/view/v046i03
* https://www.mfoot.com/blog/2015/11/22/literate-emacs-configuration-with-org-mode/

  - https://www.mfoot.com/blog/2015/11/22/literate-emacs-configuration-with-org-mode/

    https://quarto.org/docs/computations/r.html#emacs

  1.  https://www.youtube.com/watch?v=GK3fij-D1G8
  2.  https://www.mfoot.com/blog/2015/11/22/literate-emacs-configuration-with-org-mode/
  3.  https://systemcrafters.net/emacs-essentials/
  4.  https://systemcrafters.net/emacs-from-scratch/
      what are dotfile ????
  5.  emacs/init.el
  6.  https://orgmode.org/manual/Literal-Examples.html
  7.  https://docs.doomemacs.org/v21.12/modules/config/literate/

2. setting up jekyll + github pages
3. blogging with jekyll + org mode
4. Setting up org mode with Jekyll to blog (https://www.worthe-it.co.za/blog/2016-09-21-static-website-generation-with-jekyll.html)
5. workflow for blogs and projects = emcas / org mode / org roam + zotero
