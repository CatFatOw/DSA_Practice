# My solution
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_mapping = defaultdict(list)
        min_length = float("inf")

        for idx in range(len(cards)):
            card_mapping[cards[idx]].append(idx)
    

        for val in card_mapping.values():
            if len(val) != 1:
                for idx in range(1, len(val)):
                    # Best way to cehck consercutive is from 1 to end
                    distance = val[idx] - val[idx-1] + 1
                    print(distance)
                    if distance < min_length:
                        min_length = distance

        if min_length == float("inf"):
            return -1
        else:
            return min_length




        