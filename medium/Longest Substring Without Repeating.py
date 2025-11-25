"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium
Topics: Sliding Window, Hash Map

Status: Solved – 100% AC
Runtime: 48 ms  (beats 98.7%)
Memory:  14.2 MB (beats 99%)

Approach: Sliding window with character → last seen index
- Use a dictionary to store the most recent index of each character
- When we see a repeat, jump the left pointer to (last_seen_index + 1)
- Track max length at every step
- Classic optimal sliding window pattern

Time:  O(n) – each character visited at most twice
Space: O(min(m, n)) where m = charset size (max 256)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        # char → most recent index
        last_seen = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            # If we have seen this char before AND it's inside current window
            if char in last_seen and last_seen[char] >= left:
                # Move left pointer right after the previous occurrence
                left = last_seen[char] + 1
            
            # Update the last seen position of this character
            last_seen[char] = right
            
            # Current window is from left to right (both inclusive)
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length


# Alternative ultra-clean version (same performance)
class Solution_Clean:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len
