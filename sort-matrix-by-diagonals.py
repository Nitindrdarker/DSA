# You are given an n x n square matrix of integers grid. Return the matrix such that:

# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.



from ast import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #top - right is in increasing order
        # bottom - left including mid in decreasing order

        # top right corner is already sorted 
        # bottom left corner is ready sorted
        row = col = len(grid)
        if row == 1:
            return grid
        def util(i, j, reverse=False):
            r = i
            c = j
            vals = []
            while(r < row and c < col):
                vals.append(grid[r][c])
                r += 1
                c += 1
            vals.sort(reverse=reverse)
            r = i
            c = j
            while(r < row and c < col):
                grid[r][c] = vals.pop()
                r += 1
                c += 1
        for i in range(row):
            util(i, 0)
            
        for j in range(1, col):
            util(0, j, reverse=True)
        return grid



            




