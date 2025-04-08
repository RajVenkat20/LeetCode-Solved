class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        completeComp = 0

        def dfs(node, res):
            if(node in visited):
                return

            visited.add(node)
            res.append(node)
            for neighbor in graph[node]:
                dfs(neighbor, res)
            
            return res

        for source in range(n):
            if(source in visited):
                continue
            component = dfs(source, [])
            flag = True
            for v2 in component:
                if(len(component) - 1 != len(graph[v2])):
                    flag = False
                    break
            
            if(flag):
                completeComp += 1

        return completeComp