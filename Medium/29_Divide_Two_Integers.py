class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if(dividend == divisor):
            return 1

        sign = True
        if(dividend >= 0 and divisor < 0):
            sign = False
        elif(dividend < 0 and divisor > 0):
            sign = False

        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while(n >= d):
            cnt = 0
            while(n >= (d << (cnt + 1))):
                cnt += 1

            ans += (1 << cnt)
            n = n - (d * (1 << cnt))

        if(ans >= 2 ** 31 and sign):
            return 2 ** 31 - 1
        elif(ans >= 2 ** 31 and not sign):
            return -(2 ** 31)
        
        return ans if sign else (-1 * ans)