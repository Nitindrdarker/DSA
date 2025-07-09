# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.


from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        divisions = defaultdict(list)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            divisions[a].append([b, values[i]])
            divisions[b].append([a, 1 / values[i]])
        cache = {}
        
        visited = set()
        def util(start, end):
            if start not in divisions:
                return 0
            if start in visited:
                return 0
            if start == end:
                return 1
            if (start, end) in cache:
                return cache[(start, end)]
            visited.add(start)
            prod = -float("inf")
            for node, val in divisions[start]:
            
                l = util(node, end)
                if l == 0:
                    prod = 0
                else:
                    prod = l * val
                    visited.remove(start)
                    cache[(start, end)] = prod
                    return prod
            visited.remove(start)
            return 0

        res = []
        for a, b in queries:
            v = util(a, b)

            res.append(v if v != 0 else -1)
        return res

            

                

        