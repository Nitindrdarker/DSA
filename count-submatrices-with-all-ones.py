# Given an m x n binary matrix mat, return the number of submatrices that have all ones.


from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        rowSuff = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            c = 0
            for j in range(col-1, -1, -1):
                if mat[i][j] > 0:
                    c += mat[i][j]
                else:
                    c = 0
                rowSuff[i][j] = c
        ans = 0
        for i in range(row):
            for j in range(col):
                currLen = col + 1
                for k in range(i, row):
                    currLen = min(currLen, rowSuff[k][j])
                    ans += currLen
        return ans


            

        

                