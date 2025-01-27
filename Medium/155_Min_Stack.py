class MinStack:

    def __init__(self):
        self.stack = []
        self.smallStack = []

    def push(self, val: int) -> None:
        if(len(self.smallStack)):
            if(val < self.smallStack[-1]):
                self.smallStack.append(val)
            else:
                self.smallStack.append(self.smallStack[-1])
        else:
            self.smallStack.append(val)
            
        self.stack.append(val)
        
    def pop(self) -> None:
        temp = self.smallStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()