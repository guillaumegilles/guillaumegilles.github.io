---
id: jn1t24x2b4gaghjmh3h3pyx
title: Pruning
desc: ""
updated: 1709451244552
created: 1709451038567
---

[Better, Faster Network Pruning](https://www.deeplearning.ai/the-batch/researchers-devise-pruning-method-that-boosts-ai-speed/)

Pruning weights from a neural network makes it smaller and faster, but it can
take a lot of computation to choose weights that can be removed without
degrading the network’s performance. Researchers devised a computationally
efficient way to select weights that have relatively little impact on
performance.

What’s new: Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter at Carnegie
Mellon University, Facebook AI Research, Meta AI, and Bosch Center for AI
respectively devised a method for pruning by weights and activations, or Wanda.

Key insight: The popular approach known as magnitude pruning removes the
smallest weights in a network based on the assumption that weights closest
to 0 can be set to 0 with the least impact on performance. Meanwhile, unrelated
work found that, in very large language models, the magnitudes of a subset of
outputs from an intermediate layer may be up to 20 times larger than those of
other outputs of the same layer. Removing the weights that are multiplied by
these large outputs — even weights close to zero — could significantly degrade
performance. Thus, a pruning technique that considers both weights and
intermediate-layer outputs can accelerate a network with less impact on
performance.

How it works: The authors pruned a pretrained LLaMA that started with 65 billion
parameters. Given 128 sequences of tokens drawn from a curated dataset of
English text from the web, the model processed them as follows:

- For each intermediate layer, the authors computed the norm (the magnitude
  across all the input sequences for each value in the embedding).
- For each weight in the model, they computed its importance by multiplying its
  magnitude by the corresponding norm.
- They compared the importance of weights in a layer’s weight matrix row by row;
  that is, neuron by neuron. They removed 50 percent of the least important
  weights in each row. (By contrast, typical weight pruning removes the
  lowest-magnitude weights in all rows of the weight matrix; that is, across all
  neurons in the layer.)

Results: The authors tested versions of LLaMA unpruned and pruned via various methods. The models performed a language modeling task using web text. The unpruned LLaMA achieved 3.56 perplexity (a measure of the likelihood that a model will predict the next token, lower is better). Pruned by Wanda to half its original size, it achieved 4.57 perplexity. Pruned by the best competing method, SparseGPT (which both removes weights and updates the remaining ones), it achieved the same score. However, Wanda took 5.6 seconds to prune the model, while SparseGPT took 1,353.4 seconds. Pruned by magnitude pruning, the model achieved 5.9 perplexity.

Why it matters: The ability to compress neural networks without affecting their output is becoming more important as models balloon and devices at the edge of the network become powerful enough to run them. Wanda compared weights from each row in the weight matrices (pruning per neuron), rather than each weight matrix (pruning per layer) or the model as a whole. The scale at which weights are compared turns out to be important — an interesting avenue for further research.

We’re thinking: We came up with a joke about a half-LLaMA, but it fell flat.
