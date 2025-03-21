class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        size = len(s)

        ans = 0
        ans += hm[s[size - 1]]

        for i in range(size - 1, 0, -1):
            if(hm[s[i - 1]] < hm[s[i]]):
                ans -= hm[s[i - 1]]
            else:
                ans += hm[s[i - 1]]

        return ans