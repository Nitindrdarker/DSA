# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        res = 0
        isSigned = False
        if x < 0:
            isSigned = True
            x = -1 * x
        
        while(x):
            lastDigit = x % 10
            x = x // 10

            if (MAX - lastDigit) // 10 < res:
                return 0
            res = (res * 10 + lastDigit)
            
        if isSigned:
            if -1 * res >= MIN:
                return -1 * res
            return 0
        return res

