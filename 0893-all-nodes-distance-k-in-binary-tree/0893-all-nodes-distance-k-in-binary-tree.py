# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        visited = set()
        res = []

        def mapParent(node, parent):
            if node:
                parentMap[node] = parent
                mapParent(node.left, node)
                mapParent(node.right, node)
        
        def dfs(node, remainingDistance):
            if not node or node in visited:
                return 
            
            visited.add(node)

            if remainingDistance == 0:
                res.append(node.val)
            else:
                dfs(node.left, remainingDistance - 1)
                dfs(node.right, remainingDistance - 1)
                dfs(parentMap[node], remainingDistance - 1)
        
        mapParent(root, None)
        dfs(target, k)

        return res