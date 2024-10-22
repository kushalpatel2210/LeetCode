from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs_level(node):
            if not root:
                return []
            
            queue = deque([root])
            result = []

            while queue:
                current_level_length = len(queue)
                current_traversal = []

                for _ in range(current_level_length):
                    node = queue.popleft()
                    current_traversal.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

                result.append(current_traversal[-1])
            
            return result
        
        return bfs_level(root)