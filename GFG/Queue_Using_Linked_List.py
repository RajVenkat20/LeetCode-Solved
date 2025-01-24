# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
    #Function to push an element into the queue.
    def push(self, item): 
        if(self.head is None):
            self.head = Node(item)
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            
            curr.next = Node(item)

    #Function to pop front element from the queue.
    def pop(self):
        if(self.head is None):
            return -1
        elif(self.head.next is None):
            poppedVal = self.head.data
            self.head = None
            
            return poppedVal
        else:
            poppedVal = self.head.data
            self.head = self.head.next
            
            return poppedVal
        

#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
        print("~")
# } Driver Code Ends