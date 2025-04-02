class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        size = len(nums)
        rightMax = [0] * size
        greatestRight = 0

        for i in range(size - 1, -1, -1):
            rightMax[i] = greatestRight
            greatestRight = max(greatestRight, nums[i])

        maxTriplet = 0
        maxLeft = nums[0]

        for j in range(1, size - 1):
            val = (maxLeft - nums[j]) * rightMax[j]
            maxTriplet = max(val, maxTriplet)
            if(nums[j] > maxLeft):
                maxLeft = nums[j]

        return maxTriplet