class Stack:
    def __init__(self):
        self.alist = []


    def push(self, x):
        self.alist.append(x)


    def pop(self):
         self.alist.pop(-1)


    def top(self):
        return self.alist[-1]


    def size(self):
        return len(self.alist)


    def empty(self):
        return len(self.alist) == 0
s = Stack()
for i in range(10):
    s.push(i)
while not s.empty():
    print(s.top())
    s.pop()
    

