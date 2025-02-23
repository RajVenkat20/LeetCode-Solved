class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        s.sort(reverse=True)
        g.sort(reverse=True)

        p1, p2, = 0, 0
        while(p1 < len(s) and p2 < len(g)):
            if(s[p1] >= g[p2]):
                cnt += 1
                p1 += 1
            p2 += 1
            
        return cnt