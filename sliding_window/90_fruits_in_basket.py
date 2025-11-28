# My solution
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = float("-inf")
        left = 0
        
        picked = defaultdict(int)

        for right in range(len(fruits)):
            picked[fruits[right]] += 1
            
            while len(picked) > 2:
                picked[fruits[left]] -= 1
                if picked[fruits[left]] == 0:
                    picked.pop(fruits[left])
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
           
        return max_fruits



        

# Ok so the main structure was easy but a couple of things that I needed a few hints by gpt
# 1. Instead of using hash set, use a hash map to keep count of the frequecy
# 2. Initially, I only incrememnted the map only if it was a new fruit; however, it has to be all fruits this is due to the stopping condition
# While the len of the map > 2
