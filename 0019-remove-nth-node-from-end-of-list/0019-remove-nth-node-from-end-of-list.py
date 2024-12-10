# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        node = head

        while node:
            length += 1
            node = node.next
        
        node = ListNode()
        ptr = node
        node.next = head
        i = 0

        while node:
            if i == (length - n):
                node.next = node.next.next
                break
           
            node = node.next 
            i += 1

        return ptr.next