class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if(r not in range(rows) or
               c not in range(cols) or
               (r, c ) in visited or
               grid[r][c] == "0"):
               return

            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1" and (i, j) not in visited):
                    islands += 1
                    dfs(i, j)
        
        return islands
