class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num == 1):
            return True
        
        l, r = 0, num
        while l <= r:
            m = l + (r - l) // 2
            square = m * m
            if square == num:
                return True
            elif square < num:
                l = m + 1
            else:
                r = m - 1
        
        return False
            