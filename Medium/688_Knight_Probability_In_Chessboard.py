class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[1, 2], [1, -2], [-1, 2], [-1, -2],
                      [2, 1], [2, -1], [-2, 1], [-2, -1]]

        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]

        def backtrack(move, x, y):
            if(not (0 <= x < n and 0 <= y < n)):
                return 0.0
            if(move == k):
                return 1.0
            if(dp[move][x][y]):
                return dp[move][x][y]

            p = 0.0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                p += backtrack(move + 1, nx, ny)
            
            dp[move][x][y] = p / 8.0

            return dp[move][x][y]

        return backtrack(0, row, column)
            