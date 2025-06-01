


# You are given two positive integers n and limit.

# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(max(0, n - (2 * limit)), min(n, limit) + 1):
            yStarting = max(0, n - limit - i)
            yEnding = min(n - i, limit)
            if yStarting <= yEnding:
                r = (yEnding - yStarting + 1)
                ans += r
        return ans

