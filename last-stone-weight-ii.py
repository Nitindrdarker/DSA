from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        # memo = {}
        # def util(index, currSum):
        #     if index >= len(stones) or currSum >= target:
        #         return abs(currSum - (total - currSum))
        #     if currSum > target:
        #         return float("inf")


        #     if (index, currSum) in memo:
        #         return memo[(index, currSum)]


        #     take = util( index+1, currSum + stones[index])
        #     skip = util(index+1, currSum)

        #     memo[(index, currSum)] = min(take, skip)
        #     return memo[(index, currSum)]
        # return util(0, 0)
        

        dp = [[float('inf') for curr in range(target + 1)] for i in range(len(stones))]

        for i in range(len(stones) - 1, -1, -1):
            for curr in range(target, -1, -1):
                take = dp[i+1][curr + stones[i]] if (i + 1 < len(stones) and curr + stones[i] <= target) else abs((curr + stones[i]) - (total - (curr + stones[i]))) if curr + stones[i] <= target else float('inf')
                skip = dp[i+1][curr] if i + 1 < len(stones) else abs(curr - (total - curr))
                dp[i][curr] = min(take, skip)

        return dp[0][0]