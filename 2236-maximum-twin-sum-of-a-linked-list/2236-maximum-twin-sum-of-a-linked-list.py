# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = list()
        node = ListNode(0, head)
        node = node.next
        maxSum = float('-inf')

        while node:
            lst.append(node.val)
            node = node.next

        n = len(lst) 
        for i in range(n // 2):
            currSum = lst[i] + lst[n - i - 1]
            maxSum = max(maxSum, currSum)

        return maxSum
