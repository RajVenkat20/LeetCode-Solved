class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def houseRobberI(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        n = len(nums)
        sum1 = houseRobberI(nums[:(n - 1)])
        sum2 = houseRobberI(nums[1:])
        return max(sum1, sum2, nums[0])