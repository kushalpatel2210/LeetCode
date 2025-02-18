# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time O(n) space O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp
        
        # merge two halfs 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 

'''
# time and space O(n)
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
'''