from collections import defaultdict
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
        hashMap = defaultdict(lambda: Node(0))
        hashMap[None] = None

        curr = head
        while curr:
            hashMap[curr].val = curr.val
            hashMap[curr].next = hashMap[curr.next]
            hashMap[curr].random = hashMap[curr.random]
            curr = curr.next
        
        return hashMap[head]
        
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        curr = node = head 

        if not head:
            return None

        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        while node:
            hashMap[node].next = hashMap[node.next] if node.next else None
            hashMap[node].random = hashMap[node.random] if node.random else None
            node = node.next

        return hashMap[head]
'''