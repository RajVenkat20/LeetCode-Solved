class Solution:
    def maxLen(self, arr):
        hm = {}
        prefSum, res = 0, 0
        
        for i in range(len(arr)):
            prefSum += arr[i]
            
            if(prefSum == 0):
                res = i + 1
            
            if(prefSum in hm):
                res = max(res, i - hm[prefSum])
            else:
                hm[prefSum] = i
        
        return res