def findMin(arr):
    min = arr[0]
    for i in range(0, len(arr) - 1):
        if arr[i] < min:
            min = arr[i]
    return min

def findMin_rotateSortedArray(alist):
    s = 0
    e = len(alist) - 1
    if alist[s] < alist[e]:
        return alist[s]

    while s < e:
        middle = s + (e - s) // 2
        if alist[middle] < alist[e]:
            e = middle
        elif alist[middle] > alist[e]:
            s = middle + 1
        else:
            e = e - 1

    return alist[s]


testlist = [2,2,2,2,2,3,3,1,1,2]
print(findMin(testlist))
print(findMin_rotateSortedArray(testlist))

