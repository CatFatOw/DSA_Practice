# My Solution
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        prefix = [self.nums[0]]
        for i in range(1, len(self.nums)):
            prefix.append(self.nums[i] + prefix[i-1])
        return prefix[right] - prefix[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)