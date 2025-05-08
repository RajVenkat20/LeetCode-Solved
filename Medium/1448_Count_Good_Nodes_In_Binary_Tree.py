# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodes(node, maxVal):
            if(node is None):
                return 0
            
            if(node.val >= maxVal):
                return 1 + goodNodes(node.left, node.val) + goodNodes(node.right, node.val)
            else:
                return goodNodes(node.left, maxVal) + goodNodes(node.right, maxVal)


        return goodNodes(root, root.val)