class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i < j and nums[i] == nums[j] and (i * j) % k == 0):
                    cnt += 1

        return cnt