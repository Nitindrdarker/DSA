# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


from ast import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [[-(((a + 1)/(b + 1)) - (a/b)), a, b] for a, b in classes]
        heapq.heapify(heap)
        for i in range(extraStudents):
            _, a ,b = heapq.heappop(heap)
            a += 1
            b += 1
            newRatio = (a + 1) / (b + 1)
            heapq.heappush(heap, [-(newRatio - (a/b)), a, b])
        # print(heap)
        total = 0
        count = len(classes)
        while heap:
            _, a ,b = heapq.heappop(heap)
            # print(a, b)
            total += (a / b)
        
        return total / count


            
    

