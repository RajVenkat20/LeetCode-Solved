import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = nums[:k]
        heapq.heapify(minH)

        for val in nums[k:]:
            if(val > minH[0]):
                heapq.heapreplace(minH, val)

        return heapq.heappop(minH)