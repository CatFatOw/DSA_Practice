# Two pointer my solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        result = ""

        for word in s_list:
            #cat
            #[c, a, t]
            word = list(word)
            left = 0
            right = len(word) - 1
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            result += "".join(word) + " "
        return result.strip()
        