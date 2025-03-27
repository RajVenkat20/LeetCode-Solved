class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {}

        for i in range(len(order)):
            hm[order[i]] = i

        def compare(str1, str2):
            size1 = len(str1)
            size2 = len(str2)
            i, j = 0, 0
            
            while(i < size1 and j < size2):
                if(hm[str1[i]] < hm[str2[j]]):
                    return True
                elif(hm[str1[i]] > hm[str2[j]]):
                    return False
                i += 1
                j += 1
            
            if(size1 > size2):
                return False
            
            return True

        for i in range(len(words) - 1):
            if(not compare(words[i], words[i + 1])):
                return False

        return True