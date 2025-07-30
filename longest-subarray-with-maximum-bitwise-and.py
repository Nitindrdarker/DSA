# You are given an integer array nums of size n.

# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.

# The bitwise AND of an array is the bitwise AND of all the numbers in it.

# A subarray is a contiguous sequence of elements within an array.



from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        res = nums[0]
        length = 1
        c = 0
        for i in range(1, len(nums)):
            nd = res & nums[i]
            if nd != maximum:
                c = max(length, c)
                length = 1
                res = nums[i]
            else:
                res = nd
                length += 1
        return max(c, length)
        

