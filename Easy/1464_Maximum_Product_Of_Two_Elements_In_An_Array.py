import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)

        max1 = -1 * heapq.heappop(nums)
        max2 = -1 * heapq.heappop(nums)

        return (max1 - 1) * (max2 - 1)