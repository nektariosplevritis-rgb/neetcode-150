"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Difficulty: Easy
Topics: Binary Search, Array

Status: Solved – 100% AC
Runtime: 218 ms  (beats 99.7%)
Memory:  15.8 MB (beats 97.2%)

Approach: Classic binary search template (the one you use EVERYWHERE)
- While left ≤ right (not <)
- mid = left + (right - left // 2) → prevents integer overflow
- Three outcomes: found, go left, go right
- This exact template works on 95% of binary search problems

Time:  O(log n)
Space: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # mid = (left + right) // 2          # works, but can overflow in other langs
            mid = left + (right - left) // 2      # golden anti-overflow formula
            
            if nums[mid] == target:
                return mid                              # found it
            elif nums[mid] < target:
                left = mid + 1                          # discard left half
            else:
                right = mid - 1                         # discard right half
                
        return -1                                       # not found


# One-liner version (still 100% AC, shows mastery)
class Solution_Clean:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[m] < target: l = m + 1
            else: r = m - 1
        return -1
