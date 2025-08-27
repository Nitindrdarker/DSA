# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.



from ast import List
from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        weightMap = {}


        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w * 2))

                
            
        if n-1 not in adj:return -1

        seen = set()
        heap = []
        heapq.heappush(heap, (0, 0)) #weight, node
        while(heap):
            
            weight, node = heapq.heappop(heap)
            if node == n - 1:
                return weight
            if node in seen:
                continue
            seen.add(node)
            for neigh, w in adj[node]:
                heapq.heappush(heap, (weight + w, neigh))
                
        return -1
                
            
            
            
        
        
        