class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        switch = 0
        for i in range(len(s) - 1):
            if(s[i] != s[i + 1]):
                switch += 1

        return switch <= 1