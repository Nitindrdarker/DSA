# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def calcEuclidean(x, y):
            return ((x ** 2) + (y ** 2)) ** (0.5)
            

        for x, y in points:
            val = calcEuclidean(x, y)
            if len(heap) >= k:
                if -1 * heap[0][0] > val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-1 * val, x, y))
            else:
                heapq.heappush(heap, (-1 * val, x, y))
        res = []
        while(heap):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res