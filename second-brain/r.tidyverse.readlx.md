---
id: rvaj09yh6qvx8bhki659243
title: readlx
desc: ''
updated: 1680861693788
created: 1680277051695
---

# readxl a [tidyverse package](l.r.pack.tidyverse.md) to import data

~readxl~ package makes it easy to get data out of Excel and into R. Compared
to many of the existing packages (e.g. gdata, xlsx, xlsReadWrite) readxl has
no external dependencies, so it’s easy to install and use on all operating
systems. It is designed to work with tabular data.

~readxl~ supports both the legacy /.xls/ format and the modern xml-based
/.xlsx/ format. The libxls C library is used to support /.xls/, which abstracts
away many of the complexities of the underlying binary format. To parse .xlsx,
we use the RapidXML C++ library.

#+BEGIN_SRC
install.packages("tidyverse") # readxl is included in the tidyverse package

install.packages("readxl") # install the standalone package
library(readxl) # require to use the package
#+END_SRC

* ressource

- https://readxl.tidyverse.org/