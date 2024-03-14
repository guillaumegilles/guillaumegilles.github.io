---
id: ngw2b9rdzzcpaw5pe6j54o0
title: IPython
desc: ''
updated: 1691302022827
created: 1691301541059
---

IPython provides a rich architecture for interactive computing with:

- A powerful interactive shell.
- A kernel for [[jupyter]].
- Support for interactive data visualization and use of GUI toolkits.
- Flexible, embeddable interpreters to load into your own projects.
- Easy to use, high performance tools for parallel computing.

## magic function

Python has a set of predefined ‘magic functions’ that you can call with a command 
line style syntax. There are two kinds of magics, line-oriented and cell-oriented. 
Line magics are prefixed with the `%` character and work much like OS command-line 
calls: they get as an argument the rest of the line, where arguments are passed 
without parentheses or quotes. Lines magics can return results and can be used 
in the right hand side of an assignment. 

Cell magics are prefixed with a double `%%`, and they are functions that get as 
an argument not only the rest of the line, but also the lines below it in a 
separate argument.

```python
%matplotlib inline
```

> With this backend, the output of plotting commands is displayed inline within 
> frontends like the Jupyter notebook, directly below the code cell that produced 
> it. The resulting plots will then also be stored in the notebook document.

## Références

- https://ipython.org/

