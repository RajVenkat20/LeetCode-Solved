class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        size = len(s)
        cnt = 0
        if(size < k):
            return 0

        hm = {}
        for i in range(k):
            hm[s[i]] = hm.get(s[i], 0) + 1
        
        if(len(hm) == k):
            cnt += 1
        
        for j in range(k, size):
            hm[s[j - k]] = hm.get(s[j - k], 0) - 1
            
            if(hm[s[j - k]] == 0):
                del hm[s[j - k]]

            hm[s[j]] = hm.get(s[j], 0) + 1
            if(len(hm) == k):
                cnt += 1

        return cnt