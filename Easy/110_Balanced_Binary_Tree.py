# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeHeight(self, root: Optional[TreeNode]):
        if(root is None):
            return 0
        
        leftHeight = self.treeHeight(root.left)

        if(leftHeight == -1):
            return - 1

        rightHeight = self.treeHeight(root.right)

        if(rightHeight == -1):
            return - 1

        if(abs(leftHeight - rightHeight) > 1):
            return - 1
        
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.treeHeight(root) != -1

        