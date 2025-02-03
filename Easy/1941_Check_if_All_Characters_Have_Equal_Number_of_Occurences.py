class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hm = {}

        for i in s:
            hm[i] = hm.get(i, 0) + 1

        return len(set(hm.values())) == 1