class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hm = {}
        size = len(s)

        for i in range(size):
            char = s[i]
            if(char in hm):
                idx = hm[char]
                if((i - idx - 1) != distance[ord(char) - ord('a')]):
                    return False
            hm[char] = i

        return True