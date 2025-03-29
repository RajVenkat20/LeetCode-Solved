class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        size = len(sentence)
        
        for i in range(size):
            if(sentence[i][-1] != sentence[(i + 1) % size][0]):
                return False

        return True