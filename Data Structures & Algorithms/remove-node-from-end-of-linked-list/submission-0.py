# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #have a fast and slow
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        #advance fast by n step
        for i in range(n):
            fast = fast.next

        #now move everything;
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        #at this point slow.next is the node
        slow.next = slow.next.next

        return dummy.next

        