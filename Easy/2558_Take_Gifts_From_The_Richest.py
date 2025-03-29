import heapq

class Solution:
    def floorSqrt(self, n): 
        low, high = 1, n // 2
        ans = 1
        while(low <= high):
            mid = (low + high) // 2
            temp = mid ** 2
            if(temp <= n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for val in gifts:
            heapq.heappush(heap, -1 * val)

        while(k > 0):
            largest = -heapq.heappop(heap)
            root = self.floorSqrt(largest)
            heapq.heappush(heap, -root)
            k -= 1

        return -sum(heap)