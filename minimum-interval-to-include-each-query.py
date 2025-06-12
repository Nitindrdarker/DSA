# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

# Return an array containing the answers to the queries.


import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        res = [-1] * len(queries)
        intervals.sort()
        sortedQueries = sorted([(q, i) for i,q in enumerate(queries)])
        i = 0
        for q, idx in sortedQueries:
            while(i < len(intervals) and intervals[i][0] <= q):
                left, right = intervals[i]
                s = (right - left + 1)
                heapq.heappush(minHeap, (s, right))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[idx] = minHeap[0][0]
        return res

             
