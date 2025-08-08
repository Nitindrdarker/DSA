# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.



from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def count(w):
            c = 0
            sums = 0
            for i in weights:
                if i > w:
                    return False
                sums += i
                if sums > w:
                    sums = i
                    c += 1
                
            c += 1
            return c <= days
                
                
        s = sum(weights)
        left = s // days
        right = s
        res = right

        while(left <= right):
            mid = (left + right) // 2
            if count(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

    