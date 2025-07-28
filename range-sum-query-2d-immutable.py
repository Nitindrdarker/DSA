# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.



from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.prefSum = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                top = 0 if i - 1 < 0 else self.prefSum[i-1][j]
                right = 0 if j - 1 < 0 else self.prefSum[i][j-1]
                self.prefSum[i][j] = top + right + matrix[i][j] - (self.prefSum[i-1][j-1] if i > 0 and j > 0 else 0)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.prefSum[row2][col1-1] if col1 - 1 >= 0 else 0
        b = self.prefSum[row1-1][col2] if row1 - 1 >= 0 else 0
        diag = self.prefSum[row1-1][col1-1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        return self.prefSum[row2][col2] - a - b + diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
