# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskCollection = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        heapq.heapify(taskCollection)
        h = [] # min heap
        res = []
        t = 0
        while(h or taskCollection):
            if h:
                processTime, index = heapq.heappop(h)
                t += processTime
                res.append(index)
            else:
                t = taskCollection[0][0]
            while(taskCollection and t >= taskCollection[0][0]):
                e, p, i = heapq.heappop(taskCollection)
                heapq.heappush(h, (p, i))
            
        return res


            