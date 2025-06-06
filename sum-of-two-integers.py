# Given two integers a and b, return the sum of the two integers without using the operators + and -.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        INT_MAX = 2 ** 31 - 1

        while b != 0:
            carry = ((a & mask) & (b & mask)) << 1
            a = (a & mask) ^ (b & mask)
            b = carry & mask
        return a if a <= INT_MAX else ~(a ^ mask)

