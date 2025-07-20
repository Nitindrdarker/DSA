# You are given a positive integer k. You are also given:

# a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
# a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
# The two arrays contain integers from 1 to k.

# You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

# The matrix should also satisfy the following conditions:

# The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
# The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
# Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.



from collections import defaultdict
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(node, adj, visited, path, order):
            if node in path:
                #cycle
                return False
            if node in visited:
                #already visited
                return True
            path.add(node)
            visited.add(node)
            for neigh in adj[node]:
                if not dfs(neigh, adj, visited, path, order):
                    return False
            path.remove(node)
            order.append(node)
            return True

        def topo(edges):
            adj = defaultdict(list)
            for i, j in edges:
                adj[i].append(j)
            visited = set()
            path = set()
            order = []
            for node in range(1, k + 1):
                if not dfs(node, adj, visited, path, order):
                    return []
            return order[::-1]

        rowOrder = topo(rowConditions)
        colOrder = topo(colConditions)
        if not rowOrder or not colOrder:
            return []
        # convert to hashmap for easy index access(total row and col of res is k)
        rowMap = {i:idx for idx, i in enumerate(rowOrder)}
        colMap = {i:idx for idx, i in enumerate(colOrder)}

        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            r, c = rowMap[i], colMap[i]
            res[r][c] = i
        return res
    
            

        

        