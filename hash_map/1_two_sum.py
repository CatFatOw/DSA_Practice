# My Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for idx in range(len(nums)):
            num = nums[idx]
            complement = target - num

            if complement in mapping:
                return [mapping[complement], idx]
            mapping[num] = idx
        


# LC solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]