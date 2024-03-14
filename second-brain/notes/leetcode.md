---
id: xuzn32oldlc3xe3cf0gmceo
title: Leetcode
desc: 'Mes solutions aux challenges Leetcode, souvent en Python'
updated: 1697431885522
created: 1690489131821
---

## 1480. Running Sum of 1d Array
[**Easy**] - Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`. Return the running sum of `nums`.
```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
```

## 2236. Root Equals Sum of Children

[**Easy**] - You are given the `root` of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child. Return `true` if the value of the root is equal to the sum of the values of its two children, or `false` otherwise.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.right.val + root.left.val
```
