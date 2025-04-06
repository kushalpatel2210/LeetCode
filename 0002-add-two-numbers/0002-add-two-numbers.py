# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0

        while l1 or l2:
            l1Val, l2Val = 0, 0

            if l1:
                l1Val = l1.val
                l1 = l1.next
            
            if l2:
                l2Val = l2.val
                l2 = l2.next
            
            currSum = l1Val + l2Val + carry
            dummy.next = ListNode(currSum % 10)
            dummy = dummy.next
            if currSum >= 10:
                carry = 1
            else:
                carry = 0
        
        if carry:
            dummy.next = ListNode(carry)
        
        return res.next
