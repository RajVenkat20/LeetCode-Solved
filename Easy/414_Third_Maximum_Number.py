class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap, dup = [], set()

        for i in range(len(nums)):
            if(nums[i] in dup):
                continue
            if(len(heap) == 3):
                if(heap[0] < nums[i]):
                    dup.remove(heap[0])
                    heappop(heap)

                    heappush(heap, nums[i])
                    dup.add(nums[i])
            else:
                heappush(heap, nums[i])
                dup.add(nums[i])

        if(len(heap) == 1):
            return heap[0]
        elif(len(heap) == 2):
            return max(heap[0], heap[1])

        return heap[0]