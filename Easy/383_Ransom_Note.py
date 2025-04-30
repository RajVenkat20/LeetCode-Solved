class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hm1, hm2 = {}, {}

        for char in ransomNote:
            hm1[char] = hm1.get(char, 0) + 1

        for char in magazine:
            hm2[char] = hm2.get(char, 0) + 1

        for key in hm1:
            if(hm1[key] > hm2.get(key, 0)):
                return False

        return True