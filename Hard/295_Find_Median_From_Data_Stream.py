import heapq

class MedianFinder:

    def __init__(self):
        # Create 2 heaps small, and large
        # The small heap will be a max heap and the large heap will be a min heap
        # Heaps need to be of roughly same size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Since Python doesn't allow a max heap, to implement one we multiply with -1
        heapq.heappush(self.small, -1 * num)

        # Making sure every number in small heap is less than every number in large heap
        if(self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If sizes are uneven, need to balance them
        if(len(self.small) > len(self.large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if(len(self.large) > len(self.small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)     

    def findMedian(self) -> float:
        if(len(self.small) > len(self.large)):
            return -1 * self.small[0]
        if(len(self.large) > len(self.small)):
            return self.large[0]
        
        return  (-1 * self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()