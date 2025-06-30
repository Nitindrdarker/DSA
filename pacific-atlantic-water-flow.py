# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlanta = set()
        row = len(heights)
        col = len(heights[0])

        visited = set()
        def util(i, j, s):
            if i >= row or j >= col or i < 0 or j < 0 or (i, j) in s:
                return
            s.add((i, j))
            if i + 1 < row and heights[i][j] <= heights[i+1][j]:
                util(i+1, j, s)
            if i - 1 >= 0 and heights[i][j] <= heights[i-1][j]:
                util(i-1, j, s)
            if j + 1 < col and heights[i][j] <= heights[i][j+1]:
                util(i, j+1, s)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j-1]:
                util(i, j-1, s)




        for i in range(row):
            util(i, 0, pacific)
            util(i, col-1, atlanta)

        for i in range(col):
            util(0, i, pacific)
            util(row-1, i, atlanta)

        #match the same value
        res = []
        for i in pacific:
            if i in atlanta:
                res.append(i)
        return res
    


            