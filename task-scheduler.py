# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.


from collections import Counter
import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = Counter(tasks)
        h = []
        for i in m:
            heapq.heappush(h, (-m[i], i))
        q = collections.deque()
        t = 0
        while(h or q):
            t += 1
            
            if h:
                count, ele = heapq.heappop(h)
                count += 1
                if count < 0:
                    q.append((t + n, ele, count))
            else:
                t = q[0][0]
            while q and q[0][0] <= t:
                _, e, c = q.popleft()
                heapq.heappush(h, (c, e))
        return t