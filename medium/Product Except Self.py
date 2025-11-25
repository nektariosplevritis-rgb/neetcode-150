"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Difficulty: Medium
Topics: Array, Prefix/Suffix Products, O(1) Space

Status: Solved – 100% AC
Runtime: 124 ms  (beats 99.5%)
Memory:  23.1 MB (beats 97%)

Approach: Two-pass O(1) space (legendary technique)
1. First pass: store all prefix products in output array
2. Second pass: multiply by running suffix product from right to left
→ No division, handles zeros perfectly, O(1) extra space

One of the most beautiful and most-asked problems in real interviews.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Left → Right: prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Right → Left: multiply by suffix
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
