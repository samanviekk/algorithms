def orderedSequentialSearch(alist, item):
    pos = 0
    found = False ; stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found


testlist = [0 , 1, 2, 4, 5, 24, 67]
print(orderedSequentialSearch(testlist, 51))
