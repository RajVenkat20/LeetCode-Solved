class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        hm = {}

        for char in word:
            hm[char] = hm.get(char, 0) + 1

        res = len(word)
        for x in hm.values():
            deleted = 0
            for y in hm.values():
                if(x > y):
                    deleted += y
                elif(y > x + k):
                    deleted += y - (x + k)

            res = min(deleted, res)

        return res