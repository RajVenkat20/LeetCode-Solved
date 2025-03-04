class Solution:
    def floorSqrt(self, n): 
        low, high = 1, n - 1
        ans = 1
        while(low <= high):
            mid = (low + high) // 2
            temp = mid ** 2
            if(temp <= n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
            
                
        return ans