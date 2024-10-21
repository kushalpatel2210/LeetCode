# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head 
        maxSum = 0
        store = dict()
        i = 0

        while curr:
            store[i] = curr.val
            curr = curr.next
            i += 1
        
        curr = head
        start = 0
        
        while curr:
            twinIdx = i - 1 - start
            currSum = curr.val + store[twinIdx]
            maxSum = max(maxSum, currSum)
            curr = curr.next
            start += 1

        return maxSum