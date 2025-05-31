# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.



import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        #flatter the board
        flat_board = []
        for i in range(n-1, -1, -1):
            temp = []
            for j in range(n):
                if board[i][j] == -1:
                    temp.append(board[i][j])
                else:
                    temp.append(board[i][j] - 1)
            if ((n - 1) - i) % 2:
                flat_board.extend(temp[::-1])
            else:
                flat_board.extend(temp)

        visited = set()
        
        q = collections.deque()
        q.append((0, 0))
        while(q):
            val, count = q.popleft()
           
            visited.add(val)
            if val+1 == n * n:
                return count
            for next in range(1, 7):
                newVal = val + next
                if newVal >= n * n:
                    break
                if flat_board[newVal] != -1 and flat_board[newVal] not in visited:
                    visited.add(flat_board[newVal])
                    q.append((flat_board[newVal], count+1))
                elif flat_board[newVal] == -1 and newVal not in visited:
                    visited.add(newVal)
                    q.append((newVal, count+1))
        return -1



        
    
        
                




        

        