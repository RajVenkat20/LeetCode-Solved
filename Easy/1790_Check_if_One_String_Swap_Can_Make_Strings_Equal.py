class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        j = k = -1

        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                count += 1
                if(j == -1):
                    j = i
                elif(k == -1):
                    k = i

        if(count == 0):
            return True
        elif(count == 2 and s1[j] == s2[k] and s1[k] == s2[j]):
            return True

        return False
                    