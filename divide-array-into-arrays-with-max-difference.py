# You are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.

# Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:

# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.\



from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            temp = []
            for j in range(3):
                index = i + j
                if j == 0 or nums[index] - nums[i] <= k:
                    temp.append(nums[index])
                else:
                    return []
            res.append(temp)
        return res