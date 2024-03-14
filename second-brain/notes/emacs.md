---
id: keebvc6mi60p0zocugnpjai
title: emacs
desc: ""
updated: 1704752814422
created: 1689967273383
---

## Qu'est-ce qu'[Emacs](https://www.gnu.org/software/emacs/) ?

At its core Emacs is an interpreter for Emacs Lisp, a dialect of the Lisp programming language with extensions to support text editing. Now it is an extensible, customizable, free/libre text editor — and more... much more!

- ## Frame

  In a GUI emacs occupies a graphical system-level display region. It's what we call nowadays, a "windows" and it's handled by the operating system. A **frame** normally contains a window, a menu bar, tool bar, and echo area.

- ## Window

  Emacs **window** is contained inside a frame displays one Emacs buffer at any time. A frame initially contains one window, but it can be subdivided into multiple windows.

  - ### Mode line

    At the bottom of each window is a \*_mode line_, which describes what is going on in the current buffer. When there is only one window, the mode line appears right above the ; it is the next-to-last line in the frame. On a graphical display, the mode line is drawn with a 3D box appearance. Emacs also usually draws the mode line of the selected window with a different colors from that of unselected windows, in order to make it stand out.

  - ### Echo area

    The line at the very bottom of the frame is the echo area. It is used to display small amounts of text for various purposes.

