class Solution:
    def numProvinces(self, adj, V):
        provinces = 0
        visited = [False] * (V + 1)
        
        def dfsUtil(node):
            visited[node] = True
            for val in range(V):
                if(adj[node - 1][val] == 1 and (not visited[val + 1])):
                    dfsUtil(val + 1)
        
        for i in range(1, V + 1):
            if(not visited[i]):
                provinces += 1
                dfsUtil(i)
        
        return provinces