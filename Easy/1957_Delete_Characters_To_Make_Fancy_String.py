class Solution:
    def makeFancyString(self, s: str) -> str:
        size = len(s)
        if(size <= 2):
            return s
        
        ans = s[0]
        cnt = 1
        for i in range(1, size):
            if(s[i] == ans[-1]):
                cnt += 1
                if(cnt < 3):
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
        
        return ans