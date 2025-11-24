# 15. 3Sum
# Difficulty: Medium
# Date Solved: 23 Nov 2025
# Time: O(n²) | Space: O(1) excluding output

"""
Problem Summary
Given an integer array nums, return all unique triplets that sum to zero.
Solution must not contain duplicate triplets.

Key Observations
- Sorting enables two-pointer technique and easy duplicate skipping.
- Fix the first number (i), then solve 2Sum on the remaining right portion with target = -nums[i].
- Skip duplicates at all three positions (i, left, right) to guarantee uniqueness.

Solution Approach
1. Sort the array
2. For each i (0 to n-3):
   - Skip if duplicate of previous i
   - Use two pointers on [i+1 : n-1] to find pairs summing to -nums[i]
   - When a valid triplet is found, skip all duplicate left/right values
3. Collect and return all unique triplets
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result
