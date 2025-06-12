class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = 0
        size = len(nums)
        for i in range(size + 1):
            diff = abs(nums[i % size] - nums[(i + 1) % size])
            maxDiff = max(maxDiff, diff)

        return maxDiff