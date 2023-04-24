"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

""" Example
        nums = [1,2,3,4,5,6]
        target = 7
        output = [2,3]
        """

# Solution : https://www.youtube.com/watch?v=KLlXCFG5TnA        
# Brute Force
class Solution:

    def twoSum(self, nums, target):
     
     for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                output_indices = []
                output_indices.append(i)
                output_indices.append(j)
                return output_indices
                exit()
        
     

nums = [9,3,4,5,7,2,8,6] # or any list 
target = 7 # or any target
sol = Solution()
print(sol.twoSum(nums,target))



    
