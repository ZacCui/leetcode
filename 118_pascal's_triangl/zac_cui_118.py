#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-09 12:18:58
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = [None] * (i + 1)
            for j in range(i+1):
                if j == 0 or j == i:
                    temp[j] = 1
                else:
                    temp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(temp)
        return res