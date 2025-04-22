class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symMapping = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
                      ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                      ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        res = ""
        
        for sym, val in symMapping:
            if(num // val):
                cnt = num // val
                res += (sym * cnt)
                num = num % val

        return res