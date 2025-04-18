class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm = {}
        prefix = 0
        ans = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if(prefix == k):
                ans = i + 1
            
            if(prefix - k in hm):
                ans = max(ans, i - hm[prefix - k])
            
            if(prefix not in hm):
                hm[prefix] = i

        return ans