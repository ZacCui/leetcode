#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-01 15:21:50
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not len(nums): return 0
        memo = [None] * len(nums)
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1] + nums[i], nums[i])
        return max(memo)