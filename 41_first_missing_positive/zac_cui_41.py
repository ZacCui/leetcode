#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-20 23:43:01
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n > 0 and n not in dic:
                dic[n] = 1
        if not len(dic):
            return 1
        for i in range(len(nums)):
            if i + 1 not in dic:
                return i + 1
        return len(nums) + 1
        