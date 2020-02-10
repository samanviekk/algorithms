def findNextGreatest(a, x):
    for i in range(0, len(a)):
        if x == a[i]:
            return a[i]
        if a[i] < x and x < a[i + 1]:
            return a[i + 1]
    return -1
'''
def findNextGreatest(alist, x):
    s = 0
    e = len(alist) - 1
    res = -1
    while s <= e:
        mid = s + (e - s) // 2
        if alist[mid] > x:
            res = alist[mid]
            e = mid - 1
        elif alist[mid] < x:
            s = mid + 1
        else:
            return alist[mid]
    return res
'''
testarr = [1, 3, 5, 7, 10, 12]
print(findNextGreatest(testarr, 12))
