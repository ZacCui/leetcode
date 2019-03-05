#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-05 23:24:56
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy1, buy2 = prices[0], prices[0]
        sell1, sell2 = 0, 0
        
        for i in range(1, len(prices)):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)
            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2