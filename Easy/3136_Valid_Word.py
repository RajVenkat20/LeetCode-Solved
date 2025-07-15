class Solution:
    def isValid(self, word: str) -> bool:
        size = len(word)

        if(size < 3):
            return False

        vowels, consonants = False, False

        for c in word:
            if(c.isalpha()):
                if(c.lower() in "aeiou"):
                    vowels = True
                else:
                    consonants = True
            elif(not c.isdigit()):
                return False

        return vowels and consonants