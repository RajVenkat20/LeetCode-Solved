class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix = 0, 0
        lastIndex = 0
        base = 29
        power = 1
        mod = 10 ** 9 + 7

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1
            
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod

            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if(prefix == suffix):
                lastIndex = i

        suffix = s[lastIndex + 1:]
        
        return suffix[::-1] + s