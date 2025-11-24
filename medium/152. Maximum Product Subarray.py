# 152. Maximum Product Subarray
# Difficulty: Medium
# Date Solved: 23 Nov 2025
# Time: O(n) | Space: O(1)

"""
Problem Summary
Given an integer array nums, find the contiguous subarray with the largest product and return the product.

Key Observations
- A negative number can turn a current minimum into a new maximum when multiplied by another negative.
- Zeros break the continuity and reset the running product.
- We must maintain both the maximum and minimum running products at each position.

Solution Approach
Dynamic programming tracking two values:
- cur_max: largest product ending at current index
- cur_min: smallest product ending at current index
When a negative number appears, swap cur_max and cur_min before updating.

This ensures we never lose the potential for a larger product after an odd number of negatives.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            res = max(res, cur_max)
        
        return res
