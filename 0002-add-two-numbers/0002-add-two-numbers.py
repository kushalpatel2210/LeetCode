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
            currSum = carry

            if l1:
                currSum += l1.val
                l1 = l1.next
            
            if l2:
                currSum += l2.val
                l2 = l2.next
            
            carry = currSum // 10
            node.next = ListNode(currSum % 10)
            node = node.next
        
        if carry:
            node.next = ListNode(carry)
        
        return res.next