class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for var in operations:
            if(var in "++XX++"):
                res += 1
            else:
                res -= 1

        return res
        