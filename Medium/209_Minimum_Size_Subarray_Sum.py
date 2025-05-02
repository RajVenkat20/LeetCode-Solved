class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0
        res = float('inf')
        total = 0
        while(r < len(nums)):
            total += nums[r]
            while(total >= target):
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

            r += 1

        return res if res != float('inf') else 0