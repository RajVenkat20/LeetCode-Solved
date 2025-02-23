class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)

        for i in range(N):
            c = collections.Counter(word)
            c[word[i]] -= 1
            if(c[word[i]] == 0):
                del c[word[i]] 
            if(len(set(c.values())) == 1):
                return True

        return False