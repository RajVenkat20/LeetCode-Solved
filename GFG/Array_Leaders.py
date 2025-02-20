class Solution:
    def leaders(self, arr):
        if(arr == []):
            return 0
            
        maxElement = arr[-1]
        leaders = []
        leaders.append(maxElement)
        size = len(arr)
        
        for i in range(size - 2, -1, -1):
            if(arr[i] >= maxElement):
                leaders.append(arr[i])
                maxElement = arr[i]
        
        return reversed(leaders)


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends