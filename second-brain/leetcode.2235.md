---
id: oq30l9eokfl2t20d0myof2d
title: Add Two integers
desc: 'Given two integers num1 and num2, return the sum of the two integers.'
updated: 1709546249628
created: 1709544869019
tags: easy
---

1. **Example 1:**

    ```
    Input: num1 = 12, num2 = 5
    Output: 17
    Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
    ```

2. **Example 2:**

    ```
    Input: num1 = -10, num2 = 4
    Output: -6
    Explanation: num1 + num2 = -6, so -6 is returned.
    ```

## Constraints

- `-100 <= num1, num2 <= 100`

## Solution

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```