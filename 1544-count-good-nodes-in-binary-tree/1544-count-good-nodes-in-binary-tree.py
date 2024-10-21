# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float('-inf')
        goodNodes = 0

        def dfs(node, maxVal):
            nonlocal goodNodes

            if node is None:
                return
            
            if  maxVal <= node.val:
                goodNodes += 1
                maxVal = node.val

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, maxVal)

        return goodNodes