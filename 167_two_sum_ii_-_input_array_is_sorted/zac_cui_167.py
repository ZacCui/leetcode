#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-11 15:48:31
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not len(numbers): return []
        lo = 0
        hi = len(numbers) - 1
        while numbers[lo] + numbers[hi] != target and lo < hi:
            if numbers[lo] + numbers[hi] > target: 
                hi -= 1
            else:
                lo += 1
        if lo == hi: return []
        return [lo+1,hi+1]
                