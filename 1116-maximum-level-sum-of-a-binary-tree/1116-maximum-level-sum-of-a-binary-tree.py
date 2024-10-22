from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs_level(node):
            if not node:
                return 0
                
            maxSum = float('-inf')
            smallest_level = 1
            level = 1
            queue = deque([node])

            while queue:
                current_level_length = len(queue)
                current_level = []

                for _ in range(current_level_length):
                    node = queue.popleft()
                    current_level.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                sum_of_level = sum(current_level)
                
                if sum_of_level > maxSum:
                    maxSum = sum_of_level
                    smallest_level = level
                
                level += 1

            return smallest_level
        
        return bfs_level(root)
