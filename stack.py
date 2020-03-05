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
A = [3, 1, 4, 6, 7]
for i in A:
    s.push(i)
print(s.alist)
while not s.empty():
    print("top is ", s.top())

    print('................')
    s.pop()
    print("list after pop is ", s.alist)
print("size is ", s.size())
