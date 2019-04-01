#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-01 15:51:08
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [ int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]	