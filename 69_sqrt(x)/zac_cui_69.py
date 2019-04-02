#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-02 17:49:54
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (1,0): return x
        lo = 1
        hi = x
        while lo + 1 < hi:
            res = (hi + lo) // 2
            curr_value = res**2
            if curr_value > x:
                hi = res - 1
            elif curr_value < x:
                lo = res
            else:
                return res
        return lo + 1 if (lo + 1)** 2 < x else lo
        