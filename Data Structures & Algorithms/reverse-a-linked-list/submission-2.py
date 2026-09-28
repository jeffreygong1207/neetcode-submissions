# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rest = None
        start = head

        while start:
            remaining = start.next
            start.next = rest
            rest = start
            start = remaining
        
        return rest


        