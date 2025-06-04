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
        headNode = head
        dummy = dummyNode = res = Node(0)
        hashMap = {}

        while headNode:
            dummy.next = Node(headNode.val)
            hashMap[headNode] = dummy.next
            dummy = dummy.next
            headNode = headNode.next
        
        dummyNode = dummyNode.next
        while head:
            if head.random:
                dummyNode.random = hashMap[head.random]
            dummyNode = dummyNode.next
            head = head.next
        
        return res.next
