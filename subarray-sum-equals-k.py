# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.



from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        h = {0:1}
        s = 0
        res = 0
        for i in nums:
            s += i
            
            if s - k in h:
                res += h[s - k]
            h[s] = h.get(s, 0) + 1
        return res
