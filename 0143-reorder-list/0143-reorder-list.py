# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        node = head 
        stack = list()

        while node:
            stack.append(node)
            node = node.next
        
        curr = head
        n = len(stack)
        for _ in range((n - 1) // 2):
            top = stack.pop()
            top.next = curr.next
            curr.next = top
            curr = top.next
        
        stack.pop().next = None