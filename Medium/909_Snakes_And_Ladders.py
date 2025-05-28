class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        size = len(board)
        board.reverse()
        def intToPos(num):
            r = (num - 1) // size
            c = (num - 1) % size
            if(r % 2):
                c = size - 1 - c

            return [r, c]

        q = deque()
        q.append([1, 0]) # [Square, Number of moves]
        visited = set()

        while(q):
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if(board[r][c] != -1):
                    nextSquare = board[r][c]
                if(nextSquare == size * size):
                    return moves + 1
                if(nextSquare not in visited):
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1