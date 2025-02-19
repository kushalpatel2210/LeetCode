# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        res = dummy = ListNode()
        dummy.next = head
        length = 0

        while node:
            length += 1
            node = node.next
        
        for i in range(length):
            if i == length - n:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
        
        return res.next
