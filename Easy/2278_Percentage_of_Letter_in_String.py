import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        size = len(s)
        cnt = s.count(letter)

        res = math.floor(cnt / size * 100) 

        return res        