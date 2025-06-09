# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        stack = [] # monolothic decreasing
        
        while head:
            nums.append(head.val)
            head = head.next

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                _, idx = stack.pop()
                res[idx] = num
            stack.append((num, i))
        
        return res