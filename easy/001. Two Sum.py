# 1. Two Sum
# Difficulty: Easy
# Date Solved: 23 Nov 2025
# Time: O(n) | Space: O(n)

"""
Problem Summary
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input has exactly one solution, 
and you may not use the same element twice.

Key Observations
- Brute force would require O(n²) time by checking every pair.
- We can achieve O(n) time by using a hash map to store complements (target - current number).
- As we iterate through the array, we check if the current number's complement has been seen before.

Solution Approach
Use a single-pass hash table:
- For each element nums[i], compute complement = target - nums[i]
- If complement exists in the map, we have found the pair
- Otherwise, store nums[i] with its index in the map
This guarantees linear time complexity and constant additional passes.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value → index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        # LeetCode guarantees exactly one solution, so this line is never reached
        return []
