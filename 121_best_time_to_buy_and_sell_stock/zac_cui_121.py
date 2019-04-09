#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-09 19:36:20
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        mini = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            mini = min(prices[i], mini)
            max_diff = max(prices[i] - mini, max_diff)
        return max_diff