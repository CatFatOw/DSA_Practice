# My solution
from collections import defaultdict
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        mapping = defaultdict(int)
        unique_nums = set()
        result = []
        numset = set(nums)
        for num in nums:
            if num in unique_nums:
                unique_nums.remove(num)

            if mapping[num] == 0:
                unique_nums.add(num)
            
            mapping[num] += 1
          
        for num in unique_nums:
            val1 = num+1
            val2 = num-1
            if val1 not in numset and val2 not in numset:
                result.append(num)
        return list(result)


        