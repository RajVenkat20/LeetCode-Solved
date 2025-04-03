from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        visited = set()
        rows, cols = len(rooms), len(rooms[0])
        q = deque()

        def addRoom(r, c):
            if(r not in range(rows) or
               c not in range(cols) or
               (r, c) in visited or 
               rooms[r][c] == -1):
               return

            visited.add((r, c))
            q.append([r, c])

        for i in range(rows):
            for j in range(cols):
                if(rooms[i][j] == 0):
                    q.append([i, j])
                    visited.add((i, j))

        dist = 0
        
        while(q):
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist

                diff = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in diff:
                    addRoom(r + dr, c + dc)

            dist += 1