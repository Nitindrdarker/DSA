# You are given an integer array nums and an integer k.

# Your task is to determine whether it is possible to partition all elements of nums into one or more groups such that:

# Each group contains exactly k distinct elements.
# Each element in nums must be assigned to exactly one group.
# Return true if such a partition is possible, otherwise return false.



from ast import List
from typing import Counter


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        groupNumber = len(nums) // k
        count = Counter(nums)
        # print(groupNumber, count)
        for i in count:
            if count[i] > groupNumber:
                return False
        return True