# My solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the left pointer will always be smallesr than the right pointer 
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1, right+1]
            elif result > target:
                right -= 1
            else:
                left += 1
                
            


        

# LC 
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False