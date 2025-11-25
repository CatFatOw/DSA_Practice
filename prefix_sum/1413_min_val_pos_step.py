# My solution
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = float("inf")
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])
        

        for num in prefix:
            if num < min_value:
                min_value = num
        # Negative case
        if min_value < 0:
            return -1 * min_value + 1
        else:
            return 1








        