# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)
        completed = set()
        visited = set()
        def util(node):

            if node in completed:
                return True
            if node in visited:
                return False
            if len(adj[node]) == 0:
                return True
            visited.add(node)
            for neigh in adj[node]:
                if util(neigh) == False:
                    return False
            visited.remove(node)
            completed.add(node)
            return True
        for i in range(numCourses):
            if util(i) == False:
                return False

        return True