import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minH = nums[:k]
        heapq.heapify(self.minH)

        for val in nums[k:]:
            if(val > self.minH[0]):
                heapq.heapreplace(self.minH, val)

    def add(self, val: int) -> int:
        heapq.heappush(self.minH, val)
        if(len(self.minH) > self.k):
            heapq.heappop(self.minH)
        
        return self.minH[0]       

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)