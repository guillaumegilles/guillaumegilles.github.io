---
id: ox7ecx59k9717akvvply42p
title: glimpse()
desc: ''
updated: 1684231873203
created: 1680278081076
---

~glimpse()~ is like a transposed version of ~print()~: columns run down the page,
and data runs across. This makes it possible to see every column in a data frame.
It's a little like ~str()~ applied to a data frame but it tries to show you as
much data as possible. (And it always shows the underlying data, even when
applied to a remote data source.)

~glimpse()~ is provided by the pillar package, and re-exported by dplyr.
See ~pillar::glimpse()~ for more details.

https://www.rdocumentation.org/packages/dplyr/versions/1.0.10/topics/glimpse