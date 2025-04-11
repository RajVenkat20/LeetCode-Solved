class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        numEdges = len(edges)
        if(numEdges != n - 1):
            return False
        
        graph = collections.defaultdict(list)
        components = 0
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if(node in visited):
                return
            visited.add(node)
            for neighbor in graph[node]:
                if(neighbor not in visited):
                    dfs(neighbor)
                
            return

        for node in range(n):
            if(node not in visited):
                components += 1
                dfs(node)

        return components == 1