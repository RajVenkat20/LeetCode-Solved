class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right = 0, 0
        hm = collections.defaultdict(int)
        res, maxf = 0, 0

        for right in range(len(s)):
            hm[s[right]] += 1
            maxf = max(maxf, hm[s[right]])
            
            while(right - left + 1 - maxf > k):
                hm[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res