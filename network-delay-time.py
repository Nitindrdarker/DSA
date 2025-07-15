# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#             dist = [float("inf") for i in range(n + 1)]

#             dist[k] = 0
#             for i in range(n -  1):
#                 for a, b, w in times:
#                     if dist[a] != float("inf") and dist[a] + w < dist[b]:
#                         dist[b] = dist[a] + w
#             res = 0

#             for i in range(1, n+1):
#                 if dist[i] == float("inf"):
#                     return -1
#                 res = max(res, dist[i])
#             return res

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adj = defaultdict(set)

        for a, b, w in times:
            adj[a].add((b, w))
        heap = []
        heapq.heappush(heap, (0, k))
        res = 0
        while(heap):
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            res = max(res, weight)
            visited.add(node)
            for neigh, w in adj[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (weight + w, neigh))
        # print(visited)
        return res if len(visited) == n else -1
