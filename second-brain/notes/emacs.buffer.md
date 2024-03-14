---
id: m0nued9h0yamjts1ioch2lu
title: buffer
desc: ''
updated: 1680276220081
created: 1680276210244
---

:PROPERTIES:
:ID:       fa65a710-0148-4d5e-ad94-6fd6ee378571
:END:
#+title: buffer

The text you are editing in Emacs resides in an object called a /buffer/. Each
time you visit a file, a buffer is used to hold the file’s text. Each time you
invoke [dired], a buffer is used to hold the directory listing, etc.

Buffers exist as long as they are in use, and are deleted (“killed”) when no
longer needed, either by you (~C-x k RET~) or by Emacs when you exit Emacs.

- https://www.gnu.org/software/emacs/manual/html_node/emacs/Buffers.html