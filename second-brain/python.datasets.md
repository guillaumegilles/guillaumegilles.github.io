---
id: kzj0qeu2oud912lkzlf2p07
title: Datasets
desc: ""
updated: 1699602071477
created: 1696765563742
---

## Charger un fichier CSV

Datasets can read a dataset made up of one or several CSV files (in this case, pass your CSV files as a list):

```python
>>> from datasets import load_dataset
>>> dataset = load_dataset("csv", data_files="my_file.csv")
```

## Ressources

- [Hugging Face documentation](https://huggingface.co/docs/datasets/v2.14.5/en/index)
