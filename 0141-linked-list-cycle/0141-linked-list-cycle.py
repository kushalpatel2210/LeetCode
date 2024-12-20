# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using Fast and Slow pointer
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

'''
# Using set 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()

        while head:
            if head not in nodes:
                nodes.add(head)
                head = head.next
            else:
                return True
        
        return False
'''