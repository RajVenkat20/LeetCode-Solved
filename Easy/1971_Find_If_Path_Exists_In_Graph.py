from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        q.append(source)
        visited = set()      
        visited.add(source)

        while(q):
            node = q.popleft()
            if(node == destination):
                return True
            for neighbor in graph[node]:
                if(neighbor not in visited):
                    q.append(neighbor)
                    visited.add(neighbor)

        return False