# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = []
        rightmax = [0] * len(height)
        res = 0

        for i in range(len(height)):
            if not leftmax:
                leftmax.append(height[i])
            else:
                leftmax.append(max(leftmax[i-1], height[i]))
            

        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                rightmax[i] = height[i]
            else:
                rightmax[i] = max(rightmax[i+1], height[i])
        # print(leftmax, rightmax)
        for i in range(len(height)):
            h = min(leftmax[i], rightmax[i])
            res += h - height[i]
        return res

            

        