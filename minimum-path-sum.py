# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        memo = [[float('inf') for i in range(col)] for j in range(row)]

        memo[-1][-1] = grid[-1][-1]
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i == row - 1 and j == col - 1:
                    continue
                bottom = memo[i+1][j] if i+1 < row else float("inf")
                right = memo[i][j+1] if j+1 < col else float("inf")
                memo[i][j] = min(bottom, right) + grid[i][j] 
        return memo[0][0]


        # memo = {}
        # def util(i, j):
        #     if i >= row or j >= col:
        #         return float("inf")
        #     if i == row - 1 and j == col - 1:
        #         return grid[i][j]
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     bottom = util(i+1, j)
        #     right = util(i, j+1)
        #     memo[(i, j)] = min(bottom , right) + grid[i][j]
        #     return memo[(i, j)]
        # return util(0, 0)