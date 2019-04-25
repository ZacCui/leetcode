#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-25 17:57:08
'''

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate