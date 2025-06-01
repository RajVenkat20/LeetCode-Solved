class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        startColor = image[sr][sc]

        if(color == startColor):
            return image

        def dfs(i, j):
            if(i not in range(rows) or
               j not in range(cols) or
               image[i][j] != startColor):
               return
            
            image[i][j] = color
            diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in diff:
                dfs(i + dr, j + dc)

        dfs(sr, sc)
        return image