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
        copy = head
        dummy = headNode = node = Node(0)

        while head:
            node.next = Node(head.val)
            hashMap[head] = node.next
            node = node.next
            head = head.next
        
        headNode = headNode.next
        while copy:
            if copy.random:
                headNode.random = hashMap[copy.random] 
            copy = copy.next
            headNode = headNode.next

        return dummy.next

