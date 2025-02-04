class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        size = len(nums)
        if(size == 1):
            return nums[0]
        
        incSum = currSum = nums[0]

        for i in range(1, size):
            if(nums[i - 1] < nums[i]):
                currSum += nums[i]
                incSum = max(incSum, currSum)
            else:
                currSum = nums[i]

        return incSum
    
