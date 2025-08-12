# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        l = mountainArr.length()
        left = 1
        right = l - 1
        mountain = 0
        while(left <= right):
            mid = (left + right) // 2
            ele = mountainArr.get(mid)
            after = mountainArr.get(mid+1)
            before = mountainArr.get(mid-1)
            if  ele > before and ele > after:
                mountain = mid
                break
            elif ele < after:
                left = mid + 1
            elif ele < before:
                right = mid - 1
        def search(l, r, reverse = False):
            while(l <= r):
                mid = (l + r) // 2
                ele = mountainArr.get(mid)
                if ele == target:
                    return mid
                elif ele < target:
                    if reverse:
                        r = mid - 1
                    else: 
                        l = mid + 1
                else:
                    if reverse:
                        l = mid + 1
                    else:
                        r = mid - 1
            return -1
        a = search(0, mountain)
        if a != -1:
            return a
        else:
            return search(mountain+1, l-1, True)

        
            

 