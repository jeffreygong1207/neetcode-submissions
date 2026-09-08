# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        once = head
        twice = head
        while twice and twice.next:
            once = once.next
            twice = twice.next.next
            if once == twice:
                return True
        

        return False