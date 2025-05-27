# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        pending = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        aval = []
        heapq.heapify(pending)
        
        t = 0
        while(aval or pending):
            while(pending and pending[0][0] <= t):
                _, p, i = heapq.heappop(pending)
                heapq.heappush(aval, (p, i))

            if not aval:
                t = pending[0][0]
            
            if (aval):
                p, i = heapq.heappop(aval)
                res.append(i)
                t += p
        return res