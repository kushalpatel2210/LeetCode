from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            currLevel = len(q)

            for i in range(currLevel):
                node = q.popleft()
                
                if node:
                    if i == currLevel - 1:
                        res.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
        
        return res