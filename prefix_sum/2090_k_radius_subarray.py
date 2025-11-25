# My solution
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Main logic
        # Build a prefix sum
        # Check if i + k or i-k within the bounds. if no: -1
        # If satifsfies do prefix[i+k] - prefix[i-k] + nums[i-k] // 2k+1
        prefix = [nums[0]]
        result = []
        print(len(nums))
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])

        for i in range(len(nums)):
            if i + k >= len(nums) or i - k < 0:
                result.append(-1)
            else:
                print(i+k, i-k)
                values = prefix[i+k] - prefix[i-k] + nums[i-k]
                print(values)
                result.append(values // (2*k+1))
        return result
                


        