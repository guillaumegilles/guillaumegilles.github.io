---
title: Neovim
---

## Quarto + Neovim

1. [Tutorial: Hello, Quarto](https://quarto.org/docs/get-started/hello/neovim.html#fnref1)
2. [A coffee with quarto and neovim](https://www.youtube.com/watch?v=3sj7clNowlA&list=PLabWm-zCaD1axcMGvf7wFxJz8FZmyHSJ7&index=3&t=252s)
3. [Quarto Neovim Guide](https://quarto.org/docs/tools/neovim.html)

## Installation

- [Neovim](https://neovim.io/) est un éditeur de texte qui peut paraître barbare et intimidant. Mais c'est un outil extrêmement puissant. Pour configurer simplement Neovim, il suffit de créer un fichier de configuration

```shell
mkdir ~/.config/nvim
touch init.lua
```

Et copier le contenu du fichier `init.lua` de ce [répertoire GIt](https://github.com/nvim-lua/kickstart.nvim). dans le fichier sur la machine locale.

## [`mason.nvim`](https://github.com/williamboman/mason.nvim)

installed language support for us

## [`telescope.nvim`](https://github.com/nvim-telescope/telescope.nvim)

- Ouvrir Telescope : `:Telescope`

## [`Treesitter`](https://tree-sitter.github.io/tree-sitter/)

## [`lazy.nvim`](https://github.com/folke/lazy.nvim)

`lazynvim` is a plugins. manager for neovim which automatically installed plugins.

## Key bindings

### Normal mode

- `j` down
- `k` up
- `h` left
- `l` right
- `w` hop one word
- `b` back one word
- `gg` go all the way at the top of the current buffer
- `G` go all the way to the bottom
- `zz` center the line on the screen

#### Fast Navigation

- `/` search mode in the buffer
- `%` find a matching ), ], or }
- `:400` to reach the 400th line
- `0` begining of a line

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

  start recording a macro in the register /a/ ~qa~
  calling a macro in the register /a/ ~@a~

- ## Configuration

  Le fichier de configuration de Neovim, `init.lua` se trouve dans `~/.config/nvim`. La configuration est en [[Lua]]

- NOW : setting up `init.lua`
  :LOGBOOK:
  CLOCK: [2023-09-26 Tue 07:46:20]
  CLOCK: [2023-09-26 Tue 07:46:27]
  :END:

- [Effective Neovim: Instant IDE](https://www.youtube.com/watch?v=stqUbv-5u2s)
