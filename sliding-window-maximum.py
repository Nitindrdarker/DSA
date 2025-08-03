# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.\
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        left = 0
        res = []
        for right in range(len(nums)):
            if right < k:
                heapq.heappush(pq, (-nums[right], right))
            else:
                heapq.heappush(pq, (-nums[right], right))
                left += 1
            while(pq and left > pq[0][1]):
                heapq.heappop(pq)
            if(right - left + 1 == k):
                res.append(-1 * pq[0][0])
        return res

