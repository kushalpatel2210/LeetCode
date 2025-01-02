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
            
            left_subtree = dfs_post_order(node.right)
            right_subtree = dfs_post_order(node.left)
            node.left = left_subtree
            node.right = right_subtree
            
            return node
            
        return dfs_post_order(root)
