from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        currLevel = 0
        res = []

        while q:
            currLength = len(q)
            currLevel += 1
            currLevelValues = []

            for _ in range(currLength):
                node = q.popleft()

                if node:
                    currLevelValues.append(node.val)
                
                if node: 
                    q.append(node.left)
                    q.append(node.right)
        
            if currLevelValues:
                if currLevel % 2 == 0:
                    res.append(currLevelValues[::-1])
                else:
                    res.append(currLevelValues)
        
        return res
                    
        