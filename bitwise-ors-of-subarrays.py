# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        res = set()

        for i in arr:
            curr = {i}
            for j in prev:
                curr.add(j | i)
            prev = curr

            for k in prev:
                res.add(k)
        return len(res)