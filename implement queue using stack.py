class MyQueue:

    def __init__(self):
        """
        Initializing the data structure here.
        """
        self.items = []
        self.tempQueue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.tempQueue) != 0:
            self.items.append(self.tempQueue[-1])
            self.tempQueue.pop()
        self.items.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.items) != 0:
            self.tempQueue.append(self.items[-1])
            self.items.pop()
        x = self.tempQueue[-1]
        self.tempQueue.pop()
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.tempQueue) == 0:
            while len(self.items) != 0:
                self.tempQueue.append(self.items[-1])
                self.items.pop()
        return self.tempQueue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.items) == 0: #and len(self.tempQueue) == 0:
            return True
        else:
            return False

obj = MyQueue()
x = [5, 3, 2, 9, 1, 8]
for i in range(0, len(x)):
    obj.push(x[i])
print(obj.items)
print(obj.pop())
print(obj.pop())
print(obj.peek())
print(obj.empty())
print(obj.items)
print(obj.tempQueue)

