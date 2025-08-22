# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

# Return the minimum possible area of the rectangle.



from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        leftMostCoord = col + 1
        topMostCoord = row + 1
        rightMostCoord = -1
        bottomMostCoord = -1
        for y in range(row):
            for x in range(col):
                val = grid[y][x]
                if val == 1:
                    leftMostCoord = min(leftMostCoord, x)
                    topMostCoord = min(topMostCoord, y)
                    rightMostCoord = max(rightMostCoord, x)
                    bottomMostCoord = max(bottomMostCoord, y)
        length = rightMostCoord - leftMostCoord + 1
        height = bottomMostCoord - topMostCoord + 1
        return length * height