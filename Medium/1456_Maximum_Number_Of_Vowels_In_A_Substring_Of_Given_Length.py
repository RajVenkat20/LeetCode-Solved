class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if(s[i] in vowels):
                cnt += 1
        
        left = 0
        maxVowels = cnt
        for right in range(k, len(s)):
            if(s[right] in vowels):
                cnt += 1
            if(s[left] in vowels):
                cnt -= 1
            left += 1
            maxVowels = max(maxVowels, cnt)

        return maxVowels
