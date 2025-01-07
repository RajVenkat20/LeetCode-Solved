# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if(root is None):
            return res

        queue = [root]
        lr = True

        while(queue):
            size = len(queue)
            row = [0] * size

            for i in range(size):
                curr = queue.pop(0)
                idx = i if lr else (size - 1 - i)
                row[idx] = curr.val            

                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
            
            lr = not lr
            res.append(row)

        return res
        