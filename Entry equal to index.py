'''
Bruteforce method:
def entryIndex(alist):
    for i in range(0, len(alist)):
        if alist[i] == i:
            return alist[i]
    return -1
'''

#using Binary Search
def entryIndexMatch(alist):
    s = 0
    e = len(alist) - 1
    while s <= e:
        mid = s + (e - s) // 2
        if alist[mid] == mid:
            return alist[mid]
        elif alist[mid] > mid:
            e = mid - 1
        else:
            s = mid + 1
    return -1


alist = [-2, 0, 2, 4, 4, 7, 9]
print(entryIndexMatch(alist))
