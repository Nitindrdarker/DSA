# There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

# Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.


from collections import defaultdict
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        adj = defaultdict(list)
        for u, v in edges2:
            adj[u].append(v)
            adj[v].append(u)
        level = defaultdict(list)

        def getMaxDegree(node, k, p, adj):
            if k < 0:
                return 0
            d = 1
            for neigh in adj[node]:
                if neigh != p:
                    d += getMaxDegree(neigh, k-1, node, adj)
            return d
        maxDegree = 0

        for i in adj:
            maxDegree = max(maxDegree, getMaxDegree(i, k-1, -1, adj))

        adj1 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        res = []

        for i in range(len(adj1)):
            # print(i, getMaxDegree(i, k, -1, adj1))
            res.append(getMaxDegree(i, k, -1, adj1) + maxDegree)
        return res





        
