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
        stack = []
        length = 0
        dummy = head
        
        while dummy:
            length += 1
            stack.append(dummy)
            dummy = dummy.next

        curr = head
        for _ in range((length - 1) // 2):
            pop = stack.pop()
            pop.next = curr.next
            curr.next = pop
            curr = pop.next
        
        stack.pop().next = None