# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.



from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nonConnectingRegion = set()
        row = len(board)
        col = len(board[0])

        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0 or board[i][j] == 'X' or (i, j) in nonConnectingRegion:
                return 
            nonConnectingRegion.add((i, j))
            util(i + 1, j)
            util(i - 1, j)
            util(i, j + 1)
            util(i, j - 1)

        for i in range(row):
            util(i, 0)
            util(i, col - 1)
        for j in range(col):
            util(0, j)
            util(row - 1, j)
        
        
        
        for i in range(row):
            for j in range(col):
                if (i, j) in nonConnectingRegion:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'