# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.



from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]
        empties = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[i // 3][j // 3].add(board[i][j])

        
        def util(idx):
            if len(empties) == idx:
                return True
            i, j = empties[idx]
            bi, bj = i // 3, j // 3
            if board[i][j] == '.':
                for val in range(1, 10):
                    ele = str(val)
                    if ele not in box[bi][bj] and ele not in row[i] and ele not in col[j]:
                        board[i][j] = ele
                        box[bi][bj].add(ele)
                        row[i].add(ele)
                        col[j].add(ele)
                        v = util(idx + 1)
                        if v:
                            return True
                        else:
                            board[i][j] = '.'
                            box[bi][bj].remove(ele)
                            row[i].remove(ele)
                            col[j].remove(ele)
                
                return False
            
        util(0)
    
            
                        
            
                
        