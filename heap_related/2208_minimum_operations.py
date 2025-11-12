
# My solution

import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        operations = 0
        curr_sum = initial_sum = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while curr_sum > initial_sum / 2:

            # Get the root value
            max_num = (-1 * heapq.heappop(nums)) / 2
            heapq.heappush(nums, -max_num)
            curr_sum = curr_sum - max_num
            operations += 1
        return operations
    

# Leetcode Solution
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        
        return ans

        

        

        

        