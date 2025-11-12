import heapq, math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Main logic:
        # We continuously pop the root, then we floor it and heappush it root - the floor value/2 back into using for loop
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        for i in range(k):
            max_val = abs(heapq.heappop(piles))
            heapq.heappush(piles, -1 * (max_val - math.floor(max_val/2)))
            
        return -1 * sum(piles)
        