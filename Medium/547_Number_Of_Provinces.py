class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        size= len(isConnected)
        
        visited = [False] * (size + 1)

        def dfsUtil(node):
            visited[node] = True
            for val in range(size):
                if(isConnected[node - 1][val] == 1 and (not visited[val + 1])):
                    dfsUtil(val + 1)

        for i in range(1, size + 1):
            if(not visited[i]):
                provinces += 1
                dfsUtil(i)

        return provinces
