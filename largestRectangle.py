#bars = [2, 1, 5, 6, 2, 3]
def largestRectangle1(bars):
    maxarea = 0
    for e in range(0, len(bars)):
        for s in range(0, e + 1):
            width = e - s + 1
            minht = 100
            for k in range(s, e + 1):
                minht = min(minht, bars[k])
            area = minht * width
            maxarea = max(area, maxarea)
    return maxarea


def largestRectangle2(bars):
    maxarea = 0
    for e in range(0, len(bars)):
        minht = 100
        for s in range(e, -1, -1):
            minht = min(minht, bars[s])
            width = e - s + 1
            area = minht * width
            maxarea = max(area, maxarea)
    return maxarea


def largestRectangle3(bars):
   # bars.append(0)
    stack = []
    maxarea = 0
    for i in range(0, len(bars) + 1):
        while i == len(bars) or len(stack) != 0 and bars[i] < bars[stack[-1]]:
            j = stack.pop()
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            area = width * bars[j]
            maxarea = max(maxarea, area)
            if len(stack) == 0: break
        stack.append(i)
    return maxarea


def largestRectangle4(hts):
    pindex = []; maxarea = 0
    for i, h in enumerate(hts + [0]):
        while pindex and hts[pindex[-1]] >= h:
            height = hts[pindex.pop()]
            width = i if not pindex else i - pindex[-1] - 1
            maxarea = max(maxarea, height * width)
        pindex.append(i)
    return maxarea


bars = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]

print(largestRectangle1(bars))
print(largestRectangle2(bars))
print(largestRectangle3(bars))

