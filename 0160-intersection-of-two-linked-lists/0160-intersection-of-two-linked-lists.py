# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA, nodeB = headA, headB

        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA

'''
nodeA, nodeB = headA, headB
        seen = set()

        while nodeA:
            seen.add(nodeA)
            nodeA = nodeA.next
        
        while nodeB:
            if nodeB in seen:
                return nodeB
            nodeB = nodeB.next
        
        return None
'''