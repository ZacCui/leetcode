#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-07 06:42:57
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        level = 0
        self.orderBottom(root, res, level)
        res.reverse()
        return res
    
    def orderBottom(self, root: TreeNode, res: List[List[int]], level: int) -> List[List[int]]:
        if not root: return
        self.orderBottom(root.left, res, level + 1)
        self.orderBottom(root.right, res, level + 1)
        while len(res) - 1 < level :
            res.append([])
        res[level].append(root.val)
            