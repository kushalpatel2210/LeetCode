# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        oddPtr = head
        evenPtr = evenHead = head.next

        while evenPtr and evenPtr.next:
            oddPtr.next = evenPtr.next
            oddPtr = oddPtr.next
            evenPtr.next = oddPtr.next
            evenPtr = evenPtr.next
        
        oddPtr.next = evenHead

        return head