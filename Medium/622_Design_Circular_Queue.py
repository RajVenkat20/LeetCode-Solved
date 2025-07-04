class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.rear = None     

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        if(self.head is None):
            self.head = Node(value)
            self.rear = self.head
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        if(self.size == 1):
            self.head = None
            self.rear = None
        else:
            self.head = self.head.next

        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()