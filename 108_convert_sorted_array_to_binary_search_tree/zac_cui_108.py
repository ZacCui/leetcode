#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-07 07:22:52
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums): return None
        return self.buildBST(nums, 0, len(nums) - 1)
    
    def buildBST(self, nums: List[int], l: int, r:int) -> TreeNode:
        if r < l:
            return None
        if r == l:
            return TreeNode(nums[r])    
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, l, mid - 1)
        root.right = self.buildBST(nums, mid + 1, r)
        return root
        