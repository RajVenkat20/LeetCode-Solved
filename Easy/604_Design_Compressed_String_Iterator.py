import re

class StringIterator:
    def uncompress(self, s):
        i = 0
        res = []

        while(i < len(s)):
            char = s[i]
            i += 1
            cnt = 0

            while(i < len(s) and s[i].isdigit()):
                cnt = cnt * 10 + int(s[i])
                i += 1

            res.append(char * cnt)

        return "".join(res)

    def __init__(self, compressedString: str):
        self.s = self.uncompress(compressedString)
        self.i = 0
        self.size = len(self.s)

    def next(self) -> str:
        if(self.hasNext()):
            res = self.s[self.i]
            self.i += 1
            return res

        return " "

    def hasNext(self) -> bool:
        if(self.i < self.size):
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()