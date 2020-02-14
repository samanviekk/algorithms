class HeapQ:
    def __init__(self):
        self.heaplist = []

    def heapifyup(self, c):
        p = (c - 1) // 2
        while c > 0 and self.heaplist[c] < self.heaplist[p]:
            self.heaplist[c], self.heaplist[p] = self.heaplist[p], self.heaplist[c]
            c = p
            p = (c - 1) // 2

    def heappush(self, item):
        self.heaplist.append(item)
        self.heapifyup(len(self.heaplist) - 1)

    def empty(self):
        return len(self.heaplist) == 0


    def top(self):
        return self.heaplist[0]

    def heappop(self):
        self.heaplist[0] = self.heaplist[-1]
        del self.heaplist[-1]
        self.heapifydown(0)

    def heapifydown(self, p):
        lc = 2 * p + 1
        rc = 2 * p + 2
        n = len(self.heaplist)
        while p < n:
            i = -1
            if lc < n and self.heaplist[lc] < self.heaplist[p]:
                self.heaplist[lc], self.heaplist[p] = self.heaplist[p], self.heaplist[lc]
                i = lc
            if rc < n and self.heaplist[rc] < self.heaplist[p]:
                self.heaplist[rc], self.heaplist[p] = self.heaplist[p], self.heaplist[rc]
                i = rc
            if i == -1:
                break
            p = i

h = HeapQ()
x = [8, 13, 2, 6, 25, 4, 11]
for i in range(0, len(x)):
    h.heappush(x[i])

while not h.empty():
    print(h.top())
    h.heappop()



