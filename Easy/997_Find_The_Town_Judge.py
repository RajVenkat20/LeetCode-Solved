class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming, outgoing = {}, {}

        for pair in trust:
            outgoing[pair[0]] = outgoing.get(pair[0], 0) + 1
            incoming[pair[1]] = incoming.get(pair[1], 0) + 1
        
        for val in range(1, n + 1):
            if(outgoing.get(val, 0) == 0 and incoming.get(val, 0) == n - 1):
                return val

        return -1