class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1, len(words) + 1):
            temp = "".join(words[:i])
            if(s == temp):
                return True
            
        return False