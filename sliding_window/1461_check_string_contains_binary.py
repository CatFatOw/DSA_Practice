# my solution
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_strings = set()
        unique_string = ""
        if k > len(s):
            return False
        for i in range(k):
            unique_string += s[i]
        unique_strings.add(unique_string)
        
        for i in range(k, len(s)):
            unique_string = list(unique_string)
            unique_string.append(s[i])
            unique_string.pop(0)
            unique_strings.add("".join(unique_string))

        return len(unique_strings) == 2 **k 
            

        

# The main issue was the .pop(0) and the return case
# For the pop I thought it would be i-k due to most problems having, it but since we are always removing the last element of the substring
# We can just pop the last value


# Second revision (slightly more optimized)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_strings = set()
        unique_string = ""
        if k > len(s):
            return False
        for i in range(k):
            unique_string += s[i]
        unique_strings.add(unique_string)
        
        for i in range(k, len(s)):
            unique_string = unique_string[1:] + s[i]
            unique_strings.add(unique_string)
            

        return len(unique_strings) == 2 **k 
            

# This time: instead of spliting, poping, joining, etc. I realized that we can essentialy get the substring starting from indx 1
# From the current substring + the next char
# Ie
# cur_substring = "gat" -> "at" + "t" -> "att" 
# Main: "gatto"