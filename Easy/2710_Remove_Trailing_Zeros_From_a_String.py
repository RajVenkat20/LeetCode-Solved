class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        size = len(num)
        for i in range(size - 1, -1, -1):
            if(num[i] != '0'):
                return num[:i + 1]

        return num