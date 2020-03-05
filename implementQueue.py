class Queue:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def empty(self):
        return len(self.items) == 0

    def count(self):
        return len(self.items)



x = [3, 2, 8, 1]
obj = Queue()
for i in range(0, len(x)):
    obj.push(x[i])
print(obj.pop())
print(obj.peek())

