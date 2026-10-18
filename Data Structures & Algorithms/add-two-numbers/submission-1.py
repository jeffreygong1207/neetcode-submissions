# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        carry = False
        while l1 or l2:
            first = 0
            if l1:
                first = l1.val
                l1 = l1.next
            second = 0
            if l2: 
                second = l2.val
                l2 = l2.next
            total = first + second + 1 if carry else first + second
            if total >= 10:
                total = total % 10
                carry = True
            else:
                carry = False
            answer.append(total)
        if carry:
            answer.append(1)
        start = ListNode()
        dummy = start
        for number in answer:
            node = ListNode(number)
            start.next = node
            start = start.next

        return dummy.next