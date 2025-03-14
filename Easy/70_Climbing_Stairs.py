class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1 or n == 2):
            return n
            
        a = 1
        b = 1
        tot = 0

        for i in range(2, n + 1):
            tot = a + b
            a = b
            b = tot
        
        return tot