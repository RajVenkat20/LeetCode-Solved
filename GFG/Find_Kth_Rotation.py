#User function Template for python3
class Solution:
    def findKRotation(self, nums):
        ans = float('inf')
        low, high = 0, len(nums) - 1
        idx = -1

        while(low <= high):
            mid = (low + high) // 2
            if(nums[low] <= nums[high]):
                if(nums[low] < ans):
                    ans = nums[low]
                    idx = low
                break
            
            if(nums[low] <= nums[mid]):
                if(nums[low] < ans):
                    ans = nums[low]
                    idx = low
                low = mid + 1
            else:
                if(nums[mid] < ans):
                    ans = nums[mid]
                    idx = mid
                high = mid - 1

        return idx