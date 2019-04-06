#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-06 18:10:15
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.Symmetric(root.left, root.right)
        
    def Symmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None or q == None: return p == q
        return q.val == p.val and self.Symmetric(p.left, q.right) and self.Symmetric(p.right, q.left)