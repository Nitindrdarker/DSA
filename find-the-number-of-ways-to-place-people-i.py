# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

# Count the number of pairs of points (A, B), where

# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.

 


from ast import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def pointExists(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            for k in range(len(points)):
                if i == k or j == k:
                    continue
                xn, yn = points[k]
                
                if xn >= x1 and xn<= x2 and yn >= y2 and yn <= y1:
                    # print(x1, y1, x2, y2, xn, yn)
                    return True
            return False



        count = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    
                    x2, y2 = points[j]
                    if not pointExists(i, j):
                        count += 1
        return count


                