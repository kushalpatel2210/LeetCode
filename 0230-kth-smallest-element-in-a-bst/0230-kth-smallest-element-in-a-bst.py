# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if len(elements) < k:
                elements.append(node.val)
            dfs(node.right)

            return elements[-1]
        
        return dfs(root)

'''
# Brute force solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        def dfs(node):
            if not node:
                return
            
            elements.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        elements.sort()
        return elements[k - 1]
'''