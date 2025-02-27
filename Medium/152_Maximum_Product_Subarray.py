class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref, suff, n = 1, 1, len(nums)
        ans = float('-inf')
        for i in range(n):
            if(pref == 0):
                pref = 1
            if(suff == 0):
                suff = 1

            pref = pref * nums[i]
            suff = suff * nums[n - i - 1]            
            ans = max(ans, max(pref, suff))

        return ans