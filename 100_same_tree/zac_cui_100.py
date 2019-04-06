#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-06 17:13:27
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None or q == None: return p == q
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)