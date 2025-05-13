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
        hashMap = dict()
        dummyNode = head
        dummy = res = node = Node(0)

        while dummyNode:
            dummy.next = Node(dummyNode.val)
            hashMap[dummyNode] = dummy.next
            dummy = dummy.next
            dummyNode = dummyNode.next
        
        node = node.next
        while head:
            if head.random:
                node.random = hashMap[head.random]
            head = head.next
            node = node.next
        
        return res.next
            

