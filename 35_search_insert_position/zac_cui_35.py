#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-03-28 19:58:01
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return 0
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
        if lo == len(nums) - 1 and nums[lo] < target:
            return len(nums)
        return lo
            