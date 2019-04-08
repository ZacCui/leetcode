#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-08 11:38:54
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depthDiff(root) != -1 
    
    def depthDiff(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.depthDiff(root.left)
        right = self.depthDiff(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1: return -1
        return max(left, right) + 1