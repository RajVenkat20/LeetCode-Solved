class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if(endWord not in wordList):
            return 0

        nei = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1

        while(q):
            for i in range(len(q)):
                word = q.popleft()
                if(word == endWord):
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if(neiWord not in visited):
                            visited.add(neiWord)
                            q.append(neiWord)        

            res += 1

        return 0