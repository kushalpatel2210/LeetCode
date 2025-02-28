# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def postOrderDfs(node):
            if not node:
                return None
            
            left = postOrderDfs(node.left)
            right = postOrderDfs(node.right)
            
            if node == p or node == q:
                return node
            
            if left and right:
                return node
            
            return left if left else right
        
        return postOrderDfs(root)
