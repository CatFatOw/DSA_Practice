# My Solution
from collections import defaultdict
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapping = defaultdict(int)

        for char in s:
            if mapping[char] > 0:
                return char 
            else:
                mapping[char] += 1
        return None
        

# LC Solution
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "