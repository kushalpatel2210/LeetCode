import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        curr = res = ListNode()
        minHeap = []

        for lst in lists:
            if lst:
                heapq.heappush(minHeap, Node(lst))
        
        while minHeap:
            node = heapq.heappop(minHeap)
            curr.next = node.node
            curr = curr.next

            if node.node.next:
                heapq.heappush(minHeap, Node(node.node.next))
        
        return res.next
        