# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        nums.sort()
        def util(index):
            if index > len(nums):
                return
            res.append(curr.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1] :
                    continue
                curr.append(nums[i])
                util(i+1)
                curr.pop()
        util(0)
        return res
            