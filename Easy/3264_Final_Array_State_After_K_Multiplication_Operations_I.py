import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = []
        size = len(nums)
        temp = [0] * size
        
        for i in range(size):
            heapq.heappush(res, (nums[i], i))
        
        while(k > 0):
            smallest, idx = heapq.heappop(res)
            heapq.heappush(res, (smallest * multiplier, idx))
            k -= 1

        for val, idx in res:
            temp[idx] = val

        return temp