# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def util(i, j):
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i,j))
            left = util(i, j - 1)
            right = util(i, j + 1)
            top = util(i - 1, j)
            bottom = util(i + 1, j)

            return left + right + top + bottom

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return util(i, j)