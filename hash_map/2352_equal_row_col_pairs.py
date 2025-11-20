# My Solution
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        same = 0
        row_mapping = defaultdict(int)
        col_mapping = defaultdict(int)

        # populate the row/col since n xn with keys as the list and values as the index
        for row_idx in range(len(grid)):
            row_mapping[tuple(grid[row_idx])] += 1
            col_mapping[tuple([row[row_idx] for row in grid])] +=1 

       
        # Check if a val in col in row?

        for col in col_mapping:
            if col in row_mapping:
                same += col_mapping[col] * row_mapping[col]

        return same

# Leetcode solution (basically exactly the same)
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        
        return ans
       


# Main takeaways:

""" 
1. The total number of row/col matching pairs is R * C

2. To get the columns of a list we can do
row_idx = c
col = [row[row_idx] for row in grid]
"""