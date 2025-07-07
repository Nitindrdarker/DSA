from typing import List


# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1 for i in range(len(edges) + 1)]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return True
            elif size[pa] >= size[pb]:
                parent[pb] = pa
                size[pa] += size[pb]
            else:
                parent[pa] = pb
                size[pb] += size[pa]
            return False
        def find(node):
            while(node != parent[node]):
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        res = [-1, -1]
        for a,b in edges:
            isSame = union(a, b)
            if isSame:
                res = [a, b]
        return res
