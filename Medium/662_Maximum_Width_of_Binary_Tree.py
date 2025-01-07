# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0

        q = [(root, 0)]
        ans = 0

        while(q):
            size = len(q)
            minimal = q[0][1]
            first, last = 0, 0

            for i in range(size):
                currId = q[0][1] - minimal
                currNode = q.pop(0)
                
                if(i == 0):
                    first = currId
                if(i == size - 1):
                    last = currId
                if(currNode[0].left):
                    q.append((currNode[0].left, 2 * currId + 1))
                if(currNode[0].right):
                    q.append((currNode[0].right, 2 * currId + 2))
            
            ans = max(ans, last - first + 1)

        return ans

        