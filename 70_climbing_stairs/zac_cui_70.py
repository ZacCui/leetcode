#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-02 18:57:39
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if not n: return 1
        if n < 2: return n
        memo = [None] * 3
        memo[0], memo[1] = 1, 2
        for i in range(2, n):
            memo[i % 3] = memo[(i-1)%3] + memo[(i-2)%3]
        return memo[(n-1)%3]
        