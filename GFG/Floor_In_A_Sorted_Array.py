class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        low = 0
        high = len(arr) - 1
        ans = -1
        
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid] <= k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans