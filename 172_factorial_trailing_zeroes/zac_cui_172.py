#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-05-14 12:34:36
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter = 0
        while(n):
            n //= 5
            if n: counter += n
        return counter