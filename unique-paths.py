# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m
        col = n
        memo = [[0 for i in range(col)] for j in range(row)]
        memo[-1][-1] = 1
        # def util(i, j):
        #     if i >= row or j >= col:
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

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if i == row - 1 and j == col - 1:
                    continue
                # print(i, j)
                bottom = memo[i+1][j] if i+1 < row else 0
                right = memo[i][j+1] if j+1 < col else 0
                memo[i][j] = bottom + right
        return memo[0][0]
                



