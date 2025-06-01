class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = words[::-1]

        return " ".join(res)