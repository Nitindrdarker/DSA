# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            s += nums[right]
            while(left <= right and s >= target):
                
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1
                
        return 0 if res == len(nums) + 1 else res