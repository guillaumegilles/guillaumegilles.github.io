---
id: 1znsofzcbmawr836n53klvf
title: ls
desc: affiche une liste des éléments
updated: 1689891615927
created: 1680278594452
---

:PROPERTIES:
:ID:       22ecf6b6-bd91-4ef9-8b25-c134f4dd2f90
:END:
#+title: ls

Pour afficher les éléments du fichier dans lequel on se trouve, on utilise ~ls~
pour *liste*

#+begin_src shell
$ ls
#+end_src

les éléments en vert avec une astérix (*) sont des fichiers éxécutables, comme
ceux qu'on peut double-cliquer dans une GUI.

Toutefois, les éléments cachés ne sont pas visible. Dans ce cas il faut ajouter
l’argument ~-a~ :

#+begin_src shell
$ ls -a
#+end_src


** Références

- https://ubuntu.com/tutorials/command-line-for-beginners#4-creating-folders-and-files
- https://www.digitalocean.com/community/tutorials/bashrc-file-in-linux