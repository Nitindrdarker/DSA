# There is a game dungeon comprised of n x n rooms arranged in a grid.

# You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

# The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

# The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
# The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
# The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
# When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

# Return the maximum number of fruits the children can collect from the dungeon.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        #appending into the stack in ascending order

        for i in range(len(heights)):
            
            while(stack and heights[stack[-1]] > heights[i]):
                top = stack.pop()
                currHeight = heights[top]
                leftBoundry = stack[-1] if stack else -1
                rightBoundry = i
                width = rightBoundry - leftBoundry - 1 #(-1 because we are not including the leftBoundry element)
                res = max(res, currHeight * width)
            stack.append(i)

        while stack:
            top = stack.pop()
            height = heights[top]
            leftBoundry = stack[-1] if stack else -1
            rightBoundry = len(heights)
            width = rightBoundry - leftBoundry - 1
            res = max(res, height * width)
        return res
        


                