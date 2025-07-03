class Solution:
    def kthCharacter(self, k: int) -> str:
        s = ['a']
        while(len(s) < k):
            size = len(s)
            for i in range(size):
                nextChar = chr(ord('a') + ((ord(s[i]) - ord('a') + 1) % 26))
                s.append(nextChar)

        return s[k - 1]