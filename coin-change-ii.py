# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo = {}
        # def util(amount, index):
        #     if amount == 0:
        #         return 1
        #     if amount < 0 or index >= len(coins):
        #         return 0
        #     if (amount, index) in memo:
        #         return memo[(amount, index)]
        #     val = 0
            
        #     take = util(amount - coins[index] ,index)
        #     skip = util(amount, index+1)
        #     memo[(amount, index)] = take + skip
        #     return memo[(amount, index)]
        # return util(amount, 0)


        memo = [[1 for i in range(len(coins))]for j in range(amount+1)]
        
        for i in range(amount-1, -1, -1):
            for j in range(len(coins)-1, -1, -1):
                take = memo[i + coins[j]][j] if i + coins[j] <= amount else 0
                skip = memo[i][j+1] if j+1 < len(coins) else 0
                memo[i][j] = take + skip
        return memo[0][0]
                

