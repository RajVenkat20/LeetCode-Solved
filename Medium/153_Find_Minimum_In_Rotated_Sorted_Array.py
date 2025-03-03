class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')
        low, high = 0, len(nums) - 1

        while(low <= high):
            mid = (low + high) // 2
            if(nums[low] <= nums[mid]):
                minimum = min(nums[low], minimum)
                low = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                high = mid - 1

        return minimum