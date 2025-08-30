# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.



from ast import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i]:
                if nums[i] > nums[i+1]:
                    # candidate p found
                    # print(nums[i])
                    p = i
                    for j in range(i+1, len(nums)-1):
                        if nums[j-1] > nums[j]:
                            if nums[j] < nums[j+1]:
                                # found q
                                print(nums[j])
                                for k in range(j+1, len(nums)-1):
                                    if nums[k] >= nums[k+1]:
                                        return False
                                return True
                        else:
                            return False
            else:
                return False

            
                            
            
        return False
                    
                
                
            
            
                
                