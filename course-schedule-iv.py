# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.




# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         memo = {}

#         adj = defaultdict(set)
#         for a, b in prerequisites:
#             adj[b].add(a)

#         def util(node, end):
#             if end in adj[node]:
#                 return True
#             if len(adj[node]) == 0:
#                 return False
#             if (node, end) in memo:
#                 return memo[(node, end)]
#             for neigh in adj[node]:
#                 if util(neigh, end):
#                     memo[(neigh, end)] = True
#                     return True
#             memo[(node, end)] = False
#             return False
#         res = []

#         for u, v in queries:
#             res.append(util(v, u))
#         return res



from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        childs = defaultdict(set)

        adj = defaultdict(set)
        for a, b in prerequisites:
            adj[b].add(a)
        def util(node):
            if len(adj[node]) == 0:
                return set()
            if node in childs:
                return childs[node]
            for neigh in adj[node]:
                childs[node].add(neigh)
                subChild = util(neigh)
                for ele in subChild:
                    childs[node].add(ele)
            return childs[node]
        
        for i in range(numCourses):
            util(i)
        res = []
        for u, v in queries:
            res.append(u in childs[v])
        return res





                

        