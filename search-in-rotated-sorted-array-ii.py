# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.



from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin() -> int:
            left = 0
            right = len(nums) - 1
            start = left
            while(left < right):
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        pivot = findMin()
        if nums[pivot] <= target and nums[len(nums) - 1] >= target:
            start = pivot
            end = len(nums) - 1
        else:
            end = pivot
            start = 0
        while(start <= end):
            mid = (start + end) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                end = mid - 1
                while(end > start and nums[end] == nums[end + 1]):
                    end -= 1
            else:
                start = mid + 1
                while(end > start and nums[start] == nums[start - 1]):
                    start += 1
        return False 