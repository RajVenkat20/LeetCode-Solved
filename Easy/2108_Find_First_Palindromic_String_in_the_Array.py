class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while(l <= r):
            if(s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False

        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if(self.isPalindrome(word)):
                return word

        return ""