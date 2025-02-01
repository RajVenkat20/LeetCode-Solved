class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size1 = len(word1)
        size2 = len(word2)
        res = ""
        i, j = 0, 0
        flag = True

        while(i < size1 and j < size2):
            if(flag):
                res += word1[i]
                i += 1
                flag = False
            else:
                res += word2[j]
                j += 1
                flag = True

        while(i < size1):
            res += word1[i]
            i += 1
        
        while(j < size2):
            res += word2[j]
            j += 1
        
        return res