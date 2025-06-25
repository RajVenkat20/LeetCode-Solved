# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inOrd = []

        def inOrder(node):
            if(node is None):
                return
            inOrder(node.left)
            inOrd.append(node.val)
            inOrder(node.right)

        inOrder(root)
        
        l, r = 0, len(inOrd) - 1

        while(l < r):
            if(inOrd[l] + inOrd[r] == k):
                return True
            elif(inOrd[l] + inOrd[r] > k):
                r -= 1
            else:
                l += 1

        return False