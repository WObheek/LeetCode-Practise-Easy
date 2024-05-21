## Problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        #dictionary to store the each num & their index
        index_num = {}
      
        # enumerating List returns index & value
        for index,num in enumerate(nums):
            
            # complement : that would sum up to the target with the current number
            complement = target - num
            
            # Check if the complement is in dictionary
            if complement in index_num:
                return [index_num[complement], index]
            
            # If not found, add the current number and its index to the dictionary
            index_num[num]=index

