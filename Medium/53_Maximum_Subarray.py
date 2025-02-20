class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currSum = 0

        for val in nums:
            currSum += val

            if(currSum > res):
                res = currSum
            if(currSum < 0):
                currSum = 0

        return res