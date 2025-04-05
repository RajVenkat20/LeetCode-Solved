class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numSum = 0

        for i in range(k):
            numSum += nums[i]
        
        maxAvg = numSum / k

        for i in range(k, len(nums)):
            numSum -= nums[i - k]
            numSum += nums[i]
            maxAvg = max(maxAvg, numSum / k)

        return maxAvg