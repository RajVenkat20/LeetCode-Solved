class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		low, high = 1, m
        
        while(low <= high):
            mid = (low + high) // 2
            temp = mid ** n
            if(temp == m):
                return mid
            elif(temp > m):
                high = mid - 1
            else:
                low = mid + 1
                
        return -1