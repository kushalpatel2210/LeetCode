# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSuccessor(self, node):
        currNode = node.right
        while currNode and currNode.left:
            currNode = currNode.left
        return currNode

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found node

            # left child is none
            if not root.left:
                return root.right
            
            # right child is none
            if not root.right:
                return root.left

            # both child presents
            successorNode = self.findSuccessor(root)
            root.val = successorNode.val
            root.right = self.deleteNode(root.right, successorNode.val)
        
        return root