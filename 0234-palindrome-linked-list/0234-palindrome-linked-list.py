# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self, node):
        slow, fast = node, node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse(self, node):
        prev = None
        curr = node

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.find_mid(head)
        second_head = self.reverse(mid)

        ptr1, ptr2 = head, second_head

        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return True