from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if("0000" in deadends):
            return -1
        
        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])

            return res

        while(q):
            lockPos, turns = q.popleft()
            
            if(lockPos == target):
                return turns
            
            for child in children(lockPos):
                if(child not in visit):
                    visit.add(child)
                    q.append([child, turns + 1])

        return -1