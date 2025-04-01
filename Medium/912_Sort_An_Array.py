import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if(n == 1):
            return nums
        
        res = []
        heapq.heapify(nums)
        
        for i in range(n):
            res.append(heapq.heappop(nums))

        return res