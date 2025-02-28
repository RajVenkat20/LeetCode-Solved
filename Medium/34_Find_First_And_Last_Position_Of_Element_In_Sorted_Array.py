class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        size = len(nums)

        # Finding the first occurence
        low, high = 0, size -1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                first = mid
                high = mid - 1
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        # Finding the first occurence
        low, high = 0, size - 1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                last = mid
                low = mid + 1
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]