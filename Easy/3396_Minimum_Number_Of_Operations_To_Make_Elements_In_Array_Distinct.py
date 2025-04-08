from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hm = {}
        cnt = 0
        d = deque(nums)

        for num in d:
            hm[num] = hm.get(num, 0) + 1
        
        while(True):
            flag = False
            for key in hm:
                if(hm[key] > 1):
                    flag = True
                    break

            if(not flag):
                return cnt

            for i in range(3):
                curr = d.popleft()
                if(not d):
                    return cnt + 1
                hm[curr] -= 1
            
            cnt += 1