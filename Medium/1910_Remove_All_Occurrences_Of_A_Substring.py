class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        tlen = len(part)
        tend = part[-1]

        for char in s:
            res.append(char)

            if(char == tend and len(res) >= tlen):
                if("".join(res[-tlen:]) == part):
                    cnt = tlen
                    while(cnt > 0):
                        res.pop()
                        cnt -= 1

        return "".join(res)