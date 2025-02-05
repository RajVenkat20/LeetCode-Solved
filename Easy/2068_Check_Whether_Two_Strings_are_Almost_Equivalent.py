class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hm1 = {}
        hm2 = {}

        for i in word1:
            hm1[i] = hm1.get(i, 0) + 1

        for i in word2:
            hm2[i] = hm2.get(i, 0) + 1

        for k,v in hm1.items():
            if(abs(v - hm2.get(k, 0)) > 3):
                return False

        for k,v in hm2.items():
            if(abs(v - hm1.get(k, 0)) > 3):
                return False
                        
        return True