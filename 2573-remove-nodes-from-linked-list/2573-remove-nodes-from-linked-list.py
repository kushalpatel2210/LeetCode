# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        stack = []
        node = ListNode(0, head)

        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next
        
        curr = res = ListNode()
        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next

        return res.next

'''
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        def reverse(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            
            return prev
        
        curr = reversedList = ListNode(0, reverse(head))
        
        while curr and curr.next:
            if curr.next.val >= curr.val:
                minVal = curr.next.val
                curr = curr.next
            else:
                curr.next = curr.next.next
                
        res = reverse(reversedList.next)

        return res 
'''