class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        hm = {}
        vowels = ('a', 'e', 'i', 'o', 'u')

        for idx, c in enumerate(word):
            if(c in vowels):
                if(not hm):
                    start = idx
                hm[c] = idx
                if(len(hm) == 5):
                    res += min(hm.values()) - start + 1
            elif(hm):
                hm = {}

        return res