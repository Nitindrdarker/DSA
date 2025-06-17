# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.



from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # memo = {}
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        # def util(i, j):
        #     if i >= row or j >= col or obstacleGrid[i][j] == 1:
        #         return 0
        #     if i == row - 1 and j == col - 1:
        #         return 1
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     bottom = util(i+1, j)
        #     right = util(i, j+1)
        #     memo[(i, j)] = bottom + right
        #     return memo[(i, j)]
        # return util(0, 0)


        memo = [[0 for i in range(col)] for j in range(row)]
        memo[-1][-1] = 1

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if i == row - 1 and j == col - 1:
                    continue
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                    continue
                bottom = memo[i+1][j] if i+1 < row else 0
                right = memo[i][j+1] if j+1 < col else 0
                memo[i][j] = bottom + right
        return memo[0][0]