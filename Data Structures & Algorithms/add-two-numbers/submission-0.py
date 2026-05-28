# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            s = val1+val2+carry
            val = s%10
            carry = s//10
            tmp = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val+carry
            val = s%10
            carry = s//10
            tmp = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            s = l2.val+carry
            val = s%10
            carry = s//10
            tmp = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        
        while carry:
            s = carry
            val = s%10
            carry = s//10
            tmp = curr.next
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
















