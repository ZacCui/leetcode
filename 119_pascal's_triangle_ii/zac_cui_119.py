#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-09 19:02:58
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        res = [[None] * rowIndex, [None] * rowIndex ]
        for i in range(rowIndex):
            for j in range(i + 1):
                if j in {0,i}:
                    res[i%2][j] = 1
                else:
                    res[i%2][j] = res[(i-1)%2][j-1] + res[(i-1)%2][j]
        return res[(rowIndex - 1)%2]