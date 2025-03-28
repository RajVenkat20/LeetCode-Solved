class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if(r not in range(rows) or
               c not in range(cols) or
               board[r][c] != "O"):
               return 

            board[r][c] = "T"

            diff = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in diff:
                dfs(r + dr, c + dc)
        
        # Marking border "O"s as "T"s and running DFS on them
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "O" and
                   (r in [0, rows - 1] or c in [0, cols - 1])):
                   dfs(r, c)

        # Converting captured regions to X
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "O"):
                    board[r][c] = "X"

        # Reversing uncaptured regions from T to O
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "T"):
                    board[r][c] = "O"