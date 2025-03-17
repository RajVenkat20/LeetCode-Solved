#User function Template for python3
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: list[list[int]]) -> list[int]:
        res = []
        size = len(adj)
        visited = [False] * size
        
        queue = [0]
        visited[0] = True
        
        while(queue):
            curr = queue.pop(0)
            res.append(curr)
            
            for x in adj[curr]:
                if(not visited[x]):
                    visited[x] = True
                    queue.append(x)
                
        return res
