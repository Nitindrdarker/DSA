# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memo = {}
        # def util(i, isBuy):
        #     if i >= len(prices):
        #         return 0
        #     if (i, isBuy) in memo:
        #         return memo[(i, isBuy)]
        #     profit = 0
        #     if isBuy:
        #         take = util(i+1, False) - prices[i]
        #         skip = util(i+1, isBuy)
        #         profit = max(take, skip)
        #     else:
        #         sell = util(i+2, True) + prices[i]
        #         skip = util(i+1, isBuy)
        #         profit = max(sell, skip)
        #     memo[(i, isBuy)] = profit
        #     return profit
        # return util(0, True)


        memo = [[0 for i in range(2)]for i in range(len(prices))]


        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                if j == 0:
                    #isbuy
                    take = (memo[i+1][1] if i+1 < len(prices) else 0) - prices[i]
                    skip = memo[i+1][j] if i+1 < len(prices) else 0
                    memo[i][j] = max(take, skip)
                else:
                    #isSell
                    sell = (memo[i+2][0] if i+2 < len(prices) else 0) + prices[i]
                    skip = memo[i+1][j] if i+1 < len(prices) else 0
                    memo[i][j] = max(sell, skip)
        return memo[0][0]