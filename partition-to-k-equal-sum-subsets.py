# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



from ast import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums = [0] * k
        s = sum(nums)
        print(s)
        if s % k:
            return False
        target = s // k
        nums.sort(reverse=True)
        def util(index):
            if index >= len(nums):
                return all(x == target for x in sums)
            for i in range(k):
                if sums[i] + nums[index] <= target:
                    sums[i] += nums[index]
                    if util(index+1):
                        return True
                    sums[i] -= nums[index] 
                if sums[i] == 0:
                    return False
            return False
        return util(0)