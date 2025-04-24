class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, n = 0, len(nums)
        cnt = {}
        distinct = len(set(nums))
        r = 0

        for l in range(n):
            if(l > 0):
                removed = nums[l - 1]
                cnt[removed] -= 1
                if(cnt[removed] == 0):
                    cnt.pop(removed)
            while(r < n and len(cnt) < distinct):
                curr = nums[r]
                cnt[curr] = cnt.get(curr, 0) + 1
                r += 1
            if(len(cnt) == distinct):
                res += (n - r + 1)

        return res