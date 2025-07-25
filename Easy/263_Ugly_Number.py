class Solution:
    def isUgly(self, n: int) -> bool:
        if(n <= 0):
            return False
        
        def keepDividing(dividend, divisor):
            while(dividend % divisor == 0):
                dividend //= divisor

            return dividend

        for factor in [2, 3, 5]:
            n = keepDividing(n, factor)

        return n == 1