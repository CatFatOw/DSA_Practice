# My Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # The main logic will be to initialize two points
        # While the second pointer isn't equal to the first, move the second pointer. If it is equal move. Return true is the first pointer reaches the end else false 

        ptr1 = ptr2 = 0
        while ptr2 < len(t) and ptr1 < len(s):
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        return True if ptr1 == len(s) else False
            


# Leetcode
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)