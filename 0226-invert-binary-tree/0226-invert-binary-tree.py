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
            
            right_subtree = dfs_post_order(node.right)
            left_subtree = dfs_post_order(node.left)
            node.left = right_subtree
            node.right = left_subtree

            return node
            
        return dfs_post_order(root)
