# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(l):
            visited = set()
            for i in l:
                if i != '.' and i in visited:
                    return False
                if i != '.':
                    visited.add(i)
            return True


        #row
        for i in board:
            if not validate(i):
                return False
        

        #col 
        for j in range(len(board[0])):
            temp = []
            for i in range(len(board)):
                temp.append(board[i][j])
            if not validate(temp):
                return False
        


        # 3 X 3
        for r in (0, 3, 6):
            for c in (0, 3, 6):
                temp2 = []
                for i in range(3):
                    for j in range(3):
                        nr, nc = r + i, c + j
                        temp2.append(board[nr][nc])
                # print(temp2)
                if not validate(temp2):
                    return False
        return True





