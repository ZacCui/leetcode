#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-26 21:53:37
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        mapping = {}
        for i in range(26):
            mapping[chr(ord('A') + i)] = i + 1
        return sum([ mapping[s[len(s) - i - 1]]*26**i for i in range(len(s))])
        