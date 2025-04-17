class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        res = 0

        for i in range(size):
            # Odd length palindromes
            l, r = i, i
            while(l >= 0 and r < size and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while(l >= 0 and r < size and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        
        return res