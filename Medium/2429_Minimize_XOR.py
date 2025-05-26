class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countBits(num):
            ans = 0
            while(num > 0):
                if(num & 1):
                    ans += 1
                num = num >> 1
            
            return ans
        
        def isSet(num, bit):
            temp = num & (1 << bit)
            return temp != 0
        
        def setBit(num, bit):
            return num | (1 << bit)

        def unsetBit(num, bit):
            return num & ~(1 << bit)

        res = num1
        targetSetBitsCount = countBits(num2)
        setBitsCount = countBits(res)
        currBit = 0

        while(setBitsCount < targetSetBitsCount):
            if(not isSet(res, currBit)):
                res = setBit(res, currBit)
                setBitsCount += 1
            currBit += 1
        
        while(setBitsCount > targetSetBitsCount):
            if(isSet(res, currBit)):
                res = unsetBit(res, currBit)
                setBitsCount -= 1
            currBit += 1

        return res