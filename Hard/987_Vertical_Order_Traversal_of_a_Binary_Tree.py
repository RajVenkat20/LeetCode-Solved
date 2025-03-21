# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        mp = defaultdict(lambda: [])
        
        def traverse(node, vertical, level):
            if not node:
                return
            mp[vertical].append((level, node.val))
            traverse(node.left, vertical - 1, level + 1)
            traverse(node.right, vertical + 1, level + 1)
        
        traverse(root, 0, 0)
        
        result = []
        for vertical in sorted(mp.keys()):
            mp[vertical].sort()
            result.append([val for _, val in mp[vertical]])
        
        return result        
        