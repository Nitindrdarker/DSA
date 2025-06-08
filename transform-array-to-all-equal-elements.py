# You are given an integer array nums of size n containing only 1 and -1, and an integer k.

# You can perform the following operation at most k times:

# Choose an index i (0 <= i < n - 1), and multiply both nums[i] and nums[i + 1] by -1.

# Note that you can choose the same index i more than once in different operations.

# Return true if it is possible to make all elements of the array equal after at most k operations, and false otherwise.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode


from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def target(t):
            count = 0
            for i in nums:
                if i == t:
                    count += 1
            if count % 2 == 1:
                return False
            prev = -1
            c = 0
            for i in range(len(nums)):
                if nums[i] == t:
                    if prev != -1:
                        c += i - prev
                        prev = -1
                    else:
                        prev = i
                if c > k:
                    return False
            return True

        return target(-1) or target(1)
                    