# Naive Initial Solution
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)

        # Populate the defaultdict
        for idx in range(len(matches)):
            winner = matches[idx][0]
            loser = matches[idx][1]

            winners[winner] += 1
            losers[loser] += 1
        
        # Check valid winner
        for key in winners.keys():
            if key in losers:
                # Remove by setting value = 0
                winners[key] = 0
        # Check valid losers
        for key, value in losers.items():
            if value > 1 or value < 1:
                losers[key] = 0
        # Populate the correct lists       
        valid_winners = [key for (key,value) in winners.items() if value != 0]
        valid_losers = [key for (key,value) in losers.items() if value != 0]
        return [sorted(valid_winners), sorted(valid_losers)]
        