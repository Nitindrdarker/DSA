# You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

# Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        count = 0
        for right, val in enumerate(nums):
            if val - nums[left] > k:
                left = right
                count += 1
        return count + 1
                