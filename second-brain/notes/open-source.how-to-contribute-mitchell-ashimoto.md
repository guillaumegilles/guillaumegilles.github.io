---
id: 32elt71w6l6wugqnoo05owo
title: How to Contribute Mitchell Ashimoto
desc: ''
updated: 1708959566286
created: 1708958428106
---

https://mitchellh.com/writing/contributing-to-complex-projects

1. **Become a user**:

    > try to build something real using the project, even if it is small or simple. For example, prior to contributing to the Zig programming language, I created a handful of real libraries.

2. **Build the project**:

    > Learn how to build the project and get a working binary (or equivalent). The goal is to get a binary that works well enough on your system. As you go through later steps, you’ll gain experience and confidence to start chasing down more feature complete builds.

3. **Learn the Hot-Path Internals**:

    1. Trace Down
    > start with a feature or use case, and start from the outside in to trace the codepath that the feature follows

    2. Learn up
    > After tracing a feature, it is time to actually learn how the various mapped subsystems work. Whereas with the tracing phase, I start at the outermost point such as the CLI or API call, with the learning phase, I tend to start at the innermost point.

4. **Read and reimplement recent commits**:

    > As a final step to learning internals, I read recent commits relevant to the subsystems I’ve studied and test that I fully understand why the change was made. This is my “doing the problem set in the back of the textbook” portion of learning.

5. **Make a bite-size change**:

    > At this phase, you understand the technical components of the project, and its time to learn about the human components. The goal here is to make a small change and learn the contribution and review process.
