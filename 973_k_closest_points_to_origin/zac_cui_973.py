#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-11 11:49:21
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:K]