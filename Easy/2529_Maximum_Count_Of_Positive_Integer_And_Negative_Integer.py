class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        firstPos = float('inf')
        lastNeg = float('-inf')

        if(nums[0] == 0 and nums[-1] == 0):
            return 0

        size = len(nums)
        low, high = 0, size - 1

        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] > 0):
                firstPos = mid
                high = mid - 1
            else:
                low = mid + 1
        
        low, high = 0, size - 1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] < 0):
                lastNeg = mid
                low = mid + 1
            else:
                high = mid - 1

        return max(lastNeg + 1, size - firstPos)