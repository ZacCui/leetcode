#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-06 16:48:51
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n: return
        i, j = m - 1, n - 1
        index = m + n - 1
        while j >= 0:
            if i < 0 or nums1[i] <= nums2[j]:
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1
