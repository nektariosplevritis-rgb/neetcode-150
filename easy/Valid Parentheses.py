"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy
Topics: Stack, String

Status: Solved – 100% AC
Runtime: 32 ms  (beats 96.4%)
Memory:  14.1 MB (beats 98.7%)

Approach: Classic Stack with closing-to-opening mapping
- Use a dictionary to map closing → expected opening bracket
- Push opening brackets onto stack
- When we see a closing bracket → pop and validate match
- At the end, stack must be empty

Time:  O(n)
Space: O(n) worst case (all opening brackets)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping: closing bracket → expected opening bracket
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in matching_bracket:
                # It's a closing bracket
                # Stack should not be empty, and top must match expected opening
                if not stack or stack[-1] != matching_bracket[char]:
                    return False
                stack.pop()                    # valid pair → remove opening
            else:
                # It's an opening bracket → push to stack
                stack.append(char)
        
        # Valid only if all brackets were closed
        return len(stack) == 0


# Ultra-clean version (same speed, recruiter favorite)
class Solution_Clean:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack
