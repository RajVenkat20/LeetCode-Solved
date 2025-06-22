class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res, cnt = [], 0
        i, temp = 0, ""

        while(i < len(s)):
            temp += s[i]
            cnt += 1

            if(cnt == k):
                cnt = 0
                res.append(temp)
                temp = ""

            i += 1

        x = len(temp)
        if(1 <= x < k):
            temp += (fill * (k - x))
            res.append(temp)

        return res