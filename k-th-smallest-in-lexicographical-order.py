# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if n < k:
            return -1


        def getCount(prefix, n):
            current = prefix
            nextCurrent = prefix + 1
            c = 0
            while(current <= n):
                c += min(n+1, nextCurrent) - current #calculate the range from [prefix, min(n, next number rangelike betweeen 1, 2)]
                current = current * 10
                nextCurrent = nextCurrent * 10
            return c


        prefix = 1
        k -= 1
        while(k > 0):
            count = getCount(prefix, n)
            if count <= k: #count is smaller than k  so skip, and decrease the k wuith total count in this range
                prefix += 1
                k -= count
            else:
                prefix = prefix * 10
                k -= 1

        return prefix