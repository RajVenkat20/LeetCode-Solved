class Solution:
    def mySqrt(self, x: int) -> int:
        if(x <= 1):
            return x
            
        l, r = 0, x

        while(l <= r):
            m = l + (r - 1) // 2
            square = m * m

            if(square == x):
                return m
            elif(square < x):
                l = m + 1
            else:
                r = m - 1
            
        return r