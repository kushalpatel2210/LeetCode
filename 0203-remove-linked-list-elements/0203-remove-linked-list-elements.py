# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = node = ListNode()
        node.next = head

        while node:
            curr = node
            while curr.next and curr.next.val == val:
                curr = curr.next
            
            node.next = curr.next
            node = node.next
        
        return res.next