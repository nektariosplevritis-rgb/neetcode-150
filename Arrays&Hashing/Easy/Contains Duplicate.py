# Contains Duplicate
# Simple hashset check. O(n) time.

class Solution:
    def containsDuplicate(self, numbers: list[int]) -> bool:
        seen = set()
        for number in numbers:
            if number in seen:
                return True
            seen.add(number)
        return False
