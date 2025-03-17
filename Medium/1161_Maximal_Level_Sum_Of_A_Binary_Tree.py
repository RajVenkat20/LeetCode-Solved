from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if(root.left is None and root.right is None):
            return root.val
        
        maxSum = float('-inf')
        maxLevel = 1
        queue = deque()
        queue.append(root)
        i = 1

        while(queue):
            levelSum = 0

            for _ in range(len(queue)):
                curr = queue.popleft()
                levelSum += curr.val

                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)

            if(levelSum > maxSum):
                maxSum = levelSum
                maxLevel = i
            i += 1

        return maxLevel