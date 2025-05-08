# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def leftDfs(node):
            if(node is None):
                return []

            if(node.left is None and node.right is None):
                return []
            else:
                if(node.left):
                    return [node.val] + leftDfs(node.left)
                else:
                    return [node.val] + leftDfs(node.right)

        def rightDfs(node):
            if(node is None):
                return []
            
            if(node.right is None and node.left is None):
                return []
            else:
                if(node.right):
                    return rightDfs(node.right) + [node.val]
                else:
                    return rightDfs(node.left) + [node.val]

        def findLeaves(node):
            if(node is None):
                return []

            if(node.right is None and node.left is None):
                return [node.val]
            else:
                return findLeaves(node.left) + findLeaves(node.right)

        ans = [root.val] + leftDfs(root.left) + findLeaves(root.left) + findLeaves(root.right) + rightDfs(root.right)

        return ans