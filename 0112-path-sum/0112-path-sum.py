# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currSum = 0
        hasPathSum = False

        if not root:
            return False

        def dfs(node):
            nonlocal currSum, hasPathSum

            if not node:
                return hasPathSum

            currSum += node.val
            dfs(node.left)
            dfs(node.right)
            
            if not node.left and not node.right and currSum == targetSum:
                hasPathSum = True

            currSum -= node.val

            return hasPathSum
        
        return dfs(root)