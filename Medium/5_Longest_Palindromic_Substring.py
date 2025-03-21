class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        size = len(s)

        for i in range(size):
            # Odd length palindromes
            l, r = i, i
            while(l >= 0 and r < size and s[l] == s[r]):
                if(r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while(l >= 0 and r < size and s[l] == s[r]):
                if(r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return res