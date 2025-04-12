import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minH = []
        for stone in stones:
            heapq.heappush(minH, -1 * stone)

        while(len(minH) > 1):
            heavy1 = -1 * heapq.heappop(minH)
            heavy2 = -1 * heapq.heappop(minH)

            if(heavy1 != heavy2):
                diff = abs(heavy1 - heavy2)
                heapq.heappush(minH, -1 * diff)

        return -1 * minH[0] if len(minH) else 0