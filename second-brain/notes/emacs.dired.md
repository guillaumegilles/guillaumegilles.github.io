---
id: zlpymeyhaa4ymu8siuwp1ji
title: dired
desc: ''
updated: 1680276479760
created: 1680276474035
---

:PROPERTIES:
:ID:       a213d009-f463-4ee5-9097-83b4390921e1
:END:
#+title: dired

dired makes an Emacs buffer containing a listing of a directory, and optionally
some of its subdirectories as well. You can use the normal Emacs commands to
move around in this buffer, and special dired commands to operate on the listed
files. dired works with both local and remote directories.

To invoke Dired, type ~C-x d~ (dired). This reads a directory’s name using the
[minibuffer], and opens a dired [buffer] listing the files in that directory.
You can also supply a wildcard file name pattern as the minibuffer argument,
in which case the Dired buffer lists all files matching that pattern.
A wildcard may appear in the directory part as well. For instance,

#+BEGIN_SRC
C-x d  ~/foo/*.el  RET
C-x d  ~/foo/*/*.el  RET
#+END_SRC

- https://www.gnu.org/software/emacs/manual/html_node/emacs/Dired-Enter.html