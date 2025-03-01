from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        currentLevel = 0

        while queue:
            lenQ = len(queue)
            level = []
            
            for _ in range(lenQ):
                node = queue.popleft()       

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                res.append(level)
            currentLevel += 1

        return res