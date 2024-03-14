---
id: 7i7kyyjvk6r82jg938775qc
title: Org
desc: ''
updated: 1689968316346
created: 1689757306195
---

:PROPERTIES:
:ID:       002f6e45-905d-4d11-87ef-e00a54367229
:END:
#+title: org-mode

** Headlines

#+BEGIN_EXAMPLE


#+END_EXAMPLE


** Paragraphs

#+begin_example
Org uses single characters to markup *bold* /italic/, _underline_, ~code~ and
=verbatim=. Links also use minimal markup in [[https://www][website]].         :tag:
Org has more syntax, but what is shown here is enought to get started!
#+end_example

https://orgmode.org/manual/Emphasis-and-Monospace.html


** Blocks

With just a few keystrokes, it is possible to insert empty structural blocks,
such as ‘#+BEGIN_SRC’ … ‘#+END_SRC’, or to wrap existing text in such a block.


https://www.gnu.org/software/emacs/manual/html_mono/org.html#Structure-Templates


*** Quote block

#+BEGIN_QUOTE
Everything should be made as simple as possible,
but not any simpler ---Albert Einstein
#+END_QUOTE

https://www.gnu.org/software/emacs/manual/html_mono/org.html#Paragraphs


** Insert images

#+CAPTION: This is the caption for the next figure link (or table)
#+NAME:   fig:SED-HR4048
[[./img/a.jpg]]

https://www.gnu.org/software/emacs/manual/html_mono/org.html#Images

** properties

Properties are key-value pairs associated with an entry. They live in a special
drawer with the name ‘PROPERTIES’. Each property is specified on a single line,
with the key (surrounded by colons) first, and the value after it:

#+begin_example
    :PROPERTIES:
    :Title:     Goldberg Variations
    :Composer:  J.S. Bach
    :Publisher: Deutsche Grammophon
    :NDisks:    0
    :END:
#+end_example


~C-c C-x p~ Set a property. This prompts for a property name and a value.
~C-c C-c d~ Remove a property from the current entry.