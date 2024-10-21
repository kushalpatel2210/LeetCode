# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafSeq1, leafSeq2 = [], []
        
        def dfs(node, leafSeq):
            if not node:
                return
            
            if not node.left and not node.right:
                leafSeq.append(node.val)
            
            dfs(node.left, leafSeq)
            dfs(node.right, leafSeq)
        
        dfs(root1, leafSeq1)
        dfs(root2, leafSeq2)

        return leafSeq1 == leafSeq2

