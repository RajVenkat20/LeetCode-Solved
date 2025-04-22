class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num == 0):
            return "Zero"
        
        onesMap = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                   5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                   9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
                   13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                   16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                   19: "Nineteen"}

        tensMap = {20: "Twenty", 30: "Thirty", 40: "Forty",
                   50: "Fifty", 60: "Sixty", 70: "Seventy",
                   80: "Eighty", 90: "Ninety"}

        def getString(n):
            res = []
            hundreds = n // 100
            if(hundreds):
                res.append(onesMap[hundreds] + " Hundred")
            last2 = n % 100
            if(last2 >= 20):
                tens, ones = last2 // 10, last2 % 10
                res.append(tensMap[tens * 10])
                if(ones):
                    res.append(onesMap[ones])
            elif(last2):
                res.append(onesMap[last2])
            return " ".join(res)

        position = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while(num):
            digits = num % 1000
            s = getString(digits)
            if(s):
                res.append(s + position[i])
            num = num // 1000
            i += 1

        res.reverse()
        return " ".join(res)