# You are given positive integers n and m.

# Define two integers as follows:

# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # res = 0
        # for i in range(1, n+1):
        #     res += i if i % m else -i
        # return res
        # TC(O(n))
        # SC(O(1))

        totalSum = (n * (n + 1)) // 2
        quotient = n // m
        divisibleSum = 2 * (m * ((quotient * (quotient + 1)) // 2))
        return totalSum - divisibleSum
        # TC(O(1))
        # SC(O(1))