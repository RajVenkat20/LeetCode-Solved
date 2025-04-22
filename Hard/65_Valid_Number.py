class Solution(object):
    def isValidInteger(self, s):
        if(not s):
            return False

        numberSeen = False
        i = 0

        if(s[i] in ['-', '+']):
            i += 1

        while(i < len(s)):
            curr = s[i]
            if(not curr.isdigit()):
                return False
            numberSeen = True
            i += 1

        return numberSeen

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        decimalUsed = False
        numberSeen = False

        i = 0
        if(s[i] in ['-', '+']):
            i += 1
        
        while(i < len(s)):
            curr = s[i]

            if(curr.isalpha()):
                if(curr not in ['e', 'E']):
                    return False
                else:
                    return numberSeen and self.isValidInteger(s[i + 1:])
            elif(curr == '.'):
                if(decimalUsed):
                    return False
                else:
                    decimalUsed = True
            elif(curr in ['+', '-']):
                return False
            else:
                numberSeen = True

            i += 1

        return numberSeen