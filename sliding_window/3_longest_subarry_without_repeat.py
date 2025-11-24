# My Solution
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occured = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            occured[s[right]] += 1

            while occured[s[right]] > 1:
                occured[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
        