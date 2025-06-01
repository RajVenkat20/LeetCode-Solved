class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        opened = []
        for char in s:
            if char in hashmap.values():
                opened.append(char)
            elif char in hashmap:
                if opened and hashmap[char] == opened[-1]:
                    opened.pop()
                else:
                    return False
        return len(opened) == 0