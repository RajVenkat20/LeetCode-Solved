class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i, size = 0, len(word)

        while(i < size):
            cnt = 0
            curr = word[i]

            while(i < size and cnt < 9 and word[i] == curr):
                cnt += 1
                i += 1

            comp.append(str(cnt) + curr)

        return "".join(comp)