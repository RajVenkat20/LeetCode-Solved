class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        diff = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            grid[r][c] = 0
            for i, (dr, dc) in enumerate(diff):
                self.s += str(i)
                newRow, newCol = r + dr, c + dc
                if(0 <= newRow < rows and
                   0 <= newCol < cols and
                   grid[newRow][newCol] == 1):
                   dfs(newRow, newCol)

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    self.s = ""
                    dfs(r, c)
                    visited.add(self.s)

        return len(visited)
