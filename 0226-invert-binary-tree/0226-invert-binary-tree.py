# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_post_order(node):
            if not node:
                return
            
            left = dfs_post_order(node.left)
            right = dfs_post_order(node.right)
            node.left, node.right = right, left
            
            return node
        
        return dfs_post_order(root)