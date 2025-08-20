# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

from ast import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0 and matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + matrix[i][j]
                res += matrix[i][j]
        return res
                
        


        