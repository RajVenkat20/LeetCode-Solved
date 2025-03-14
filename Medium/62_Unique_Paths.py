class Solution:
    def helperPath(self, m: int, n: int, i: int, j: int, dp: list[list[int]]) -> int:
        if(i >= m or j >= n):
            return 0
        if(i == m - 1 and j == n - 1):
            return 1
        if(dp[i][j] != -1):
            return dp[i][j]
        dp[i][j] = self.helperPath(m, n, i + 1, j, dp) + self.helperPath(m, n, i, j + 1, dp)

        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]
        return self.helperPath(m, n, 0, 0, dp)