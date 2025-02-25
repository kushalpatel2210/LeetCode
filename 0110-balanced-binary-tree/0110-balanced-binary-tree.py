# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = 0
        result = True

        def dfs(node):
            nonlocal height, result

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
 
            if abs(left - right) > 1:
                result = False
            
            return 1 + max(left, right)

        dfs(root)
        return result
        