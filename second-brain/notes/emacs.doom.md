---
id: cuk0r33rozva90imsvb8413
title: doomemacs
desc: ''
updated: 1680248704927
created: 1680248692243
---

:PROPERTIES:
:ID:       15a0d36f-d436-4e4c-8bc1-f3bf33832efa
:END:
#+title: doomemacs

* What is doomemacs

Doomemacs is a Emacs distribution (flavor) configured to use Emacs out of the
box. To personalize Doomemacs, 3 files are accessible in ~~/.doom.d~

1. ~init.el~: to enable or disable Domemacs modules
2. ~config.el~: private and custom configuration of Doomemacs
3. ~packages.el~: install packages for Doomemacs on top of which we can already
   find in ~./init.el~ and ~./config.el~

* shell commands
- ~$doom sync~ to synchronize your private config with Doom by installing missing
  packages, removing orphaned packages, and regenerating caches. Run this
  whenever you modify your private ~init.el~ or ~packages.el~, or install/remove
  an Emacs package through your OS package manager (e.g. mu4e or agda).
- ~$doom upgrade~ to update Doom to the latest release & all installed packages.
- ~$doom doctor~ to diagnose common issues with your system and config.
- ~$doom env~ to dump a snapshot of your shell environment to a file that Doom
  will load at startup. This allows Emacs to inherit your ~PATH~, among other things.
- ~$doom build~ to recompile all installed packages (use this if you up/downgrade
  Emacs).
