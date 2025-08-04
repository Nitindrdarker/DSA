# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = {}
        left = 0
        res = 0
        for right in range(len(fruits)):
            h[fruits[right]] = h.get(fruits[right], 0) + 1
            while(left <= right and len(h) > 2):
                h[fruits[left]] -= 1
                if h[fruits[left]] == 0:
                    del h[fruits[left]]
                left += 1
            res = max(right - left + 1, res)
        return res