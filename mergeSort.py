def mergeSort(alist, s, e):
    if s >= e:
        return
    mid = s + (e - s) // 2
    mergeSort(alist, s, mid)
    mergeSort(alist, mid + 1, e)
    merge(alist, s, mid, e)

def merge(alist, s, mid, e):
    if s >= e:
        return
    a1 = []
    a2 = []
    for i in range(s, mid + 1):
        a1.append(alist[i])
    for i in range(mid + 1, e + 1):
        a2.append(alist[i])

    i = 0
    j = 0
    k = s
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            alist[k] = a1[i]
            i = i + 1

        else:
            alist[k] = a2[j]
            j = j + 1
        k = k + 1


    while i < len(a1):
        alist[k] = a1[i]
        i = i + 1
        k = k + 1

    while j < len(a2):
         alist[k] = a2[j]
         j = j + 1
         k = k + 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist, 0, len(alist) - 1)
print(alist)