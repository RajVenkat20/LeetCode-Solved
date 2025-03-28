class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if((r, c) in visit or 
               r not in range(rows) or
               c not in range(cols) or
               heights[r][c] < prevHeight):
               return
            
            visit.add((r, c))

            diff = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in diff:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if((r, c) in pacific and (r, c) in atlantic):
                    res.append([r, c])

        return res