- ## Buffer

  The text you are editing in Emacs resides in an object called a **buffer**. Each time you visit a file, a buffer is used to hold the file’s text. Each time you invoke `dired`, a buffer is used to hold the directory listing, etc. Buffers exist as long as they are in use, and are deleted (“killed”) when no longer needed, either by you or by Emacs when you exit Emacs.

  - ### Mini buffer

    The minibuffer is where Emacs commands read complicated arguments, such as file names, buffer names, Emacs command names, or Lisp expressions. We call it the “minibuffer” because it’s a special-purpose buffer with a small amount of screen space. You can use the usual Emacs editing commands in the minibuffer to edit the argument text.

  - ### Major mode

    Every buffer possesses a **major mode**, which determines the editing behavior of Emacs while that buffer is current. The mode line normally shows the name of the current major mode. The least specialized major mode is called _fundamental mode_. This mode has no mode-specific redefinitions or variable settings, so that each Emacs command behaves in its most general manner, and each user option variable is in its default state. Most major modes fall into three major groups:

    - modes for normal text, either plain or with mark-up, like Org Mode,
    - modes for specific programming languages, [[Python]] mode, [[R]] mode, etc.
    - modes that are not associated directly with files; they are used in buffers created for specific purposes by Emacs, like `dired`.

  - ### Minor mode

    A minor mode is an optional editing mode that alters the behavior of Emacs in some well-defined way. Unlike [major modes], any number of minor modes can be in effect at any time. The best example is [evil mode](https://github.com/emacs-evil/evil). minor mode is useful to customize one's wrkflow!

  - ## Org Mode

    A major mode for keeping notes, authoring documents, computational notebooks, literate programming, maintaining to-do lists, planning projects, and more — in a fast and effective plain text system. On retrouve la même philosophie dans [[Quarto]].

- ## Dired

  Dired makes an Emacs buffer containing a listing of a directory, and optionally some of its subdirectories as well. You can use the normal Emacs commands to move around in this buffer, and special dired commands to operate on the listed files. Dired works with both local and remote directories.

  To invoke Dired, type `C-x d`. This reads a directory’s name using the minibuffer, and opens a dired [buffer] listing the files in that directory. You can also supply a wildcard file name pattern as the minibuffer argument, in which case the Dired buffer lists all files matching that pattern. A wildcard may appear in the directory part as well.

- ## Eshell

  Eshell is a shell-like command interpreter implemented in Emacs Lisp. It invokes no external processes except for those requested by the user, with an interface similar to command shells such as `bash`, `zsh`, `rc`, or `4dos`.

- ## Configuration

  The primary way to configure Emacs is to edit its configuration file which is written in a language called Emacs Lisp. Here are the places where you might find the main configuration file:

  - `~/.emacs` or `~/.emacs.el` - the old location for the configuration file (not recommended!)
  - `~/.emacs.d/init.el` - The main configuration file in the Emacs config folder (recommended on macOS and Windows)
  - `~/.config/emacs/init.el`` - Follows Linux desktop environment guidlines (recommended on Linux!)

- ## Distribution

  - ## Doomemacs

    Doomemacs is a Emacs distribution (flavor) configured to use Emacs out of the box. To personalize Doomemacs, 3 files are accessible in `/.doom.d`:

    - `init.el`: to enable or disable Domemacs modules
    - `config.el`: private and custom configuration of Doomemacs
    - `packages.el`: install packages for Doomemacs on top of which we can already find in `./init.el` and `./config.el`
    - #### Shell commands
      - `$ doom sync` to synchronize your private config with Doom by installing missing packages, removing orphaned packages, and regenerating caches. Run this whenever you modify your private `init.el` or `packages.el`, or install/remove an Emacs package through your OS package manager (e.g. mu4e or agda).
      - `$ doom upgrade` to update Doom to the latest release & all installed packages.
      - `$ doom doctor` to diagnose common issues with your system and config.
      - `$ doom env` to dump a snapshot of your shell environment to a file that Doom will load at startup. This allows Emacs to inherit your `PATH`, among other things.
      - `$ doom build` to recompile all installed packages (use this if you up/downgrade Emacs).

- ## Key bindings
  id:: keebvc6mi60p0zocugnpjai
  - ### Éléments essentiels
    - `C-x` : il faut appuyer _simultanèment_ sur les touches `Ctrl` et `x`
    - `M` : signifie **Meta**, sur les claviers récents il s’agit de la touche `Alt` ;
    - `S` : `Shift`
    - `s` : `super`, c’est-à-dire la touche « windows » ;
    - `M-x`: accéder aux commandes Emacs
  - ### kit de survie dans emacs
    - `C-x C-f` ouvrir un fichier
    - `C-x C-s` sauvegarder un fichier
    - `M-w` copier (ctrl + c)
    - `C-y` coller (ctrl + v)
    - `C-w` couper (ctrl + x)
    - `C-/` annuler
    - `C-s` rechercher dans le fichier
    - `C-x C-c` quitter emacs
  - ### Help
    - `C-h r` read emacs manuel
    - `C-h +` emacs tutorial
    - `C-h v` show documentation for any variable
    - `C-h f` show documentation for any function
    - `C-h o` to look up a symbol (functions, variables, faces, etc).
  - ### Naviguer dans le buffer
    - C-f Forward one character
    - C-n Next line
    - C-b Back one character
    - C-p Previous line
    - `C-l` recenter top bottom
    - `C-M-l` reposition window
    - C-a Beginning of line
    - M-f Forward one word
    - M-a Previous sentence
    - M-v Previous screen
    - M-< Beginning of buffer
    - C-e End of line
    - M-b Back one word
    - M-e Next sentence
    - C-v Next screen
    - M - > End of buffer
  - ## Gestion des frames
    - `C-z` minise frame
  - ## Typing
    - `C-g` quit: cancel running or partially typed command
  - ## Dired
    - `C-x d` open directory (dired)
  - ## Windowmanagement
    - `C-x 2` split window vertically
    - `C-x 3` split window horizontally
    - `C-x 1` back to one window
    - `C-x o` switch to the next window
    - `C-x C-+` zoom in
    - `C-x C--` zoom out
    - `C-x C-0` default zoom
  - ## Buffer
    - `C-x b` switch between buffer
    - `C-x C-b` list of all the buffers
    - `C-x k` kill buffer
    - `C-M-x` <eval-defun> evalue la ligne ou le curseur est positioné
  - ### Org Mode
    - `C-c C-x p` Set a property. This prompts for a property name and a value.
    - `C-c C-c d` Remove a property from the current entry.
    - `C-c C-,` insérer un block
    - `C-c C-t` Rotate the TODO state of the current item among
    - `C-c C-c` evaluate bloc of code

* Comment exporter un fichier `Org` dans un autre format

[[id:c8f72885-9331-401f-877f-37fb3ce73dc2][emacs exporting]]

- [[https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html][GNU Emacs manual]]
- [[https://www.gnu.org/software/emacs/manual/html_node/eintr/index.html][An Introduction to Programming in Emacs Lisp]]
- [[https://www.gnu.org/software/emacs/manual/html_node/elisp/index.html][Emacs Lisp Reference Manual]]

Vi-style : https://www.gnu.org/software/emacs/manual/html_node/viper/index.html

- variables et fonction

#+begin_src emacs-lisp

setq emacs-variables t

#+end_src

#+begin_src emacs-lisp

emacs-functions -1

#+end_src

- Se déplacer dans Emacs

https://www.gnu.org/software/emacs/tour/index.html

The most basic buffer movement commands move point (the cursor) by rows (lines) or columns (characters):

C-f Forward one character
C-n Next line
C-b Back one character
C-p Previous line

Here are some ways to move around in larger increments:

C-a Beginning of line
M-f Forward one word
M-a Previous sentence
M-v Previous screen
M-< Beginning of buffer
C-e End of line
M-b Back one word
M-e Next sentence
C-v Next screen
M-> End of buffer

- key bindings

[[id:2f6788bb-b268-4f24-af24-9a3d0f7c3a52][emacs-key-bindings]]
[[id:cd94bced-a7fa-402c-81f3-703b75e8d5f7][evil-key-bindings]]

At its core Emacs is an interpreter for Emacs Lisp, a dialect of the Lisp
programming language with extensions to support text editing. Now it is an
extensible, customizable, free/libre text editor — and more... much more!

- how emacs is build

** [[id:3635c984-e4f5-4b8e-a267-6a0744444cd5][frame]]
** [[id:7762a729-68b2-4d84-ae09-ee3bbd02c481][window]]
\*\* [[id:fa65a710-0148-4d5e-ad94-6fd6ee378571][buffer]]

- _scratch_
- _message_

** [[id:4774793e-0a63-4be5-ac62-c9d8de575667][mode line]]
** [[id:0a4cbc0f-4e38-4fd1-869b-c7f172a47eb2][echo area]]
** [[id:6a572b16-a5a7-4fbf-b6c7-19d7db0e925e][minibuffer]]
** [[id:0a1e869f-45ef-4f07-a939-506c4c351e87][major mode]]
**\* [[id:c6c36175-8e57-412b-9f99-56342786729a][org-mode]]
\*\*** [[id:0e00c59d-d036-47cb-ac59-fffd7da9ddeb][org-noter]]
**_ [[id:a213d009-f463-4ee5-9097-83b4390921e1][dired]]
_** [[id:4195d1d6-56e6-4cb0-9029-96fdf6877e1c][eshell]]
** [[id:ee2a18a5-015f-471c-9f3f-2eb9d8e172bb][minor mode]] \*** [[id:66859053-c296-4bf7-8ee6-7535dff92a3c][evil-mode]]

- Configuration
  The primary way to configure Emacs is to edit its configuration file which is
  written in a language called Emacs Lisp. Here are the places where you might
  find the main configuration file:

* ~/.emacs or ~/.emacs.el - the old location for the configuration file (not recommended!)
* ~/.emacs.d/init.el - The main configuration file in the Emacs config folder (recommended on macOS and Windows)
* ~/.config/emacs/init.el - Follows Linux desktop environment guidlines (recommended on Linux!)

- [[id:93656438-c7a3-4e29-bc3f-889947ee6def][### emacs packages]]
- [[id:1cd31faf-9bfd-4852-8ffd-e8524cbe0745][emacs key bindings]]
  Emacs uses a combination a key to quickly access several fonctionality.

- Emacs distro
  \*\* [[id:15a0d36f-d436-4e4c-8bc1-f3bf33832efa][doomemacs]]

- footnotes

* [[https://www.gnu.org/software/emacs/][GNU Emacs]]
* [[https://systemcrafters.net/emacs-from-scratch/basics-of-emacs-configuration/][The Basic of Emacs configuration]]
