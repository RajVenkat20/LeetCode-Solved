class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        hm = {0: 1}
        cnt = prefSum = 0

        for i in range(len(nums)):
            prefSum += nums[i]

            if(prefSum - goal in hm):
                cnt += hm[prefSum - goal]

            hm[prefSum] = hm.get(prefSum, 0) + 1

        return cnt