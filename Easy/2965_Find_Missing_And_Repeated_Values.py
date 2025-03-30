class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hm = {}
        n = len(grid)
        res = []

        for i in range(n):
            for j in range(n):
                hm[grid[i][j]] = hm.get(grid[i][j], 0) + 1
                if(hm[grid[i][j]] == 2):
                    res.append(grid[i][j])

        for i in range(1, (n ** 2) + 1):
            if(hm.get(i, 0) == 0):
                res.append(i)
                return res