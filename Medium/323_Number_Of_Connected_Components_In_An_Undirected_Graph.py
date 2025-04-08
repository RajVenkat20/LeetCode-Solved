from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            if(node in visited):
                return

            visited.add(node)
            for neighbor in graph[node]:
                if(neighbor not in visited):
                    dfs(neighbor)
            
            return

        for source in range(n):
            if(source not in visited):
                components += 1
                dfs(source)

        return components