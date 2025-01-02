# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs_post_order(node):
            if not node:
                return 0
            
            left_subtree = dfs_post_order(node.left)
            right_subtree = dfs_post_order(node.right)

            # visit Node
            return max(left_subtree, right_subtree) + 1

        return dfs_post_order(root)
