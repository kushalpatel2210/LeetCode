# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = slow = fast = ListNode()
        fast.next = head

        for i in range(n):
            fast = fast.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
    
        slow.next = slow.next.next

        return res.next

