class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)        
        low, high = 1, n - 2

        if(n == 1):
            return nums[0]
        if(nums[0] != nums[1]):
            return nums[0]
        if(nums[n - 1] != nums[n - 2]):
            return nums[n - 1]

        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid - 1] != nums[mid] != nums[mid + 1]):
                return nums[mid]
            elif((mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1])):
                low = mid + 1
            else:
                high = mid - 1