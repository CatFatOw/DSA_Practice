# My Solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m -1 
        j = n -1
        end_len = m + n - 1

        while i >= 0 and j >= 0:
            # Case 1 nums2 value is greater 
            if nums2[j] > nums1[i]:
                nums1[end_len] = nums2[j]
                j -= 1
            # Case 2 nums1 value is greater 
            else:
                nums1[end_len] = nums1[i]
                i -= 1
            end_len -= 1

       
        while j >=0:
            nums1[end_len] = nums2[j]
            j -= 1
            end_len -= 1
        return nums1

        
        
# Leetcode
def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans