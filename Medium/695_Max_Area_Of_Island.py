class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()

        def dfs(r, c):
            if(r not in range(rows) or
               c not in range(cols) or
               (r, c) in visited or
               grid[r][c] == 0):
               return 0
            
            visited.add((r, c))

            area = 1
            diff = [[1, 0], [0, -1], [-1, 0], [0, 1]]

            for dr, dc in diff:
                area += dfs(r + dr, c + dc)

            return area

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] != 0 and (i, j) not in visited):
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea