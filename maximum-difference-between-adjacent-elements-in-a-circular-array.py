# Given a circular array nums, find the maximum absolute difference between adjacent elements.

# Note: In a circular array, the first and last elements are adjacent.

 

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        m = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            m = max(m, abs(nums[i] - nums[i-1]))
        return m
