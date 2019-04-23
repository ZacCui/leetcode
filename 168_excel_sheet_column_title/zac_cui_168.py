#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-23 22:11:49
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        dic = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        res = []
        while n > 0:
            res.append(dic[(n-1)%26])
            n = (n-1) // 26
        res.reverse()
        return ''.join(res)