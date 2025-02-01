class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        res = list(s)
        vowelStr = "aeiouAEIOU"

        while(i < j):
            while(i < j and res[i] not in vowelStr):
                i += 1
            
            while(i < j and res[j] not in vowelStr):
                j -= 1

            res[i], res[j] = res[j], res[i]

            i += 1
            j -= 1

        return "".join(res)