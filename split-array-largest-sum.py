# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.


from ast import List
from math import ceil


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(s):
            currSum = 0
            count = 0
            for i in nums:
                if i > s:
                    return float("inf")
                currSum += i
                if currSum > s:
                    currSum = i
                    count += 1

            count += 1
            return count
        totalSum = sum(nums)
        left = ceil(totalSum / k)
        right = sum(nums)
        res = 0
        while(left <= right):
            mid = (left + right) // 2
            c = canSplit(mid)
            if c == k:
                res = mid
                right = mid - 1
            elif c > k:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
            # print(mid, canSplit(mid))
        return res


        
