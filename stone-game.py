# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        memo = {}
        def util(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            isEven = (j + i) % 2 == 0
            left = util(i+1, j) + (piles[i] if isEven else 0)
            right = util(i, j-1) + (piles[j] if isEven else 0)
            memo[(i, j)] = max(left, right)
            return memo[(i, j)]
            

        a = util(0, len(piles)-1)
        return total - a < a