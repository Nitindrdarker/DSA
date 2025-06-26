# Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

# Alice and Bob take turns, with Alice starting first.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.



from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefSum = [0]
        for i in piles:
            prefSum.append(prefSum[-1] + i)
        memo = {}
        def util(isA, m, index):
            if index >= len(piles):
                return 0
            if (isA, m, index) in memo:
                return memo[(isA, m, index)]
            curr = 0
            for i in range(index, min(index + (2 * m), len(piles))):
                if isA:
                    currSum = prefSum[i+1] - prefSum[index]
                    curr = max(curr, currSum + util(False, max(m, i+1 - index), i+1))
                else:
                    curr = min(util(True, max(m, i+1 - index), i+1), curr) if curr != 0 else util(True, max(m, i+1 - index), i+1)
            memo[(isA, m, index)] = curr
            return curr
        return util(True, 1, 0)                
                
 