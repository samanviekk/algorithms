class Stack:
    def __init__(self):
        self.items = []
        self.maxItems = []

    def push(self, x):
        if len(self.maxItems) == 0 or x > self.maxItems[-1]:
            self.maxItems.append(x)
        self.items.append(x)

    def pop(self):
        if self.items[-1] == self.maxItems[-1]:
            self.maxItems.pop()
        self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

    def getMax(self):
        return self.maxItems[-1]


s = Stack()
A = [5, 3, 9, 1, 2]
for i in range(0, len(A)):
    s.push(A[i])
print("max item is ", s.getMax())
print("top item is", s.top())
s. pop()
s. pop()
s. pop()
print("max item is ", s.getMax())



