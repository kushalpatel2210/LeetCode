"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = head
        res = headNode = node = Node(0)
        dct = {}

        while head:
            node.next = Node(head.val, head.next)
            dct[head] = node.next
            head = head.next
            node = node.next
        
        headNode = headNode.next
        while copy:
            if copy.random:
                headNode.random = dct[copy.random]
            copy = copy.next
            headNode = headNode.next
        
        return res.next

