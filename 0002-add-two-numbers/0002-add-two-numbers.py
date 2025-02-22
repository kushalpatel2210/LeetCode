# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = node = ListNode()
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currSum = val1 + val2 + carry
            carry = 1 if currSum >= 10 else 0

            node.next = ListNode(currSum) if currSum < 10 else ListNode(currSum % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next
        
        if carry > 0:
            node.next = ListNode(carry)
        
        return res.next

             