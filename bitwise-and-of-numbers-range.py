# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shiftCounter = 0
        while(left != right):
            left = left >> 1
            right = right >> 1
            shiftCounter += 1
        return left << shiftCounter

        
