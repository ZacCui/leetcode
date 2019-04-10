#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-10 12:02:36
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a