# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


from ast import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        def findRow(count, r, c):
            e = []
            o = []
            while(c < col and r >= 0):
                if count % 2 == 0:
                    e.append(mat[r][c])
                    r -= 1
                    c += 1
                else:
                    o.append(mat[r][c])
                    r -= 1
                    c += 1
            
            if e:
                return e
            if o:
                return o[::-1]
        #its always starting from left and bottom sides
        #for first column
        count = 0
        res = []
        for i in range(row):
            c = 0
            r = i
            res.extend(findRow(count, r, c))
            count += 1
        # now for bottom row
        for j in range(1, col):
            r = row - 1
            c = j
            res.extend(findRow(count, r, c))
            count += 1

        return res
        
            

