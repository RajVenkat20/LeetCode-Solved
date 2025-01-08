# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if(root is None):
            return res
        
        queue = [root]

        while(queue):
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)

                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
            res.append(level[-1])
        
        return res

        