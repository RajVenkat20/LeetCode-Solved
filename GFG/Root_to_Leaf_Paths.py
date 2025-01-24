
from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def recurPath(self, node, path, paths):
        if(node is None):
            return
        
        path.append(node.data)
        
        if(node.left is None and node.right is None):
            paths.append(list(path))
        else:
            self.recurPath(node.left, path, paths)
            self.recurPath(node.right, path, paths)
        
        path.pop()
            
    
    def Paths(self, root):
        paths = []
        self.recurPath(root, [], paths)
        
        return paths
        
