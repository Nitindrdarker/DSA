# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.




from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        adj = defaultdict(list)
        completed = set()
        for i, j in prerequisites:
            adj[i].append(j)
        def util(node):
            if node in completed:
                return True
            if node in visited:
                # print(visited)
                return False

            if len(adj[node]) == 0:
                res.append(node)
                completed.add(node)
                return True
            visited.add(node)
            for neigh in adj[node]:
                if util(neigh) == False:
                    return False
            # print(node)
            res.append(node)
            completed.add(node)
            return True

        for i in range(numCourses):
            
            if not util(i):
                return []
        return res
        