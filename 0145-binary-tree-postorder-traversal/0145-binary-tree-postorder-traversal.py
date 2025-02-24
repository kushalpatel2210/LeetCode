# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post_order_traversal = list()

        def post_order_dfs(node):
            if not node:
                return
            
            post_order_dfs(node.left)
            post_order_dfs(node.right)
            post_order_traversal.append(node.val)
        
        post_order_dfs(root)

        return post_order_traversal