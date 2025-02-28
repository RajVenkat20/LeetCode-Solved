class Solution:
    def getCeil(self, a, n, x):
        ceil = -1
        low = 0
        high = n - 1
    
        while(low <= high):
            mid = (low + high) // 2
    
            if(a[mid] >= x):
                ceil = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return ceil


    def getFloor(self, a, n, x):
        floor = -1
        low = 0
        high = n - 1
    
        while(low <= high):
            mid = (low + high) // 2
    
            if(a[mid] <= x):
                floor = mid
                low = mid + 1
            else:
                high = mid - 1
    
        return floor

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lb = self.getFloor(nums, n, target)

        print(lb)
        
        if(lb == -1 or nums[lb] != target):
            return [-1, -1]

        return [min(lb, self.getCeil(nums, n, target)), max(lb, self.getCeil(nums, n, target))]