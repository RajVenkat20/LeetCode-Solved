class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hm = {}
        
        for char in magazine:
            hm[char] = hm.get(char, 0) + 1

        for char in ransomNote:
            if(char not in hm):
                return False
            elif(hm[char] == 1):
                del hm[char]
            else:
                hm[char] -= 1

        return True