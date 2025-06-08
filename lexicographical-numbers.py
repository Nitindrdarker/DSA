# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 



from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        val = []
        def util(i):
            if i > n:
                return
            val.append(i)
            for j in range(10):
                if i * 10 + j > n:
                    break
                util(i * 10 + j)
        for i in range(1, 10):
            util(i)

        return val