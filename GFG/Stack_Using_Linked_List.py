class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
    def __init__(self):
        self.head = None
    
    #Function to push an integer into the stack.
    def push(self, data):
        if(self.head is None):
            self.head = StackNode(data)
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            
            curr.next = StackNode(data)
            
    #Function to remove an item from top of the stack.
    def pop(self):
        if(self.head is None):
            return -1
        elif(self.head.next is None):
            return self.head.data
        else:
            curr = self.head
            while(curr.next.next):
                curr = curr.next
            
            poppedVal = curr.next.data
            curr.next = None
        
        return poppedVal


#{ 
 # Driver Code Starts
class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])
    idx = 1
    for _ in range(T):
        sq = MyStack()
        line = data[idx].strip()
        nums = list(map(int, line.split()))
        idx += 1
        n = len(nums)
        i = 0
        while i < n:
            QueryType = nums[i]
            i += 1
            if QueryType == 1:
                a = nums[i]
                i += 1
                sq.push(a)
            elif QueryType == 2:
                print(sq.pop(), end=" ")
        print()
        print("~")

# } Driver Code Ends