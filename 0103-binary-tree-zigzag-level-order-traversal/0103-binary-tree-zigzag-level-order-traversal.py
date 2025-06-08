# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        i = 0

        while q:
            currLevel = []
            
            for _ in range(len(q)):
                node = q.popleft()
                
                if node:
                    currLevel.append(node.val)

                if node and node.left:
                    q.append(node.left)
                
                if node and node.right:
                    q.append(node.right)
            
            if currLevel:
                if i % 2 == 0:
                    res.append(currLevel)
                else:
                    res.append(currLevel[::-1])
            i += 1

        return res