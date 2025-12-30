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
        # Find mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse from mid
        mid = slow.next
        slow.next = None
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        
        # Re-arrange
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1
            first, second = tmp1, tmp2


