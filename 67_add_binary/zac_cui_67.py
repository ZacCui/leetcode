#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-02 16:45:47
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
        