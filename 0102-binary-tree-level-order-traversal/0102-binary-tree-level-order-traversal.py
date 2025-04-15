from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            currLength = len(q)
            currLevel = []

            for _ in range(currLength):
                node = q.popleft()

                if node:
                    currLevel.append(node.val)

                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
            if currLevel:
                res.append(currLevel)
        
        return res