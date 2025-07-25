# You are given an integer array nums.

# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.



from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximum = max(nums)
        if maximum <= 0:
            return maximum


        count = set(nums)
        res = 0
        for i in count:
            if i > 0:
                res += i
        return res
