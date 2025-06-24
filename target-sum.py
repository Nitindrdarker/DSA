# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.




from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        # memo = {}
        # def util(index, curr):
        #     if index == len(nums):
        #         if curr == target:
        #             # print(l)
        #             return 1
        #         return 0
        #     if index > len(nums):
        #         return 0
        #     if (index, curr) in  memo:
        #         return memo[(index, curr)]
            

        #     pos = util(index+1, curr + nums[index])
        #     neg = util(index+1, curr - nums[index])
        #     memo[(index, curr)] = pos + neg
        #     return memo[(index, curr)]
        # return util(0, 0)
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[n][target] = 1  # base case: after all elements, we want to reach target

        for i in range(n - 1, -1, -1):
            for total, count in list(dp[i + 1].items()):
                dp[i][total + nums[i]] += count
                dp[i][total - nums[i]] += count

        return dp[0][0]