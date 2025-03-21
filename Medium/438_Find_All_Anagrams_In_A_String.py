class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        psize = len(p)
        ssize = len(s)
        if(psize > ssize):
            return []

        pcount, scount = {}, {}

        for i in range(psize):
            pcount[p[i]] = pcount.get(p[i], 0) + 1
            scount[s[i]] = scount.get(s[i], 0) + 1
        
        res = [0] if scount == pcount else []

        l = 0
        for r in range(psize, ssize):
            scount[s[r]] = scount.get(s[r], 0) + 1
            scount[s[l]] -= 1
        
            if(scount[s[l]] == 0):
                scount.pop(s[l])

            l += 1

            if(scount == pcount):
                res.append(l)
        
        return res