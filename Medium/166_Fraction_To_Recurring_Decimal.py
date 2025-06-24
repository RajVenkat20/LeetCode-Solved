class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if(numerator == 0):
            return "0"

        res = []
        if((numerator < 0) != (denominator < 0)):
            res.append('-')

        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        rem = num % den
        if(rem == 0):
            return "".join(res)

        res.append(".")
        fracPosition = {}

        while(rem):
            if(rem in fracPosition):
                res.insert(fracPosition[rem], '(')
                res.append(')')
                break

            fracPosition[rem] = len(res)
            rem *= 10
            digit = rem // den
            res.append(str(digit))
            rem %= den

        return "".join(res)