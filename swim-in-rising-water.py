# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).



import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)] #time, row, col
        row = len(grid)
        col = len(grid[0])
        visited = set()
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while(h):
            t, i, j = heapq.heappop(h)
            if i == row - 1 and j == col - 1:
                return t
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for r, c in neighbors:
                nr, nc = i + r, j + c
                if nr >= row or nc >= col or nr < 0 or nc < 0 or (nr, nc) in visited:
                    continue
                heapq.heappush(h, (max(t, grid[nr][nc]), nr, nc))
