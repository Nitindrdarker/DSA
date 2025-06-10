# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.pointCount = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # find the side length of the square
        #we can find the length between two points either with same y axis point or same x axis point
        x, y = point
        d = 0
        total = 0
        for p, c in list(self.pointCount.items()):#list because
            x1, y1 = p
            if x != x1 and y1 == y:#checking for points on same y axis
                d = x1 - x
                total += c * self.pointCount.get((x, y + d), 0) * self.pointCount.get((x1, y1 + d), 0)
                total += c * self.pointCount.get((x, y - d), 0) * self.pointCount.get((x1, y1 - d), 0)
        return total

            

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)