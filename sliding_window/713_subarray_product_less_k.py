# My solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        product = 1

        if k <= 1:
            return 0
        
        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

        
        
        
        

# Lc solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
                
            ans += right - left + 1

        return ans