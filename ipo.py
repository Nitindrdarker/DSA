# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.



import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pair = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(pair)
        enqueued = []
        res = 0
        c = w
        while pair or enqueued:
            
            while(pair and pair[0][0] <= c):
                cap, profit = heapq.heappop(pair)
                heapq.heappush(enqueued, (-1 * profit, cap))


            if enqueued:
                profit, cap = heapq.heappop(enqueued)
                c += -1 * profit
                res += 1
            else:
                return c

            if res == k:
                return c
        return c


            

            
            
