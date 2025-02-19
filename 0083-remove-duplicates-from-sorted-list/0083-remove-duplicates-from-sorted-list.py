# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, head)
        curr = head

        while curr:
            tmp = curr
            while tmp.next and tmp.next.val == curr.val:
                tmp = tmp.next
            curr.next = tmp.next
            curr = curr.next
        
        return node.next
