# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).



from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        memo = {}
        def util(i, j):
            if i >= row or i < 0 or j >= col or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            down = left = right = up = 0
            curr = matrix[i][j]
            if i + 1 < row and matrix[i+1][j] > curr:
                down = util(i+1, j)
            if i - 1 >= 0 and matrix[i-1][j] > curr:
                up = util(i-1, j)
            if j + 1 < col and matrix[i][j+1] > curr:
                right = util(i, j+1)
            if j - 1 >= 0 and matrix[i][j-1] > curr:
                left = util(i, j-1)
            memo[(i, j)] = max(left, right, up, down) + 1
            return memo[(i, j)]
        res = 0
        for i in range(row):
            for j in range(col):
                res = max(res, util(i, j))
        return res


