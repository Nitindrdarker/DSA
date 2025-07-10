# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



from collections import *
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if (n < 2):
            return [i for i in range(n)]
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)


    


        q = deque()
        for i in adj:
            if len(adj[i]) == 1:
                q.append(i)


        while(len(adj) > 2):
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                for neigh in adj[node]:
                    adj[neigh].remove(node)
                    if len(adj[neigh]) == 1:
                        q.append(neigh)
                del adj[node]

        
        return list(adj.keys())


            
            
