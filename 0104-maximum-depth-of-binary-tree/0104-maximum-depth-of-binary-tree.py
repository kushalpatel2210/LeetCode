# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            height = max(left, right)

            return height
        
        return dfs(root)

