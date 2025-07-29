# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = b = None
        acount = bcount = 0
        for i in nums:
            
            if a == i:
                acount += 1
            elif b == i:
                bcount += 1
            elif bcount == 0:
                b = i
                bcount += 1
            elif acount == 0:
                acount += 1
                a = i
            else:
                acount -= 1
                bcount -= 1
        target = (len(nums) // 3) + 1
        res = []
        
        if a != None and nums.count(a) >= target:
            res.append(a)
        if b != None and nums.count(b) >= target:
            res.append(b)
        return res
