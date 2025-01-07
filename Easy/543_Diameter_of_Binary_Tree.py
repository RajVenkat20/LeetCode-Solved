# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeHeightDiamterCalc(self, root, diameter) -> int:
        if(root is None):
            return 0

        lh = self.treeHeightDiamterCalc(root.left, diameter)
        rh = self.treeHeightDiamterCalc(root.right, diameter)

        diameter[0] = max(diameter[0], lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.treeHeightDiamterCalc(root, diameter)    
        return diameter[0]
