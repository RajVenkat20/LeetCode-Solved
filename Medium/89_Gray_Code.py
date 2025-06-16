class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, isPresent = [0], set([0])

        def dfs(n):
            if(len(res) == (1 << n)):
                return True
            
            curr = res[-1]

            for i in range(n):
                nextNum = curr ^ (1 << i)
                if(nextNum not in isPresent):
                    isPresent.add(nextNum)
                    res.append(nextNum)
                    if(dfs(n)):
                        return True
                    isPresent.remove(nextNum)
                    res.pop()
            return False

        dfs(n)
        return res