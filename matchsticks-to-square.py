# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)
        if totalSum % 4:
            return False
        sideLength = totalSum // 4
        side = [0] * 4
        matchsticks.sort(reverse=True)
        def util(index):
            if index >= len(matchsticks):
                return side[0] == side[1] == side[2] == side[3]
                
            for i in range(4):
                val = matchsticks[index]
                if side[i] + val <= sideLength:
                    side[i] += val
                    if util(index + 1):
                        return True
                    side[i] -= val
                if side[i] == 0:
                    return False
            return False
        return util(0)
                        

            

