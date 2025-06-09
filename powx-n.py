# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def util(x, n):
            if n == 1:
                return x
            val = util(x, n//2)
            if n % 2 == 0:
                return val * val
            return val * val * x
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1/util(x, abs(n))
        return util(x, n)
                