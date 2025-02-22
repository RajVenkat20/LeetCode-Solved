class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1 + str2 != str2 + str1):
            return ""
        
        def gcd(n1, n2):
            while(n2):
                n1, n2 = n2, n1 % n2
            return n1

        idx = gcd(len(str1), len(str2))

        return str1[:idx]