# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count(k):
            c = 0
            for i in piles:
                c += ceil(i / k)

            return c <= h
        # print(count(3))
        left = 1
        right = max(piles)
        res = right
        while(left <= right):
            mid = (left + right) // 2
            if count(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1


        return res