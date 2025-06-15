"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                nxt = curr.next

                # find tail of child
                tail = curr.child
                while tail.next:
                    tail = tail.next
                
                curr.next = curr.child
                curr.child.prev = curr

                if nxt:
                    nxt.prev = tail
                    tail.next = nxt
                
                curr.child = None
            
            curr = curr.next

        return head