# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        while head and head.next:
            if head.next in seen:
                return head.next
            seen.add(head)
            head = head.next
        
        return None