# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, p, q):
        if(p is None and q is None):
            return True
        elif(p is None or q is None):
            return False

        return p.val == q.val and self.preOrder(p.left, q.right) and self.preOrder(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        
        p = root.left
        q = root.right

        return self.preOrder(p, q)
        
        