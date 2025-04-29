class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxNum, size = max(nums), len(nums)
        l, maxCnt = 0, 0
        res = 0

        for r in range(size):
            if(nums[r] == maxNum):
                maxCnt += 1
            while(maxCnt == k):
                if(nums[l] == maxNum):
                    maxCnt -= 1
                l += 1
            res += l

        return res