# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        node = head

        while node:
            lst.append(node.val)
            node = node.next
        
        l, r = 0, len(lst) - 1
        while l <= r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True
'''