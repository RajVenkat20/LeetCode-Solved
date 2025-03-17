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


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends