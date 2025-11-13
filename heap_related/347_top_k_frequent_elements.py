# My solution
from collections import defaultdict
import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        # Establishes the frequncy counter 
        for num in nums:
            mapping[num] += 1

        heap = []
        for key, val in mapping.items():
            h.heappush(heap, (val, key))
            if len(heap) > k:
                h.heappop(heap)
        return [val[-1] for val in heap]
        

        


# Leetcode solution
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]