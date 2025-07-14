# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell



import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        h = []
        heapq.heappush(h, (0, 0, 0))#diff, i, j
        neigh = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        res = 0
        while(h):
            diff, i, j = heapq.heappop(h)

            if (i, j) in visited:
                continue
            if i == row - 1 and j == col - 1:
                return diff
            visited.add((i, j))
            for r, c in neigh:
                nr, nc = i + r, j + c
                if nr >= row or nc >= col or nr < 0 or nc < 0 or (nr, nc) in visited:
                    continue
                heapq.heappush(h, (max(abs(heights[i][j] - heights[nr][nc]), diff), nr, nc))
      

                    



            