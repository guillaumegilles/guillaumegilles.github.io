# Emacs Key Bindings

[[emacs]] uses a combination a key to quickly access several fonctionality.

## Essentials to know

- `C-x` il faut appuyer _simultanèment_ sur les touches `Ctrl` et `x`
- `M` signifie _Meta_, surles clavier récent il s’afit de la touche `Alt`
- `S` `Shift`
- `s` `super`. c’est-à-dire la touche « windows »
- `M-x` permet d’accéder aux commandes d’Eemacs

## Navigating inside [[emacs-buffer]]

The most basic buffer movement commands move point (the cursor) by rows (lines)
or columns (characters):

- `C-l` recenter top bottom
- `C-M-l` reposition window

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

## kit de survie dans emacs

- `C-x C-f` ouvrir un fichier
- `C-x C-s` sauvegarder un fichier
- `M-w` copier (ctrl + c)
- `C-y` coller (ctrl + v)
- `C-w` couper (ctrl + x)
- `C-/` annuler
- `C-s` rechercher dans le fichier
- `C-x C-c` quitter emacs
- `C-f` Forward one character
- `C-n` Next line
- `C-b` Back one character
- `C-p` Previous line

## Help

- `C-h r` read emacs manuel
- `C-h +` emacs tutorial
- `C-h v` show documentation for any variable
- `C-h f` show documentation for any function
- `C-h o` to look up a symbol (functions, variables, faces, etc).

## Fast navigation

- `/` search mode in the buffer
- `%` find a matching ), ], or }
- `:400` to reach the 400th line
- `0` begining of a line

* emacs

\*\* Ctrl + c / Ctrl + v

\*\*\* yank (copier)

- `y` yank = copy
- `yy` yank a line

\*\*\* put (coller)

- `p` put /after/ the cursor = past
- `P` put /before/ the cursor

\*\*\* delete things (couper)

- `x` delete a character

- `dw` delete a word
- `d$` delete from the cursor to the end of a line
- `dd` delete an entire line
- `3dd` delete 3 lines

- `diw` delete in word (point in a word)
- `di"` delete inner quotation mark at point
- `dt(` delete till parenthese

\*\* gestion des frames

- `C-z` minise frame

\*\* typing

- `C-g` quit: cancel running or partially typed command

\*\* dired

- `C-x d` open directory (dired)

\*\* [[id:7762a729-68b2-4d84-ae09-ee3bbd02c481][window]] management

\*\*\* split

`C-x 2` split window vertically
`C-x 3` split window horizontally
`C-x 1` back to one window

\*\*\* switching between [[id:7762a729-68b2-4d84-ae09-ee3bbd02c481][window]]

`C-x o` switch to the next [[id:7762a729-68b2-4d84-ae09-ee3bbd02c481][window]]

`C-x C-+` zoom in
`C-x C--` zoom out
`C-x C-0` default zoom

\*\* buffer

`C-x b` switch between buffer
`C-x C-b` list of all the buffers
`C-x k` kill buffer
`C-M-x` <eval-defun> evalue la ligne ou le curseur est positioné

- [[id:c6c36175-8e57-412b-9f99-56342786729a][org-mode]]

`C-c C-,` insérer un block

\*\* org roam

(("C-c n l" . org-roam-buffer-toggle)
("C-c n f" . org-roam-node-find)
("C-c n g" . org-roam-graph)
("C-c n i" . org-roam-node-insert)
("C-c n c" . org-roam-capture)
;; Dailies
("C-c n j" . org-roam-dailies-capture-today))

\*\* visibility cycling

`TAB` rotate current subtree among the states
,-> FOLDED -> CHILDREN -> SUBTREE --.
'-----------------------------------'

`S-TAB` rotate the entire buffer among the states
,-> OVERVIEW -> CONTENTS -> SHOW ALL --.
'--------------------------------------'

\*\* TODO sparse trees

\*\* todo

`C-c C-t` Rotate the TODO state of the current item among

,-> (unmarked) -> TODO -> DONE --.
'--------------------------------'

\*\* bloc

`C-c C-c` evaluate bloc of code

\*\* properties

`C-c C-x p` set a property. This prompts for a property name and a value.
`C-c C-c d` remove a property from the current entry.

- Command mode (normal mode)

\*\* find and jump

find the next _ after point `f_`find the next _ *before* point`F*`
jump one place before * after point `t_`
jump one place before _ *before* point `T_`

mark text using character mode `m[a-z]`
mark line using line mode `M[a-z]`
jump to position marked `a` `'a`

looking for the same word after the point in file `#`
looking for the same word before the point in file `\*`

find the word /foo/ after point `/foo`
jump to the next word found after point `n`
jump to the next word found before point `N`
search the word /foo/ before point `?foo`

\*\* replace and change command

`r` replaces a character under the cursor
`R` enters Replace mode until <ESC> is pressed to exit

`cw` changes part or all of a word
change a character `l` `c`
change inner word at point `lié` `ciw`
change inner quotation mark at point `ci"`
change inner paranthese at point `ci(`
change inner square bracket at point `ci[`
change inner sfsdfs at point `ci{`

\*\* oups…

`u` undo
`C-r` redo

`:s/old/new/g` _substitue_ 'old' with 'new'
`:#,#s/old/new/g` *substitute every occurenec of 'old' by 'new' between lines # and #
`:%s/old/new/g` *substitue\* every occurrence in the whole buffer

`.` repeat the last command entered

\*\* Commands

\*\*\* writing files

`:w` _writes_ the file = saves
`:w <filename>` _writes_ the changes made into a file name <filename>
`:#,#w FILENAME` _writes_ the lines # through # in file FILENAME.
`:r FILENAME` retrieves disk file FILENAME and inserts it into the current buffer following the cursor position

\*\*\* quit emacs

`:q` quit
`:q!` quit + /without/ saving
`:qa!` quit + alert + /without/ saving

`:wq` write + quit
`:wqa` write + quit + alert

`:!<shell command>` execute external command like `ls`, `rm`, etc.

\*\* indent

indent to the right `>`
indent to the left `<`
indent a line automatically `==`

- insert text

`i` insert mode /before/ the cursor
`I` insert mode at the begining of the line
`a` insert mode /after/ the cursor
`A` insert mode at the end of the line

`o` _open_ command to insert mode /under/ the current line
`O` _open_ command to insert mode /above/ the current line

- Visual mode

`v` visual mode
visual bloc mode `Ctrl-v`

----- vim registers

Vim registers are spaces in memory that Vim uses to store some text or
operation details. Each of these spaces has an identifier so that it can be
accessed later.

To see the list of registers `:reg`

---- macros

start recording a macro in the register /a/ `qa`
calling a macro in the register /a/ `@a`

[//begin]: # "Autogenerated link references for markdown compatibility"
[emacs]: emacs.md "Emacs"
[emacs-buffer]: emacs-buffer.md "Emacs Buffer"
[//end]: # "Autogenerated link references"
