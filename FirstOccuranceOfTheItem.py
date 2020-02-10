def firstOccurance(alist, item):
    s = 0
    e = len(alist) - 1
    res = -1
    while s <= e:
        mid = s + (e - s) //2
        if alist[mid] == item:
            res = mid
            e = mid - 1
        elif item < alist[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return res

def lastOccurance(alist, item):
    s = 0
    e = len(alist) - 1
    res = -1
    while s <= e:
        mid = s + (e - s) //2
        if alist[mid] == item:
            res = mid
            s = mid + 1
        elif item < alist[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return res

def countOccurances(alist, item):
    i = firstOccurance(alist, item)
    if i == -1:
        return i
    j = lastOccurance(alist, item)
    return j - i + 1


testlist = [2, 4, 4, 4, 4, 10, 10, 10, 18, 20]
res = countOccurances(testlist, 4)
print(res)
