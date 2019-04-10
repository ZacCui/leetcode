#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-10 16:37:21
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        maxi = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxi += prices[i] - prices[i - 1]
        return maxi