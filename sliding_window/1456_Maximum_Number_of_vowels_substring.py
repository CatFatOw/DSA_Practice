# My solution
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o","u"])
        # Fixed sldiing window
        curr = 0
        
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr 
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i-k] in vowels:
                curr -= 1
            ans = max(curr, ans)
            
                
        return ans

        

# The only difficulty encountered was using ans as both a running and max sum
# Lesson learned: use ans only for 1 task
