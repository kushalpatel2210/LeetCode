# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
                
            return 1 + max(left, right) 

        if not root:
            return True
        
        left = dfs(root.left)
        right = dfs(root.right)

        if abs(right - left) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)