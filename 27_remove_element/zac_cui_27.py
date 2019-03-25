#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-25 22:28:35
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num = 0
        j = len(nums)
        while num < j:
            if val == nums[num]:
                nums[num] = nums[j - 1]
                j -= 1
            else:
                num += 1 
        return num