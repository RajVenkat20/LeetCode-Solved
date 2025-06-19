# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        visited = []

        def total(node):
            if(not node):
                return 0
            visited.append(total(node.left) + total(node.right) + node.val)
        
            return visited[-1]

        sumTotal = total(root)
        visited.pop()

        return sumTotal / 2.0 in visited