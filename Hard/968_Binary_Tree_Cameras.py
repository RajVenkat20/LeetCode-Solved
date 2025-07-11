# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        covered = set({None})

        def dfs(node, par = None):
            if(node is None):
                return

            dfs(node.left, node)
            dfs(node.right, node)

            if(par is None and node not in covered or
               node.left not in covered or node.right not in covered):
               self.ans +=1
               covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans