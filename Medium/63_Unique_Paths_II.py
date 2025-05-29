class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if(grid[0][0] == 1):
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def helperPath(i, j):
            if(i >= m or j>=n or grid[i][j] == 1):
                return 0
            if(i == m - 1 and j == n - 1):
                return 1
            if(dp[i][j] != -1):
                return dp[i][j]

            dp[i][j] = helperPath(i + 1, j) + helperPath(i, j + 1)

            return dp[i][j]

        return helperPath(0, 0)