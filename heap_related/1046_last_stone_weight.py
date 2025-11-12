# My Solution

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * val for val in stones]
        heapq.heapify(stones)
        print(stones)
        # We wanna max heap where root is the max of the values
        # Game stops when stones <= 1
        while len(stones) > 1:
            # We pop twice first is y then x
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
        

            # Conditions 
            if x == y:
                continue 
            else:
                # X destroyed, but y -= x
                y = y - x
                heapq.heappush(stones, -1 * y)
        return -1 * stones[0] if stones else 0


# Leetcode Solution
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # turns an array into a heap in linear time
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0


        
