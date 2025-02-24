# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = list()

        def in_order_dfs(node):
            nonlocal traversal 

            if not node:
                return None

            in_order_dfs(node.left)
            traversal.append(node.val)
            in_order_dfs(node.right)
        
        in_order_dfs(root)
        return traversal
