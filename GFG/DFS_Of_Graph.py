#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        size = len(adj)
        res = []

        visited = [False] * size
        visited[0] = True
        
        def dfsUtil(val):
            visited[val] = True
            res.append(val)
            
            for x in adj[val]:
                if(not visited[x]):
                    dfsUtil(x)
        
        dfsUtil(0)
        
        return res
        