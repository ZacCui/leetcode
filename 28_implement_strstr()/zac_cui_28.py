#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-27 15:06:17
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not len(needle): return 0
        if len(haystack) < len(needle): return -1
        diff = len(haystack) - len(needle) + 1
        for i in range(diff):
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i
        return -1