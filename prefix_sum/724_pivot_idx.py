# My Solution (some help need)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])
        print(prefix)
        
        right = len(nums) - 1
        for left in range(len(prefix)):
            left_side = prefix[left] - nums[left]
            right_side = prefix[right] - prefix[left]
            if left_side == right_side:
                return left 
        return -1
        