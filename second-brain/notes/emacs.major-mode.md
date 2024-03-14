---
id: mc0p9d7llmwt4i9n08epglb
title: major mode
desc: ''
updated: 1680276417172
created: 1680276405004
---

:PROPERTIES:
:ID:       0a1e869f-45ef-4f07-a939-506c4c351e87
:END:
#+title: major mode

Every buffer possesses a *major mode*, which determines the editing behavior of
Emacs while that buffer is current. The [mode line normally] shows the name of
the current major mode. The least specialized major mode is called
/fundamental mode/. This mode has no mode-specific redefinitions or variable
settings, so that each Emacs command behaves in its most general manner, and
each user option variable is in its default state.

Most major modes fall into three major groups:

1) modes for normal text, either plain or with mark-up, like [org-mode]
2) modes for specific programming languages, [python] mode, [R] mode, etc.
3) modes that are not associated directly with files; they are used in buffers
created for specific purposes by Emacs, like [dired].

- https://www.gnu.org/software/emacs/manual/html_node/emacs/Major-Modes.html