# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def max_depth(node):
            if node is None:
                return 0
            
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)

            return max(left_depth, right_depth) + 1
        
        return max_depth(root)