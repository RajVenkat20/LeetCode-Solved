from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet= defaultdict(set)
        gridSet = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if(board[i][j] == '.'):
                    continue
                if(board[i][j] in rowSet[i] or
                   board[i][j] in colSet[j] or
                   board[i][j] in gridSet[(i // 3, j // 3)]):
                   return False
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                gridSet[(i // 3, j // 3)].add(board[i][j])

        return True