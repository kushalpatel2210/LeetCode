# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        node = head
        firstPtr, lastPtr = None, None
        start = 1
        
        while node:
            if start == left - 1:
                firstPtr = node
            if start == right:
                lastPtr = node.next
                node.next = None
            node = node.next
            start += 1
        
        
        def reverse(node, lastPart):
            prev = lastPart
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            
            return prev

        if firstPtr:
            currNode = reverse(firstPtr.next, lastPtr)
            firstPtr.next = currNode
        else:
            # reversal started at head
            head = reverse(head, lastPtr)

        return head
