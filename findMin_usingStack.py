class Stack:
    def __init__(self):
        self.items = []
        self.minItems = []

    def push(self, x):
        if len(self.minItems) == 0 or x < self.minItems[-1]:
            self.minItems.append(x)
        self.items.append(x)

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')

        if self.items[-1] == self.minItems[-1]:
            self.minItems.pop()
        self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

    def getMin(self):
        if self.empty():
            raise IndexError('min(): empty stack')
        return self.minItems[-1]

    def popMin(self):
        x = self.minItems[-1]
        temp = []
        while self.items[-1] != x:
            y = self.items[-1]
            temp.append(y)
            self.items.pop()
        self.items.pop()
        self.minItems.pop()

        for j in range(len(temp)-1, -1, -1):
            self.items.append(temp[j])
            if temp[j] < self.minItems[-1]:
                self.minItems.append(temp[j])


s = Stack()
A = [5, 4, 9, 1, 2, 3]
for i in range(0, len(A)):
    s.push(A[i])
print(s.items)
print(s.minItems)
s.popMin()
print(s.items)
print(s.minItems)
print(s.getMin())
s.popMin()

print(s.items)
print(s.minItems)

print(s.getMin())
