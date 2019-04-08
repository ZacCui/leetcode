#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-08 11:55:25
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.right:
            return left + 1
        if not root.left:
            return right + 1
        return min(left,right) + 1
