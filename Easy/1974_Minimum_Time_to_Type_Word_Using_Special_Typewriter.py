class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        count = 0
        curr = 'a'

        for i in word:
            count = min(abs(ord(i) - ord(curr)), 26 - (abs(ord(i) - ord(curr))))
            ans += count + 1
            curr = i
        
        return ans