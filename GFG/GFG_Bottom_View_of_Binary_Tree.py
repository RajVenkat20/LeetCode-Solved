from collections import deque

class Solution:
    def bottomView(self, root):
        if(root is None):
            return []
            
        hashmap = {}
        leftmost = 0
        q = deque()
        q.append((root, 0))
        
        while(q):
            top = q.popleft()
            curr = top[0]
            idx = top[1]
            
            hashmap[idx] = curr.data
            
            leftmost = min(idx, leftmost)
            
            if(curr.left):
                q.append((curr.left, idx - 1))
            if(curr.right):
                q.append((curr.right, idx + 1))
                
        ans = []
        
        while leftmost in hashmap:
            ans.append(hashmap[leftmost])
            leftmost += 1
            
        return ans