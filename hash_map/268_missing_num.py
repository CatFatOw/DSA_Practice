class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        valid = [num for num in range(n+1)]

        for num in valid:
            if num not in nums:
                return num
        