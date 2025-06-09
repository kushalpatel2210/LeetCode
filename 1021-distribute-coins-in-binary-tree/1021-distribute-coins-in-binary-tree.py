# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return [0, 0] # [size, coins]
            
            l_size, l_coins = dfs(node.left)
            r_size, r_coins = dfs(node.right)

            size = l_size + r_size + 1
            coins = l_coins + r_coins + node.val

            res += abs(size - coins)
            return [size, coins]
        
        dfs(root)
        
        return res