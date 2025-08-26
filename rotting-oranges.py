# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        freshCount = 0
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))
        if freshCount == 0:
            return 0
        totalOrange = freshCount + len(q)
        
        while(q):
            i, j, time = q.popleft()
            if grid[i][j] == 1:
                grid[i][j] = 2
                freshCount -= 1
            if freshCount == 0:
                return time
            for r, c in neighbours:
                ni, nj = r + i, c + j
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                    q.append((ni, nj, time+1))
        return -1

            