---
id: nzcgfkzdroik2wvr0ma5wlj
title: gc()
desc: garbage collection
updated: 1684231764621
created: 1680278040356
---

A call of `gc()` causes a garbage collection to take place. This will also take
place automatically without user intervention, and the primary purpose of
calling gc is for the report on memory usage. For an accurate report `full = TRUE`
should be used.

It can be useful to call `gc()` after a large object has been removed, as this
may prompt R to return memory to the operating system.

## références

- https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/gc