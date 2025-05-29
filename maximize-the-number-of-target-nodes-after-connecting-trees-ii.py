# There exist two undirected trees with n and m nodes, labeled from [0, n - 1] and [0, m - 1], respectively.

# You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

# Node u is target to node v if the number of edges on the path from u to v is even. Note that a node is always target to itself.

# Return an array of n integers answer, where answer[i] is the maximum possible number of nodes that are target to node i of the first tree if you had to connect one node from the first tree to another node in the second tree.

# Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

from collections import defaultdict, deque
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        def adjMap(edges, adj):
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adjMap(edges1, adj1)
        adjMap(edges2, adj2)
        # print(adj2)
        def bfs(node, adj):
            q = deque([(node, 0, -1)])
            even, odd = set(), set()
            while(q):
                node, parity, parent = q.popleft()
                if parity == 0:
                    even.add(node)
                else:
                    odd.add(node)

                for neigh in adj[node]:
                    if neigh != parent:
                        new_parity = 0 if parity == 1 else 1
                        q.append((neigh, new_parity, node))
                
            return [even, odd]
                
        even2, odd2 = bfs(0, adj2)
        even1, odd1 = bfs(0, adj1)
        # print(even2, odd2, adj2)
        max2 = max(len(even2), len(odd2))
        res = [0] * (len(edges1) + 1)

        for i in range(len(adj1)):
            if i in even1:
                res[i] = len(even1) + max2
            else:
                res[i] = len(odd1) + max2
        return res
            
