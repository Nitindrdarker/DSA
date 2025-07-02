# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

# The lock initially starts at '0000', a string representing the state of the 4 wheels.

# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.


from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        invalids = set(deadends)
        start = "0000"
        q = deque()
        q.append((start, 0))
        visited = set()
        if start in invalids:
            return -1
        while(q):
            node, t = q.popleft()
            if node == target:
                return t 
            for i in range(4):
                val = (int(node[i]))
                newNode = node[:i] + str((val + 1) % 10) + node[i+1:]
                if newNode not in invalids and newNode not in visited:
                    q.append((newNode, t + 1))
                    visited.add(newNode)

                newNode = node[:i] + str((val - 1) if val > 0 else "9") + node[i+1:]
                if newNode not in invalids and newNode not in visited:
                    q.append((newNode, t + 1))
                    visited.add(newNode)
        return -1
            
                


            