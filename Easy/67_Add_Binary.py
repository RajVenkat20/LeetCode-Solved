class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while(m >= 0 or n >=0 or carry):
            total = carry
            if(m >= 0):
                total += int(a[m])
                m -= 1
            if(n >= 0):
                total += int(b[n])
                n -= 1
            result.append(str(total % 2))
            carry = total // 2
        
        return "".join(result[::-1])