#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-08 13:53:23
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
        if not root: return False
        val = _sum - root.val
        if val == 0 and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)