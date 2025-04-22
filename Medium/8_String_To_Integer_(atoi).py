class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if(not s):
            return 0

        i = 0
        sign = 1
        number = 0

        if(s[i] == '-'):
            i += 1
            sign = -1
        elif(s[i] == '+'):
            i += 1    

        while(i < len(s)):
            curr = s[i]

            if(not curr.isdigit()):
                break
            else:
                number = number * 10 + int(curr)

            i += 1
        
        number *= sign
        maxPos = 2 ** 31 -1
        maxNeg = -(2 ** 31)

        if(number > maxPos):
            return maxPos
        elif(number <= maxNeg):
            return maxNeg

        return number