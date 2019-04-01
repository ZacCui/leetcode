#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-01 15:36:48
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])