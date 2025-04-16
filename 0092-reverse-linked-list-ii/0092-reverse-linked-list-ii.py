# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        then = curr.next
        for _ in range(right - left):
            curr.next = then.next
            then.next = prev.next
            prev.next = then
            then = curr.next
        
        return dummy.next