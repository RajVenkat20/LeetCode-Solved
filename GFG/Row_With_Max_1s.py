class Solution:
    def firstOccurence(self, row, size):
        low, high = 0, size - 1
        idx = -1
        
        while(low <= high):
            mid = (low + high) // 2
            
            if(row[mid] == 1):
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return idx
            
            
    def rowWithMax1s(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        maxOnes = 0
        ans = -1
        
        for i in range(rows):
            index = self.firstOccurence(arr[i], cols)
            if(index != -1 and cols - index > maxOnes):
                maxOnes = cols - index
                ans = i
            
        return ans