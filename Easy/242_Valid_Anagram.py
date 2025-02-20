def isAnagram(self, s: str, t: str) -> bool:
        size1 = len(s)
        size2 = len(t)

        if(size1 != size2):
            return False
        
        hm1, hm2 = {}, {}

        for val in s:
            hm1[val] = hm1.get(val, 0) + 1
        
        for val in t:
            hm2[val] = hm2.get(val, 0) + 1

        for key in hm1:
            if(hm1[key] != hm2.get(key,0)):
                return False
        
        return True