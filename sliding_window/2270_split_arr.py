# My solution
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        n = len(nums)
        splits = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])
        
        for i in range(len(nums)):
            left = prefix[i]
            right = prefix[n-1] - prefix[i]

            if left >= right and i < n - 1:
                splits += 1
        return splits


# LC solution
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans