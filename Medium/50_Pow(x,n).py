class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        temp = n
        
        if(temp < 0):
            temp = -1 * temp
        
        while(temp > 0):
            if(temp % 2 == 1):
                ans = ans * x
                temp = temp - 1
            else:
                x = x * x
                temp = temp / 2
        
        if(n < 0):
            ans = 1 / ans
        
        return ans
