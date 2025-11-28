# My Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow
    
# Basically no need to worry about even or odd length as the slow ptr moves 1 step and fast moves 2 steps so it is always exactly
# 1/2 of the way