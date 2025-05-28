class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        res, n = 0, len(s)

        for i in range(1, 27):
            L = i * count
            if(L > n):
                break

            l, d = 0, Counter()
            for r, c in enumerate(s):
                d[c] += 1
                if(r - l + 1 == L):
                    if(all(x == count or x == 0 for x in d.values())):
                        res += 1
                    d[s[l]] -= 1
                    if(d[s[l]] == 0):
                        d.pop(s[l])
                    l += 1

        return res