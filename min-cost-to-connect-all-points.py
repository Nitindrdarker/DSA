# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



from collections import defaultdict
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calc(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        h = []
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                d = calc(x1, y1, x2, y2)
                adj[i].append([d, j])
                adj[j].append([d, i])


        h.append([0, 0]) # dist, node
        visited = set()
        res = 0
        while(h):
            dist, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            res += dist

            for neighDist, neigh in adj[node]:
                if neigh not in visited:
                    heapq.heappush(h, (neighDist, neigh))
        return res


                
                
                
