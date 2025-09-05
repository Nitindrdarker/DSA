# You are given two integers num1 and num2.

# In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.

# Return the integer denoting the minimum number of operations needed to make num1 equal to 0.

# If it is impossible to make num1 equal to 0, return -1.



class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        def countBits(val):
            count = 0
            while val > 0:
                count += val & 1
                val >>= 1
            return count

        for m in range(1, 61):
            val = num1 - m * num2
            if val < 0:
                # if num2 is positive or zero, no point continuing
                if num2 >= 0:
                    break
                

            bits = countBits(val)
            if bits <= m and val >= m:
                return m
        return -1
